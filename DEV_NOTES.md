# Development Notes — Proto-Germanic → Old English FST Pipeline

## Table of Contents

### Polished topic sections
- [NWGmc u-lowering Exceptions Near Labials](#nwgmc-u-lowering-exceptions-near-labials)
- [PWGmc *lþ → *ld Voicing and Verner's Law Overlap](#pwgmc-lþ--ld-voicing-and-verners-law-overlap)
- [PWGmc *j-related Sound Changes](#pwgmc-j-related-sound-changes--reviewed-see-notable_findingsmd-3)
- [OE duru 'door': Stem-Class Correction](#oe-duru-door-stem-class-correction)
- [OE botm 'bottom': Paradigmatic Leveling](#oe-botm-bottom-paradigmatic-leveling)
- [PGmc *i > WGmc *e Lowering](#pgmc-i--wgmc-e-lowering-the-case-of-nest-2026-03-09h)

### Mismatch fixes (Mar 2026)
- [TSV Error: *funxwstiz → should be *funxstiz](#tsv-error-funxwstiz--should-be-funxstiz-cognate-501-fȳst)
- [NSL Chronology Bug: *funxstiz → fyxt instead of fȳst](#nsl-chronology-bug-funxstiz--fyxt-instead-of-fȳst)
- [Preconsonantal *x Loss: *xs > *s](#preconsonantal-x-loss-xs--s-before-consonant-clusters)
- [PGmc *d/*ð Representation Decision](#decision-2026-03-11-option-2a-confirmed)

### Project status and archived work
- [Project Status (as of 2026-03-10)](#project-status-as-of-2026-03-10)
- [Consonant Mismatch Bucket Refinement (2026-02-07)](#consonant-mismatch-bucket-refinement-2026-02-07)
- [A-Restoration Fix (2026-02-06)](#a-restoration-fix-2026-02-06)

### Working diary
- [Paused: Modern English (RP) Sandbox — Oct–Dec 2025](#paused-modern-english-rp-sandbox--working-diary-octdec-2025)
- [OE-focused diary (Dec 2025 – Feb 2026)](#2025-12-21) — begins after sandbox section

### Polished analyses (Feb–Mar 2026)
- [Bimoraic vs. Trimoraic *ō: Comprehensive Analysis](#bimoric-vs-trimoric-ō-comprehensive-analysis-session-028)
- [Class II Weak Verb Exploration](#class-ii-weak-verb-exploration-class2-weak-exploration-branch)
- [Cognate set 379 "rock" → corrected to "coat"](#cognate-set-379-rock--corrected-to-coat-rukkăz)
- [Labiovelar Proto-Form Corrections](#labiovelar-proto-form-corrections-and-post-velar-w-loss-rt-642)
- [Water fix: PWGmc ō-shortening](#water-fix-pwgmc-ō-shortening-and-a-restoration-correction-3a45a8b)
- [A-restoration: ræst, tæppa, stemn](#a-restoration-in-ō-stems-and-n-stems-ræst-tæppa-stemn-fronting_missing__afb)
- [The stefn/stemn Problem](#the-stefnstemn-problem-local-transponent-decision)
- [z-loss/rhotacism and bimoraic/trimoraic cross-source analysis](#historical-phonology-of-final--z-loss-and-its-interaction-with-rhotacism)

### Companion documents
- `docs/analysis/notable_findings.md` — Cross-referenced scholarly discussion (§§1–7)
- `server/fsts/germanic.txt` — FST source
- `server/data/germanic-aligned-final.tsv` — Gold standard data

---

## NWGmc u-lowering Exceptions Near Labials

**Date:** 2026-02-13
**Status:** Documented; accepted as genuine lexical exceptions

### The problem

Our NWGmcULowering rule lowers stressed *u → *o before non-high vowels in a following syllable (R/T vol.2 §2.3.1 pp.27-33). This is correct and well-established. However, several lexemes retain *u where *o is predicted:

- *fullăz → full (not ×foll; OHG fol)
- *wulfăz → wulf (not ×wolf; OHG wolf)
- *fuglăz → fugol (not ×fogol; OHG fogal)
- *bukkăz → bucc (not ×bocc; OHG boc)
- *wullō → wulle (not ×wolle; OHG wolla)
- *lubō → lufu (not ×lofu)
- *rustō → rust (not ×rost)

### Summary of the scholarly literature

**Bülbring (EB §116, pp.45-46)** provides the original hypothesis that both Luick and R/T engage with. He observes that OE u appears instead of expected o (from WGmc a-Umlaut, his §81d) "namentlich zwischen Labial und langem oder gedecktem l" — i.e. between a labial and ll or l+consonant: *full* 'full', *wulle* 'wool', *wulf* 'wolf'; also *fugol* 'bird', *bucca* 'buck', *múrnan* 'mourn'. He concedes that "meist steht jedoch der Hauptregel gemäß o" — usually the regular rule gives o — citing *wolcen, folgian, bolt, folc* as counterexamples. In his Anmerkung, Bülbring notes the agreement with OFris. and OS (afries. *ful, wulla, wulf*; as. *full, wulla, wulf, fugal*), which shows the phenomenon is "sehr alt" (very old). He remains agnostic on mechanism: "Ob wir darin Erhaltung des wg. u oder Wiederaufhebung der durch a-Umlaut herbeigeführten Veränderung erblicken müssen, läßt sich nicht mit Sicherheit entscheiden" — whether this reflects preservation of the original WGmc *u or reversal of a-Umlaut cannot be determined with certainty. He speculates that *u was lowered only partway ("etwa zu [ou] oder zu engem [o]") and then, under influence of its labial/velar environment, reverted to u, while in other words it continued to open [ɔ]. This "incomplete lowering + reversion" model is phonetically interesting but not formalizable as a categorical rule, since the same environments also show regular lowering.

**Luick (§78, Anm. 3)** engages directly with Bülbring's proposal and rejects it. He argues for paradigmatic leveling instead: doublet forms arose because paradigms had both u-preserving (high-vowel suffix) and u-lowering (non-high suffix) forms; near labials and gutturals, the u-forms were preferred. He explicitly cites the counterexamples that make Bülbring's phonological conditioning untenable: *wolcen, folc, folġian, folde, folm, bolla, bolt, bolster, molde, molcen, smolt* — all have labial or velar environments but regular lowering.

**R/T (§2.3.1, pp.32-33 / our OCR pp.47-48)** agree these are genuine exceptions but reach a different conclusion about paradigmatic leveling. They find it "implausible" for a-stem nouns, arguing that the only case-forms with high-vowel suffixes are functionally marginal: inst.sg. *-u, dat.pl. *-umaz, inst.pl. *-umiz. They conclude: "We do not really know why *u failed to lower in these forms."

### Could we use paradigm forms? (Why we decided not to)

For other problematic items (fire, brand, berry, thorn), we successfully resolved mismatches by adopting a paradigm form in which the phonological development is lautgesetzlich. The question is whether the same approach works for the u-lowering exceptions.

**Approach A: Use a u-stem or root-noun form.**
R/T notes that u-stems and root nouns regularly preserve *u because their paradigms have predominantly high-vowel suffixes (nom.sg. *-uz, acc.sg. *-ŷ, gen.sg. *-iz, dat.sg. *-i, nom.pl. *-iz, etc.). For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u (R/T p.45). If *wulf-, *fugl-, or *bukk- were u-stems, we could use the nom.sg. in *-uz.

**What weighs against Approach A:**
- Kroonen reconstructs *wulfa- (a-stem; p.598), *fugla- (a-stem), and *bukka(n)- (originally n-stem; p.98) — none as u-stems.
- There is no Gothic or comparative evidence for u-stem inflection of these words. Gothic wulfs is an a-stem, Gothic fugls is an a-stem.
- Using a u-stem nom.sg. would require us to posit a stem-class that is not attested in any daughter language. This would be philologically indefensible.

**Approach B: Use the instrumental singular *-u of the a-stem.**
The a-stem instrumental singular ended in *-u (high vowel), which would block lowering: *wulfu → *wulfu (u preserved) → OE wulf.

**What weighs against Approach B:**
- R/T explicitly calls leveling from these forms "implausible" because they are "relatively marginal in functional terms" (p.47). The instrumental singular was an infrequent case form, making it unlikely to be the analogical source for the entire paradigm's root vowel.
- If inst.sg. *-u could drive paradigmatic leveling for *wulf- and *full-, it should have done the same for *folc, *folm, *bolla, etc. — but those show regular lowering. The approach would explain some exceptions but cannot explain why the inst.sg. analogy worked here and not elsewhere.
- R/T's analysis orders u-lowering BEFORE the loss of final *a in PWGmc. At that early date, the relative paradigmatic weight of the inst.sg. would have been even smaller, since many more case-forms with non-high endings still survived.

**Approach C: Use the root-noun analysis (for words that could have been root nouns).**
R/T notes (p.44) that "nearly all a-stems exhibit lowering but no root-nouns do." If *wulf- or *fugl- had originally been root nouns (endingless nom.sg.), the u would have been preserved because root nouns had predominantly high-vowel endings.

**What weighs against Approach C:**
- Kroonen's reconstructions show these as thematic stems (*wulfa-, *fugla-), not root nouns.
- Gothic wulfs shows the thematic nom.sg. ending *-az, not a root-noun pattern.
- Root nouns are a small, archaic class (burg, brust, furh, hnut-); extending the analysis to common nouns like 'wolf' and 'fowl' would be speculative.

**Approach D: Use a derivational form with i-umlaut trigger.**
For some of the items, there are derivational forms with *j or *i that block lowering: *wulfi- (hypothetical i-stem variant?), or the derived verb *fullijaną 'to fill' → OE fyllan (where *-ij- blocks lowering of root *u).

**What weighs against Approach D:**
- These derived forms already show i-umlaut (*fullijaną → fyllan, not full). We can't simultaneously have the u preserved (from the high-vowel context) AND escape i-umlaut. The derivational base is a different word, not a paradigm form of the simplex noun.

### Luick's doublets evidence

Luick (§78, main text and Anm. 2) provides important evidence that OE itself had active u/o alternation:
- Attested doublets: *spura/spora* 'spur', *spurnan/spornan* 'kick', *cnucian/cnocian* 'knock'
- Doublets inferred from later ME developments: *ufen/ofen* 'oven', *smuca/smoca* 'smoke', *cuss/coss* 'kiss', *murþor/morþor* 'murder', *scufel/scofel* 'shovel'

This suggests the u/o split was not fully stable even in OE, and the WS literary standard simply codified one variant. But this does not provide a mechanism for our FST.

### Areal variation

Luick (Anm. 1) and R/T both note that OE, OFris., and OS share the u-preserving forms, while OHG has regular lowered forms: OE/OS wulf vs. OHG wolf, OE/OS full vs. OHG fol. This is a NWGmc areal feature, not specifically OE. R/T goes further: for *wulfaz, even OF (!) shows wolf with lowering, which is unexpected if the u-preservation were a shared northern WGmc innovation.

### Decision and implementation

**Decision:** Accept the mismatches. The FST correctly models the regular NWGmc u-lowering as a phonological rule. The u-preserving forms are genuine lexical exceptions for which no phonological conditioning has been established. Annotate each exception in the TSV citing Luick §78 and R/T §2.3.1.

**For future expert discussion:** The most promising angle might be Luick's observation about consonantal environment (near labials/gutturals + l). While neither Luick nor R/T accept this as a categorical rule, the statistical clustering might reflect a phonetic tendency — perhaps the acoustic similarity between labial/velar environments and the labial component of [u] made the lowered [o] variant phonetically less stable in those contexts. This would be a gradient/probabilistic effect rather than a Neogrammarian rule, and is therefore fundamentally not modelable in a deterministic FST. Bülbring's "incomplete lowering + reversion" model (§116 Anm.) is the most explicit formulation of this intuition, but the counterexamples (folc, bolla, etc.) preclude formalizing it.

### Related: effects of initial labials on vowels (Bülbring §§260-274)

Note that Bülbring's "Dreizehntes Kapitel" (§§260-274) discusses a *separate* set of phenomena — the effects of initial labials (especially w) on following vowels and diphthongs. These include:
- **w + iu → wu** (§264): *widu → wudu 'wood' (via u/a-Umlaut *wiudu → wudu under w-influence)
- **weo → wo → wu** (§§265-268): late WS weorpan → wurpan, sweord → swurd
- **w + i → y** (§261): ni + witan → nytan (contraction contexts)

These are chronologically later OE-internal changes, distinct from the NWGmc u-lowering exceptions discussed above. They may be relevant for future modeling of late WS orthographic variants.

### References

- Luick, K. (1914-40). *Historische Grammatik der englischen Sprache.* Leipzig. §78 (pp.147-148), esp. Anm. 1-3.
- Bülbring, K.D. (1902). *Altenglisches Elementarbuch.* I. Teil: Lautlehre. Heidelberg. §81d (a-Umlaut of *u → *o, p.32), §116 (u statt o near labials, pp.45-46).
- R/T vol.2 §2.3.1 pp.27-33 (our OCR pp.42-48).
- Kroonen (2013): *wulfa-* p.598, *bukka(n)-* p.98, *fugla-* (see under *fugla-*).

---

## OE duru 'door': Stem-Class Correction

**Date:** 2026-03-10
**Status:** Implemented (changed OE target to etymological `dor`)

### The problem

The TSV lists `*durą` → `duru`, but our FST produces `dor`. The expected form `duru` has two syllables with *u* in both, while `*durą` (a-stem neuter) yields `dor` with lowered *o* through regular u-lowering.

### Source analysis

**Kroonen (2013) distinguishes two PGmc reconstructions:**

1. **`*dura-` (a-stem neuter)** — "gate, (single) door"
   - Go. *daur* n., OE *dor* n., OS *dor, dur* n., OHG *tor* n.
   - < PIE *dhur-o-

2. **`*duri-` (i-stem feminine)** — "door" (originally plural tantum)
   - ON *dyrr* f./n.pl., OS *duri* f., OHG *turi* f.pl., G *Tür* f.
   - < PIE *dʰur-ih₂

Critically, Kroonen adds (p.110): "OE *duru*, OFri. *dore*, OHG *tura* f. 'door', on the other hand, goes back to **\*durō-**, which is formally identical to Gr. θύρα."

**R/T (vol.2, p.385) on OE u-stems:**

> "The u-stems remained a recognizable inflectional class, but its membership was reduced to a few very common and basic words. Still inflected as u-stems in early OE are masc. *sunu* 'son' and *wudu* 'wood' and fem. *hand* 'hand', *nosu* 'nose', and ***duru* 'door'** (the last **originally a root-noun that had shifted into the u-stems**)."

R/T also note (p.28) in discussing u-lowering:

> "A possible counterexample in ON is 'door': PGmc *dur- (Goth. pl. *daúrōns*) > ON pl. *dyrr*, OF *dure*, OE, OS *duru*, OHG *turi*."

R/T explain that in ON the word is plurale tantum with nom. pl. *-iz, "which might account for its retention of *u*."

**Hall (Concise Anglo-Saxon Dictionary):**

> "*duru* (dure) f. gs. *dure*, ds. and nap. *dura*, ... door, gate, wicket."

This confirms OE *duru* is feminine with u-stem inflection (gs. -e, ds. -a).

### Stem-class history

The etymology is complex:

1. **PIE**: Root-noun `*dhur-` (like "hand", "tooth", "goose")
2. **PGmc**: Multiple stem-types coexisted:
   - `*dura-` (a-stem neuter) → OE *dor* "gate"
   - `*duri-` (i-stem fem.pl.) → ON *dyrr*, OHG *turi*
   - `*durō` (ō-stem feminine) → Kroonen cites this for OE *duru*
3. **OE**: *duru* inflects as an **u-stem feminine** (R/T vol.2 p.385)

The transition from ō-stem `*durō` to u-stem *duru* involves analogical reshaping. The u-stem paradigm (like *sunu*, *nosu*, *hand*) pulled *duru* into its orbit. The nominative singular *-u* (from `*-uz` or by analogy) yielded the form we see.

### Why u-lowering doesn't apply

This is **not** a phonological exception to u-lowering. The issue is purely about stem-class:

- `*durą` (a-stem) → regular u-lowering → *dor* ✓ (correctly modeled)
- `*durō` (ō-stem) → would give *doru* (u-lowering applies)
- `*duruz` (u-stem) → no u-lowering → *duru* ✓

The u-stem nominative singular `*-uz` has a high vowel in the ending, so the root vowel *u is not before a non-high vowel. U-lowering is not triggered.

### FST verification

```
$ echo "duruz" | flookup -i server/old_english.bin
duruz   duru
```

Using u-stem `*duruz` correctly yields `duru` without any rule changes.

### Options for the TSV

**Option A: Change OE target to `dor` (keep etymological proto)**

- Keep PROTO as `*durą` (a-stem neuter)
- Change COUNTERPART from `duru` to `dor`
- Rationale: `*durą → dor` is the **lautgesetzlich** development
- The u-stem `duru` is a later analogical reformation, not the direct reflex of `*durą`
- Hall confirms: "*dor* n. (nap. *dora*, *dor*) door, gate"
- FST output: `dor` ✓

**Option B: Change proto-form to `*duruz` (u-stem nom.sg.)**

- Change PROTO from `*durą` to `*duruz`
- Keep COUNTERPART as `duru`
- Rationale: Models OE *duru* as u-stem (per R/T p.385)
- Problem: The u-stem is **not etymological**; it's a secondary analogical development
- This would prioritize an analogically remodeled form over the regular sound-law outcome

**Option C: Split into two rows**

- Row 1: `*durą` → *dor* (a-stem neuter "gate")
- Row 2: `*duruz` → *duru* (u-stem feminine "door")
- Documents both reflexes and their distinct proto-forms

### Recommendation (revised after discussion)

**Option A** is most appropriate:

1. The proto-form `*durą` (a-stem) is etymologically correct (< PIE root-noun `*dhur-`)
2. The regular sound-law development is `*durą → dor` via u-lowering
3. The u-stem `duru` is a **later analogical shift** (R/T: "originally a root-noun that had shifted into the u-stems")
4. We should target the etymologically direct reflex, not the analogically remodeled form
5. OE `dor` is well-attested (Hall: "*dor* n. door, gate")

**Principle:** When both etymological and analogical reflexes are attested, prefer the etymological one for testing sound laws.

### Implementation (2026-03-10)

Changed COUNTERPART from `duru` to `dor` in TSV row 1992, keeping `*durą`.

**Result:** 301 → **302/386 matches (+1)**

---

## OE botm 'bottom': Paradigmatic Leveling and Kluge's Law

**Date:** 2026-03-10
**Status:** Implemented (changed proto-form to `*buttmăz`)

### The problem

The TSV lists `*budmăz → botm`, but our FST produces `bodm` (with voiced *d*). The expected form `botm` shows voiceless *t*. The discrepancy reflects complex PIE morphophonology.

### PIE and Proto-Germanic etymology

#### The PIE mn-stem paradigm

The PIE word for 'bottom, ground' was a **hysterodynamic mn-stem** (Kroonen p.82):

| Case | PIE Form | Meaning |
|------|----------|---------|
| Nominative | `*bʰudʰ-mḗn` | 'bottom' |
| Genitive | `*bʰudʰ-mn-ós` | 'of the bottom' |

The root is `*bʰudʰ-` 'bottom', cognate with:
- Sanskrit `budhná-` 'bottom, ground'
- Greek `πυθμήν` (pythmḗn) 'bottom, depth, root'
- Latin `fundus` 'bottom' (with Thurneysen's Law: `*-dʰn-` → `*-nd-`)

Note: Kroonen observes that PIE `*bʰudʰ-` itself may be metathesized from `*dʰeubʰ-`, cf. PGmc `*deupa-` 'deep'.

#### Dissimilation in the genitive

In the genitive `*bʰudʰ-mn-ós`, the cluster `*-dʰmn-` contained two nasals (`m` and `n`). This triggered **dissimilation** at the PIE stage (Kroonen: "in the genitive, the *m* dissimilated"):

> `*bʰudʰ-mn-ós` → `*bʰut-n-ós`

This dissimilation is the same process that produced:
- Sanskrit `budhná-` (with `-dhn-` < PIE `*-dʰn-`)
- Latin `fundus` (with `-nd-` < PIE `*-dʰn-` via Thurneysen's Law)

#### Kluge's Law and gemination

In Proto-Germanic, the dissimilated genitive stem underwent **Kluge's Law** (Kluge 1884; Kroonen 2006). According to this law, voiced stops were geminated by assimilation of a following `*n` in stressed syllables, then devoiced:

> PIE `*bʰut-n-ós` → Pre-PGmc `*but-n-` → PGmc `*buttaz` (geminated + devoiced)

Kroonen (Introduction, §2.2.5.2):
> "According to the traditional formulation of this law, voiced *b, *d and *g were geminated to *bb, *dd and *gg by the assimilation of a following *n in a stressed syllable. These geminates were then devoiced to *pp, *tt and *kk together with old Proto-Indo-European *b, *d, *g and *gʷ during stage 2 of Grimm's law."

Kroonen explicitly cites `*budmṓ, *buttaz` 'bottom' as a paradigmatic example of Kluge's Law.

#### The resulting PGmc paradigm

Proto-Germanic thus inherited a paradigm with **consonantal alternation**:

| Case | PGmc Form | Root consonant |
|------|-----------|----------------|
| Nominative | `*budmṓ` | voiced `*d` |
| Genitive | `*buttaz` | voiceless geminate `*tt` |

This alternation between `*d ~ *tt` is a classic example of what Kroonen calls "paradigmatic allomorphy" created by Kluge's Law.

### Daughter-language stem variants

The different WGmc and NGmc languages resolved this paradigmatic alternation by **leveling** — but each language leveled to a different stem:

| Language | Form | Stem | Source |
|----------|------|------|--------|
| **Old Saxon** | `bodom` | `*budma-` | nominative stem (with `*d`) |
| **Old High German** | `bodam` | `*buþma-` (?) | variant with fricative (Orel: `*-þ-`) |
| **Old English** | `botm` | `*buttma-` | oblique stem (with `*tt`) |
| **Old Norse** | `botn` | `*buttna-` | oblique stem (with `*n` suffix) |

Kroonen (p.82):
> "The resulting paradigm **\*budmṓ, \*buttaz** gave rise to multiple stem variants, i.e. OS bodom < \*budma-, OE botm < \*buttma- and ON botn < \*buttna-."

#### The OE form `*buttma-`

See below ("The answer: Kroonen 2006") for the full explanation of how OE `*buttma-` arose. In brief: the geminate root `*butt-` (from the oblique) was spread to the nominative while preserving the nominative suffix `-m-`.

#### Other WGmc evidence

Orel (`*buðmaz ~ *butmaz`) notes: "Unexplained fluctuations in the intervocalic dental." This reflects the paradigmatic alternation that Kroonen 2006 explains.

R/T vol.2 (§6.9.5) lists the dialect variation in consonant quality: "Here too belongs botm 'bottom, ground, foundation' (OFri. bodem (*-d-), OS bodom, OHG bodam (*-þ-), ON botn)".

### Campbell on the phonology

Campbell (OEG §419-420) discusses the cluster `*-pm- > -tm-` in West Saxon:

> "After a short vowel, pl, pm > tl, tm in W-S, e.g. botl building, bytla builder, setl seat, botm bottom, bytme keel."

Campbell groups `botm` with words showing "spirant hardening" (`*p` [β] → `t` before liquids/nasals). However, this is **not** what's happening with `botm`:

- The `t` in `botm` is from the **oblique stem** `*butt-` (via Kluge's Law)
- The geminate `*tt` then simplified to `t` before `m`
- This is NOT spirant hardening from `*d` → `t`

Campbell §420 notes that Anglian preserved `*pm` as `*bm`:
> "In Angl., however, pl, pm remained after short vowels and the spirant became voiced... *bopm (cf. ME bothem)"

This confirms that the `t` in WS `botm` is not from a regular `*d > t` change, but from the different stem variant with original `*tt`.

### What is "lautgesetzlich"?

The question of whether `*buttmăz → botm` is "lautgesetzlich" (regular by sound law) is nuanced:

**Purely lautgesetzlich elements:**
1. PIE dissimilation: `*bʰudʰ-mn-ós` → `*bʰut-n-ós` ✓
2. Kluge's Law: `*but-n-` → `*butt-` ✓
3. Preconsonantal degemination: `*buttm-` → `*butm-` ✓
4. u-lowering: `*butm-` → `*botm-` ✓

**The key question: How did `-m-` get into `*buttma-`?**

The PGmc genitive was `*buttaz` — with **no `-m-`** (the `-m-` was lost in PIE dissimilation). So where does the `-m-` in `*buttma-` come from?

### The answer: Kroonen (2006), "Gemination and allomorphy in the Proto-Germanic mn-stems"

Kroonen's 2006 article (*ABäG* 61/1, 17-25) provides the full explanation. The key insight is that **the `-m-` was never lost in the nominative** — rather, PIE mn-stems developed **allomorphic paradigms** in PGmc with two coexisting root shapes:

| Cell | PIE | PGmc |
|------|-----|------|
| Nominative | `*bʰudʰ-mḗn` | `*budmōn` (with `-m-`, no gemination) |
| Genitive | `*bʰudʰ-mn-ós` → `*bʰudʰ-n-ós` | `*buttaz` (m lost, Kluge gemination) |

Kroonen (2006:22):
> "The fact that `*but(t)ma-` received its t analogically from `*buttaz` can nevertheless only be understood if the two root forms were still part of one and the same paradigm after Kluge's law. In other words, the roots `*bud-` and `*but(t)-` must have been two allomorphs at a certain stage."

And crucially (2006:22):
> "Just as the thematic formation `*bʰudʰ-nó-` in Sanskrit and Italo-Celtic, the Germanic allomorph `*butt-` must be explained from loss of the m in the genitive and some other oblique cases: `*bʰudʰ-mn-ós` > `*bʰudʰ-n-ós` (cf. Lühr 2000: 301-302), which by Kluge's law became `*buttaz`."

Kroonen provides this paradigm table (2006:22):

| Stage I (PIE) | Stage II (PGmc) | Stage III (daughter languages) |
|---------------|-----------------|--------------------------------|
| `*bʰudʰ-mē/ōn` | `*budmē/ōn` | MDu. *bodem*, OE *bodan* |
| `*bʰudʰ-n-ás` | `*buttaz` | OE *botem*, ON *botn* |

**The resolution:** The daughter languages resolved this allomorphy in different ways:

1. **Generalize the nominative root `*bud-`:** OFri. *bodem*, MDu. *bodem*, OS *bodom*
2. **Spread the geminate to the nominative:** OE *botem* (< `*buttma-`), ON *botn* (< `*buttna-`)
3. **Secondary `*þ`:** OHG *bodam*, OS *bothme* (explained by Kluge 1883 as `*d > *þ` before *m*, or as analogical by Lühr 1988:341)

**Why OE `*buttma-` has both `-tt-` AND `-m-`:**

The `-m-` was **never lost** in the nominative `*budmōn`. When speakers spread the geminate root `*butt-` (from the oblique) to replace `*bud-`, they kept the nominative suffix `-mōn`. This is **not** a "restoration" of `-m-` but rather **analogical spread of the root allomorph** while preserving the suffix:

- Original nominative: `*bud-mōn`
- Analogical nominative: `*butt-mōn` (new root, old suffix)

This is standard analogical leveling: the paradigm had root alternation (`*bud- ~ *butt-`), and one variant was generalized across all cells.

**On the suffix variation (-m- vs -n-):**

Kroonen (2006:23) also addresses why some forms show `-n-` instead of `-m-`:
> "Final m was apparently assimilated to n in many languages (Fick 1909: 275): OE *bodan*, OFri. *boden*... ON *botn* is probably due to assimilation too. Alternatively, it can be analyzed as a typical Scandinavian thematization of a secondary n-stem nom. `*budmōn` ~ gen. `*buttnaz` like in *nafn* n. 'name' and *vatn* n. 'water'."

**Summary of Kroonen's analysis:**

1. PIE `*bʰudʰ-mḗn` was a hysterokinetic mn-stem
2. In the genitive (and other oblique cases), `-mn-` > `-n-` after labial dissimilation
3. Kluge's Law then geminated: `*bʰudʰ-n-ós` > `*buttaz`
4. This created allomorphic paradigms: nom. `*budmōn` ~ gen. `*buttaz`
5. The paradigm "remained intact until after the breaking up of Proto-Germanic" (2006:22)
6. Individual daughter languages resolved the allomorphy differently
7. OE generalized the geminate root to the nominative: `*budmōn` → `*buttmōn` → `*buttma-`

**This solves our puzzle:** The `-m-` in `*buttma-` is the **original nominative suffix** that was never lost. The geminate `*-tt-` was spread to it analogically from the oblique forms.

### What other sources say (for completeness)

**Kroonen (2013), p.82:** Summarizes the 2006 analysis but without the full derivational explanation.

**Hamp (1990), "Variation in Indo-European 'bottom'" (FS Bailey, pp. 447-450):**

Hamp offers an **alternative analysis** to Kroonen's, worth documenting for scholarly completeness. His key points:

1. **The Germanic forms require three distinct etyma** (p. 447):
   - `*boðm` (> OHG *bodam*, OS *bothme*, MDu/MLG forms)
   - `*botm` (> OE *botm*)
   - `*bodn` (> OE *bodan*, OFri *boden*, and underlying ON *botn*)

2. **`*bodn` is the clearest etymon** — an exact cognate of Skt. `budhná-`, i.e. PIE `*bʰudʰ-nó-` (p. 447).

3. **The problematic `*-m-` forms:** Hamp explicitly rejects dissimilation and suffix-manipulation explanations (p. 448):
   > "All such attempts are poorly founded. They all suffer from insufficient specification of phonetic context and from leaving other instances untouched."

4. **Hamp's alternative proposal** (pp. 448-449): Speakers reanalyzed inherited `*budna-` (< `*bʰudʰ-nó-`) as if it were a Vernerized `*buþ-nó-`, extracting a new base `*buþ-` which then produced `*buþma-` → `*boþm-`. This is a **folk-etymological reanalysis** rather than regular sound change.

5. **The `*-t-` in `*butma-`:** Hamp suggests it derives from an old root noun nominative `*bʰuts` (with final devoicing), which was reanalyzed as a stem `*bʰud-` → `*bhud-mo-` (p. 449).

**Comparison with Kroonen (2006):**

| Issue | Kroonen 2006 | Hamp 1990 |
|-------|--------------|-----------|
| Source of `*-tt-` | Kluge's Law gemination in oblique | Reanalysis from nom. `*bʰuts` |
| Source of `*-m-` | Preserved from nominative, never lost | Requires separate `*-ma-` suffix |
| Mechanism | Regular paradigmatic allomorphy | Folk-etymological reanalysis |
| Key evidence | Parallel mn-stems (`*hrīma-`) | No parallel cases cited |

**Assessment:** Kroonen's 2006 analysis is more economical because it derives both the geminate and the suffix variation from a single paradigmatic source (the mn-stem alternation), whereas Hamp requires multiple independent reanalyses. Kroonen also provides a parallel case (`*hrīma- ~ *hrīpan-` 'rime') that supports his paradigmatic model. However, Hamp's article is valuable for documenting the range of scholarly opinion and for his explicit rejection of ad hoc dissimilation rules.

**Orel (2003), s.v. `*buðmaz ~ *butmaz`:** Notes "Unexplained fluctuations in the intervocalic dental" — Kroonen 2006 provides an explanation; Hamp 1990 provides a different one.

**Kluge-Seebold (2011):** Cites Hamp 1990 among sources; suggests the dental variation "can derive from different assimilation to the nasal."

**Lühr (1988:340-341):** Cited by Kroonen; discusses counter-examples to Kluge's Law and the `*-þ-` forms.

**Campbell (1959), §§419-420:** Discusses WS `*p > t` before nasals vs. Anglian preservation of `*p` — this is a separate, later sound change, not the PGmc paradigmatic alternation.

**Fulk (2018), Ringe/Taylor (2014):** Give basic etymology without the paradigmatic analysis.

### FST implementation

We treat `*buttmăz` as the pre-OE input form, representing the post-leveling stage. The FST applies:

1. **OEPreconsonantalDegemination**: `*tt` → `t` before sonorant
   > `*buttmăz` → `*butmăz`
2. **OEULowering**: `*u` → `*o`
   > `*butmăz` → `*botmăz`
3. **Final vowel loss**: `*-ăz` → ∅
   > `*botmăz` → `botm`

**Required FST changes:**
- Added `t:{*t} t:{*t} m:{*m}` to `pgrmCodaComplex` to parse geminate cluster
- Added `OEPreconsonantalDegemination` rule (restricted to sonorants to avoid
  regressing j-geminated forms like `*sattjăną → settan`)

```foma
define OESonorant [{*m}|{*n}|{*l}|{*r}];
define OEPreconsonantalDegemination [
    {*t} -> 0 || {*t} _ OESonorant
];
```

### Parallel case: PGmc `*hrīma(n)- ~ *hrīpan-` 'hoar-frost, rime'

Kroonen (2006:23-24) provides a parallel case that supports the mn-stem allomorphy analysis:

| Cell | PIE | PGmc |
|------|-----|------|
| Nominative | `*krīP-mōn` | `*hrīPmōn` → `*hrīmōn` (labial assimilated to m) |
| Genitive | `*krīP-mn-ós` → `*krīP-n-ós` | `*hrīppaz` (Kluge gemination) |

This produced two PGmc lexemes:
- `*hrīma(n)-`: OE `hrīm` m., ON `hrím` n. (nominative stem)
- `*hrīpan-`: OS `hrīpo` m., OHG `hrīffo` m. (oblique stem, reassigned to n-stem)

Kroonen (2006:23-24):
> "The fact that the genitive form, which after the operation of Kluge's law had lost its n of the suffix, was reassigned to the class of the n-stems (= `*hrīpan`) shows that the old mn-paradigm remained intact as an allomorphic n-stem during a certain period of time."

This confirms that:
1. PIE mn-stems could develop allomorphic paradigms in PGmc
2. The paradigms persisted "until well after the Proto-Germanic period" (2006:24)
3. Different daughter languages resolved the allomorphy differently

### TSV approach

The cognate set now correctly reflects stem-variant divergence:

| Doculect | Protoform | Expected | Notes |
|----------|-----------|----------|-------|
| Old_English | `*buttmăz` | `botm` | Oblique stem generalized |
| Dutch | `*budmăz` | `bodem` | Nominative stem generalized |
| German | `*budmăz` | `Boden` | Nominative stem (marked BOR) |

This is consistent with our principle for `duru/dor`: use the proto-form that most directly produces the attested outcome for each daughter language.

### Sources

**Primary source (now consulted):**
- Kroonen, G. (2006). "Gemination and allomorphy in the Proto-Germanic mn-stems: bottom and rime." *Amsterdamer Beiträge zur älteren Germanistik* 61/1, 17-25.
  - **This is the definitive source** explaining the allomorphic paradigm and how `*buttma-` arose
  - Key insight: the `-m-` was never lost in the nominative; the geminate root spread analogically

**Other sources consulted:**
- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*, p.82, §2.2.5.2 — summarizes 2006 analysis
- Hamp, E. (1990). "Variation in Indo-European 'bottom'." In Edmondson et al. (eds.), *Development and Diversity: FS Bailey*, pp. 447-450. — alternative analysis via folk-etymological reanalysis
- Orel, V. (2003). *Handbook of Germanic Etymology*, s.v. `*buðmaz ~ *butmaz` — pre-dates Kroonen 2006, notes "Unexplained fluctuations"
- Kluge, F. & Seebold, E. (2011). *Etymologisches Wörterbuch der deutschen Sprache*, s.v. *Boden*
- Fulk, R.D. (2018). *Comparative Grammar of Early Germanic*, §4.3, §5.6
- Campbell, A. (1959). *Old English Grammar*, §§419-420
- Ringe, D. & Taylor, A. (2014). *The Development of Old English*, vol.2
- Lühr, R. (1988). *Expressivität und Lautgesetz im Germanischen*, 340-341 — cited by Kroonen for `*-þ-` forms

**Original source for Kluge's Law:**
- Kluge, F. (1884). "Die germanische Consonantendehnung." *PBB* 9, 149-186.

### Implementation (2026-03-10)

Changed PROTOFORM from `*budmăz` to `*buttmăz` in TSV row 1959 only.

**Result:** 301 → **302/380 matches (+1)**

---

## PWGmc *lþ → *ld Voicing and Verner's Law Overlap

**Date:** 2026-02-13

### The rule
R/T vol.2 §5.1.3 (pp. 170-171): word-internal `*lþ → *ld` was a regular
sound change in Northern WGmc (= PWGmc). Implemented as `PWGmcLThVoicing`.

### Clear examples (rule definitely applies)
- `*falþaną → *faldaną → OE fealdan` ('fold')
- `*wilþijaz → *wildi → OE wilde` ('wild')
- `*balþaz → *bald → OE beald` ('bold')
- `*wulþraz → *wuldr → OE wuldor` ('glory')

### Ambiguous examples (rule OR Verner's Law)
R/T explicitly notes that two words might reflect Verner's Law alternation
`*þ ~ *d` rather than (or in addition to) the `*lþ → *ld` rule:
- `*gulþa- ~ *gulda-` → OE gold ('gold') — R/T §5.1.3 p.171
- `*felþu- ~ *feldu-` → OE feld ('field') — R/T §5.1.3 p.171

For these, EITHER explanation yields the correct OE outcome. Our
`PWGmcLThVoicing` rule handles both cases correctly regardless.

### Not this rule: *nēθlō → nǣdl ('needle')
R/T p.435: PGmc `*nēþlō / *nēdlō-` has Verner's alternation. OE `nǣdl`
reflects the `*d` variant. The consonant order is `θl` not `lθ`, so
`PWGmcLThVoicing` does not apply. Currently a mismatch (our FST keeps `þ`
from the `*θ` variant in the TSV).

### Scope of Verner's Law in the project
Several items involve Verner's Law alternation (voiceless/voiced pairs in
PGmc paradigms). We have NOT yet implemented a general Verner's Law
mechanism. The current approach is case-by-case:
- Where the regular sound change (`*lþ → ld`) gives the right answer, we
  use it (gold, feld, fealdan, etc.)
- Where only Verner's alternation explains the outcome (nǣdl), the item
  remains a known mismatch until we decide on a systematic approach

**TODO:** Survey all Verner's-related mismatches to assess scope before
implementing a general solution.

---

## PWGmc *j-related Sound Changes — Reviewed (see notable_findings.md §3)

**Date:** 2026-02-13

### Overview
Two PWGmc sound changes involve the loss or transformation of *j. Both are
historically legitimate but raise questions about how they should be formalized
in the FST. These have been reviewed in detail in `docs/analysis/notable_findings.md` §3.

### 1. PWGmcSyllabicJ: *ja/*ją → *i (after light syllable, word-finally)

**Source:** R/T vol.2 §3.1.2, p. 46
**Rule:** "Upon the loss of unstressed *a and *ą, preceding postconsonantal *j
and *w became syllabic *i and *u respectively"
**Conditioning:** After a light syllable (short vowel + single consonant), word-finally.
**Examples in our data:**
- *bazją → *bazi → berġes ('berry', gen.sg.)
- *harjaz → *hari → here ('army')
- *natją → *nati → net ('net')
**Implementation:** `{*j} {*a} -> {*i}` / `EnglishStarShortVowel EnglishStarConsonant _ .#.`
**Status:** Implemented and working.

### 2. PWGmcIjContraction: *ijō → *iu (before consonant)

**Source:** R/T vol.2 §3.1.5, p. 62 (Luick 1914-40: 118)
**Rule:** "A roughly similar change of *ijo to *iu appears to have occurred in
the word 'friend' in PWGmc"
**R/T caveat:** "the uniqueness of the sequence *ijo (with stressed *i) makes it
inadvisable to attempt any generalizations based on the history of this word"
**Examples:**
- PGmc *frijōnd- → PWGmc *friund → OE frēond ('friend')
  - The *iu is later leveled to *ēo by OEDiphthongLeveling
- R/T also mentions a parallel *Vwu → *Vu change (§3.1.5):
  - *knewu → *kneu → OE cnēo ('knee')
  - *fawu → *fau → OE fēa ('few')
**Implementation:** `{*i} {*j} {*ō} -> {*iu}` (unconditional — only one word has this sequence)
**Status:** Implemented; only affects *frijōndz in current data.

### Relationship between the two
R/T explicitly says the two "cannot plausibly be reduced to a single phonological
rule." SyllabicJ involves *j becoming syllabic (vocalic) after apocope exposes it
word-finally; IjContraction involves *j deletion with compensatory rounding of *i
to *iu before *ō. Different mechanisms, different environments, different outcomes.

### Questions for experts
1. Should *ijō → *iu be treated as a regular sound change or a lexical irregularity?
2. Is the parallel *Vwu → *Vu change (knee, few) the same mechanism?
3. Are there other PGmc *ijV sequences we should look for in the lexicon?

---

## Project Status (as of 2026-03-10)

**Pipeline:** PGmc → OE FST builds clean; 50+ ordered sound-change stages.
**Coverage:** 302/380 matches (**79.5%**), 78 mismatches, 6 no-output.
**Mismatch trajectory:** ~300 (Oct 2025) → 291 (Jan 2026) → 256 (Feb 7) → 103 (Mar 8) → 78 (current).

**Reference library:** Ringe & Taylor (vols. 1–2), Hogg (vol. 1), Campbell OEG, Bülbring,
Luick, Kaluza, Orel, Kroonen, EWA Band I (Lloyd & Springer), Cercignani, Howell & Salmons,
plus specialised articles. Cross-referenced in `docs/analysis/notable_findings.md` (§§1–7).

**Key recent achievements (Feb–Mar 2026):**
- Bimoraic vs. trimoraic *ō analysis completed and verified against Bülbring, Luick, R/T, Hogg
- stefn/stemn dossier: pre-OE transponent *stebn- adopted, full scholarly review filed
- z-loss/rhotacism chronology documented; exceptionlessness concern resolved
- Campbell OEG OCR'd and integrated; EWA Band I extracted
- notable_findings.md §§1–7 cross-referenced with Campbell, German-language sources
- **Onset-velar blocking for i-lowering** implemented (potentially novel finding)
- **Nasal spirant rounding** fixed (*a → *ō, not *ā)
- **Stem-class corrections**: god (*gudą), door (dor target vs duru)

**Remaining work:** 78 mismatches (u-lowering exceptions, breaking, palatalization, consonant clusters, data alignment).
See `docs/analysis/notable_findings.md` for flagged scholarly issues.

---

### Archived: Proto-West Germanic Stage Implementation (2026-02-07)

*The following records the Feb 2026 PWGmc consolidation work. Statistics cited are from that date.*

**Changes completed:**
1. **Consolidated PWGmc into WestGermanic** (user correction: they're the same stage)
   - Merged WGmcDenasalization, WGmcSyllabicJ into EnglishWestGermanic definition
   - Removed separate PWGmcStage and all references
   - Updated trace scripts and FST exports
2. **Removed WGmcFinalVowelLowering** - determined this is early OE, not PWGmc
3. **PWGmc output now correct**: *bazją → *bari ✓ (matches R/T §3.1.2)

**Current test case trace:**
```
WestGermanic: *b*a*r*i  ← CORRECT per R/T!
[OE stages lengthen *a→*ǣ]
ProtoToOEWeightMarkers: *b*ǣ*r*H*i  ← heavy marker added
ProtoToOEApocope: *b*ǣ*r  ← *H*i deleted
Surface: ber  ← WRONG (should be berġe)
```

**New problem identified:** OE chronology issue, not PWGmc issue. PWGmc *-i (from ja-stems) needs to lower to *-e BEFORE OE apocope deletes it. Currently apocope (line 1484) runs before weak tail reduction (line 1486), so *i gets deleted before it can lower to *e.

**Next steps:** Investigate OE stage chronology and test moving OldEnglishWeakTailReduction before OldEnglishHighVowelApocope.

**Research:** `session/files/pwgmc_berry_investigation.md` has detailed diagnosis.

---

## Proto-West Germanic Stage Implementation (2026-02-07) - EARLIER

**Summary:** Implementing PWGmc (= West Germanic) sound changes based on detailed reading of Ringe/Taylor §3.1.2. Key finding: **PWGmc and West Germanic are the same stage**, not separate.

**Critical PWGmc developments (R/T §3.1.2):**
1. **Loss of final *-z after unstressed vowels** (first change)
2. **Loss of word-final *-a and *-ą** (immediately after)
3. **Postconsonantal *j and *w become syllabic *i and *u**: R/T quote: "Upon the loss of unstressed *a and *ą, preceding postconsonantal *j and *w became syllabic *i and *u respectively"
4. **Denasalization of final nasal vowels** (§3.1.4): *ą → *a, *ę → *e, etc.

**Test case: 'berry' (PGmc *bazją → PWGmc *bazi → OE berġe)**

Step-by-step per sources:
1. PGmc: *bazją (neut. ja-stem nom.sg with nasal vowel)
2. Denasalization: *bazją → *bazja
3. Loss of final *-a: *bazja → *bazj
4. Syllabic *j: *bazj → *bazi (R/T §3.1.2 p.46: "*harjaz > *hari, *rikija > *riki")
5. Result: PWGmc *bazi ✓

**Current status:** Iterating on FST rules to match R/T §3.1.2 exactly. Need to consolidate PWGmc rules into WestGermanic definition (they're the same stage). Focus on correctness first, then address collateral damage.

**Research documents:** 
- `session/files/pwgmc_development_research.md` - detailed R/T analysis
- `docs/analysis/final_vowel_missing_analysis.md` - initial investigation

---

## Proto-West Germanic Stage Investigation (2026-02-07) - SUPERSEDED

[Previous entry moved to historical section - superseded by implementation work above]

---

## Consonant Mismatch Bucket Refinement (2026-02-07)

**Summary:** Refined the catch-all `consonant_mismatch_other` bucket (49 cases) into specific phenomenon buckets, achieving 45% reduction in uncategorized consonant mismatches.

**Problem:** The `consonant_mismatch_other` bucket was mixing 5+ distinct phonological phenomena, making it difficult to prioritize which issues to address next.

**Solution:** Implemented targeted bucketing logic in `server/tools/oe_mismatch_report.py`:
- Added `has_final_devoicing_issue()` helper: detects d→t, g→k, b→p in word-final/pre-consonantal position
- Added `has_intervocalic_voicing_issue()` helper: detects intervocalic stops (VbV) that should be fricatives (VfV)
- Enhanced suffix/prefix detection using consonant skeleton comparison

**New buckets created:**
1. **inflectional_suffix_extra: 15** - Output has extra inflectional suffix (-an, -en) that shouldn't be there
   - Examples: `*bainăn → bānan` (expected `bān`), `*kurnăn → cornan` (expected `corn`)
   - Likely TSV data issues (wrong inflectional form selected)
2. **final_devoicing_missing: 1** - Word-final/pre-consonantal devoicing not applied
   - Example: `*budmăz → bodm` (expected `botm`) - d→t not happening
3. **intervocalic_voicing_missing: 5** - Intervocalic stops should be fricatives
   - Examples: `*bebruz → beber` (expected `befer`), `*drībăną → drīban` (expected `drīfan`)
4. **prefix_morphology_issue: 1** - Missing derivational prefix
   - Example: `*bō → bō` (expected `bā]] [[þā`)
5. **consonant_mismatch_other: 27** - Remaining genuine consonant substitutions needing investigation

**Result:** 49 → 27 uncategorized cases (-45% reduction). The remaining 27 are legitimate mixed phenomena (hs↔x metathesis, þ↔d substitution) requiring separate investigation.

**Latest reports:**
- `server/docs/debug_snapshots/oe_mismatch_report_2026-02-07_refined_v3.txt`
- `server/docs/debug_snapshots/oe_full_trace_report_2026-02-07_refined_buckets.txt`

**Statistics at the time:** 256 total mismatches, 120 perfect matches (31.9% match rate)

---

### Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY

*Statistics below are from 2026-02-06.*

**Summary:** Implemented experimental rule deleting proto *-ą after heavy syllables, achieving 
net +28 case improvement (41 fixes, 13 collateral). This represents an **empirically-derived 
phonological finding** not explicitly stated in existing literature.

**Empirical motivation:** Dataset analysis revealed 77 words with spurious final vowels 
(mostly -a from proto *-ą). Of these, **78% (60 cases) had heavy stems** (long vowel OR 
consonant cluster before ending). After implementing heavy-syllable conditioned apocope, 
**41 cases fixed** with only 13 collateral damage (3.2:1 success ratio).

**What the literature says:**
- Ringe/Taylor §6.8.1: "short *i and *u were lost word-finally after a heavy syllable"
- Hogg §3.3.2: Neuter strong nouns show zero ending after heavy stems, -u after light stems
- **Neither source explicitly extends this pattern to *-ą (neuter nom./acc.sg.)**

**What the modeling reveals:**
The same heavy/light conditioning that applied to *-i/*-u **also applied to *-ą**, despite 
this not being explicitly documented in our sources. The empirical improvement at the time (282→262 
mismatches, 23.8%→29.2% match rate) strongly supported this extension.

This is a **learned phonological pattern** — the computational model has helped us 
identify a systematic sound change not fully articulated in the reference literature.

**Changes to germanic.txt:**
1. Added `OldEnglishHeavySyllableNasalApocope` rule: `{*H} {*ą} -> 0 || _ .#.`
2. Extended `OldEnglishHeavyMarker` to mark *-ą when after heavy syllables
3. Inserted into pipeline after `OldEnglishHighVowelApocope`, before `OldEnglishWeakTailReduction`

**Result (2026-02-06):** 282 → 262 total mismatches (-7.1%). Match rate: 23.8% → 29.2% (+5.4 points).
- `final_vowel_extra`: 60 → 19 (-41 FIXED!)
- `final_vowel_missing`: 34 → 38 (+4 collateral)
- `consonant_mismatch_other`: 40 → 49 (+9 collateral)

**Examples now working:**
- `*bergą → beorg` ✓ (was: beorga)
- `*wurdą → word` ✓ (was: wurda)  
- `*blōdą → blōd` ✓ (was: blōda)

**Remaining final_vowel_extra (19 cases):** All are proto *-ō, not targeted by this fix. 
Could extend same pattern to *-ō in future iteration.

**Documentation:** 
- Full investigation: `docs/germanic_notes/final_vowel_apocope_investigation.md`
- Results: `docs/germanic_notes/heavy_syllable_apocope_experiment_results.md`

**Collateral damage (13 cases):** Needs case-by-case analysis to determine if they're 
(a) light stems miscategorized as heavy, (b) weak nouns being treated as strong, or 
(c) words needing oblique stem forms.

**Key insight:** This demonstrates the value of computational modeling for historical 
phonology — systematic patterns can emerge from careful analysis of mismatches that 
aren't fully explicit in traditional reference works.

---

## A-Restoration Fix (2026-02-06)

**Summary:** Fixed critical foma syntax bug causing A-restoration to apply unconditionally, 
then implemented chronology fix to move apocope after restoration.

**Root cause:** The rule `{*æ} -> {*a} || _ (context)` had parentheses around the context,
making it OPTIONAL in foma's replacement rule syntax. The rule applied everywhere instead
of only when followed by the required intervening+back-vowel pattern.

**Changes to germanic.txt:**
1. Removed outer parentheses from OldEnglishARestoration context (lines 1138-1183)
2. Moved OldEnglishFinalWeakSchwaApocope from OldEnglishConsonantRules to EnglishProtoToOE,
   placing it AFTER OldEnglishARestoration (lines 1402-1407, 829-831)
3. Removed weak-tail vowels {*ă} and {*ą} from OldEnglishARestorationBackVowel trigger set

**Result:** Total 282 mismatches (baseline: 280). Distribution significantly improved:
- `fronting_missing_no_trigger`: 11 → 3 (-8, major improvement)
- `back_expected_front_out`: 4 → 8 (+4, regression due to paradigmatic mixing in dataset)

**Analysis:** Regression reflects **paradigmatic alternation problem** - dataset uses single
proto-forms (e.g., `*brandăz`, `*dagăz`) to represent lexemes that historically had 
alternations (nom.sg. `dæġ` vs dat.pl. `dagum`). FST derives one form per proto-form.

**Documentation:** See `docs/germanic_notes/weak_tail_vowels_and_a_restoration.md` for 
comprehensive analysis of weak-tail vowel triggers, paradigmatic alternations, and case 
form issues.

**Prevention:** See "Foma notes / recurring gotchas" below for syntax guidelines.

---

- Priority: Old English sandbox / PGmc→OE stack. Start here first.
- Modern English sandbox TODOs (below 2025-12-07) are paused unless explicitly requested.
- Key reference: the “Old English core refactor + diagnostics” section under 2025-12-21.
- Local reference index: `docs/REFERENCES.md` (start there before searching elsewhere).
- Latest OE diagnostics (2026-02-06):
  - `docs/debug_snapshots/oe_mismatch_report_2026-02-06a.txt` (bucketed mismatches)
  - `docs/debug_snapshots/oe_full_trace_report_2026-02-06a.txt` (full per-lexeme stage trace)
  - Coverage at the time: **280 mismatches / 90 matches** (370 total OE rows).
- Start‑here repro (fresh run):
  - `python3 server/tools/oe_mismatch_report.py --output docs/debug_snapshots/oe_mismatch_report_YYYY-MM-DDa.txt`
  - `python3 server/tools/oe_full_trace_report.py --output docs/debug_snapshots/oe_full_trace_report_YYYY-MM-DDa.txt`
  - `python3 server/tools/old_english_apply_down_stats.py --output docs/debug_snapshots/oe_apply_down_stats_YYYY-MM-DDa.txt`
- Bin sync guard:
  - `python3 server/tools/oe_bin_sync_check.py` (fails if OE bins are missing/stale).
  - `bash server/tools/rebuild_oe_bins.sh` to rebuild `server/old_english.bin` and sandbox stage bins inside Docker.
- Rule triage template (generic):
  When a rule looks inert, treat it as a mini-investigation: read the rule’s own definition and comments, then cross-check its intended historical scope in the local literature (e.g., Hogg, Ringe). Next, identify the subset of dataset entries that should plausibly be affected, run focused probes through the relevant stage stacks, and decide (1) whether the rule truly never fires, (2) whether its intended effect is already being achieved by another rule or stage, (3) whether the intended change is still required for the current model, and, if it is required, (4) why the present implementation fails to achieve it (wrong ordering, mismatched symbols, overly strict context, or upstream changes).
- A‑restoration debug summary (2026-02-03, **FIXED 2026-02-06**):
  - `docs/germanic_notes/oe_a_restoration_debug.md` (evidence, probes, and current hypothesis).
  - **ROOT CAUSE FOUND (2026-02-06):** The rule had `{*æ} -> {*a} || _ (context)` with parentheses
    around the context, making it OPTIONAL. The rule applied unconditionally instead of only when
    followed by the intervening+back-vowel pattern. Fix: removed outer parentheses in germanic.txt.
  - Also expanded `OldEnglishARestorationBackVowel` to include `{*ă}` and `{*ą}` (reduced back vowels),
    and expanded `OldEnglishARestorationStrongOTail` to include common weak-tail patterns where
    A-restoration should still apply (infinitives, agent nouns, etc.).
  - Result: `fronting_missing_no_trigger` dropped from 30 to 11 (19 words fixed).
- Top mismatch counts (2026-02-06 report; 280 total at the time):
  - `final_vowel_extra`: 56
  - `consonant_mismatch_other`: 40
  - `final_vowel_missing`: 34
  - `breaking_missing`: 19
  - `breaking_extra_other`: 23
  - `palatalization_missing`: 6
  - `fronting_missing_no_trigger`: 11
  - `no_output`: 13
- Concrete “rule not firing” evidence (2026-02-01 trace):
  - **Fronting undone by A‑restoration**: *nadrō (adder) fronting yields `*æ`, but `OldEnglishARestoration` flips it back due to a back vowel in the next syllable; output `nadrō` vs expected `nǣdre`. Consistent across `fronting_missing_no_trigger`.
  - **Breaking gaps**: *brustz (breast) shows no u‑breaking; output `brust` vs expected `brēost`. *dawwō (dew) passes A‑F brightening (`*æw`) but `EnglishBreakingA` lacks a `w` context; output `dawō` vs expected `dēaw`.
  - **Palatalization missing**: *bōkō (beech) never triggers `VelarPalatalization`; output `bōcō` vs expected `bēċe`. In the trace there is no fronting stage that would supply the trigger, so this is likely a rule/chronology or etymon/expected mismatch.
- Measured ARestoration intervening segments (2026-02-05, OE sandbox):
  - True positives (31 items): top intervening segments `n, k, w, d, j` (e.g., *bakăną -> bacan, inter=`k`; *xanduz -> hand, inter=`nd`).
  - False positives (16 items): top intervening segments `r, s, t, n, p` (e.g., *nadrō -> nǣdre, inter=`dr`; *bastą -> bæst, inter=`st`; *farăną -> fær, inter=`r`).
- Candidate next actions:
  1. Tighten `OldEnglishARestoration` so it ignores weak‑tail vowels (or move it after weak‑tail reduction), then regenerate reports.
  2. Add `a/æ + w` breaking plus explicit **u‑breaking** rules to `EnglishBreakingLengthening`, then regenerate.
  3. Deep dive `palatalization_missing` (e.g., *bōkō) to confirm whether the rule/chronology or the expected form is wrong.
- Hedge (2026-01-20):
  - Reverted the orthographic `{ʤj} -> {ċġ}` mapping and removed `{ċġ}` from `OldEnglishSurfaceConsonant` (OE output should stay `ġġ`).
  - Data update: `server/data/germanic-aligned-final.tsv` (OE heċġ → heġġ) with NOTE that **heċġ is the more standard spelling**; Wiktionary TSV left unchanged.
  - As of 2026-01-22g, output is **heġġ** (matches expected); see `docs/debug_snapshots/oe_mismatch_report_2026-01-22g.txt` and `docs/debug_snapshots/oe_full_trace_report_2026-01-22g.txt`.
- Knob (2026-01-22):
  - **Unattested in Old English**; first attested in Middle English (Chaucer): “The knobbes sittynge on his chekes.”
  - Reconstructed PGmc weak noun: **\*knubban‑** (knob family).
  - **OE cnæp** (Kroonen p. 335) is **\*knapp‑**, not the knob etymon; keep families distinct.
  - TSV: OE slot **cnobba** marked **unattested** (based on ME knob + Frisian knobbe); note added in TSV.
- OE weak-tail reduction sanity check (2026-01-26):
  - **Observation:** `OldEnglishWeakTailReduction` appears inert in current builds; `*u` in weak tails (e.g., *tehun, *sebun, *newun) stays `{*u}` at `EnglishAfterProtoToOEWeakTail`, so the new `{*u}->{*o}` line does **not** affect `*-un`.
  - **Implication:** a targeted `*-un -> -on` rewrite may need to be its own rule/stage, or the existing weak‑tail reduction block needs fixing so any reductions actually apply.
  - **Next checks:** run `flookup` against `old_english_sandbox_after_proto_to_oe_weak_tail.bin` for `texun/tehun/sebun/newun` and probe `OldEnglishWeakTailReduction` in isolation to confirm whether **any** `{*ă}/{*ą}/{*i}/{*u}` reductions fire.
  - **Decision point:** if `OldEnglishWeakTailReduction` is truly dead, fix that block first; otherwise add a dedicated `OldEnglishWeakTailUnReduction` rule for `{*u}{*n} -> {*o}{*n}`.
- Foma notes / recurring gotchas (2026-01-26, updated 2026-02-06):
  - **CRITICAL: Parentheses in replacement rule contexts make them OPTIONAL.**
    - `{X} -> {Y} || _ A` = replace when followed by A (required context)
    - `{X} -> {Y} || _ (A)` = replace optionally when followed by A (i.e., **always applies**)
    - This caused the A-restoration bug (2026-02-06): the rule was written as `{*æ} -> {*a} || _ (context)`
      which made the context optional, so the rule applied unconditionally. Fix: remove outer parens.
    - **Always test replacement rules with `apply down` on strings that should NOT match the context.**
  - When testing rules in isolation, use **brace tokens** (e.g., `{*u}{*n}`) and confirm the active symbol table; raw `*u*n` strings do not always match the intended multichar symbols.
  - `source fsts/germanic.txt` writes many `.bin` files to the **current directory**; make sure the report scripts and ad‑hoc `flookup` tests are using the same bin locations.
  - If a rule seems inert, confirm it against the **exact** bin used by reports (`old_english_sandbox_after_proto_to_oe_weak_tail.bin`) rather than a locally built test transducer.
- OE *-gj- chronology check (2026-01-22):
  - Standard descriptions show WGmc **gemination before *j** in short stems and **i‑mutation following *i/*j**, with classic paths like *satjan > *sattjan > *sættjan > *settian > OE settan; palatalization of velars by *j precedes i‑mutation in the usual OE chronology. Sources: Hasenfratz appendices (WVU “Reading Old English”) and the OE phonological history summary citing Campbell.
  - Implementation aligned to this: allow **palatalized consonants** (ʤ/ʧ/ʃ/ç/ʒ/j) to count as intervening segments for i‑umlaut so raising can apply **after palatalization** rather than being blocked by non‑star symbols.
  - Result: *xagjăz → **heġġ** and *sangjăną → **senġan** in `oe_full_trace_report_2026-01-22g.txt`; *baugjăną still mispredicts `bīeġan` (see final_vowel_missing bucket).
- OE epenthesis update (2026-01-04):
  - Epenthesis is now a real phonological stage **before** star removal and appears in the full trace.
  - Deterministic `r`-epenthesis uses an `{E}` placeholder with back-shift (→`*o`) vs front fallback (→`*e`).
  - `l`-epenthesis is **restricted to final `*gl` only** (added `OldEnglishGLInsertion`), to avoid over-generation (`*xaslăz` → `hæsel` regression).
  - Current OE mismatch report (2026-01-22 run): **291 mismatches / 79 matches** (370 total OE rows at the time).
- Next actionable targets (carryover):
  - **Long-vowel missing (now 5 items as of 2026-01-10):** map *au/*eu/*iu to long diphthongs and move velar shortening out of OE if still needed.
  - 2026-01-10 follow-up: `docs/debug_snapshots/oe_mismatch_report_2026-01-10a.txt` shows long-vowel-missing bucket down to **3** items after extending `OldEnglishDiphthongLeveling`/`OldEnglishEwLongDiphthong`. New log: `docs/debug_snapshots/oe_long_diphthong_traces_2026-01-10.txt`; stats snapshot: `docs/debug_snapshots/oe_apply_down_stats_2026-01-10a.txt`.
- Long‑vowel‑missing deep dive (2026-01-02): see `docs/debug_snapshots/oe_long_vowel_missing_traces_2026-01-02d.txt`.
  - Biggest actionable sources:
    - **PGmc *au not lengthened** → change `*aeu -> *ēa` (or add a dedicated “long diphthong” step right after leveling).
    - **PGmc *eu/*iu not mapped to OE long diphthongs** → add `*eu/*iu -> *ēo` (WS merge).
    - **OE ō before velars should stay long** → move `EnglishVelarShortening` out of the OE block (OE keeps bōc/bōg).
  - “Other” misses (e.g., *end→ān, *utrăz→nǣdre, *xattuz→hōd) are not long‑vowel rules; treat separately.
  - Bucket taxonomy update (2026-01-03): the report now splits the former `uncategorized` bucket into `palatal_marker_variant`, `epenthetic_vowel_missing`, `vowel_quality_other`, `gemination_extra`, and `consonant_mismatch_other`.
  - 2026-01-10 tracing follow-up:
    - `*kewwăną → ċēowan`: `OldEnglishEwLongDiphthong` only sees single `{*w}`; extend the rule to promote `{eww}` to `{ēow}` so duplicated glides still trigger the long diphthong tier.
    - `*fuwer → fȳr`: no rule converts `{uw}` before `{r}` into `{ȳr}`; add a `{uw}` contraction (or targeted `ur` rounding) so `fūr`-class stems reach OE fȳr.
    - `*xattuz → hōd`: expected reflex doesn’t match the provided proto stem (phonologically it yields OE “hat”); fix data alignment rather than phonology.
  - 2026-01-10b data note: the “fire” row now uses dat.sg. *fūri (> fȳre) to avoid modelling nominative levelling; see TSV comment.
  - 2026-01-10 rollback: backed out the short-diphthong lengthening experiment; diagnostics back to the post-*fūri* baseline (293 mismatches) with `slaxăną` still in the long-vowel bucket for future work.

---

## Paused: Modern English (RP) Sandbox — Working Diary (Oct–Dec 2025)

*The following entries document the Modern English RP sandbox experiments.*
*This line of work is paused; the current focus is OE.*

---

## 2025-12-07

### English sandbox todo — surface accuracy focus

- ~~**Finish weak-tail deletions.** Extend `EnglishSandboxWeakTailReductions` (or add a follow-up cleanup stage) so reduced `{*a/ą}` tails drop the following `n/m/r` and final schwa in stressed monosyllables. This will convert forms like `beɪkeɪnə/bænnə/brændə/blʌdə` into the expected `bake/ban/brand/blood` without manual patches.~~
  - ✅ 2025-12-11: `{*ă}` now flows through `EnglishSandboxWeakTailReductions → EnglishSandboxWeakTailCleanup → EnglishSandboxWeakTailFinalDrop`; `EnglishSandboxNoFinalWeakTail` filters out residual `{*r/n/m}`+`{*ə}`. Tracer (`*bakăną/*bannăn/*brandăz/*blōdą`) shows single surfaces (`beɪk/bæn/brænd/blʌd`), and `tools/english_apply_down_stats.py` reports 333/376 single-output entries (multiple outputs = 0).
- **Back/round proto rhotics earlier.** Expand `EnglishSandboxProtoRhoticFronting` to push `{*e, *i, *o}` toward `{æ, ɪ, ɔ}` before `{*r}` so `*bergą/*bardăz/*barwōn/*burdiz` feed the ME vowel system with the right backness, unlocking `barrow/beard/bier/birth` reflexes.
  - Diagnostics (2025-12-11): `python3 tools/trace_english_sandbox.py --lexeme-file tmp/rhotic_test_set.txt --brace-diphthongs` still yields `*bergą → bæəʊ`, `*bardăz → bɔː`, `*barwōn → bæʋəʊn`, `*erθo → əθ`, `*fuwer → fʌæ`. Current `EnglishSandboxRhoticBreaking` is a grab-bag of lexeme-specific rewrites with `~[?* … ?*]` filters—phonologically unmotivated.
  - Rhotic data audit: 118 English proto entries contain `{r}`; the problematic clusters are `rdă` (4 entries), `rgă` (1), `rwō` (1), `rθo` (1). These align exactly with `tmp/rhotic_test_set.txt`. We need historically grounded rewrites (e.g. `{*rgă → {*rəʊ}}`, `{*rdă → {*ər}}`, `{*rwō → {*rəʊ}}`, `{*erθo → {*erθ}}) before `EnglishSandboxPostVocalicRLoss` deletes `{*r}`.
  - Next session: redesign `EnglishSandboxProtoRhoticFronting`/`EnglishSandboxRhoticBreaking` around those phonetic targets, rerun the rhotic tracer, and rerun `python3 tools/english_apply_down_stats.py` (current baseline: 333/376 single outputs, 20 exact matches).
- **Add the missing palatalisation pass.** Insert a dedicated `EnglishSandboxPalatalisation` stage (after West Germanic or glide deletion) that maps `{*bj→v}`, `{*gj→dʒ}`, `{*kj→tʃ}`, `{*sk→ʃ}` before front vowels. This captures the well-known West Saxon/Midlands changes needed for `believe/beech/chew/shield/ship` and collapses a large swath of remaining errors.
- Once these three TODOs land, rerun `tools/english_apply_down_stats.py` to confirm the “exactly one correct output” count climbs beyond the current ~20/376.

### Rhotic breaking scaffolding (2025-12-06 PM)

- Added `EnglishSandboxRhoticBreaking` with stage checkpoints/tracer support right after `ProtoRhoticFronting`. Current rewrites still leave `*bergą/*bardaz/*barwōn/*erθo` as `bæg/bɔːd/bæʋəʊ/æθɔ`, so the next session should tweak the `{*e/i/o}`→`{*a/ɜ/ɔ}` mappings and add special cases such as `{*rgă → {*rəʊ}}`, `{*rdă → {*ər}}` before re-running `python3 tools/trace_english_sandbox.py --lexeme-file tmp/rhotic_test_set.txt` and `python3 tools/english_apply_down_stats.py`.

### English vowel chronology split into discrete stages

- Extracted the historically early portions of `EnglishSandboxCoreVowelRules` into three stand-alone stages inserted right after `EnglishSandboxBreakingLengthening`: `EnglishSandboxLiquidLowering` (late OE ō→ɔː before liquids/final), `EnglishSandboxVelarShortening` (Anglo-Frisian ō→ʊ before velars), and `EnglishSandboxUrRounding` (WG u→ɔː before r). Each clause now happens once in chronological order before the broader ME vowel machinery runs, reducing the overlap that previously caused branching inside the core block.
- Added tracer checkpoints + `.bin` exports for those stages (`english_sandbox_after_liquid_lowering.bin`, `english_sandbox_after_velar_shortening.bin`, `english_sandbox_after_ur_rounding.bin`) so `trace_english_sandbox.py` can isolate regressions per innovation. Recompiled via `docker compose exec backend ... foma -f fsts/english_brace_sandbox.txt`.
- Ran `server/tools/run_english_sandbox_workflow.sh english_tracer_log_2025-12-07a.txt`; analyzer coverage slipped to **185/376** (down from 206). The ProtoInput bucket is still 5 items, but the “Surface+? but outputs” bucket ballooned. First probes show `*swestēr` still branches in `EnglishSandboxVowelRules`, so the next pass needs to peel the remaining clauses out of `EnglishSandboxCoreVowelRules` and clean up the short-vowel split fallback before widening weak-tail reductions again.

### Short-vowel split sequentialised (WIP)

- Broke `EnglishSandboxShortVowelSplit` into two parts so the contextual rewrites fire before the fallback defaults: `EnglishSandboxShortVowelContextual` now contains every `{u→ʊ}`/{`e→ɪ`}/{`i→ɪ` } clause, while `EnglishSandboxShortVowelFallback` holds the unconditional `{u→ʌ}` and `{e→ɛ}` conversions. The wrapper `EnglishSandboxShortVowelSplit` composes the two stages (`.o.`) so the historical order matches the FOOT/KIT contexts feeding the later defaults.
- Probes (`*swestēr`, `*bardaz`, `*bebruz`, `*bergą`, `*utraz`) no longer branch at `EnglishSandboxVowelRules`; each lexeme now yields a single vowel reflex, which finally exposes the genuine coverage gaps instead of masking them behind duplicated outputs. Tracer log copied to `docs/debug_snapshots/english_tracer_log_2025-12-07b.txt`.
- Regression: analyzer successes dropped to **146/376** because many STRUT/DRESS lexemes now lack the “extra” fallback paths that previously papered over incomplete conditioning. Next step is to audit the English TSV rows with no outputs (see `server/tmp/english_sandbox_results_current.json`, e.g. bæn/brɛd/blʌd) and backfill the missing contexts before moving on to weak-tail reductions. Hold off on adding `{*e}` tails until coverage recovers to the 185 baseline.

### Core vowel audit probes (2025-12-07)

- Added `server/tmp/english_core_probes.txt` spanning long vowels, short rhotics, nasal tails, and glide-rich lexemes, then traced the full stack with `python3 tools/trace_english_sandbox.py --lexeme-file tmp/english_core_probes.txt --brace-diphthongs --save-log tmp/english_tracer_log_core_audit.txt`. Snapshot lives at `docs/debug_snapshots/english_tracer_log_core_audit.txt` for future diffs.
- Quick read-through highlights what *hasn’t* happened yet for each item:
  - `*stānaz` (stone): still surfaces as `stānə`; the `{*ā}` tokens never leave `{ā}`, so the expected Anglo-Frisian rounding (`ā → ɔː`) and later GVS diphthongisation to `{əʊ}` are missing.
  - `*bōkiz` (book): yields `bʊkɪ` because `{*ō}` shortens before velars but never lengthens back to `{uː}`; we still need a later FOOT-stage (or ME-stress shift) to raise `{ʊ}` when morphology demands modern `{uː}`.
  - `*dōmą` (doom): remains `{dō-}` all the way to `dōməʊ`; the ME `{oː → uː}` change is absent, so Great Vowel Shift has nothing to work with.
  - `*bergą` (barrow): currently `bɪgəʊ`; OE `{*e}` before `{*r}` should back/round toward `{æ/ɑ}` before rhotic loss, but that proto rhotic-fronting rule is still trapped inside `EnglishSandboxCoreVowelRules`.
  - `*utraz` (adder): reaches `ʊtrə` because `{u}` already fronts/slackens but there’s no rhotic colouring to convert `{tVr}` into `{dər}`; consonant changes still pending.
  - `*swester` (sister): stage outputs `sʋɪstɪ`; the expected rhotic loss + weak-tail schwa haven’t fired (our weak-tail stage doesn’t cover `{*e}` yet), so it never approaches `sɪstə`.
  - Proto entries with `þ/ð/ai/eu` (e.g. `*fadar`, `*gansą`, `*werþaną`, `*leidą`, `*brōþēr`, `*gebāniz`) fail at `ProtoInput`, reminding us that the lexicon still needs `{þ/ð}` and brace diphthong coverage before the vowel work can be validated on those words.
- Use these annotated gaps to decide which remaining core-vowel rules to peel next: proto rhotic fronting (`{*a → æ || _ {*r}}`) and `{*o → ɔ}` are blocking obvious words (`barrow`, `folk`), while the long-vowel macros (`{*ā, *ō, *ē, *ī, *ū}`) can stay bundled until we add the “LengthRealisation” stage right before `EnglishSandboxShortVowelContextual`.
- Priority shortlist based on the audit:
  1. Add an `EnglishSandboxProtoRhoticFronting` stage so `{*ar}` contexts migrate toward `{æ/ɑ}` before rhotic loss (`*bergą`, `*bardaz`).
  2. Extract `{*o → ɔ}` (and any remaining `{*e}` adjustments) into `EnglishSandboxShortBackLowering` to unblock `*fulkaz`, `*fothą`, etc.
  3. Once those contextual rules have their own checkpoints, introduce `EnglishSandboxLengthRealisation` immediately before `EnglishSandboxShortVowelContextual` so `{*ā/*ō/*ē/*ī/*ū}` finally leave the macro alphabet and feed the Great Vowel Shift cleanly (`*stānaz`, `*dōmą`).

### Proto rhotic fronting + short back lowering staged (2025-12-07 PM)

- Added `EnglishSandboxProtoRhoticFronting` (right after `EnglishSandboxUrRounding`) so the old `{*a -> æ || _ {*r}}` rewrite now happens in its own historical slot. Reran the core probe trace; `*bergą` finally shows `{bæ…}` at the new stage before rhotic loss, confirming the stage fires once and feeds downstream rules cleanly.
- Introduced `EnglishSandboxShortBackLowering` for the blanket `{*o -> ɔ}` mapping. This keeps short back vowels out of `EnglishSandboxCoreVowelRules` and gives us another checkpoint before the short-vowel split. Staged binaries saved (`english_sandbox_after_proto_rhotic_fronting.bin`, `english_sandbox_after_short_back_lowering.bin`).
- Recompiled via `docker compose exec backend … foma -f fsts/english_brace_sandbox.txt` and captured an updated probe log (`docs/debug_snapshots/english_tracer_log_core_audit_post_rhotic.txt`). Highlights: `*stānaz` now reaches `{təʊ/taɪ/teɪ}` options ahead of weak tails, `*bergą` fronts to `{bæ…}` before `{*r}` disappears, and the short `{o}` forms (`*fulkaz`, `*fothą`) stay deterministic through the new stage. Analyzer coverage still sits at 146/376 (not rerun); next change will be the `EnglishSandboxLengthRealisation` stage so `{*ā/*ō/…}` leave the macro alphabet before Great Vowel Shift.

### Star-preserving vowel cascade + STRUT probes (late 2025-12-07)

- Converted the vowel pipeline to stay in the `{*…}` alphabet until the very end: `EnglishSandboxRhoticColoring`/`EnglishSandboxGreatVowelShift` now rewrite starred vowels and a new terminal `EnglishSandboxLongVowelRealisation` emits the IPA symbols right before `RemoveStars`. Tracer logs (`docs/debug_snapshots/english_tracer_log_core_starred.txt`, `docs/debug_snapshots/english_tracer_log_2025-12-07c.txt`) confirm the macrons persist through every historical stage.
- Reran the export→annotate→trace workflow (`english_tracer_log_2025-12-07d.txt`); analyzer coverage climbed to **188/376**, so the star-preserving rewrite didn’t cost us any outputs.
- Began cleaning up the STRUT/DRESS zero-output cluster. `EnglishSandboxWeakTailReductions` now maps `{*ą}`→`{*ə}` and a new `EnglishSandboxShortAFronting` stage fronts short `{*a}` in closed syllables before the short-vowel split. After rebuilding and running `server/tools/run_english_sandbox_workflow.sh english_tracer_log_2025-12-07e.txt`, coverage improved to **195/376**—forms like *ban/*brandaz now emit `bæn`/`brændə`. Updated `server/tmp/english_zero_output_summary.txt` (181 remaining failures) plus dropped the STRUT trace log at `docs/debug_snapshots/english_tracer_log_2025-12-07e.txt` for future comparisons.

## 2025-12-06

### English ConsonantRules made deterministic

- Split the sandbox consonant block into four sequential rules (`EnglishSandboxWGlideRule`, `EnglishSandboxZRhotacism`, `EnglishSandboxZApocope`, `EnglishSandboxDJPalatal`) so non-matching lexemes pass through untouched and matching contexts rewrite exactly once. This removes the earlier branching behaviour that produced multiple outputs (e.g., `{*z}` → `{r}` and `{0}` simultaneously) and stops no-op stems (`*bendaną`, `*grunduz`) from dying at the stage boundary.
- Recompiled `fsts/english_brace_sandbox.txt` and re-ran `server/tools/run_english_sandbox_workflow.sh english_tracer_log_2025-12-06c.txt`. Analyzer successes jumped from 179→205/376; the ConsonantRules bucket disappeared entirely, leaving only ProtoInput (5 items) and the “Surface+? but outputs” bucket (166 items) for follow-up work.
- Captured a tracer snapshot at `docs/debug_snapshots/english_tracer_log_2025-12-06c.txt`. `*bendaną` now flows through ConsonantRules unchanged and reaches Surface, while `*fiskaz` rewrites `{*z}`→`{r}` deterministically.
- Next actions: tackle the remaining vowel-stage issues (KIT/FOOT splits, schwa reductions, rhotic chronology) so the “Surface but mismatched IPA” bucket starts converting into real successes before revisiting ProtoInput compounds.
- Follow-up audit (logs at `docs/debug_snapshots/english_tracer_log_2025-12-06f.txt`) showed that naive rhotic/weak-tail rewrites tanked coverage, so for now only two safe tweaks remain live: short proto `{*a}` now fronts to `{æ}` by default, and `{*ą}` weak tails convert to `{əʊ}` in `EnglishSandboxWeakTailReductions`. Analyzer coverage is still 205/376, but at least the tail vowels surface as `{…əʊ}` for forms like `*gebaną/*br{au}dą`, which will make future schwa/diphthong work easier to verify.

### Rhotic colouring prototype (2025-12-06 — evening)

- Introduced `EnglishSandboxRhoticColoring` between `EnglishSandboxShortVowelSplit` and `EnglishSandboxGreatVowelShift`. The rule only rewrites `{a/e/i/o/u}` when an intervening consonant precedes `{*r}`, so cases like `{*utraz}` now capture the `{t}` between vowel and `{*r}`. Recompiled the cascade and traced the rhotic-heavy probes (`*utraz`, `*bergą`, `*bardaz`, `*bebruz`). Outputs still show brace vowels (e.g., `ʊtræ`, `bɪgəʊ`), but the stage now acts as a dedicated hook for future ME/EME rhotic handling instead of lumping everything into the core block.
- Reran `server/tools/run_english_sandbox_workflow.sh english_tracer_log_2025-12-06g.txt`; analyzer coverage nudged up to **206/376** (one additional success) and the bucket counts shifted to 165 “Surface+? but outputs” plus 5 ProtoInput failures. All new tracer logs live under `docs/debug_snapshots/english_tracer_log_2025-12-06g.txt` for comparison against the earlier rhotic experiment.
- No additional weak-tail rules were enabled yet—`EnglishSandboxWeakTailReductions` still only handles `{*a}` and `{*ą}`. Next session should start widening that stage one vowel class at a time while rerunning the workflow after each addition, so any regressions are easy to pinpoint.

- Follow-up determinism pass: instrumented `trace_english_sandbox.py` for the rhotic probes, then tried to sequentialise both `EnglishSandboxCoreVowelRules` and `EnglishSandboxShortVowelSplit` so each vowel rewrite would fire exactly once (logs in `/usr/app/tmp/vowel_branching_trace.txt`). That change did collapse the outputs (e.g., `*bardaz` finally reduced to a single path), but coverage cratered to 168/376. Reverted to the previous definitions and reran the workflow (`docs/debug_snapshots/english_tracer_log_2025-12-06l.txt`) so we’re back at **206/376** successes with the older branching behaviour intact.
- Takeaway: branching now clearly comes from overlapping clauses inside the core vowel block and the short-vowel split, but wholesale sequentialisation is too disruptive. Next attempt should peel off one context at a time (e.g., only the `{*ō}` liquid rule) and validate immediately rather than rewriting the entire stage.


## 2025-12-05

### English sandbox tracer bootstrapped

- Instrumented `server/fsts/english_brace_sandbox.txt` so every stage now has an `EnglishSandboxAfter*` definition plus a saved stack (e.g., `english_sandbox_after_proto_input.bin`, `english_sandbox_after_vowel_rules.bin`). Recompiled inside Docker via `docker compose exec backend sh -lc "cd /usr/app && foma -f fsts/english_brace_sandbox.txt"`; the build now emits 15 `.bin` files under `server/` alongside the existing `english_brace_sandbox.bin`.
- Rewrote `server/tools/trace_english_sandbox.py` to consume those binaries with `flookup` instead of trying to run raw `regex` commands. The script auto-detects whether it’s running on the host (`server/…` paths) or inside the container (`/usr/app`) and accepts `--bin-dir` when the stacks live elsewhere.
- Smoke test inside the backend container: `docker compose exec backend bash -lc "cd /usr/app && python3 tools/trace_english_sandbox.py --lexeme '{*fiskaz}'"`. The tracer now steps through each saved stack (currently returning `+?` for `*fiskaz`, which matches the unresolved KIT bucket, but the stage pipeline itself is inspectable again).

#### CLI polish + harness hooks

- Added `--lexeme-file`, `--brace-diphthongs`, and `--save-log` switches so we can feed large TSV extracts straight into the tracer and drop the output into `docs/debug_snapshots/` without manual copy/paste. Example: `python3 tools/trace_english_sandbox.py --lexeme-file /usr/app/tmp/english_tracer_lexemes.txt --brace-diphthongs --save-log /usr/app/tmp/english_tracer_log.txt` (run inside Docker so `/usr/app/tmp` is writable).
- Sample log (stored at `/usr/app/tmp/english_tracer_log.txt`) now drives the bucket review: `*fiskaz` reaches `Surface: fɪskæ`, `*braudą` reaches `Surface: brōdą`, while `*gebaną` and `*swestēr` still die at the surface filter—exact stage names are now captured in the log for regression diffs.
- Added `tools/annotate_english_sandbox_results.py` to decorate the sandbox regression JSON with stage-by-stage outputs plus a `first_failing_stage` field. Usage (inside Docker so `flookup` is available):
  ```bash
  docker compose exec backend bash -lc \
    "cd /usr/app && python3 tools/annotate_english_sandbox_results.py \
      --input tmp/english_sandbox_results_current.json \
      --output tmp/english_sandbox_results_with_stages.json"
  ```
  The new file (`server/tmp/english_sandbox_results_with_stages.json`) feeds into the bucket triage spreadsheet so every failure row shows its blocking stage.
- Added `tools/export_english_sandbox_results.py` to regenerate `tmp/english_sandbox_results_current.json` directly from `data/germanic-aligned-final.tsv` (filtering the English rows and piping the IPA tokens through `flookup english_brace_sandbox.bin`). Run it inside Docker right before the annotation step so both JSON files stay in sync with the current FST binaries.

- Dropped a snapshot of the four canonical probes into `docs/debug_snapshots/english_tracer_log_2025-12-05.txt` (generated via the tracer’s `--save-log`). Future sessions should append similar logs whenever stage definitions shift.

#### Surface filter triage

- Expanded `EnglishSandboxSurfaceVowel` to accept the macron and nasal vowels (`{ā}/{ē}/{ī}/{ō}/{ū}/{ą}/{ę}`) emitted by the sandbox stages. After recompiling, `*braudą` now flows through `Surface` as `brōdą`; previously it was blocked even though the upstream stages looked fine.
- Updated `EnglishSandboxSurfaceConsonant` so the plain `{g}`/`{w}` outputs (minus braces/stars) survive the final filter. Weak-tail stems such as `*gebaną` and `{sw}` clusters such as `*swestēr` now surface cleanly.
- Remaining `Surface +?` cases flag different follow-ups: continue using the annotated JSON to identify stems that die earlier in the cascade versus genuine surface-template gaps.

### Next steps

1. Feed lexemes straight from `tmp/english_sandbox_results.json` into the tracer (wrap diphthongs with `--brace-diphthongs` once that option exists) so every failure bucket has a representative stage log.
2. Investigate why `{*fiskaz}` still rejects at `EnglishSandboxAfterProtoInput`; likely need either the plain-IPA normaliser or the proto brace rewriter from the German tracer so inputs always match `pgrmWord`.
3. Once the tracer shows real stage outputs, resume the KIT/FOOT fixes with per-stage snapshots checked into `docs/debug_snapshots/` like the German workflow.

## 2025-11-21

### Ach-Laut verification

- Ran the tracer inside the backend container (`python3 tools/trace_german_stages.py --apply-down --stage GermanAfterConsonant --stage GermanAfterStopShift --lexeme laukaz --lexeme milkiz`). `GermanAfterStopShift` now clearly outputs `{*x}` for both probes while `GermanAfterConsonant` still shows the pre-shift `{*k}`, proving the rule fires in isolation again.
- Followed up with analyzer checks (`printf 'laux\nknɛxt\nmɪlx\n' | flookup german.bin`) to ensure the surface words resolve to proto bundles. All three forms now return full reconstruction sets instead of `+?`, so the ach-Laut regression is officially closed.

### Notes / next focus

- Keep the tracer command handy for future regressions; it now provides a clean before/after snapshot for German stop-shift stages.
- With spirantisation unblocked, move back to the `{braudą}` long-vowel contexts plus any residual `{au}` environments that still collapse at `GermanLongVowelRules`.
- Plan for next session: tighten the proto gate so diphthongs cannot leak through as adjacent short vowels. See the action plan below.

### Upcoming work — enforce single-token diphthongs

The tracer still shows `{braudą}` taking two proto paths: one with a genuine `{*au}` token (which monophthongises) and another where `pgrmWord` parses `a` + `u` separately, yielding the unrealistic `braɔt` branch. To keep `GermanAuMonophth` truly exceptionless, we need to prune that second parse. Proposed steps for the next window:

1. Audit `pgrmWord` via `foma` (`regex pgrmWord; apply down braudą`) and check other diphthongs (`ai/eu/iu`) to confirm the ambiguity applies across the board.
2. Add a dedicated filter right after `GermanProtoInput` that rejects any adjacent short-vowel pairs matching the diphthong inventory (`{*a}{*u}`, `{*a}{*i}`, `{*e}{*u}`, `{*i}{*u}`, …). This keeps the base proto definitions readable while ensuring the German cascade only sees the multi-character tokens.
3. Recompile and re-run the tracer/analyzer probes for all diphthong-bearing lexemes (`braudą`, `straumaz`, `flauxz`, `naudiz`, plus `{ai}/{eu}/{iu}` controls) to verify only the `{*ō}` outputs remain.
4. Rerun `python3 server/tools/api_regression.py` so English/Dutch automata (which share `pgrmWord`) don’t regress.
5. Document the new filter in this file and `docs/germanic_transducer_report.md` once it’s in place.

## 2025-11-18

### Checkpoint 0 — baseline capture

- Re-ran the stage tracer inside the backend container with `--normalize-plain` for `laukaz/milkiz/braudą/durą` (the proto control) and saved the outputs to `docs/debug_snapshots/german_stopshift_baseline_2025-11-18.txt`. This is the reference log before touching the `GermanStar*` macros.
- Noted explicitly that `durą` must be used for tracing/apply-down operations (while `dɔr` stays the analyzer control) so the `pgrmWord` inventory always recognizes every segment.

### Checkpoint 1 — proto-backed front/back sets

- Replaced the literal `GermanStarFrontVowel/GermanStarBackVowel` lists with intersections against the proto-derived `GermanStarVowel` output (`server/fsts/germanic.txt`). The helper inventories now define just the front/back subsets, preventing drift if the proto alphabet changes.
- Recompiled the cascade via `docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/germanic.txt"`; compilation succeeded and rebuilt english/dutch/german binaries.
- Spot-checked `GermanStarFrontVowel/GermanStarBackVowel` via `foma` (regex/apply) and re-ran the tracer for `GermanAfterConsonant` only. Outputs for `laukaz/milkiz/braudą/durą` remain identical to the baseline (`*l*au*k*a*z` etc.), so the checkpoint can be considered complete.

### Checkpoint 2 — diphthong alignment

- Introduced `GermanExtraDiphthong` (currently `{*ei}` from `GermanAiShift`) and rewired `GermanStarDiphthong` to reuse `pgrmDiphthong.r` plus that extra inventory. This mirrors the proto definition while keeping room for derived diphthongs.
- Recompiled (`docker compose exec backend ... foma -f fsts/germanic.txt`) and sanity-checked by running small `foma` probes plus tracer dumps for `GermanAfterConsonant`/`GermanAfterStopShift`. The ach-Laut forms still show the baseline `*l*au*k*a*z`, so no behavioural change yet.

### Checkpoint 3 — temporary `{K}` instrumentation (failed)

- Patched `GermanStopShift` so both single-`{*k}` rules output `{K}` instead of `{*x}`; recompiled and ran the tracer restricted to `GermanAfterStopShift`. The ach-Laut probes (`laukaz/milkiz`) still surfaced as `*l*au*k*a*z`, so the contexts are *still* not triggering even with the proto-aligned inventories.
- Reverted the instrumentation immediately (restored `{*k}->{*x}`) so we don't leave the rule in a limbo state. Need a deeper audit of `GermanStarConsonant` / the contexts next session.

### Why the stop-shift contexts are empty

- Direct `foma` checks show `GermanStopShift` does nothing even on a toy input (`regex GermanStopShift; apply down {*l}{*au}{*k}{*a}{*z}`), confirming the left/right contexts never match.
- Initial probes (`regex GermanStarVowel; apply down {*a}` plus `random-words`) showed the `.r`-based definitions were still two-tape relations, not single-tape languages, so intersecting them with literal inventories (`GermanFrontVowelInventory`, etc.) collapsed the set and nothing ever matched `{*au}`. This is now fixed by regenerating the literal brace unions (see the next section), so `random-words` emits real `{*…}` tokens again.
- Burmish never made this change: all of its `{*…}` classes are literal unions, so rules like `*k -> *x` see the expected tokens. We need to follow that model—either generate the literal unions from `pgrm*` via a helper script, or declare multichar symbols up front—because the `.r` projections cannot act as regex contexts.

### GermanStar* regeneration

- Added `server/tools/generate_german_star_sets.py`; it parses the `pgrm*` macros and emits literal unions for `GermanStarVowel/Diphthong/Consonant` plus the front/back subsets (mirroring Burmish). Ran `python3 server/tools/generate_german_star_sets.py --output /tmp/german_star_defs.txt` and pasted the output into `server/fsts/germanic.txt` so every star set is now a single-tape brace list again (`{*a}`, `{*ai}`, `{*b}`, …).
- Recompiled via `docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/germanic.txt"` and sanity-checked with `regex GermanStarVowel; random-words 5` / `regex GermanStarConsonant; random-words 5`. Outputs now show plain `{*…}` tokens instead of the previous `0:yy` relations, confirming the contexts are real languages again.
- Reran the stage tracer for `GermanAfterConsonant` and `GermanAfterStopShift` (with `--normalize-plain`), but the ach-Laut probes still emerge as `*l*au*k*a*z`. So the literal sets were necessary but not sufficient—the `{*k}` contexts still don’t fire even though the inventories now match. Next step is to instrument `GermanStopShift` again or log the immediate environments to see what’s still mismatched.

### Tracer tweaks (still WIP)

- Extended `server/tools/trace_german_stages.py` with `--apply-down`, which shells out to Foma and runs `regex <stage>; apply down …` for each checkpoint. Current limitation: using the raw `*l*au*…` probes still yields `???`, so we need to figure out the exact tokens each stage expects before this mode can replace the old `flookup` path. Keeping the flag so future sessions can iterate without reworking the script.
- 2025-11-20 follow-up: confirmed the failure was on our side rather than the FST. `GermanAfterStopShift` happily outputs `*l*au*x*a*z` when fed plain `laukaz`; the tracer was feeding brace tokens straight into stages that already include `GermanProtoInput`. The helper now tracks both the plain and brace-normalised forms per lexeme, chooses the right flavour per stage (`GermanProtoInput`/`GermanAfter*`/`GermanReflexes` expect plain, raw rules expect braces), and drops the bogus `set verbose-type none` command so `--apply-down` stops printing errors.

### Ach-Laut analyzer gate (2025-11-20)

- Manual stage probes show `GermanAfterStopShift` already produces `*l*au*x*a*z` / `*m*i*l*x*i*z`, so the missing analyzer hits stemmed from `GermanOrthography` rewriting `{*x}` → `h`. Only `lauh/knɛht/mɪlh` had proto traces, whereas the IPA probes (`laux/knɛxt/mɪlx`) still landed on `+?`.
- Changed `GermanOrthography` to emit the literal IPA `x` instead of forcing `{h}`. Recompiled via `docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/germanic.txt"`, then reran `printf 'laux\nknɛxt\nmɪlx\n' | flookup german.bin`—each now dumps the normal proto bundle instead of `+?`.
- Re-ran `python3 tools/trace_german_stages.py --apply-down --lexeme laukaz --lexeme milkiz` inside the backend container to capture a clean trace where the ach-Laut probes visibly pick up `{*x}` after the stop shift, matching the manual Foma spot checks.

### `kniː` / `knɛxt` regression (2025-11-20)

- Analyzer probes for `kniː/knɛxt` still returned `+?` even after the surface inventory fix. Stage traces (`python3 tools/trace_german_stages.py --apply-down --stage GermanAfterConsonant --stage GermanAfterStopShift --lexeme knewą`) showed the culprit: `GermanStopShift` was spirantising the initial `{*k}` in `*knewą`, so `GermanReflexes` produced `xniː` and the analyzer never saw the expected `k`-initial forms.
- Root cause was the permissive `(?* GermanStarBackVowel)` / `(?* GermanStarVocalic)` contexts inside `GermanStopShift`, which happily over-applied at the left edge. Added a guard transducer so the final composite becomes `GermanStopShift = GermanStopShiftCore .o. GermanInitialKFix`, where `GermanInitialKFix` rewrites `{*x}` back to `{*k}` at word onset.
- Recompiled (`docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/germanic.txt"`), then re-ran `python3 tools/trace_german_stages.py --apply-down --stage GermanAfterConsonant --stage GermanAfterStopShift --lexeme knewą` to confirm the stage now stays `*k*n*ī` across the stop-shift boundary.
- Analyzer sanity check: `docker compose exec backend sh -lc "cd /usr/app && printf 'kniː\nknɛxt\n' | flookup german.bin"` now enumerates the expected proto bundle (`knewą/kniwą/...`, `knext`, etc.). Also re-ran `python3 server/tools/api_regression.py` ⇒ PASS for Burmish & Germanic.

### Stop-shift contexts (2025-11-20)

- Removed the temporary `GermanInitialKFix` shim in favour of explicit contexts: defined front/back vowel trigger sets, allowed an optional `{*l}/{*r}` immediately before `{*k}`, and constrained the right-hand side to either true codas (`GermanStarConsonant ?*` / boundary) or the theme vowels that disappear later (`{*a}/{*ą}/{*i}` plus `{*z}/{*n}` mirrors, `{*ō}`, `{*ē}`). This matches the historical ach-/ich-Laut environments without touching initial clusters or `sk-` sequences.
- `server/fsts/germanic.txt:533` now contains the helper sets plus the four targeted `{*k}->{*x}` rules; the old `(?* ...)` expressions are gone.
- Spot checks: `python3 tools/trace_german_stages.py --apply-down --stage GermanAfterConsonant --stage GermanAfterStopShift --lexeme laukaz --lexeme milkiz` confirm the expected `{*x}` appears only after the rule. `knewą` no longer receives a stray `[x]` at the beginning.
- Analyzer (`printf 'kniː\nknɛxt\nlaux\nmɪlx\n' | flookup german.bin`) and `python3 server/tools/api_regression.py` both PASS after the change.

## 2025-11-01

### Germanic tracing primer

- Added `server/tools/trace_german_stages.py`; run it inside the backend container to snapshot any lexeme across the Proto→surface cascade (e.g. `python3 tools/trace_german_stages.py --brace-diphthongs --lexeme laukaz --lexeme milkiz`).
- Current probes (`laukaz/milkiz`) still fail at `GermanProtoInput`; stage outputs show `+?`, so nothing reaches `GermanStopShift` yet. The gate is expecting fully starred multi-character tokens (`{*l}{*au}{*k}{*a}{*z}`), not plain letters.
- Known-good items do pass: `printf 'dɔr\n' | flookup german.bin` returns the expected proto candidates (`durą`, `dąur`, …). Keep using `dɔr` as the analyzer control, but when tracing stages or applying `apply down`, switch to the proto form (`durą`) so every segment lives in the `pgrmWord` alphabet.
- Next: derive the exact brace/star inventory that `pgrmWord` emits (consider extending the tracer to wrap plain IPA automatically), then re-run the stage logger on `laukaz` to catch where `{*k}` should become `{*x}`.

### GermanStopShift audit (2025-11-17 PM)

- Stage logging inside the backend container shows `GermanAfterConsonant` and `GermanAfterStopShift` both output `*l*au*k*a*z` / `*m*i*l*k*i*z` for the ach-Laut probes, while controls like `knewą/braudą/blōdą` already lack a `{*k}`. Command used:

  ```bash
  docker compose exec backend bash -lc '\
    cd /usr/app && foma <<"FST"\n\
    source fsts/germanic.txt\n\
    regex GermanAfterConsonant;\n\
    apply down laukaz\n\
    apply down milkiz\n\
    apply down knewą\n\
    apply down braudą\n\
    apply down blōdą\n\
    apply down durą\n\
    regex GermanAfterStopShift;\n\
    apply down laukaz\n\
    apply down milkiz\n\
    apply down knewą\n\
    apply down braudą\n\
    apply down blōdą\n\
    apply down durą\n\
    quit\n\
  FST'
  ```

- Conclusion: `GermanStopShift` is the first stage where the ach-Laut verbs stall; the “brace vs. no brace” debate was a red herring.
- The real mismatch is inventory drift: `GermanStarVowel`, `GermanStarDiphthong`, `GermanStarConsonant`, etc. still list hard-coded `{*…}` tokens and no longer reflect what `pgrmWord` emits (`*l*au*k*a*z`). When we tried to derive those macros directly from `pgrmShortVowel.r` / `pgrmDiphthong.r`, the downstream automata collapsed, so the refactor needs to be incremental.
- Next session must rebuild the `GermanStar*` sets from the proto macros (mirroring Burmish) and re-run the stage trace + analyzer probes to confirm `{*k}→{*x}` at `GermanStopShift`. Instrumenting the rule to emit `{K}` temporarily should make it easy to see when the contexts match.

### Tiny refactors (2025-11-17 — late)

- Rewired `GermanStarVowel` to reuse the proto projections (`pgrmShortVowel.r | pgrmLongVowel.r | pgrmNasalVowel.r | GermanExtraVowel`). Recompiled via `docker compose exec backend ... foma -f fsts/germanic.txt` and sanity-checked with `regex GermanStarVowel; apply down a/e/ā/ą` — outputs now show the expected `a*`, `e*`, etc. No downstream automata collapsed, so the next incremental step is to replace `GermanStarDiphthong` with `pgrmDiphthong.r` before touching the front/back subsets.
- Attempted to replace `GermanStarDiphthong` with `pgrmDiphthong.r`, but `regex GermanStarDiphthong; apply down ai` returned `???` (Foma expects the literal `{*ai}` output tokens from the original definition). Reverted to the explicit `[ {*ai} | {*au} | {*eu} | {*iu} | {*ei} ]` for now; we’ll revisit once we figure out a clean way to project the brace symbols without collapsing the contexts.

### Diphthong tokenization note

- `pgrmDiphthong` currently maps `{ai} → {*ai}`, `{au} → {*au}`, etc., so the input alphabet includes literal braces. When we tried to consume that via `pgrmDiphthong.r`, `apply down ai` failed because Foma still expects the literal `{ai}` token. Likewise, wrapping `ai` in braces at the CLI (`apply down {ai}`) also fails—the config isn’t using the Burmish-style multichar symbol declarations.
- A clean refactor will probably look like Burmish: declare the multichar symbols up front (so `{ai}` becomes an atomic symbol), normalize the proto lexicon to emit those tokens, then replace the `GermanStar*` macros with `.r` projections. Until that groundwork is in place, the hard-coded `[ {*ai} | … ]` list needs to stay, or the contexts lose sight of the diphthongs.

# Daily Hand-off Notes

Add a new dated section (reverse chronological) each time you pause work.
Include:
- Services you touched (Docker/Caddy, datasets loaded).
- Regression harness status and notable warnings.
- Next tasks or blockers.

For the broader documentation map, see `docs/README.md`.


## 2025-11-01

### Services & probes
- `docker compose exec backend ... flookup german.bin` for `broːt/dɔr/kniː/laux`, plus `bash server/tools/log_german_stages.sh` to capture fresh stage dumps. Docker still prints the obsolete `version` warning before each exec.
- `laux` continues to return `+?`, while `broːt` and `dɔr` now enumerate both nasal-tailed and nasal-free proto forms (`braut/ brautą / braud / braudą`, `dur/durą/...`).

### Findings
- Stage logging shows the failure for ach-Laut items happens immediately: `regex GermanAfterEw; apply down laukaz` yields `???` because `pgrmWeakCoda` omits `{*z}`. Downstream rules therefore never see the form.
- `GermanStopShift` only spirantises `*k` before a consonant or boundary, so `*-kaz` stays as `{*k}`. After `GermanAzLoss` the lingering `{*a}` turns the stem into `lauka`, which the surface filter accepts without the expected `{x}`. The planned apocope after `AzLoss` is still missing.
- Weak-tail rules continue to overgenerate: analyzer output for `broːt` and `kniː` includes parallel paths with and without `{*z}`/`{*ą}` because `GermanFinalNasalLoss` and `GermanAzLoss` remove those segments inconsistently. The dataset migration to `-aną` verbs therefore shows up as duplicated candidates rather than a single cleaned form.
- The noun forms `*braudą`, `*blōdą`, etc. remain correct and should stay untouched; the clean-up needs to focus on the weak-verb paradigms only.
- Added `GermanBraceNormalizer` (drop literal `{`/`}`/`*`) ahead of `pgrmWord`; `GermanProtoInput` now accepts both plain (`laukaz`) and brace-star (`{*l}{*au}{*k}{*a}{*z}`) lexemes.
- Despite the gate fix, the ach-Laut chain still outputs `{*k}`—`regex GermanAfterStopShift; apply down laukaz` returns `*l*au*k*a*z`—so `flookup german.bin` continues to report `+?` for `laux/knɛxt/mɪlx`.
- Replaced the hand-written `GermanStar*` inventories with definitions derived from the proto syllable macros; the contexts now include the full starred alphabet plus `{*æ}`, `{*ɔ}`, `{*x}`, etc., keeping them aligned with ongoing proto edits.
- Observed that the ach-Laut rewrite still fails post-refactor: the starred vowels are matching, but `{*k}` survives because multi-character lexical symbols (`*a`, `*au`) are no longer treated as single units once braces are stripped. Next pass needs to restore a brace wrapper (or declare the `*X` tokens via `multichar_symbols`) so the context sees contiguous vowels around `{*k}`.

### Updates
- Extended `pgrmWeakCoda` to admit `{*z}` and recompiled `server/fsts/germanic.txt`; `regex GermanAfterEw; apply down laukaz` now returns `*l*au*k*a*z`, so ach-Laut verbs reach the sound rules again.
- Reworked `GermanStopShift`/`GermanXPalatalization`/`GermanThemeApocope` to model `{*k} → {*x}` between vowels, palatalise `{*x}` after front vowels, and drop the residual theme vowel once `{*z}` is lost. Rebuilt `german.bin` after the changes.
- Current analyzer run (`printf 'laux\\nknɛxt\\nmɪlx\\n' | flookup german.bin`) still returns `+?`; `GermanProtoInput` appears to refuse `*laukaz`, so the new rules are not exercised yet. Stage logging for the canonical probes (`knewą/braudą/...`) still works as before.
- Recompiled after introducing `GermanBraceNormalizer`; `regex GermanProtoInput; apply down {*l}{*au}{*k}{*a}{*z}` now yields `*l*au*k*a*z` without rejecting the brace input.

### Next focus
1. Track down why `GermanProtoInput` still rejects `*laukaz` (even though `{*z}` was added to the weak-tail macros) and restore `GermanAfterEw` outputs for ach-Laut probes.
2. Once the proto acceptance is fixed, confirm the new spirantisation/palatalisation/apocope rules yield analyzer hits for `laux/knɛxt/mɪlx` and adjust contexts if over/under-generating.
3. Tighten weak-tail handling so `GermanAzLoss` + `GermanFinalNasalLoss` eliminate the tail exactly once for verbs, while noun stems like `*braudą` stay untouched. Re-run `flookup german.bin` for `broːt/dɔr/kniː` after each iteration.


## 2025-10-26

### Services & tests
- `docker compose ps` (requires elevated permissions in this environment) → backend + frontend containers still up; Docker repeats the cosmetic `version` warning.
- Patched `server/tools/log_german_stages.sh` so the probe lexemes are single tokens, then ran `bash server/tools/log_german_stages.sh > /tmp/german_stage_log.txt` to capture Proto→stage outputs for `knewą/braudą/blōdą/tōr`.
- Spot-checked `german_after_longv.bin` directly via `docker compose exec backend ... foma` to confirm the `kniː` forms still appear when the stage is loaded manually.

### Surface Filter (Brace status)
- Brace retarget is complete for the German cascade (surface and intermediate stages all use `{*…}`); English/Dutch still need to be converted.
- Spent most of the session ping-ponging between brace and plain-IPA surface filters; each variant worked in isolation but failed once composed with `GermanReflexes`. The takeaway is that half measures don’t work: either the entire pipeline lives in the brace alphabet (like Burmish) or it will keep collapsing at the final filter.
- We now commit to the brace strategy for Germanic as well. The current files still reflect the older IPA experiments, but the next window will rebuild **every stage** (ProtoWord downward, plus surface filter) so braces are baked in consistently.

### Next plan (next window — brace-first rebuild)
1. Start from `ProtoWord` and reintroduce braces at each German rule, mirroring the Burmish conventions (i.e., every literal surface symbol is wrapped as `{…}` before it leaves its rule block).
2. Recreate `GermanSurfaceVowel/Consonant` in the brace alphabet, making sure the inventory covers all symbols emitted downstream (long vowels, diphthongs, clusters, `{pf}`, `{ts}`, `{ç}`, `{x}`, etc.).
3. Only after the brace-based surface filter composes cleanly with `GermanReflexes` do we rerun `flookup german.bin` for `kniː/broːt/bluːt/tōr` and rerun `server/tools/log_german_stages.sh` to verify everything lines up.
4. With the brace pipeline solid, return to the `{braudą}` long-vowel issue (still dies at `GermanAfterLongV`) and adjust those rules knowing the surface layer is no longer the culprit.

### Findings
- `*knewą` now propagates all the way to `GermanPreSurface` as `{knɪw, knɛw, kniw, kniɔ, kniː}`, so the analyzer gap stems solely from `GermanSurface` still rejecting `{knV}` outputs.
- `*braudą` makes it through `GermanAfterAu` as `{braudą, brōdą}` but vanishes as soon as `GermanLongVowelRules` compose; the long-vowel block (or its contexts) is zeroing out the `{au}` stems.
- `*blōdą` and `*tōr` remain healthy controls (`bloːt/bluːt`, `toːr/tuːr`), matching the prior manual probes.

### Next focus
- Loosen `GermanSurface` / inventory so `{knV}` outputs (and future `{x}/{ç}` cases) pass through to `GermanReflexes`.
- Rework `GermanLongVowelRules` and its neighboring filters so `{braudą → brōdą}` survives past the long-vowel stage instead of collapsing to `???`.

## 2025-10-31

### Services & probes
### German ach-Laut backlog (2025-10-31 follow-up)
- Diagnostics: forms ending in modern `x` such as `laux/knɛxt/mɪlx` still fail because `GermanStopShift` only spirantises `*k` before another consonant or word boundary; it never sees the `*k` when the suffix `*a{z}` is still present. After `GermanAzLoss`, the leftover `{*a}` remains, so the chain produces something like `lauka`, which does not match the UI.
- Plan:
  1. Extend `GermanStopShift` so `*k -> *x` applies before `{*a}{*z}` (and similar suffixal vowels) in `*-kaz/-kiz` paradigms.
  2. Add an apocope rule immediately after `GermanAzLoss` to delete the residual `{*a}` once `{*z}` has gone, yielding the expected ach-Laut codas.
  3. Re-run `server/tools/log_german_stages.sh` with probes `{braudą, laukaz, straumaz, mīlkaz}` and confirm via `flookup` that `laux/knɛxt/mɪlx` now return proto candidates without overgeneration.
  4. Keep weak-tail verbs in the regression set so the new apocope does not undo the recent nasal-tail fixes.

- Containers still running (`docker compose ps`).
- Analyzer checks (post fix): `docker compose exec backend sh -lc "cd /usr/app && printf 'kniː\nbluːt\nbroːt\ndɔr\n' | flookup german.bin"`.
  - `kniː` ⇒ `wąknī/ąknī/kąnī/knąī`.
  - `bluːt` ⇒ `blaut/blōwt/blōt/blūt`.
  - `broːt` now returns `braut`.
  - `dɔr` continues to emit the full `dur` bundle.
- Stage snapshots (`bash server/tools/log_german_stages.sh > /tmp/german_stage_log.txt`).
  - `GermanAfterLongV` now outputs `brūdą` for `braudą`.
  - `GermanPreSurface` shows `brūd/brōd` alongside the existing ew-chain traces.
- Regression harness: `python3 server/tools/api_regression.py` ⇒ PASS for Burmish & Germanic.

### Findings
- Adding `{*au} -> {*ō}` inside `GermanLongVowelRules` keeps `{braudą}` in play; analyzer and staged outputs agree.
- `{durą → dɔr}` remains healthy, so the long-vowel fix didn’t disturb consonant-shift handling.

### Next focus
1. Audit remaining `{au}` contexts to ensure non-coronal environments stay diphthongal after the new rule.
2. Rerun the stage logger + regression harness after any additional tweaks.

### Proto filter follow-up
- Trimmed `pgrmOnsetCore` to the standard singletons, s-clusters, and stop+liquid combos; removed outlier patterns like `{*w}{*w}{*j}` and `{*n}{*x}{*w}{*s}{*t}`.
- Split `pgrmNasalVowel` out of the short-vowel class so we can restrict ą/ę to word-final open syllables; recompiled and confirmed `nę`/`ną` pass while `nęz`/`nąs` are rejected.
- Re-ran `flookup` sanity checks (`kniː/bluːt/broːt/dɔr`) and the API harness (`python3 server/tools/api_regression.py`) — both pipelines still PASS.

### German surface filter (queued)
1. Added `server/tools/collect_german_surface_inventory.py` to pull the segment set from the Stage-3 TSV (with colon→macron and affricate normalisation).
2. Rewrote `GermanSurfaceVowel/Consonant` to use brace tokens populated from that inventory (`{ā}`, `{ɔy}`, `{pf}`, `{ts}`, `{ç}`, `{ʁ}`, etc.) while keeping the ≤3 consonant structure.
3. Recompiled via `foma -f fsts/germanic.txt`, reran `bash server/tools/log_german_stages.sh` and spot `flookup` probes (`broːt/laus/lauf/laux`), then re-ran `python3 server/tools/api_regression.py` — all PASS.

## 2025-10-25

### Services & tests
- `docker compose up -d` (warning: compose `version` key is obsolete).
- Backend reachable at `http://127.0.0.1:5001`; run Caddy via `docs/runbook.md`
  when the UI is needed.
- Regression harness: `python3 server/tools/api_regression.py` ⇒ PASS for both
  burmish/germanic.
- German probes:
  ```bash
  docker compose exec backend sh -c "cd /usr/app && printf 'kniː\nbroːt\nbluːt\ntoːr\n' | flookup german.bin"
  ```
  `kniː`, `broːt`, `bluːt` ⇒ `+?`; `toːr` ⇒ multiple proto outputs.
- Instrumented stages with `foma` (true `apply down`):
  ```bash
  docker compose exec backend sh -c "cd /usr/app && printf 'load stack german_after_longv.bin\napply down knewą\nquit\n' | foma"
  ```
  → `knewą, kniwą, kniuą, kniːą`. After `GermanFinalNasalLoss` the outputs are
  `{knew, kniw, kniu, kniː}`. `GermanPreSurface` yields `{knɪw, knɛw, kniw, kniɔ, kniː}`
  but the final `GermanSurface` filter rejects them, which is why `apply down` on
  `german.bin` still returns `???` for `knewą`.
- Added `server/tools/german_surface_prep.py` as a stop-gap mapper: it splits
  clusters (kn-/pf-/ts-) and wraps each IPA symbol in braces so we can post-
  process `GermanPreSurface` outputs outside the giant FST. Usage example:
  `printf 'kniː\nbroːt\n' | python3 server/tools/german_surface_prep.py`.
  Baking the same logic directly into `server/fsts/germanic.txt` currently hits
  Foma's `Stack full!` limit, so we may eventually need to adopt HFST or split
  the German automaton across multiple files.

### Next focus
- Instrument each German stage (ProtoWord → surface) to capture intermediate
  forms for `*knewą/*braudą/*blōdą`.
- Revisit non-dental `{au}` reflexes and admit `{x}/{ç}` in `GermanSurface` once
  stage logging confirms the choke point.

### Notes
- Documentation index lives in `docs/README.md`; run instructions in
  `docs/runbook.md`.
- Stage logs + surface-filter diagnosis summarized in
  `docs/germanic_transducer_report.md` (2025‑10‑26 update).

## 2025-10-04

### Quick Start Tomorrow
1. Open a fresh terminal window.
2. `cd ~/caprWIP-fresh`
3. Start the services: `docker compose up -d`
   - Rebuild first if desired: `docker compose build`
4. Visit http://localhost:5002 in the browser.
5. Load `burmish-aligned-final.tsv`; the cognate boards and FST editor will then both work.

### Current State
- Latest commits pushed to `update` (most recent: `cd31b59 Interfile glottal-initial board titles`).
- Frontend sorting now trims leading `*`/`?` and interfiles `ʔ`+consonant entries with their plain consonant counterparts; `ʔ`+vowel entries still sort near the end.
- Clean stack: `docker compose up -d` is enough to resume work.

### Tips
- Need to adjust ordering further? Edit `cognate-app/src/App.svelte`, rebuild, and restart.
- To inspect board titles in the UI, open the dev console and check `window.loaded.boards` after loading data.

See you tomorrow!

- Enabled brace-star tokens at the proto layer by removing `RemoveStars` from `GermanProtoInput`; rewrote `GermanEwChain`, `GermanAuMonophth`, and `GermanLongVowelRules` to operate on `{*…}` symbols.
- Added `GermanRemoveStars` immediately after `GermanFinalNasalLoss` so downstream rules still see plain tokens; stage logging now includes both `GermanAfterNasal` (starred) and `GermanAfterStarDrop` (plain) for visibility.
- Updated `GermanHtShift`/`GermanAiShift` contexts to accept star tokens and extended the remover to unwrap `{*ei}` alongside the other brace-star segments.
- Generator still fails on `braudą` in `german.bin` because later rules and the surface filter haven’t been converted yet; brace migration continues in next session.

### Next focus
- Convert the remaining downstream rules (`GermanAzLoss`, vowel adjustments, consonant shift, etc.) so they consume brace-star tokens; push `GermanRemoveStars` as late as possible.
- Rebuild `GermanSurface` as a brace-only filter once the cascade stays in braces; shift any star/brace stripping into the final presentation layer.
- Re-run `server/tools/log_german_stages.sh` and key `flookup` probes after each chunk to confirm analyser/generator symmetry before modifying the surface filter.


- Shifted `GermanRemoveStars` to follow `GermanFinalNasalLoss` after converting that rule to brace-star tokens; stage logging now records `GermanAfterNasal` (starred) before `GermanAfterStarDrop` (plain).
- Converted `GermanHtShift`/`GermanAiShift` contexts to expect star tokens and extended the remover to cover `{*ei}`; downstream stages still operate on plain inventory after the drop.
## 2025-11-30

### Proto gate tightened for diphthongs

- Captured a fresh baseline before touching the proto definitions:
  - `python3 server/tools/api_regression.py` ⇒ PASS for Burmish & Germanic.
  - `python3 tools/trace_german_stages.py --apply-down --stage GermanProtoInput --stage GermanAfterAu --lexeme braudą --lexeme straumaz --lexeme flauxz --lexeme naudiz --lexeme stainaz --lexeme beudan --lexeme liugan --lexeme glaiwaz --lexeme beutan` logged the duplicate `{*a}{*u}` vs `{*au}` outputs for `braudą` only.
- Split the proto weak tails into explicit zero vs. vowel-initial inventories and added `pgrmStrongPlainLight/Heavy` helpers so only heavy syllables (diphthong, long vowel, or short vowel + coda) can precede vowel-headed tails. `pgrmWord` now routes `braudą` through the diphthong path while blocking the `[a] + [u d ą]` parse.
- Recompiled (`docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/germanic.txt'`) and reran the tracer command above: `GermanProtoInput` now emits a single `{*au}` token for every probe, and `GermanAfterAu` shows only the monophthongised branch for `braudą`.
- Analyzer sanity check: `printf 'laux\nknɛxt\nmɪlx\nbroːt\n' | flookup german.bin` still returns the expected proto bundles; `broːt` no longer keeps the `braɔt` branch alive.
- Front-end payloads unchanged: `python3 server/tools/api_regression.py` still passes for both datasets, confirming that the tightened proto gate does not filter out legitimate entries.

### Emergency English rollback

- Restored the production English cascade to the pre-brace definitions so the UI has a working analyzer again. Replaced the brace-aware block in `server/fsts/germanic.txt` with the legacy IPA rules while keeping the sandbox (`server/fsts/english_brace_sandbox.txt`) intact for ongoing experiments.
- Recompiled via `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/germanic.txt'`; the resulting `english.bin` once again has full state/arc counts.
- Regression harness replacement: piped all 362 attested English IPA forms through both stacks. `english.bin` now reconstructs 119 forms (rest still `+?` due to longstanding gaps), while `english_brace_sandbox.bin` remains empty—exactly what we want for comparing future brace work against a functioning baseline.
- Next brace steps stay in the sandbox: feed `pgrmWord`, rebuild brace-aware surface filters, only then swap the finished automaton back into `server/fsts/germanic.txt`.

## 2025-12-01

### Brace sandbox brought online

- Swapped the sandbox cascade onto the brace proto inventory by introducing `EnglishSandboxProtoInput pgrmWord`, rewiring every rule block to consume the `EnglishSandboxStar*` helpers, and pushing `RemoveStars` down to just before the surface filter. `english_brace_sandbox.bin` now compiles as a full 18 kB automaton (195 states / ~8 M paths) instead of the empty 160 byte stub we had yesterday.
- Surface acceptance still mirrors the legacy IPA stack (`EnglishSandboxSurface` expects plain `{b}/{iː}`), but every upstream stage lives entirely in braces so debugging and stage tracing match the German/Burmish pattern. Running the attested-form harness shows 175/362 English IPA forms now reconstruct via the sandbox (production `english.bin` remains at 119/362), giving us a functional brace baseline to compare against.

### Failure inventory & next steps

- Logged the 187 remaining `+?` cases. They cluster around schwa-heavy words (`ə/əʊ` targets such as `bærəʊ`, `fəʊl`, `bɔtəm`), rounded long vowels (`ɔː` in `bɔːl`, `kɔːn`, etc.), and short rounded syllables with `ʊ` (`bʊk`, `brʊk`, `bʊzəm`). These environments currently lack brace-aware mappings in `EnglishSandboxVowelRules`, so the cascade never produces the requested outputs even though the surface filter would admit them.
- Conclusion for tomorrow: add the missing vowel rules (e.g. `{*o}/{*ō}`→`{ɔ}/{ɔː}`, `{*u}`→`{ʊ}` in the relevant contexts, and `{*a}`→`{ə}/{əʊ}` in weak syllables) rather than relaxing the surface filter. After each rule block, recompile and re-run the harness to track how many of the 187 failures drop off. Only once the sandbox meets or exceeds the IPA baseline should we plan the production swap.

### Sandbox vowel expansion

- Introduced `EnglishSandboxStarNasal/Liquid/VelarStop` helpers so the vowel block can target `{*ai}` vs. `{*au}` sequences and the liquid-heavy `{*a}` contexts without repeating literal sets.
- Extended `EnglishSandboxVowelRules` with the first batch of brace-aware mappings:
  - `{*ai}` now yields `{əʊ}` before nasals, velars, labials, and the `gw/kn/xw` clusters that cover the attested `bəʊn/fəʊl/snow/stone/soul/token` cases.
  - `{*au}` exposes an `{əʊ}` branch in addition to `{aʊ}/{oː}`, `{*ō}` can realise `{ɔː}` or `{ʊ}` in the usual `r/l/#` and velar-k environments, and `{*a}` picks up `{ɔː}` before `l/r/w`.
  - Added a dedicated schwa cleanup for the weak-tail templates (`-az/-an/-nē/-gą/-lō/-raz`) so `hammer`, `bottom`, `weapon`, etc. stop stalling solely because the tail vowel stayed as `{a}`.
- `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'` recompiles the sandbox to a 21.7 kB automaton (201 states / 23 M paths). Quick probes such as `printf 'bɔːl\nkɔːn\nfəʊl\nbəʊn\nbʊk\n' | flookup english_brace_sandbox.bin` now return full proto bundles instead of `+?`.
- `python3 server/tools/api_regression.py` still PASS for both Burmish and Germanic datasets, so the extra branches did not perturb the production analyzer.

### Historical staging scaffolding

- Split the vowel stack into `EnglishSandboxCoreVowelRules` (stressed vowels + rounding/raising) and a follow-on `EnglishSandboxLateReductionRules` block that handles the weak-tail schwa conversions. The sandbox now composes these two definitions in series, matching the historical order where vowel quality shifts precede widespread unstressed reduction. No outputs changed, but the pipeline is ready for future WG/ME-era stages without becoming a single monolithic rewrite block.
- Annotated the block with explicit "West Germanic / Old English" and "Late Middle English" comments so the chronological stages are documented directly in the FST, per the Burmish/German style.
- Recompiled (`docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'`), yielding the same surface behaviour as before (20.7 kB / 201 states). Future iterations can introduce West Germanic monophthongisation and ME diphthongisation as separate stages without disturbing the late reduction rules.

### WG monophthongisation stage

- Added `EnglishSandboxWestGermanic` to the cascade (between glide deletion and the vowel rules) so proto `{*ai}`/`{*au}` first collapse onto the historical long vowels `{*ā}`/`{*ō}` before Middle/Modern English rules run. The new stage keeps everything in the proto alphabet—no WGMARK tokens—and mirrors how the German/Burmish stacks segregate their era-specific rule blocks.
- Moved the old `{*ai}`/`{*au}` IPA rewrites onto `{*ā}`/`{*ō}` inside `EnglishSandboxCoreVowelRules`, preserving every contextual mapping we already depend on (`bəʊn`/`stəʊn`/`fəʊl`, etc.) while letting us inspect `{*bān}`, `{*stān}` intermediate outputs.
- `docker compose exec backend sh -lc "cd /usr/app && foma -f fsts/english_brace_sandbox.txt"` now produces a 23.5 kB sandbox automaton (209 states / 32 M paths). Spot checks via `printf 'bəʊn\nstəʊn\nfəʊl\nbɔːl\n' | flookup english_brace_sandbox.bin` show the analyzer surfacing both the WG monophthongised forms (`bān/stān/fāl/bōl`) and the legacy `{*bain}` branches, so we can trace the historical stage outputs directly.

### Great Vowel Shift split

- Broke the downstream vowel block into `EnglishSandboxGreatVowelShift` plus the existing late-reduction stage so the open-syllable long vowels now pass through an explicit `{ɑː}/{oː}` layer before modern diphthongs appear. `EnglishSandboxCoreVowelRules` now stops at `{iː}/{uː}/{ɑː}/{oː}/{ɔː}` outputs, while the new stage handles `{oː → aʊ/əʊ}` and `{ɑː → eɪ/aɪ/əʊ}` with the same environments we already tuned.
- Recompiled again (`docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'`), yielding a 24.0 kB sandbox automaton (213 states / 29.6 M paths). Regression spot checks for `bəʊn/stəʊn/fəʊl/bɔːl` still produce the expected proto bundles plus the new intermediate stages, confirming behaviour stayed constant while the chronology became inspectable.

## 2025-12-02

### Open-syllable lengthening stage

- Added `EnglishSandboxOpenSyllableLengthening` between the West Germanic collapse and the core vowel rules so short `{*a/e/i/o/u}` lengthen whenever they precede a single consonant plus another vowel (e.g., `*nama` now exposes `{*nāma}` before the Great Vowel Shift layer).
- Recompiled via `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'`; `english_brace_sandbox.bin` grows to 30.4 kB (254 states / 32.9 M paths) and the tracer now shows `{*nāma}` / `{*bēra}` intermediate forms alongside the later Modern English reflexes.
- `python3 server/tools/api_regression.py` still PASS for Burmish & Germanic datasets, confirming the new stage doesn’t perturb production analyzers.

### Breaking/rounding stage

- Pulled the `{*a}`→`{ɔː}` liquid/glide rules out of `EnglishSandboxCoreVowelRules` and replaced them with an Anglo-Frisian style `EnglishSandboxBreakingLengthening` stage that rewrites `{*a}` to `{*ō}` before `{*l}/{*r}/{*w}`.
- Recompiled (`docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'`): `english_brace_sandbox.bin` is now 31.0 kB (260 states / 29.3 M paths) and stage logging exposes `{*bōl}/{*bōrd}` outputs prior to the Modern English vowel layers.
- `python3 server/tools/api_regression.py` continues to PASS for both datasets, so the refactor kept the working analyzer stable while making room for future post-vocalic /r/-loss.

### Short-vowel split & weak-tail staging

- Updated `EnglishSandboxCoreVowelRules` to leave short `{*e}`/`{*u}` as `{e}`/`{u}` tokens and inserted a new `EnglishSandboxShortVowelSplit` stage that now pushes `{u}`→`{ʊ}` before velars, weak-tail `z`/`m` clusters, and dark `{l}` codas while handing `{e}`→`{ɪ}` only in nasal/liquid-heavy codas; everything else defaults to `{ɛ}`/`{ʌ}` so the split sits chronologically between the OE core and the Great Vowel Shift.
- Lifted the schwa clean-up rules into `EnglishSandboxWeakTailReductions`, keyed directly to `pgrmWeakTailVowel.r`, and run that stage after the short-vowel split so reductions don’t erase the new conditioning. Recompiling via Docker now yields a 25.1 kB sandbox automaton (223 states / 5.2 M paths) and the regression harness still passes for Burmish & Germanic.
- Spot checks (`printf 'bʊk\nbrʊk\nbʊzəm\n' | flookup english_brace_sandbox.bin`) show `bʊk/brʊk` emitting `bōk/brōk` proto bundles through the new stage, while `bʊzəm` still reports `+?` because the `{u}`→`{ʊ}` rule doesn’t yet cover the `z + weak tail` parse.

### Failure buckets & historical targets

- Bottom-up sweep: `python3 - <<'PY' …` loops the 376 English entries from `server/data/germanic-aligned-final.tsv` through `docker compose exec backend sh -lc 'cd /usr/app && flookup english_brace_sandbox.bin'` and writes `tmp/english_sandbox_results.json`. Current sandbox stats: 119/376 successes (matching the production analyzer) and 257 failures.
- Failure clustering by IPA lines up with the outstanding historical stages: 108 KIT cases (`{ɪ}` in closed syllables), 31 FOOT/STRUT cases (`{ʊ}`), 61 weak-tail schwa outputs (`{ə/əʊ}`), 69 `{r}`-bearing entries still awaiting post-vocalic /r/-loss, and 29 `{ɔ/ɔː}` forms that want better breaking.
- Top-down staging notes before touching code:
  - **Late OE short-vowel conditioning**: finish the FOOT–STRUT stage so `{*u}` first branches to `{ʊ}` in dark-l/velar/alveolar codas, then feeds `{ʌ}` in open or dental contexts; likewise confine the KIT split to nasal/liquid + consonant codas (stop globally rewriting `{e}`).
  - **ME /r/-loss**: add a post-breaking stage that deletes `{r}` after vowels/codas (mirroring historical smoothing) so `{*bōr}` surfaces as `{bɔː}` before Late Reduction derives `board`/`bier` outcomes.
  - **Weak-tail clean-up**: continue driving reductions via `EnglishSandboxWeakTailVowel` so schwa mappings target the templated tails instead of ad-hoc contexts.
- For each block, validate against the relevant bucket from `tmp/english_sandbox_results.json` and log stage traces so the top-down picture stays anchored to the bottom-up error counts.

### TODO (next session)

- Broaden the `{u}`→`{ʊ}` contexts (e.g., `z + weak tail`, alveolar stops) and log which of the remaining `{ʌ}` cases still need special handling so `bʊzəm/pʊt` stop failing.
- Tighten the `{e}`→`{ɪ}` side so KIT only fires in the nasal/liquid clusters we actually attest; add stage logging for representative lez pairs to confirm.
- With the breaking stage in place, start sketching a post-vocalic /r/-loss layer before moving back toward the production cascade swap.

### KIT sweep (status: reverted to baseline)

- Replayed the dockered `flookup` harness (`python3 - <<'PY' …`) to isolate the true KIT cases (filtering out `aɪ/eɪ/ɔɪ`). We still have 35 `{ɪ}` forms headed by `fish/give/six/will` plus the `{ɪə}`+`r` items (`beard/bier/deer/spear/year`).
- Restored the brace-aware helper sets (`EnglishSandboxPlainVocalic/Liquid/Nasal`), the `{*u}` contexts, and `EnglishSandboxPostVocalicRLoss` after rolling back an experimental smoothing stage that tanked the harness. `english_brace_sandbox.bin` is back to the 179/376 success baseline.
- `python3 server/tools/api_regression.py` remains green, so the sandbox is stable again for the next round of KIT work (detailed smoothing + consonant-cluster contexts).

### Short-vowel fixes + /r/-loss scaffold

- Added plain helper sets (`EnglishSandboxPlainVocalic/Liquid/Nasal`) so late-stage rules can reason about the brace-free vowels while still matching against the starred consonants passed along from the proto inventory.
- Reworked `EnglishSandboxShortVowelSplit` to cover the documented FOOT/STRUT environments: `{*u}` now targets `{ʊ}` before velars, `{*z/m/n}` plus weak-tail templates, dark `{*l}`, `{*r}`, and the `{*f}/{*s}/{*θ}` codas (`wolf/wool`), while KIT contexts keep `{*e}`→`{ɪ}` before nasals/liquids. Everything else still falls through to `{ʌ}`/`{ɛ}`.
- Inserted `EnglishSandboxPostVocalicRLoss` (after the vowel stack but before weak-tail reductions) so `{*r}` drops after any plain vowel plus a consonant/word boundary, giving us a chronological hook for the upcoming smoothing work.
- Reran the attested-form sweep (same `python3 - <<'PY' …` harness as above): 179/376 English entries now reconstruct (up from 119), with the failure buckets collapsing to KIT = 61, FOOT = 3, weak-tail schwa = 51, /r/-bearing = 54, and `{ɔ/əʊ}` = 18. Spot checks show `bəʊn/bəʊθ` retrieving `{*bōr}` bundles prior to loss, while known outliers like `bʊzəm` and the irregular `ʋʊl/ʋʊlf` remain on the TODO list.
- `python3 server/tools/api_regression.py` still PASS for Burmish & Germanic after the rewrites, so the sandbox tweaks stay isolated.

### KIT sweep (WIP)

- Fed the KIT bucket through the same dockered `flookup` harness (`python3 - <<'PY' …`) after filtering out diphthongs (`aɪ/eɪ/ɔɪ`). The remaining 35 entries are the genuine `{ɪ}` cases headed by `fish/give/six/will` alongside the `{ɪə}` + post-vocalic /r/ cohort (`beard/bier/deer/spear/ year`, etc.).
- Updated `EnglishSandboxCoreVowelRules` so short `{*i}` finally drops its star and enters the plain alphabet, and extended `EnglishSandboxShortVowelSplit` with `{i}`→`{ɪ}` rewrites in closed syllables / word-final contexts. This keeps the KIT conditioning in the same stage as the `{*e}`/{`*u`} splits instead of leaving `{*i}` untouched.
- The attested-form harness still lands at 179/376 successes (KIT bucket = 35) because the stubborn cases need post-vocalic /r/ smoothing (`{ɪ}`→`{ɪə}` before the new `EnglishSandboxPostVocalicRLoss`) or suffixal analogies (`sieve/singe/timber`). Logged them here so the next pass can target `{ɪə}` outputs without sacrificing the `{bəʊn}/{fʊt}` improvements we just landed.

## 2025-12-04

### KIT/FOOT contexts + /r/-smoothing harness

- Extended EnglishSandboxShortVowelSplit so FOOT now targets alveolar codas in both starred and plain alphabets ({t/d/z} + weak-tail templates, plain {l/r} codas) and added a plain {*i}->{i} feed so the KIT split can finally act on closed {i} syllables. Introduced EnglishSandboxPostVocalicRSmoothing between the vowel stack and /r/-loss so {ɪ} can surface as {ɪə} before EnglishSandboxPostVocalicRLoss deletes {r}.
- Recompiled via docker compose exec backend sh -lc "cd /usr/app && foma -f fsts/english_brace_sandbox.txt" and wrote the attested-form sweep to tmp/english_sandbox_results.json with the Python harness (loops 376 English IPA forms through flookup english_brace_sandbox.bin).
- Current sandbox stats: 134/376 successes (down from the previous 179 baseline). Failure buckets from the JSON lens land at KIT=49, FOOT=21, weak-tail=44, post-vocalic /r/=58, rounded {ɔ/əʊ}=28, plus 118 uncategorised other items that need triage.
- Spot checks show the new /r/ smoothing exposes {bird/birr} for bɪəd/bɪər, but bʊzəm and pʊdər remain +? even after the broader {u} contexts. Need to audit why so many previously good entries dropped during this pass before attempting further vowel work.

### KIT tracing & stage export plan

- Added  as a first pass at stage tracing, but the sandbox stages currently emit ??? because the cascade never saves intermediate automata. Full traces will require refactoring the FST to save each stage (similar to the GermanAfter* bins) so we can flookup them directly inside Docker.
- Next session: split out the sandbox stages into explicit save targets (e.g., english_sandbox_after_glide.bin, english_sandbox_after_vowel_rules.bin), update the docker build to emit those bins, and then rerun the tracer to capture true stage-by-stage outputs for KIT words (*fiskaz, *gebaną, *swestēr).
- Once tracing works, resume the KIT fixes bucket-by-bucket (post-vocalic /r/, {sk} palatalisation, nasal+stop, sw glides) with harness checks after each change so we stay ≥179/376.
## 2025-12-12

### English gold IPA normalized to RP / non-rhotic baseline

- Cleaned every English row in `server/data/germanic-aligned-final.tsv` whose counterpart contains an orthographic `r` but whose surface tokens still ended in a vowel + `r`. Each of the 40 affected entries now drops the trailing `r` (e.g. `adder ædər→ædə`, `fire faɪər→faɪə`, `door dɔːr→dɔː`). Mirrored the same edits into the staged snapshot (`server/pipeline/output/germanic/stage3/germanic-aligned-final.tsv`) so downstream docs stay in sync.
- Added `server/tools/validate_english_rhoticity.py` to guard the policy going forward. The helper scans any TSV for English rows where the tokens end in `…V r` and fails fast; CI/local runs should call `python3 server/tools/validate_english_rhoticity.py` (optionally pointing it at the stage3 export) whenever the gold data changes.
- Reran the validator on both the canonical and stage3 TSVs — both now report “No rhotic entries detected.” Next time the gold file is touched, run the validator before committing so we don’t regress toward GA-style outputs again. Once the analyzer tweaks land, rerun `python3 server/tools/english_apply_down_stats.py` to confirm the RP-aware surfaces align with the updated targets.

### Rhotic development roadmap (historical targets before coding)

- **Proto rhotic fronting / colouring.** Replace the `{*rgă→rəʊ}` placeholder mindset with staged vowel shifts that mirror the historical chronology.
  - Pre-OE: specify how `{*er}` becomes `{æər}/{ɜːr}`, `{*ir}` becomes `{ɪr}`, `{*or}/{*ur}` becomes `{ɔːr}` before any breaking occurs. List the actual proto clusters (`rdă`, `rgă`, `rwō`, `rθo`, …) so the rules operate on contexts rather than word lists.
  - OE breaking: document the environments that should introduce `{ea/eo/ia}` diphthongs so ME smoothing can later yield RP `ɪə/ɛə/ɜː` without hard-coded outputs.
  - ME smoothing + post-vocalic /r/ loss: describe the sequence (breaking → smoothing → /r/ loss) so `EnglishSandboxRhoticBreaking`/`RhoticColoring` can implement the correct order once we update the rules.
### Modern English (OE→Modern) roadmap — paused
- These steps are intentionally separated from PGmc→OE work; only resume if explicitly requested.

- **Consonant resolution.** Note explicitly why RP keeps /θ/ in `earth/hearth` but /d/ in `herd/word/sword` (OE retention vs. later analogical leveling). The current single-output rewrite matches the intended behaviour, but the reasoning should be recorded so future edits don’t reintroduce branching.
- **Weak-tail & schwa preservation.** RP retains final /ə/ in orthographic `-er/-re` endings (`faɪə`, `ædə`). Outline which morphological endings should keep vs. drop the schwa so `EnglishSandboxWeakTailCleanup` can be rewritten with historical cues instead of deleting every `{*ə}` at word end.
- **Next execution steps:** once the above roadmap is nailed down, implement the stages in order (ProtoRhoticFronting → OE breaking/smoothing → Post-vocalic /r/ loss → Weak-tail cleanup). After each change, rerun `python3 tools/trace_english_sandbox.py --lexeme-file tmp/rhotic_test_set.txt --brace-diphthongs` and `python3 server/tools/english_apply_down_stats.py` to measure progress beyond the current 21/376 baseline.

#### Detailed blueprint (grounded in the standard OE/ME chronology)

- **Anglian colouring before breaking (pre-7th c.).**
  - `{*e}` in `{*er}` clusters should front/back toward `{æɑr}` so the later OE breaking produces `ea`. Limit this to `{*r}` followed by a consonant or boundary; leave glide environments alone so `seer`-type words stay bright.
  - `{*i}` in `{*ir}` (except before `{*j}`) lowers to `{*er}` then `{*æɑr}`, matching the documented change that feeds `bird`, `first`, etc.
  - `{*o}`/`{*u}` before `{*r}` should raise to `{*ur}/{*ɔːr}` only when followed by a consonant, mirroring WG rounding that later yields RP /ɔː/.
  - Capture these contexts in `EnglishSandboxProtoRhoticFronting` so OE breaking has the right inputs.

- **OE breaking + ME smoothing.**
  - Add an `EnglishSandboxOEBreaking` stage: `{æ}` → `{ea}` before `{*rC}` or `{*lC}`, `{e}` → `{eo}` before `{*rC}`, `{i}` → `{ie}` before `{*rC}`. These match the conditions in Campbell §§216–219 and explain why `bear/bier` diverge from `bar`.
  - Follow with an `EnglishSandboxMESmoothing` stage (before post-vocalic /r/ loss) that maps `{ea/eo/ie}` + `{*r}` to the RP nuclei: `{ea}` → `{ɛə}`, `{ie}` → `{ɪə}`, `{eo}` → `{ɜː}` (voicing-dependent). This should replace the lexeme-specific rewrites currently living in `EnglishSandboxRhoticBreaking`.

- **Consonant outcomes.**
  - Document the historical split: native `{*rθ/ð}` clusters retain /θ/ in RP (`earth/hearth`), while `{*rd}` words level to /d/ in late ME (`herd/word/sword/bird`). Keep the Foma rule single-output but annotate these buckets so we know why the mapping exists and where it should apply.

- **Weak-tail schwa.**
  - RP keeps schwa in orthographic `-er/-re` (from OE `-ere`). Plan to guard those endings via a morphological check (e.g., look for `{*r}` + weak-tail vowel) so `EnglishSandboxWeakTailCleanup` only drops `{*ə}` when the historical dialect really loses it.

- **Execution order reminder.**
  1. Implement the contextual colouring rules in `EnglishSandboxProtoRhoticFronting` (using the `list_rhotic_contexts.py` inventory as a sanity check) and verify via tracer that `{*bergą/*bardaz/*barwōn}` take the correct vowels before breaking.
  2. Introduce the explicit OE breaking + ME smoothing stages, removing the hacky `{*rgă→rəʊ}` rewrites from `EnglishSandboxRhoticBreaking`.
  3. Revisit `EnglishSandboxRhoticBreaking` only after the vowel stages are in place so it simply handles consonant selection (θ vs. d) and any remaining diphthong adjustments.
  4. Redesign the weak-tail cleanup to respect RP schwa retention.
  5. After each milestone, rerun the rhotic tracer and `english_apply_down_stats.py` to ensure we stay branch-free and track improvements beyond the current 21/376 exact matches.

### Old English staging / TSV overhaul (PGmc → OE layer)
- Completed and superseded; see the 2025-12-21 consolidated PGmc→OE TODOs for current work.
- Open question: should the TSV adopt PGmc **ǭ** (e.g., *rindǭ*) instead of the current **ō**-only convention? For now we normalized to **ō** to keep the dataset consistent; revisit if we decide to shift the entire PGmc orthography.

## 2025-12-12

### Old English data population
- Added a Wiktionary scraper (`server/tools/fetch_old_english_from_wiktionary.py`) and parsed the Swadesh + API data into `server/data/old_english_wiktionary.tsv`; the updater now merges both sources and writes IPA/tokens/notes back into the aligned Germanic TSVs.
- Ran the helper across all 376 English concepts so the Old English rows now have attested lemmas (373 entries auto-filled; annotated `fodder fōdor` and `tongs tange` manually, marked `knob` as lacking an OE cognate per the etymology).
- Documented the workflow in `README.md` + `docs/runbook.md`, and added `server/tools/validate_old_english_pairs.py` to guard the 1:1 English↔OE coverage going forward.

- **PGmc→OE stage split.** Added `EnglishProtoToOE` inside `server/fsts/germanic.txt` so the early vowel/weak-tail rules share a single hook and tracer snapshot (`english_after_proto_to_oe.bin`).

### Proto→OE instrumentation & findings (2025-12-12)
- Consolidated the early PGmc→OE vowel/weak-tail rules under `EnglishProtoToOE` and added the `english_after_proto_to_oe.bin` stage log so we can trace that layer independently of the later ME/RP stack.
- Wrote `server/tools/evaluate_proto_to_oe.py` and ran it against `english_after_proto_to_oe.bin`: only 1/376 Old English rows matched at that time; this baseline is superseded by the 2025-12-21 diagnostics (see current focus above).
- Next coding steps now live in the consolidated PGmc→OE TODOs under 2025-12-21.

## 2025-12-21

---

*End of paused Modern English sandbox diary. OE-focused diary entries follow.*

---

## 2025-12-21

### Old English core refactor + diagnostics
- Split the English pipeline into `OldEnglishCore` + `EnglishOEToModern` so the OE transducer is not just an alias of Modern English (`server/fsts/germanic.txt`).
- Added OE-specific surface filter and orthography: `OldEnglishSurface`, `OldEnglishRemoveStars`, `OldEnglishOrthography` now apply at the end of the OE stack (including `x -> h`, `θ -> þ`, `ʃ -> ċ`).
- Phonological tweaks in the PGmc→OE block:
  - Removed blanket final *a apocope; retained only `*ą/*ă -> *a` (per high-vowel apocope focus).
  - Added `OldEnglishSkPalatalization` (`*sk -> ʃ` before front vowels).
  - Added a conservative high-vowel apocope rule for final `*i/*u` after heavy or two-light syllable patterns (approximate segmental conditioning; still needs refinement).

### PGmc→OE TODOs (consolidated)
- **Separation model:** Old English is its own doculect with a PGmc→OE stack (`OldEnglishCore` + OE surface/orthography). Modern English is a separate doculect with an OE→Modern stack (`EnglishOEToModern`), and OE work should not use ME/RP rules.
- **Definition locality (housekeeping):** move PGmc→OE rule definitions so they live adjacent to the OE stack (mirroring how Dutch-specific rules sit near the Dutch stack), instead of being scattered among Modern English rule blocks.
- **Proto gate coverage:** `xw/hw` clusters already pass `EnglishProtoInput`; remaining ProtoInput failures are elsewhere (e.g., `*xabukăz`, `*xemenăz`, `*xnakkăz`, `*regna-bugōn`, `*sumerăz`). Focus on missing onset/weak‑tail clusters, not `xw/hw`.
- **High‑vowel apocope expansion:** broaden final `*i/*u` deletion beyond the current “long/diphthong + C” and “two light syllables” conditions; target observed `-i/-u` outputs (e.g., `ballu/bebru/balgi/bugu/crafti/fehu/felþu`) while staying phonetic.
- **Weak‑tail cleanup (`-ana` → `-an`):** reshape or drop weak‑tail `ă/ą` endings in verbs so outputs like `bacana/gennana/brecana/brengana/brūcana` converge on attested `-an`.
- **OE consonant innovations:** add the missing PGmc→OE consonant changes (palatalisation in OE contexts, rhotic prep, targeted lexical replacements) so stage outputs align with `COUNTERPART` without using ME/RP rules.
  - Early final‑ă apocope (post‑z deletion) now in place; `*dagăz` yields `dæġ`. See potential side‑effects list at `docs/debug_snapshots/oe_final_a_apocope_side_effects_2025-12-23.txt`.
- **Validation loop:** after each change, rerun the OE evaluator (`python3 tools/evaluate_proto_to_oe.py --bin old_english.bin`) and keep `docs/debug_snapshots/` traces for regressions.

### PGmc→OE chronology audit (2025-12-21)
- **Sources consulted (web, Dec 21 2025):**
  - Wikipedia: *Phonological history of Old English* (breaking/back mutation, high‑vowel loss, h‑loss, syncopation ordering).
  - Wikipedia: *Ingvaeonic nasal spirant law* (nasal loss before fricatives + compensatory lengthening).
  - Wikipedia: *Old English phonology* (palatalization/velar vs palatal distributions).
  - Cambridge Core: *Reconstructing the historical phonology of Old English* (debate over standard chronology of fronting/breaking).

- **Reference timeline (condensed, with known debates):**
  - i‑umlaut (front mutation) precedes many OE alternations; later syncopation and vowel loss are ordered after it in standard accounts. 
  - Breaking/retraction of front vowels before h, rC, lC (and some w contexts) is dialect‑conditioned and not uniform across OE. 
  - Ingvaeonic nasal spirant law deletes nasals before fricatives with compensatory lengthening (‑ns‑, ‑nþ‑, ‑mf‑). 
  - Back mutation (u‑umlaut) diphthongizes short e/i (sometimes a) before back vowels in the following syllable, with strong dialect differences. 
  - High‑vowel loss deletes unstressed i/u after heavy syllables (long vowel/diphthong or closed syllable), but not after light syllables. 
  - H‑loss and contraction occur after breaking in standard accounts; vowel contraction follows h‑loss.
  - Palatalization of velars (k/g, and sc) before front vowels yields ċ/ġ alternations and later phonemic splits.

- **What our current PGmc→OE stack already models:**
  - WG monophthongisation (*ai/*au → *ā/*ō).
  - Open‑syllable lengthening.
  - Anglo‑Frisian breaking/rounding before liquids, r, and w.
  - Velar shortening of *ō; u‑rounding before r.
  - Weak‑tail marker/reduction; conservative high‑vowel apocope.
  - *sk‑palatalisation before front vowels.

- **Major gaps vs. the reference chronology (priority‑ordered):**
  1. i‑umlaut is absent (core OE morphology driver).
  2. Back mutation (u‑umlaut) is absent and dialect‑sensitive.
  3. Ingvaeonic nasal spirant law is absent and should affect vowel length and nasal loss.
  4. High‑vowel loss conditioning is under‑applied relative to heavy vs. light syllable split.
  5. H‑loss + contraction are missing, and the timing vs. breaking is not modeled.
  6. Breaking/back‑mutation order and dialect conditioning are not modeled; current rules are too broad.
  7. Palatalization of velars beyond *sk (k/g before front vowels; ċ/ġ outcomes) is missing.

- **Immediate next steps (OE‑only, chronological order):**
  1. Add i‑umlaut with clean conditioning; trace impact on OE counterparts.
  2. Add back‑mutation (u‑umlaut) with conservative, dialect‑agnostic defaults.
  3. Add Ingvaeonic nasal spirant law + compensatory lengthening.
  4. Re‑specify close‑vowel loss to match heavy vs. light syllable conditioning.
  5. Add h‑loss and contraction; re‑check breaking order afterward.
  6. Add palatalization for velars before front vowels (ċ/ġ), not just *sk.

### OE evaluator snapshot (old_english.bin)
- Total OE rows: 376
- Matches: 2
- No output: 21
- Mismatches: 353
- Sample mismatches: `*bakăną -> bacana` vs `bacan`, `*bōkō -> bucō` vs `bēċe`, `*balgiz -> balgi` vs `bielġ`.
- Common issue bucket still dominated by `-ana` outputs and lingering final high vowels.

### Ending diagnostics (old_english.bin)
- Final vowel distribution: `a` 212, `n` 43, `ō` 33, `i` 22, `u` 20.
- Final high vowels: `i` 22, `u` 20; most common contexts `ti/di` for `-i`, `þu/du/tu` for `-u`.
- Sample `-i/-u` outputs: `ballu` (ball), `bebru` (beaver), `balgi` (belly), `crafti` (craft), `bugu` (bough).
- Sample `-ana` outputs where target is `-an`: `bacana` (bake), `gennana` (begin), `brecana` (break), `brengana` (bring), `brūcana` (brook).

### OE diagnostics refresh (2025-12-21)
- Recompiled FSTs and reran `tools/evaluate_proto_to_oe.py` against `old_english.bin`; totals unchanged (Matches 2 / No output 21 / Mismatches 353). Snapshot: `docs/debug_snapshots/oe_eval_2025-12-21.txt`.
- Recomputed final‑vowel distribution + `-i/-u` contexts; counts unchanged and examples still dominated by final high vowels and `-ana` endings. Snapshot: `docs/debug_snapshots/oe_final_vowel_diag_2025-12-21.txt`.

## 2025-12-21 (plan update: regular sound change only)

### Guiding assumption (Hill 2014)
- Sound change is regular and phonetically conditioned; apparent grammatical conditioning is modeled as regular sound change plus analogy/borrowing. We encode only the regular phonological development in the FSTs.

### New diagnostics captured
- `docs/debug_snapshots/oe_tail_bucket_2025-12-21b.txt`: lists all `-i`, `-u`, `-ana` outputs with proto + attested OE.
- `docs/debug_snapshots/oe_tail_bucket_classified_2025-12-21b.txt`: classifies `-ana` outputs by attested OE ending (e.g., `-an`, `-ian`, `-can`, `other`).
- `docs/debug_snapshots/oe_high_vowel_targets_2025-12-21b.txt`: classifies `-i/-u` outputs by attested OE final (vowel vs consonant).
- `docs/debug_snapshots/oe_high_vowel_weight_diag_2025-12-21b.txt`: estimates heavy vs light syllable before final `-i/-u`.
- `docs/debug_snapshots/oe_ana_noninfinitive_2025-12-21b.txt`: isolates `-ana` outputs with non‑infinitive attested endings (must not be deleted by OE sound change).

### Next steps (phonological only, no morphological conditioning)
1. **High‑vowel loss (regular):** use the weight diagnostics to implement a heavy‑syllable‑conditioned final *i/*u apocope. Prefer explicit heavy/light marking (H/L) inserted by segmental context, then delete markers after the rule; avoid morphological categories.
2. **Weak‑tail *a (schwa) handling:** do **not** blanket delete `-ana` in PGmc→OE. Only apply any *a loss if a purely phonological environment deletes it without touching the non‑infinitive list; otherwise defer to later (OE→ME) as analogical leveling.
3. **Umlaut/back‑mutation sanity check:** confirm the new umlaut/back‑mutation rules apply only in phonological environments (following *i/*j or back vowels/w) with a small probe list; tighten triggers if over‑application appears.
4. After each change: rebuild via Docker, rerun OE evaluator + the two diagnostics, and snapshot in `docs/debug_snapshots/`.

### High‑vowel loss debug (2025-12-21)
- Found nondeterminism in the new H‑marker rule: `OldEnglishWeightMarkers` was inserting `{H}` in multiple optional positions, yielding both apocopated and non‑apocopated outputs (e.g., `ballu` + `ball`).
- Fixed by rewriting final `*i/*u` directly to `{H}{*i}/{H}{*u}` in heavy contexts, then deleting `{H}{*i}/{H}{*u}` in `OldEnglishHighVowelApocope`.
- Added stage bins to isolate the fix:
  - `english_after_proto_to_oe_weak_tail.bin`
  - `english_after_proto_to_oe_weight_markers.bin`
  - `english_after_proto_to_oe_apocope.bin`
  - `english_after_proto_to_oe_weight_cleanup.bin`
- Verification (sample probes): `balluz/balgiz/bebruz` now yield a **single** output at each stage, with apocope firing deterministically in heavy contexts.
- Updated diagnostics:
  - `docs/debug_snapshots/oe_eval_2025-12-21e.txt` (Matches 8 / No output 18 / Mismatches 350).
  - `docs/debug_snapshots/oe_final_vowel_diag_2025-12-21e.txt` shows **0** final `-i/-u` outputs after the heavy‑syllable apocope.

### OE weak‑tail marker fix (2025-12-21)
- Renamed `EnglishWeakTailMarker/EnglishWeakTailReduction` to `OldEnglishWeakTailMarker/OldEnglishWeakTailReduction` and confined them to marking only the weak‑tail vowel.
- Old behaviour collapsed `*a n(n) ą` into a single `{*ă}`, deleting the `n(n)` cluster (e.g., `*banną → *ba` in `ProtoToOE`), which violated the “no blanket -ana deletion” policy.
- New marker rules only rewrite `*n/*m + *ą` to `*n/*m + *ă`, so `*banną → *banna` at `ProtoToOE` and the tail stays intact for later, phonologically justified cleanup.
- Recompiled `fsts/germanic.txt` + `fsts/old_english_sandbox.txt` and captured:
  - `docs/debug_snapshots/oe_eval_2025-12-21g.txt` (Matches 5 / No output 11 / Mismatches 360).
  - `docs/debug_snapshots/oe_apply_down_stats_2025-12-21g.txt` (apply‑down coverage snapshot).
  - `docs/debug_snapshots/oe_tracer_log_2025-12-21g.txt` (OE sandbox tracer).

### OE weak‑tail nasal vowel loss (PGmc *‑aną → OE ‑an) (2025-12-21)
- Replaced the heavy‑syllable apocope experiment with a chronologically correct PGmc→OE rule: drop final `*ą` after `*n`/`*m` at word‑end, then reduce remaining `*ą/*ă` to `*a`.
- This targets the early loss of final nasal vowels (infinitive `*‑aną → ‑an`) without touching the later loss of final `‑n`.
- Diagnostics (post‑change):
  - `docs/debug_snapshots/oe_eval_2025-12-21j.txt` (Matches 13 / No output 11 / Mismatches 352).
  - `docs/debug_snapshots/oe_apply_down_stats_2025-12-21j.txt` (apply‑down coverage snapshot).
  - `docs/debug_snapshots/oe_tracer_log_2025-12-21j.txt` (OE sandbox tracer).
- `docs/debug_snapshots/oe_tail_bucket_2025-12-21j.txt` + `oe_tail_bucket_classified_2025-12-21j.txt` (tail bucket after nasal‑vowel loss).
- Note: the tail bucket still contains `swan` (`*swanăz → sʋana`), which is not from `*‑aną`; flag for later review of `*‑ăz` handling.

### OE diagnostics follow‑up: orthography + rhotacism (2025-12-22)

- Updated `server/tools/evaluate_proto_to_oe.py` to default to `old_english.bin` (post‑orthography + surface filter). New totals: Matches 24 / No output 18 / Mismatches 334.
- Comparing `english_after_proto_to_oe.bin` vs `old_english.bin` shows 7 items lose outputs only after the OE surface filter; all 7 still contain `{*z}` (or heavy clusters) and are rejected by `OldEnglishSurfaceConsonant` (no `z`).
- Tracing those 7 (`bazją`, `deuzą`, `xazwăz`, `xuzdą`, `liznōjăną`, `mizdō`, `funxwstiz`) shows `EnglishZRhotacism` never fires; `ConsonantRules` leaves `{*z}` intact in every case.
- Likely structural issue: `EnglishStarVocalic` (and other `EnglishStar*`) are defined before `GermanStar*` and appear to compile as literal symbols (foma logs show 1‑arc sets), so the rhotacism context never matches.
- Even if the set is fixed, the current rule `V _ V` is historically too narrow: PGmc *z should rhotacize in post‑vocalic contexts like V‑z‑j/w/n/d‑V (berry, hair, learn, meed, hoard) before later glide/umlaut changes. Chronology: rhotacism must be early (before w‑glide changes and OE vowel rules).
- `funxwstiz` (fist) is not a rhotacism case; it survives with a heavy `xʋst` cluster and fails the OE surface coda limit (needs separate cluster simplification / h‑loss logic).

### OE sandbox mismatch patterns (2025-12-22)
- **Scope note:** work is focused on the **OE sandbox** for now; do not apply ME/RP fixes to these issues.
- **Mismatch pattern sweep (summary):**
  - Missing i‑umlaut/fronting (most frequent).
  - Missing palatalization (ċ/ġ outcomes absent).
  - Missing breaking/diphthongs (eo/ie).
  - Missing final ‑e.
  - Missing final ‑n (including infinitive ‑an).
- **OE sandbox TODOs (from mismatch patterns):**
  1. **I‑umlaut/fronting:** broaden or re‑order triggers so OE front vowels appear where expected.
  2. **Palatalization:** add/repair k/g → ċ/ġ before front vowels (and ordering vs. umlaut).
  3. **Breaking:** strengthen OE breaking contexts (before r/l/h clusters, etc.).
  4. **Final ‑e retention:** prevent weak‑tail cleanup from removing OE final ‑e where attested.
  5. **Final ‑n retention:** ensure infinitive/weak verb ‑an survives; confirm no over‑drop after nasal‑vowel loss.

### OE i‑umlaut status (2025-12-22)
- **What we added:** expanded `OldEnglishIUmlaut` to cover `*æ → *e`, `*e → *i`, and `*ū → *ȳ`; added `*ȳ` to starred vowel inventories + `OldEnglishRemoveStars`.
- **What works now (ordering probe):** i‑umlaut fires inside the PGmc→OE block before weak‑tail cleanup/apocope (e.g., `mūsiz → *m*ȳ*s`, `brūdiz → *b*r*ȳ*d`, `fōtiz → *f*ē*t`). Snapshot: `docs/debug_snapshots/oe_iumlaut_ordering_probe_2025-12-22.txt`.
- **What is still missing:** fronting/raising does not trigger in many common i/j contexts (`laubjăną`, `sandjăną`, `bazją` still un‑fronted), so the **trigger environment is still too narrow** and diphthong umlaut (ea/eo → ie/īe) is not modeled yet.
- **Resources & probes already available:**
  - Ordering probe: `docs/debug_snapshots/oe_iumlaut_ordering_probe_2025-12-22.txt`
  - Full‑set i/j‑trigger probe: `docs/debug_snapshots/oe_iumlaut_fullset_probe_2025-12-22.txt`
  - Candidate list (heuristic i/j triggers): `docs/debug_snapshots/oe_iumlaut_candidates_2025-12-22.txt`
- **Next steps:** relax the right‑context for i‑umlaut (beyond `EnglishStarConsonantSeq` where needed), add diphthong umlaut rules (ea/ēa, eo/ēo → ie/īe), and re‑run the full‑set probe + OE apply‑down stats to check for over‑application.

### OE breaking reorder + diagnostics (2025-12-22)
- **Breaking now precedes GH‑marking and W‑glide** so the conditioning consonants are still visible when OE breaking applies; this matches the chronology (breaking before h‑loss and before later glide re‑analysis). Implemented in both `server/fsts/germanic.txt` and `server/fsts/english_brace_sandbox.txt`.
- **Sandbox breaking rules aligned to OE** (`*a/*æ → *ea`, `*e → *eo`, `*i → *ie` in rC/lC/h/w contexts). This replaced the old `{*a → *ō}` placeholder.
- **Tracer instrumentation updated** to include `WGlide` and rebuilt the per‑stage bins; new probe log: `docs/debug_snapshots/oe_breaking_probe_2025-12-22f.txt` (shows `*bergą → *eo`, `*bardăz → *ea`, `*erθo → *eo`, `*fextăną → *eo` at `BreakingLengthening`).
- **Regression scan (OE apply‑down):** `docs/debug_snapshots/oe_apply_down_stats_2025-12-22p.txt` shows 22 exact matches / 370; mismatch buckets still dominated by i‑umlaut/fronting and missing breaking/diphthongs.

### OE i‑umlaut deep dive (2025-12-23)
- **Targeted umlaut misses (tight heuristic):** only 3 suspected true i‑umlaut failures when PGmc has an i/j trigger and OE expected shows an umlauted vowel but output does not. See `docs/debug_snapshots/oe_i_umlaut_deep_dive_2025-12-23.txt`.
  - `*rugiz` → expected **ryġe**, output **rūġ** (u‑umlaut miss)
  - `*jugunθiz` → expected **ġeoguþ**, output **ġūgyþ** (u‑umlaut miss)
  - `*sōkjăną` → expected **sēċan**, output **suscġan** (ō‑umlaut miss)
- **Palatalization warning:** cases where expected **ċ** surface as **sc** are now visible; that’s a palatalisation failure in the OE stack (orthography is masking it), not a spelling preference. Keep an eye on outputs like `suscġan` vs expected `sēċan`.

### OE palatalization vs fronting/umlaut split (2025-12-23)
- **Snapshot:** `docs/debug_snapshots/oe_palatal_vs_fronting_split_2025-12-23.txt`.
- **Key diagnosis:** the 7 “palatalization missing” cases are **not** palatalization-rule failures; palatalization never triggers because the **front‑vowel context is missing**. These are **fronting/breaking/umlaut issues** upstream.
- **True i‑umlaut misses (strict trigger):** only 1 case (`*rugiz → ryġe` expected, output `rūġ`).  
  The bulk of the “i‑umlaut/fronting missing” bucket is actually **fronting missing with no i/j trigger** (143 cases).
- **Next actions:** prioritize fronting/breaking changes that create front‑vowel contexts (esp. for *bōkō, *θankăz, *dranką, *fleugăną, *xunăgą), then re‑check palatalization buckets.

### OE i‑umlaut/fronting bucket diagnostics (2026-01-01)
- **RemoveStars fix:** added `{*ċ} -> ċ` and `{*ġ} -> ġ` in `OldEnglishRemoveStars` so orthography outputs no longer leak starred palatals. This dropped `no_output` mismatches from 50 → 12.
- **Updated apply‑down stats:** `docs/debug_snapshots/oe_apply_down_stats_2026-01-01a.txt` (still 40 exact matches / 370 total).
- **Top buckets:** i_umlaut_or_fronting_missing (147), other (124), breaking_missing (30), no_output (12), long_vowel_missing (10).
- **Bucket subgrouping (heuristic, broader set = 178 items):** `docs/debug_snapshots/oe_iumlaut_fronting_subgroups_2026-01-01.txt`.
  - back_vowel_follow_only: 98 (likely **a‑restoration** contexts per Hogg)
  - iumlaut_trigger_only: 3 (cleanest true i‑mutation misses)
  - nasal_block_only: 2 (fronting blocked before nasals)
- **Staged traces for each subgroup:** `docs/debug_snapshots/oe_iumlaut_fronting_subgroup_traces_2026-01-01.txt`.
  - i‑mutation trigger examples: *furxtīn → fōrhtīn (expected fryhtu), *raukiz → reaċ (expected rēc), *rugiz → rūġ (expected ryġe)
  - back‑vowel follow examples: *bergą → beorga (expected beorg), *bōkō → bucō (expected bēċe), *gennăną → ġennan (expected beginnan)
  - nasal‑block examples: *dranką → drænca (expected drenċ), *tangō → tængō (expected tange)

### OE ai cleanup + ǣ surface fix (2026-01-01)
- Removed `OldEnglishAiMonophthongization` (never fires because WG monophthongization already rewrites *ai → *ā).
- Added `{*ǣ} -> ǣ` to `OldEnglishRemoveStars` so OE surface accepts long fronted a (e.g., *dailiz → dǣl, *xaiθiz → hǣþ).
- Updated mismatch totals (post-fix): Total mismatches 324; i_umlaut_or_fronting_missing 22; breaking_missing 18; long_vowel_missing 30; palatalization_missing 17; other 225; no_output 12.
- New snapshot: `docs/debug_snapshots/oe_stage_traces_2026-01-01i.txt`.

### OE diagnostics: mismatch closeness + diacritics (2026-01-02)
- Apply-down stats (latest run): `docs/debug_snapshots/oe_apply_down_stats_2026-01-02h.txt`
  - Exactly one correct output: **64 / 370** (no_output 12; multiple outputs 0).
  - Mismatch buckets: i_umlaut_missing_true 16; fronting_missing_no_trigger 33; breaking_missing 20; long_vowel_missing 6; palatalization_missing 3; other 216.
- **Closeness scan** highlights that many mismatches are near-misses:
  - `docs/debug_snapshots/oe_mismatch_closeness_2026-01-02a.txt` shows most mismatches at distance 1–2 (81 at dist=1, 112 at dist=2).
  - `docs/debug_snapshots/oe_mismatch_closeness_norm0_2026-01-02.txt` lists 11 cases where normalized (diacritic-stripped) distance is 0, e.g. `*dōną → dōn` vs expected `don`, `*etăną → ētan` vs `etan`, `*fiskăz → fisc` vs `fisċ`, `*skīnăną → scīnan` vs `sċīnan`.
- **Diacritic mismatch traces** (`docs/debug_snapshots/oe_diacritic_mismatches_traces_2026-01-02.txt`) confirm these are orthography/diacritic alignment issues rather than phonology failures (e.g., `*tredăną → trēdan`, `*sturmăz → stōrm`, `*θurnuz → þōrn`, `*fadēr → fædēr`).
- **Long-vowel missing probe narrowed** to 6 items (previously 7):
  - Current list: `*kewwăną → ċeowwan (expected ċēowan)`, `*xazwăz → hærw (expected hǣr)`, `*xattuz → hatt (expected hōd)`, `*end → end (expected ān)`, `*slaxăną → sleaan (expected slēan)`, `*wegăz → weġ (expected wē)`.
  - Traces in `docs/debug_snapshots/oe_long_vowel_missing_traces_2026-01-02d.txt`.

### Unified OE mismatch report (2026-01-03)
- New script: `server/tools/oe_mismatch_report.py` supersedes `oe_mismatch_patterns.py` + the separate “other subtypes” report.
- Latest unified report: `docs/debug_snapshots/oe_mismatch_report_2026-01-03a.txt` (includes the main buckets plus the “other” subcategories side by side).

### OE orthography cleanup + reports (2026-01-18)
- **Dotted palatal orthography:** `OldEnglishOrthography` now maps `/ʃ/` to `{sċ}` and allows `{sċ}` in the surface filter.
- **/dʒ/ + /j/ spelling:** `OldEnglishOrthography` maps `{ʤj}` to `{ċġ}`; `{ʤ}` and `{j}` still map to `ġ`.
- **Reports run (latest):**
  - `server/docs/debug_snapshots/oe_mismatch_report_2026-01-18w.txt`
  - `server/docs/debug_snapshots/oe_full_trace_report_2026-01-18w.txt`
- **Totals (2026-01-18w):** total mismatches 294; `palatal_marker_variant` = 0; `gemination_extra` = 2.
- **Hedge trace:** `oe_full_trace_report_2026-01-18w.txt` shows `hedge` outputs **both** `hæġġ` and `hæċġ` (Orthography + Surface), indicating nondeterminism is still present.
- **Open issue:** need deterministic pre-orthography cleanup so `*dʒ` + `*j` (and `dʒ` + `j`) coalesce to `{ʤj}` before orthography; avoid producing both `ħeġġ`/`hæġġ` and `hæċġ`.
- **Operational note:** Docker socket permissions intermittently blocked `docker compose exec` in this session; reports were rerun only after restoring Docker access.

### Foma CLI gotchas (2026-01-18)
- **Semicolons matter:** `regex` commands must end with `;` or the network won’t compile (no output from `print words/size`).
- **Reliable one-off tests:** use `foma` with stdin to avoid interactive issues, e.g.
  - `printf 'regex {ʤ} {*j} -> {ʤj};\napply down "ç*æʤ*j"\nquit\n' | foma`
  - Output: `"ç*æʤj"` (confirms the merge rule works on the hedge pre‑orthography form).

### HIGH PRIORITY: PGmc final *-un behavior (2026-01-25)
- **Problem:** PGmc final `*-un` is misbehaving across the “ten/seven/nine” set.
  - `*texun` → model output **teoun**, expected **tīen** (full trace: `server/docs/debug_snapshots/oe_full_trace_report_2026-01-25e.txt`).
  - `*sebun` → model output **sobun**, expected **seofon** (same report).
  - `*newun` → model output **nēowun**, expected **nigon** (same report).
- **Note:** `*sebun` and `*newun` did not appear in the short mismatch report because the default output lists only a limited number of examples per bucket. With a larger `--examples` count, they show up under:
  - `breaking_missing` (`*sebun`)
  - `front_expected_back_out` (`*newun`)
  - Reference: `server/docs/debug_snapshots/oe_mismatch_report_2026-01-25f.txt`
- **Likely cause:** `OldEnglishWeakTailReduction` (in `server/fsts/germanic.txt`) currently reduces `*ă`, `*ą`, and final `*i` but **does not touch `*u`**, so `*-un` does not get the weak‑tail treatment at all.
- **Action needed:** treat this as a high‑priority phonology fix. Investigate how weak‑syllable pressure / vowel balance should affect `*-un` in OE; adjust `OldEnglishWeakTailReduction` (or upstream conditioning) accordingly; then re‑run full trace + mismatch to confirm `teoun/sobun/nēowun` move toward **tīen/seofon/nigon**.
- **Next actions checklist:**
  - Pin down the consensus on OE weak‑syllable reduction for `*-un` (Hogg + any standard handbooks).
  - Trace current `*-un` paths in the FST stack to see exactly where it diverges.
  - Draft a minimal rule update, test on `*texun`, `*sebun`, `*newun`, and scan for side effects.
  - Re‑run `oe_full_trace_report` and `oe_mismatch_report` to confirm bucket movement and any regressions.

### OE full trace report: stages that never fire (UPDATED 2026-02-06)
- **STATUS**: From original 20 non-firing stages, **18 are now firing** after recent fixes.
- **Current report**: `server/docs/debug_snapshots/oe_full_trace_report_2026-02-06.txt`
- **Remaining non-firing (2 only)**:
  - **ProtoInput** - 0 changes (proto gate stage, no transformations expected)
  - **WeightCleanup** - 0 changes (needs investigation)
- **DELETED (1 stage)**:
  - **LiquidLowering** - Deleted 2026-02-06; no evidence for "lowering before liquids"; already handled by weak-tail reduction
- **FIXED / Now firing (18 stages)**:
  - ARestoration ✓ (41 changes) - **Fixed 2026-02-06** via context rule repair
  - VelarFricativePalatalization ✓ (36 changes)
  - IUmlaut ✓ (85 changes)
  - JClusterCoalescence ✓ (1 change)
  - BackMutation ✓ (6 changes)
  - NasalSpirantLengthening ✓ (2 changes)
  - NasalSpirantLoss ✓ (4 changes)
  - WeakTailNasalLoss ✓ (97 changes)
  - WeakTailUnReduction ✓ (3 changes)
  - WeakTailReduction ✓ (95 changes)
  - WeightMarkers ✓ (95 changes)
  - HighVowelApocope ✓ (41 changes)
  - JLossAfterHeavy ✓ (17 changes)
  - HLoss ✓ (3 changes)
  - Contraction ✓ (2 changes)
  - ProtoToOEWeightMarkers ✓ (41 changes)
  - ProtoToOEApocope ✓ (41 changes)
  - ProtoToOEWeightCleanup ✓ (54 changes)

### OE sound-change reference index (2026-02-02)
- **New index file:** `docs/references/oe_sound_change_index.md`
  - Collects frequently reused citations and exact `rg`/`sed` commands for Hogg and Ringe/Taylor.
- **Why:** we keep re-checking the same passages during OE chronology work; this keeps lookups fast and consistent.

## Bimoric vs. Trimoric *ō: Comprehensive Analysis (Session 028)

### Sources
- R/T vol.2 §3.1.4 (lines 4035–4130): "Further Auslautgesetze"
- R/T vol.2 §2.1.4 (lines 1670–1770): NWGmc raising of word-final *-ō
- R/T vol.2 §5.2 (lines 9282–9450): Northern WGmc morphological innovations
- R/T vol.2 §6.7.1 (lines 14836–14930): Early changes of front vowels
- R/T vol.2 lines 17180–17240: Systematic derivation chains for OE endings

### The Three Fates of Word-Final *ō

R/T describes three distinct developments of unstressed word-final *ō,
depending on quantity (bimoric vs trimoric) and chronology:

**Path A: PNWGmc Raising (bimoric *ō that is word-final in PGmc)**
- Rule: PGmc word-final bimoric *-ō → PNWGmc *-ū → *-u (raising + shortening)
- R/T line 1672: "PGmc word-final bimoric non-nasalized long *-ō became
  short *-u in unstressed syllables in PNWGmc."
- OE reflex: -u after light syllable, lost after heavy (same as inherited *-u)
- Examples: ō-stem nom.sg. *gebō → PNWGmc *gebu → OE giefu
  a-stem neut. nom-acc.pl. *grasō → PNWGmc *grasu → OE grasu
  1sg pres. indic. *kwemō → PNWGmc *kwemu → OE cumu
- **Our FST**: Modelled by NWGmcFinalLongORaising: {*ō} → {*u} || _ .#.
  This is CORRECT for this path.

**Path B: PWGmc Unrounding (bimoric *ō that becomes word-final LATER)**
- Rule: bimoric *ō that was NOT word-final at the PNWGmc stage (because
  it had *-z, *-n, or other endings) → after those endings are lost → now
  word-final → PWGmc *-a → OE -e (via unstressed fronting)
- R/T line 4035–36: "Word-finally... surviving bimoric long ō-vowels became
  PWGmc *a"
- The word "surviving" is key — these survived the PNWGmc raising because
  they weren't word-final yet when that raising operated.
- OE reflex: -e (from *-a via unstressed fronting/raising)
- Examples: ō-stem acc.sg. *gebō(n?) → *gebō (after ending loss) → PWGmc
    *geba → OE giefe
  ō-stem gen.sg. *gebōz → *gebō (after z-loss) → PWGmc *geba → OE giefe
  fem. n-stem nom.sg. *tungōn → *tungō̃ (after n-loss, nasalized) →
    PWGmc *tunga → OE tunge
- **Our FST**: For fem. n-stems, modelled by NWGmcNStemNLoss: {*ō}{*n} →
  {*ǭ} word-finally, then {*ǭ} → {*æ} → OE -e. This covers the n-stem case.
  For other "surviving bimoric" cases (acc.sg., gen.sg. of ō-stems), we DON'T
  have a rule — but these paradigm cells aren't in our TSV data.

**Path C: Trimoric *ō (→ PWGmc *ō → OE -a)**
- Rule: trimoric *ō → PWGmc *ō (stays long) → shortens late → OE -a
- R/T line 4036: "trimoric long ō-vowels became PWGmc *ō"
- R/T line 17230: "masc. n-stem nom.sg. -a < *-ā < PWGmc *-ō < PGmc *-ō"
  (R/T explicitly classifies this *ō as trimoric)
- OE reflex: -a
- Examples: masc. n-stem nom.sg. *namō → PWGmc *namō → OE nama
  gen.pl. *dagō → PWGmc *dagō → OE daga
  ō-stem nom.pl. *gebōz → PWGmc *gebō → OE giefa
  Class II weak iptv. 2sg *salbō → PWGmc *salbō → OE sealfa
    (R/T line 17187: "iptv. 2sg. -a < *-ā < PWGmc *-ō < PGmc *-ō")
- **Our FST**: Modelled by {*ô} symbol (trimoric). {*ô} is exempt from
  NWGmcFinalLongORaising, and shortens to {*a} in OEUnstressedLongVowelShortening.
  Currently used only for masc. n-stems. COULD ALSO BE USED for:
  - Class II weak verb iptv. 2sg (see below)
  - gen.pl. forms (not in TSV)
  - ō-stem nom.pl. (not in TSV)

### Implications for Class II Weak Verbs

The three Class II weak verbs in the mismatch report (suffix_form__eian_vs_ian):
  *burōjăną → boreian (expected borian)
  *liznōjăną → lierneian (expected leornian)
  *makōjăną → maceian (expected macian)

The infinitive suffix *-ōja- is a MORPHOLOGICAL innovation (northern WGmc
analogical remodelling of Class II on the model of Class I, R/T §5.2). It is not
a regular sound change. OE -ian does not derive by regular phonology from
*-ōjanan.

R/T's paradigm (lines 9395–9420, §5.2) for *ardōn 'to dwell':
  infinitive: *ardōjan > OE eardian  (morphological remodelling, NOT regular)
  iptv. 2sg:  *ardō > OE earda       (regular; trimoric *ō → -a)
  2sg:        *ardōs > OE eardas      (regular; *ō before consonant → -a-)
  3sg:        *ardōþ > OE eardaþ      (regular; *ō before consonant → -a-)

The REGULAR forms (iptv. 2sg, 2sg, 3sg) preserve the original *-ō- stem vowel
without the *-ōja- extension. These are candidates for TSV encoding.

### Issues to Resolve

1. **A-restoration with {*ô}**: When we test `makô` through the FST, AFB fronts
   root {*a} → {*æ}, but A-restoration doesn't fire because {*ô} is not in
   PGmcStarBackVowel or OEARestorationTriggerVowel. This produces
   *mæċa* (with spurious fronting + palatalization) instead of *maca*.
   FIX: Add {*ô} to OEARestorationTriggerVowel.

2. **{*ô} in non-final position**: For forms like *makôþi (3sg), {*ô} is medial,
   not word-final. OEUnstressedLongVowelShortening handles this
   (it applies to non-initial syllables generally, not just word-final).
   Need to verify this works.

3. **pgrmWord acceptance**: The shape `makô` (CVC + ô) needs to be accepted
   by the input FST. Since {*ô} is in pgrmWeakTailVowel, forms like `makô`
   should parse as: strong syllable `mak` + weak tail vowel `ô`. Need to verify.

4. **Other items using {*ô}**: Currently only 11 masc. n-stem sets use {*ô}.
   Could also apply to Class II weak verb citation forms if we switch to
   iptv. 2sg or another regular form. But we need to decide: do we change
   the citation form for these verbs, or just document the mismatch?

### Non-final *ō (medial syllables)

R/T line 4037–38: "In other unstressed syllables both these vowels became *ō"
This means in MEDIAL position (not word-final), bimoric and trimoric *ō
MERGED to *ō. So the bimoric/trimoric distinction is only relevant word-finally
(and before word-final *r). Our FST handles this correctly: OEUnstressedLong
VowelShortening operates on non-initial syllables regardless of position.

Examples (R/T lines 4090–4120):
  *mēnōþiz 'months' → *manōþi → OE mōnaþ (medial *ō → *ō)
  *salbōd(ēd)un 'they anointed' → *salbōdun → OE sealfodon (*ō → o)
  *salbōþi '(s)he anoints' → *salbōþi → OE sealfaþ (*ō → a)

Wait — the last example has *ō → a, not *ō → o. Let me check the context.
Actually, the 3sg *salbōþi has *ō in an open MEDIAL syllable before *þ(i).
R/T says (line 4100): "PGmc pres. 3sg. *salbōþi '(s)he anoints' ...> OE sealfaþ".
The *ō becomes -a- in this position. This is consistent with late shortening
of unstressed *ō → *a in OE, rather than through the PWGmc *a unrounding.

### All 8 Class II Weak Verbs in TSV (all produce -eian)

| PGmc form      | FST output    | Expected OE     | Bucket               |
|----------------|---------------|-----------------|----------------------|
| *burōjăną      | boreian       | borian          | suffix_form__eian_vs_ian |
| *liznōjăną     | lierneian     | leornian        | suffix_form__eian_vs_ian |
| *makōjăną      | maceian       | macian          | suffix_form__eian_vs_ian |
| *likkōjăną     | liċceian      | liccian         | palatal_extra__j_triggered |
| *skawōjăną     | sċaweian      | scēawian        | breaking_missing__ea  |
| *xandlōjăną    | handleian     | handle          | final_vowel_missing   |
| *sundrōjăną    | sundreian     | sundor-         | cons_mismatch        |
| *wainōjăną     | wāneian       | hwīnan          | i_umlaut_missing     |

ALL share the -eian issue. The *-ōja- suffix is morphological (R/T §5.2:
analogical remodelling of Class II weak on the model of Class I), not phonological.
Our FST cannot and SHOULD NOT model this analogical change.

### Options for Resolution

**Option A: Change citation form to iptv. 2sg** (e.g., *makō → maca)
- Pro: Regular sound change, same development as masc. n-stems (trimoric *ō)
- Con: Requires encoding as *makô (trimoric); needs A-restoration fix for {*ô};
  changes the citation form across all 4 languages in each cognate set

**Option B: Change citation form to 3sg pres. indic.** (e.g., *makōþi → macaþ)
- Pro: Regular development with more morphology visible
- Con: More complex form; still needs *ō → -a- modelling in medial position;
  other languages may not match (German/Dutch 3sg forms differ)

**Option C: Document as non-regular and exclude from mismatch counting**
- Pro: No FST or TSV changes needed; acknowledges the morphological nature
- Con: 8 items remain as "known non-regular" mismatches; doesn't test our
  *ō development at all for Class II verbs

**Option D (hybrid): Use iptv. 2sg for the OE row only, keep *-ōjăną for others**
- This doesn't work: all rows in a cognate set share the same protoform

**Recommendation**: Option A (iptv. 2sg with trimoric *ô) for verbs where
it works cleanly, combined with Option C (documentation) for verbs where
the iptv. form introduces other complications. First need to fix A-restoration
for {*ô} to make Option A viable.

### A-Restoration Gap for {*ô}

Current problem: `makô` → `mæċa` (wrong) instead of `maca` (correct).

Derivation trace for `makô`:
1. AFB: {*a} → {*æ} (before {*k}, which is non-nasal consonant) ✓
2. A-restoration: {*æ} should restore to {*a} before back vowel {*ô} in next
   syllable — BUT {*ô} is NOT in OEARestorationTriggerVowel, so restoration
   FAILS. ✗
3. Velar palatalization: {*k} before {*æ} (front) → {*ʧ} ✗ (should not fire
   because root vowel should be *a, not *æ)
4. OEUnstressedLongVowelShortening: {*ô} → {*a}
5. Orthography: → mæċa (wrong)

Fix needed: Add {*ô} to OEARestorationTriggerVowel:
  define OEARestorationTriggerVowel [EnglishStarBackVowel | {*æ} | {*ô}];

This is principled: {*ô} IS a back vowel (it's trimoric *ō), it just can't be
in PGmcStarBackVowel because that would cause regressions in vowel rules.
A-restoration specifically should see it as triggering restoration.

Also check whether {*ǭ} should ALSO be in OEARestorationTriggerVowel.
Fem. n-stems like *tungōn → {*t}{*u}{*n}{*g}{*ǭ}: if AFB fronted the root
vowel, it should be restored before the back {*ǭ}. But {*u} doesn't undergo
AFB (only {*a} does), so this case doesn't arise for *tung-. May arise for
other fem. n-stems with {*a} in root: *xertōn → heorte has {*e} from breaking,
not {*a}, so no AFB issue. Will monitor.

---

## Class II Weak Verb Exploration (class2-weak-exploration branch)

**Date:** 2026-02-24
**Branch:** class2-weak-exploration (from update HEAD bd54207)
**Status:** In progress

### Background

Class II weak verbs in PGmc have the suffix *-ōja- (e.g., *makōjăną 'to make'). The OE reflex is *-ian* (e.g., *macian*), but R/T vol.2 §5.2 explicitly states this *-ian* is **morphological** (analogical remodelling), not a regular phonological development from *-ōja-. The regular phonological outcome of *-ōja- is *-eian* (with i-umlaut of *ō → *ē by the *j*), which is what our FST correctly produces.

> "The Class 2 weak verbs are characterized in NWGmc by the stem-forming suffix *-ō(ja)- ... but the actual OE suffix -i(g)an is the result of a complex of analogical changes" (R/T §5.2, our OCR pp. 282ff)

### Test forms: imperative 2sg and 3sg present indicative

To test the *regular* phonological developments, we use paradigm forms where the suffix is lautgesetzlich:

**Imperative 2sg** (*-ō, trimoric): PGmc *makō → OE maca
- The trimoric *ō is modelled as {*ô} in our notation
- {*ô} → OE -a via OEUnstressedLongVowelShortening (line 1317)
- This path does NOT involve the morphological *-ōja- suffix

**3sg present indicative** (*-ōθi): PGmc *makōθi → OE *maceþ (regular) / macaþ (attested, analogical)
- The *i in *-ōθi triggers i-umlaut of the *ō, giving *ē → e
- The regular phonological outcome is -eþ, not -aþ
- Attested macaþ has -aþ by analogy with the rest of the paradigm

### Findings

#### 1. A-restoration fix for {*ô}

Before the fix, `makô → mæċa` (wrong). The problem: OEARestorationTriggerVowel did not include {*ô}, so AFB fronted root *a → *æ without A-restoration undoing it. The *æ then triggered palatalization of *k → *ʧ (→ ċ).

**Fix:** Added {*ô} to OEARestorationTriggerVowel (line ~1190):
```
define OEARestorationTriggerVowel [EnglishStarBackVowel | {*æ} | {*ô}];
```

After fix: `makô → maca` ✓

**Justification:** {*ô} (trimoric *ō) IS a back vowel — it triggers A-restoration just like any other back vowel in the following syllable. It is deliberately excluded from PGmcStarBackVowel (to avoid regressions in general vowel rules), so it needs explicit inclusion in the trigger set.

R/T §6.3.1 p.205: "Weak verbs of class II always exhibit retracted a rather than æ before a non-nasal consonant in a monosyllabic root syllable, since at the time retraction occurred the following syllable always contained *ō or *a."

#### 2. 3sg weak tail pattern

The pgrmWeakTailVowel filter (line ~279) explicitly enumerates allowed weak-tail patterns. The 3sg ending *-ōθi was missing.

**Fix:** Added `ō:{*ō} θ:{*θ} i:{*i}` to pgrmWeakTailVowel (line ~328).

#### 3. θ/þ encoding convention

The FST uses θ (Greek theta, U+03B8) for the voiceless dental fricative in proto-forms. The original test rows incorrectly used þ (thorn, U+00FE) in the PROTO column. The mismatch report's `normalize_proto()` converts þ→θ, masking this issue.

**Convention:** PROTO column in TSV must use θ, matching existing entries like `*baθą`.

#### 4. Results summary

| Form | FST output | Expected OE | Status |
|------|-----------|-------------|--------|
| makô | maca | maca | ✓ |
| makōθi | maceþ | maceþ (regular) | ✓ |
| burô | bura | bora | ✗ u-lowering |
| burōθi | boreþ | boreþ | ✓ |
| liznô | lierna | leorna | ✗ stressed vowel (ie vs eo) |
| liznōθi | lierneþ | leorneþ | ✗ same root issue |
| likkô | liċca | licca | ✗ spurious palatalization |
| likkōθi | liċceþ | licceþ | ✗ same root issue |
| skawô | sċawa | scēawa | ✗ missing ēa + spurious ċ |
| skawōθi | sċaweþ | scēaweþ | ✗ same root issue |

### Remaining root-level issues (shared with other lexemes)

These issues affect the Class II test forms but are NOT specific to Class II verbs — the same problems appear in other words with the same roots.

#### A. u-lowering (u → o before back vowel)

**Affected:** *burô → bura (expected bora), also *bugô → buga (expected boga), *fulô → fula (expected fola), *uxsô → uxa (expected oxa)

**Issue:** NWGmcULowering should lower *u → *o before non-high vowels in a following syllable. But these n-stem nominatives with {*ô} suffix retain u. The same problem exists for related words in the `vowel_quality__u_o_alternation` bucket.

**Note:** Some u-retentions are documented exceptions (bucc, fugol, wulf — see DEV_NOTES §1 above). But buga/boga, fula/fola are different: the expected form IS the lowered one (boga, fola), so u-retention here is a FST bug, not a documented exception.

#### B. Stressed vowel ie vs eo (*liznô → lierna vs leorna)

**Affected:** *liznô → lierna (expected leorna), *liznōjăną → lierneian (expected leornian)

**Issue:** The root *lizn- should give OE leorn- (with eo from breaking of e before rn). Our FST produces ie instead of eo. This is a stressed vowel quality issue in the `vowel_quality__stressed_vowel` bucket. Needs investigation: the *i → *e lowering and then breaking to *eo should give eo, not ie.

#### C. Spurious palatalization of geminate *kk (*likkô → liċca vs licca)

**Affected:** *likkô → liċca (expected licca), *likkōθi → liċceþ (expected licceþ)

**Issue:** OE palatalization of *k → ċ before front vowels is correct in general, but geminate *kk should NOT be palatalized in this context. The *i in the root is a front vowel, but geminate velars resist palatalization (R/T §6.4.1). This may be a missing condition in OEVelarPalatalization.

#### D. Missing ēa diphthong + sk/sc issue (*skawô → sċawa vs scēawa)

**Affected:** *skawô → sċawa (expected scēawa), *skawōθi → sċaweþ (expected scēaweþ)

**Issues:**
1. Missing ēa: The root *skaw- should give scēaw- with ēa diphthong. The *aw sequence should produce ēaw via some vowel development, but our FST keeps it as aw.
2. sk → sċ vs sc: Our FST produces sċ (palatalized) where sc is expected. The sk → sc change is not palatalization but a general OE shift of /sk/ → /ʃ/ spelled ⟨sc⟩.

### Proto-form notes

**`*nablô` (navel):** Competing reconstructions. Kroonen reconstructs PGmc *nablōn- (stem *nablan-), but R/T vol.2 §6.3.1 p.206 gives pre-retraction *nabulō with medial vowel (cf. OHG nabalo). The medial *u may be PWGmc-level epenthesis. Current TSV form *nablô follows Kroonen. For A-restoration to fire correctly in the pipeline, *nabulô may be needed, since R/T's chronology places epenthesis (§6.9.5, mid-7th c.) much later than retraction (§6.3, pre-6th c.).

---

## Cognate set 379 "rock" → corrected to "coat" (*rukkăz)

**Date:** 2026-03-01
**Status:** Fixed

### The problem

Cognate set 379 (GLOSSID 200) was glossed "rock" (apparently meaning stone)
with PGmc \*rukkiz (i-stem) and the following forms:
- OE: rocc
- German: Ruck
- Dutch: ruk
- English: rock

This set was a mess: three different etymologies had been conflated.

1. **OE rocc "garment/tunic"**: from PGmc \*rukkaz (masc. a-stem, Kroonen
   \*hrukkaz); cognates German Rock "skirt/coat", Dutch rok "skirt". The OE
   word is well attested (brēostrocc, pistolrocc, bisċoprocc etc.).

2. **OE \*rocc "rock formation"**: attested only in the compound stānrocc.
   Etymology uncertain — possibly from Medieval Latin rocca (itself perhaps
   from Celtic), not a native Germanic word at all. ModE "rock" (stone) is
   partly from OE \*rocc, partly from Anglo-Norman roque.

3. **German Ruck "jerk/jolt"**, Dutch ruk "pull/jerk": from MHG ruc, OHG
   rucch, related to the verb rücken "to push, move". This is a completely
   different root, unrelated to the garment word.

### Resolution

Replaced the cognate set with the garment word, which has a well-established
PGmc reconstruction and reflexes in all four languages:
- PGmc \*rukkăz (masc. a-stem; Kroonen \*hrukkaz pp.250-1)
- OE: rocc "upper garment, tunic" (attested)
- German: Rock "skirt, jacket" /ʁɔk/
- Dutch: rok "skirt" /rɔk/
- English: rock (archaic "garment", from ME rocke < OE rocc)
- Concept changed from "rock" (stone) to "coat" (garment)
- Proto-form changed from \*rukkiz (i-stem, wrong) to \*rukkăz (a-stem, correct)

The a-stem nom.sg. \*-ăz ending means no \*-i- trigger, so:
- No i-umlaut (PGmc \*u stays as \*u, lowered to OE o by NWGmc u-lowering) ✓
- No palatalization of \*kk (no following front vowel) ✓
- Pipeline output: rocc ✓

---

## Unstressed *-ag → -ig (R/T §6.9.6)

**Date:** 2026-03-01
**Status:** Implemented (OELateUnstressedAgSuffix)

### The sound change

R/T §6.9.6 (pp.349-350): Late unstressed \*-ag(-) → \*-æg(-) → \*-eg(-) → -ig(-).
After i-umlaut and epenthesis. R/T: "inherited \*a adjacent to palatals eventually
became i." Examples:
- PGmc \*modagaz → OE modig 'spirited, brave'
- PNWGmc \*hailagaz → OE hālig 'holy'
- PWGmc \*hunag → \*huneg → OE hunig 'honey'

Before back vowels the intermediate -eg- is preserved with velar g (e.g.,
dat. pl. monegum), so late palatalization restricted to word-final position.

### Implementation

Rule `OELateUnstressedAgSuffix` in germanic.txt, placed after OEEpentheticVowel:
1. Front medial unstressed \*a → \*e before \*g (requires V+C+ before)
2. Palatalize \*g → \*ʤ after \*e at word boundary (not before back V)
3. Raise \*e → \*i before palatal \*ʤ (medial only, requires V+C+ before)

All three steps restricted to medial (non-initial) position to prevent regressions
on stressed-syllable forms (e.g. \*xagjăz → heġġ, which should keep stressed \*e).

---

## Labiovelar Proto-Form Corrections and Post-Velar *w Loss (R/T §6.4.2)

**Date:** 2026-03-06
**Status:** Implemented (OEPostVelarWLoss) + TSV fixes
**Mismatches:** 113 → 109

### The problem

Three mismatch items involved PGmc *gw clusters from labiovelars:
- *snaigwăz → snāgw (expected snāw): cons_mismatch__g_vs_w
- *swalgwōn → swealgwe (expected swealwe): cons_mismatch__g_vs_w
- *singwăną → singwan (expected singan): cons_mismatch__w_vs_n
- Also *θegnăz → þeġn (expected þæġn): vowel_quality__ae_e_alternation

### Research

**Snow (*snaigwăz → *snaiwăz):** Both Kroonen (p.460, *snaiwa-) and R/T (p.171, *snaiwaz) reconstruct PGmc with *w, not *gw. There was never a labiovelar in this word. The TSV proto was simply wrong, likely from automated extraction confusion.

**Swallow (*swalgwōn → *swalwōn):** Kroonen (p.495, *swalwōn-) and R/T (p.185, PWGmc *swalwa) both reconstruct without *g. The TSV proto was confused with the verb *swelganą 'to swallow (food)' — the bird name has no etymological *g.

**Sing (*singwăną):** This genuinely had a PGmc labiovelar *g^w (Kroonen p.437, *singwan-; R/T p.215, *sing^wanan). After PWGmc labiovelar resolution (R/T §3.1.3), the cluster became *ngw. Then per R/T §6.4.2, *w was lost after non-initial velars: *singwan → singan.

**Thane (*θegnăz):** R/T reconstruct *þegnaz with *e and give OE þegn. The TSV target þæġn was incorrect; changed to þeġn to match both R/T and our pipeline output.

### Analysis of *gw developments

R/T §6.4.2 "Loss of *w after non-initial velars" covers post-palatalization simplification. The outcomes differ based on allophony of *g:

1. After nasal (*ngw): *g = stop [g], so *w is lost → *ng (singan, stincan)
2. Post-vocalic (*Vgw): *g = fricative [ɣ], so *g is lost → *Vw (snāw)
3. After liquid (*lgw): same as post-vocalic → *lw (swealwe)

For cases 2-3, we corrected the TSV proto-forms to remove the spurious *g.
For case 1, we added the OEPostVelarWLoss rule.

### Implementation

**Rule:** `OEPostVelarWLoss` — `{*w} → 0 || {*n} {*g} _`
**Pipeline position:** After OEVelarPalatalization (per R/T chronology)
**TSV changes:** snow, swallow protos corrected; thane target corrected
**New weak tail:** w:{*w} ō:{*ō} n:{*n} added for *swalwōn

## Water fix: PWGmc ō-shortening and A-restoration correction (3a45a8b)

### Problem
PGmc *watōr (r/n-stem nom.sg.; Kroonen *watar-/*watan-) needed to produce OE wæter. Two issues:

1. **PWGmc ō-shortening (R/T §3.1.4):** "Word-finally, and before word-final *r, surviving bimoric long ō-vowels became PWGmc *a." So *watōr → PWGmc *watar.

2. **A-restoration over-application:** After AFB fronted both *a's in *watar to *æ (giving *wætær), A-restoration incorrectly fired because `{*æ}` was in `OEARestorationTriggerVowel`. This restored stressed *æ → *a, giving "water" instead of "wæter".

### Root cause: {*æ} should NOT trigger A-restoration

The `{*æ}` symbol was added to the A-restoration trigger set based on an incorrect analysis that suffix *a (like gen.sg. *-as), after being fronted to *æ by AFB, still triggers restoration as an "underlyingly back" vowel.

**R/T's paradigm disproves this (§6.3.2, p. 199):**
- gen.sg. *dagas → *dæges → OE **dæges** (NOT *dages) — A-restoration does NOT fire
- nom.pl. *dagos → OE **dagas** — A-restoration DOES fire (suffix *-os has genuine back *o)
- dat.pl. *dagum → OE **dagum** — A-restoration DOES fire (suffix *-um has genuine back *u)

This proves that only genuine back vowels (*o, *u, *ō, *ū, *ô) trigger A-restoration. Fronted suffix vowels (*æ from AFB'd *a) do NOT trigger it.

### Fix
1. **Removed `{*æ}` from `OEARestorationTriggerVowel`** — now defined as `[EnglishStarBackVowel | {*ô}]`
2. **Added `PWGmcPreFinalRShortening`:** `{*ō} → {*a} || _ {*r} .#.` in PWGmcChanges
3. **Added `ō:{*ō} r:{*r}` weak tail** for r-stem endings
4. **TSV:** OE water proto *watną → *watōr (correct PGmc r/n-stem nom.sg.)

### Derivation
*watōr → (PWGmc ō-shortening) *watar → (AFB) *wætær → (A-restoration: NO trigger, *æ is not back) *wætær → (§6.9.6 unstressed merger) wæter ✓

### Impact
- No regressions. 106 mismatches (unchanged). Health check clean.
- All A-restoration-dependent forms verified: bacan, wadan, wascan, hlaþan, grafan, ġeall, hamer all correct.

---

## A-restoration in ō-stems and n-stems: ræst, tæppa, stemn (fronting_missing__afb)

### Overview

The mismatch report shows three `fronting_missing__afb` items where the pipeline produces a form with restored *a where the OE target has *æ (or *e from i-umlaut):

| Proto | Pipeline output | TSV target | Stem class |
|-------|----------------|------------|------------|
| *rastō | rast | ræst | ō-stem f. |
| *tappô | tappa | tæppa | n-stem m. |
| *stamnăz | stamn | stemn | (see below) |

All three share a common thread: A-restoration fires because the suffix vowel is back, but the standard OE form shows a front root vowel. Two require the "oblique form" approach we have used elsewhere (fire, cow, night); the third requires a proto-form correction.

### Background: A-restoration and paradigmatic leveling

R/T §6.3.1–6.3.2 establish that A-restoration (retraction of *æ → *a) is triggered by a back vowel (*o, *u, *ō) in the following syllable. Our pipeline implements this correctly: `OEARestorationTriggerVowel` = `[EnglishStarBackVowel | {*ô}]`.

The critical insight comes from R/T's paradigm of "dæg" (day, §6.3.2 p.193):
- Gen.sg. *dagas → dæges: suffix *-as has *a, which after AFB becomes *-æs (front) → no restoration → dæg-
- Nom.pl. *dagos → dagas: suffix *-os has *o (back) → restoration fires → dag-
- Dat.pl. *dagum → dagum: suffix *-um has *u (back) → restoration fires → dag-

Principle: **original PGmc *a in suffixes is fronted by AFB and does NOT trigger restoration. Original PGmc *o, *u in suffixes stay back and DO trigger restoration.**

### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

**Pipeline derivation (nom.sg.):**
*rastō → (NWGmc final *-ō raising) *rastu → (AFB) *ræstu → (A-restoration: *u is back ✓) *rastu → (apocope after heavy syllable) → rast

This is **phonologically correct** for the nom.sg. The *-ō → *-u (back) triggers restoration.

**But the attested OE form is ræst (BT headword "ræst").**

**Explanation — paradigmatic leveling from oblique cases:**

The ō-stem paradigm of *rastō:
- Nom.sg. *rastō → *rastu → restoration → rast (back *-u triggers)
- Acc.sg. *rastō̃ → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
- Gen.sg. *rastōz → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
- Dat.sg. *rastōi → PWGmc *rastē → AFB (no *a in suffix to front) → ræste (no restoration)

Only the nom.sg. has the back suffix *-u that triggers A-restoration. All oblique cases (acc., gen., dat.) have front suffix vowels → no restoration → ræst- throughout. The majority oblique pattern was generalized to the nom.sg.: ræst.

**Contrast with n-stems like crabba (R/T p.207):** R/T list n-stem forms with restored *a: *krabbō → crabba, *rakkō → racca, *maþō → maþa. In these cases, the nom.sg. (with restoration from back *-u < *-ô) was generalized instead, possibly because the nom.sg. is the most frequently encountered form of n-stems.

**Sources:**
- BT: headword "ræst" f. 'rest, repose, bed, grave'. Oblique forms: ræste (gen./dat.sg.).
- Kroonen (p.420): *rasto- f. 'interval' — Go. rasta, ON rost, OE rest, OS rasta, OHG rasta. (Kroonen gives OE "rest", i.e. ræst with late OE æ→e.)
- R/T §6.3.1–6.3.2: paradigmatic alternation between a and æ due to A-restoration is explicitly discussed for a-stems (dæg/dagas); same logic applies to ō-stems.

**Proposed resolution — oblique form approach:**

Following the precedent of fire (*fūri → fȳre, dat.sg.), cow (*kūi → cȳ, dat.sg.), night (*naxti → niht, dat.sg.), and hammer (*xamaras → hameres, gen.sg.), we can use an oblique form of *rastō where the suffix does NOT trigger A-restoration.

The difficulty is that the standard ō-stem oblique endings (*-ōz gen.sg., *-ōi dat.sg.) contain *-ō, which is a back vowel that would ALSO trigger restoration in our pipeline. The pipeline applies rules at the PGmc input level and does not separately model the pre-AFB shortening of *-ōz → PWGmc *-a.

However, R/T (p.314) show that ō-stem acc.sg./gen.sg. -e derives from PGmc *-ō/*-ōz → PWGmc *-a. The suffix *-a (from *-ō shortening) then undergoes AFB → *-æ (front), which does NOT trigger restoration. Our pipeline's existing a-stem gen.sg. encoding *-as produces the same result: the suffix *a is fronted by AFB and doesn't trigger restoration.

Tested: `rastas → ræstes` ✓ (the gen.sg. form with correct ræ- root).

**Decision needed:** We could (a) use gen.sg. *rastas → OE ræstes, changing both the proto and the OE target (parallel to hammer, swan, brand); or (b) document ræst as a known morphological exception with an ALIGNMENT note that the pipeline gives the regular nom.sg. reflex rast but the standard form ræst reflects paradigmatic leveling.

**Complication with (a):** The encoding *rastas uses the a-stem gen.sg. ending *-as, but *rastō is an ō-stem, whose gen.sg. is *-ōz (→ PWGmc *-a → OE -e). The pipeline cannot process *-ōz because it is not in the pgrmWeakTailVowel list, and even if added, the *-ō component would trigger A-restoration. Using *-as is thus a pragmatic encoding that gives the correct phonological result but misrepresents the morphological class.

### Case 2: *tappô → tappa (expected tæppa) — n-stem masculine

**Pipeline derivation (nom.sg.):**
*tappô → (NWGmc final *-ô development) *tappō → *tappu → (AFB) *tæppu → (A-restoration: *u is back, *ô is in trigger set ✓) *tappu → (apocope? or *-u → *-a) → tappa

This is **phonologically correct** for the nom.sg. The *-ô ending is back and triggers restoration.

**But the attested OE form is tæppa (BT headword "tæppa, m.").**

**Explanation — paradigmatic leveling from oblique cases:**

The n-stem masculine paradigm of *tappô:
- Nom.sg. *tappô → *tappu → restoration → tappa (back *-u triggers)
- Acc.sg. *tappanun → *tappan → AFB *tæppæn → tæppan (suffix *-a fronted → no restoration)
- Gen.sg. *tappanaz → *tappan → AFB *tæppæn → tæppan (suffix *-a fronted → no restoration)
- Dat.sg. *tappani → *tappan → AFB *tæppæn → tæppan (suffix *-a fronted → no restoration)

Only the nom.sg. has restoration; all oblique cases have front suffix vowels (PGmc *a in suffix fronted by AFB). The majority oblique pattern (tæpp-) was generalized. This is the opposite direction from the crabba/racca pattern, where the nom.sg. form won out.

**Sources:**
- BT: headword "tæppa, m." — 'a tap, plug, stopper'. Oblique: tæppan.
- Kroonen: *tappô is an n-stem. No further etymology.
- Web search confirms: tæppa is standard WS, tappa not attested as a standard form.

**Proposed resolution — oblique form approach:**

The n-stem acc./gen./dat.sg. ending *-an (from *-anun, *-anaz, *-ani) can be encoded as *-ăn in our pipeline. The suffix *-ă is not a back vowel, so A-restoration does not fire.

Tested: `tappăn → tæppan` ✓

This is clean and parallel to other oblique usages in the project. We change the proto to *tappăn and the OE target to tæppan (the oblique form is well-attested in BT). The derivation is fully lautgesetzlich:

*tappăn → (AFB: root *a → *æ, suffix *ă → ... treated as front) → *tæppæn → (various) → tæppan ✓

### Case 3: stefn / stemn 'voice' — the stefn/stemn problem

**⚠ THIS IS A MAJOR FLAGGED PROBLEM — see also notable_findings.md §5 and the "Return later" section below.**

This item exposes a genuine disagreement in the literature about how to reconstruct the Proto-Germanic preform of the word for 'voice'. The OE evidence is clearer than the Proto-Germanic evidence. The project therefore uses a **local pre-OE transponent** for the OE pipeline and defers the cross-Germanic reconstruction to a later stage.

---

#### A. Practical project decision

**Operational decision (implemented):** The TSV uses pre-OE transponent **\*stebnō** (citation form, ō-stem nom.sg.) as input to the OE pipeline. Pipeline output: **stefn**. The OE target is **stefn**, not stemn.

The form **stemn** is treated as a later secondary WS variant produced by the assimilation fn → mn (Bülbring §485: "Im Ws. geht f vor n + Vokal in m über"; he dates the assimilation to Alfred's time or later). The OE target stefn is the conservative form attested from the earliest glossaries onward.

The previous TSV proto-form \*stamnăz was ad hoc — an a-stem masculine with root *a* that no source reconstructs. It produced pipeline output "stamn" (with no mechanism to front the root vowel), confirming it was wrong.

---

#### B. Why this is the right temporary decision

The TSV needs a form that actually yields the conservative OE output through the pipeline's sound changes. The pre-OE transponent \*stebn- (with root *e* already present, and the *-bn-* cluster that regularly becomes *-fn-*) satisfies this requirement:

- `stebnō → stefn` — pipeline output matches the attested conservative OE form
- No new rules needed; *bn → fn is already handled
- The root *e* is inherited (not produced by umlaut or other mechanism)

**This is explicitly a transponent for the OE stage, not a claim to have solved Proto-Germanic.** The form \*stebnō happens to be the reconstruction given by R/T (p.330), but we are using it here specifically because it works for OE, not because we are adjudicating the deeper reconstructional question. Multiple PGmc starting points could yield the same pre-OE \*stebn- (see §D–E below), and discriminating between them requires evidence from other daughter languages that the OE pipeline cannot provide.

---

#### C. Primary Old English and English-historical evidence

**Early OE attestations:**

The earliest attested form is **stebn** (Corpus Glossary 2164, c.800; R/T p.330). This is the most archaic form, preserving the original *-bn-* cluster.

The form **stefn** (with *bn → fn*, labial devoicing/spirantisation before nasal) is the standard early WS form. It is abundantly attested: Alfred's works, the Vespasian Psalter gloss, and many other early sources. Bülbring (§445) lists "stebn stefn stemn 'Stimme'" as the chronological sequence after short syllable. Northumbrian texts (Lindisfarne, Rushworth) consistently have **stefn** (Bülbring §485: "das Nordh. stets ... stefn Pl. stefno").

The form **stemn** (with *fn → mn*, nasal assimilation) is specifically late WS. Bülbring (§485) explicitly restricts the fn → mn change to WS: "Im Ws. geht f vor n + Vokal in m über: emne 'eben', hræmn hremn 'Rabe' ... stemn 'Stimme'." He adds: "kGl. efne; das Nordh. stets efne, stefn Pl. stefno, hræfnas" — i.e. Kentish and Northumbrian preserve fn, only WS has mn. Bülbring (§62 Anm. 3) dates the assimilation explicitly: "Da die Einwirkung der Nasale auf e allein der frühesten urengl. Zeit angehört, so bleibt e vor dem erst in Alfreds Zeit auftretenden, aus f hervorgegangenen m erhalten: stemn 'Stimme', emne 'eben' (aus älterem stefn, efne)."

Luick (§75 Anm. 1) agrees: "e vor jüngerem mn aus fn: emn 'eben', stemn 'Stimme'."

**The parallel of efn / emn 'even' (< PGmc \*ebnaz):**

R/T (p.330) present the parallel explicitly:
> PGmc \*ebnaz 'level, even, equal' (Goth. ibns, ON jafn) → PWGmc \*ebn → OE \*ebn → efen ~ efn → emn

The chain ebn → efn → emn is structurally identical to stebn → stefn → stemn. Both show:
1. Original *-bn-* cluster
2. Labial devoicing: bn → fn
3. Late WS nasal assimilation: fn → mn

The parallelism confirms that stemn is secondary (from stefn, from stebn), not primary.

**Middle English continuation:**

Luick (Hist. Gr. §347, p.418) provides decisive ME evidence. He notes that when OE words with syllabic nasals after short syllables passed into ME, the development depended on whether the nasal was still syllabic or had become part of a consonant cluster. For stefn, he gives:

> ME **stevne** 'Stimme' (from OE oblique stefne), beside ME **stem** 'Stimme' (from OE stefn with cluster simplification)

The ME form **stevne** (with -v- < OE -f-) proves that the immediate pre-ME form had *-fn-*, not *-mn-*. If stemn (with -mn-) had been the primary OE form, ME would show \*stemne, not stevne. The fact that ME continues the fn-type, not the mn-type, confirms that stemn was a late and specifically WS variant, while stefn was the form that actually fed into ME.

The same argument applies to the parallel word: ME **evene** (with -v-) < OE efne (not < emne). Again, the fn-type, not the mn-type, is ancestral to the ME form.

**Summary of OE chronology:**
1. Pre-OE \*stebn- (preserved in CorpGl stebn, c.800)
2. Early OE stefn (bn → fn; general across all dialects)
3. Late WS stemn (fn → mn; specifically West Saxon, Alfredian period or later)
4. ME stevne (continues the fn-type, confirming stemn is secondary)

---

#### D. Comparative Germanic evidence

| Language | Form(s) | Source | Notes |
|----------|---------|-------|-------|
| **Gothic** | stibna f. | Kroonen p.480 | Points to *stebn- or *stibn- (e/i-grade with *-bn-) |
| **Old Saxon** | stemna f. | Kroonen p.480 | Points to *stemn- (e-grade with *-mn-) |
| **Old High German** | stimma, stimna f. | Kroonen p.480 | stimna points to *stimn- (i-grade with *-mn-); stimma to *stimmō- (with gemination) |
| **Old Frisian** | stemme f. | Kroonen p.480 | Points to *stemm- (geminate) or *stemn- |
| **Old Norse** | — | | Not directly attested in this meaning |
| **Dutch** | stem c. | | Continues WGmc *stemn- or *stemm- |
| **Old English** | stebn, stefn, stemn | R/T p.330, Bülbring §445 | Chronological chain (see §C above) |

**Where the daughter languages agree:** All WGmc forms point to an e-grade root vowel *stem-* (or, in OHG *stimna*, an i-grade *stim-* that could reflect raising before nasal). Gothic stibna likewise points to *steb(i)n- with front vowel (e or i). There is no daughter-language evidence for an a-grade or o-grade root in the nominative.

**Where the daughter languages diverge:** The consonantism of the medial cluster varies:
- **\*-bn-** type: Gothic stibna, OE stebn/stefn
- **\*-mn-** type: OS stemna, OE stemn (secondary)
- **\*-mm-** type: OHG stimma, OFri. stemme

This three-way split is the core of the reconstructional problem. Depending on which is taken as primary, the others must be derived by assimilation or dissimilation.

---

#### E. History of scholarship

**R/T (vol.2, p.330; 2014):** Reconstruct **\*stebnō** (ō-stem f., e-grade, *-bn-*). They present the derivation as: \*stebnō → PWGmc \*stebnu → OE stebn → stefn → stemn. They treat *-bn-* as the original cluster, with fn and mn as successive OE-internal assimilations. This analysis takes Gothic stibna as the most conservative witness for the consonantism. R/T place this word in a discussion of epenthesis after short syllables, alongside \*swefnaz → swefn, \*hrabnaz → hrefn → hræfn → hremn, \*ebnaz → efen ~ efn → emn. All share the *-bn-* → *-fn-* → *-mn-* trajectory.

**Kroonen (EDPG p.480, 488; 2013):** Gives the headword as **\*stimnō-** f. but discusses multiple PGmc variants reflecting PIE ablaut. He states that Go. stibna and OHG stimna "point to \*stem-n-" (e-grade), while OE stemn, stefn, OFri. stemme, OS stemna "are usually derived from \*stamnjo- < \*stom-n-" (o-grade with j-umlaut). He interprets the variation as preserving "remnants of the PIE ablaut" across different thematizations. In his introductory discussion (p.xxxvi), Kroonen discusses the \*-mn- → \*-bn- change and notes that the word for 'voice' shows "all three possibilities" (\*-mn-, \*-bn-, \*-mm-). He proposes that the ablauting n-stem nominative \*stemd alternated with a genitive \*stimmaz and a dative \*stemeni, and that thematization into an ō-stem produced the different daughter-language variants.

**Orel (Handbook of Germanic Etymology, p.374; 2003):** Gives the headword as **\*stebnò ~ \*stemnò** sb.f., explicitly listing BOTH consonant variants as coordinate alternatives. He glosses the cognates: "Goth stibna 'voice', OE stefn, stemn id., OFris stifne, stemme id., OS stemna id., OHG stimna, stimma id." He concludes: **"Of unknown origin"** — i.e. he explicitly leaves the deeper etymology open, declining to commit to the Hittite/Greek comparanda that other scholars accept. His bibliography references include Wennerberg (*Sprache* XVIII, 28–29), who follows the connection to \*stom- 'mouth'. Orel's dual headword \*stebnò ~ \*stemnò is the most honest representation of the state of knowledge: neither consonant type can be shown to be primary on purely comparative grounds.

**Fulk (Comparative Grammar of the Early Germanic Languages, §6.11 n.6; 2018):** In a footnote on PGmc consonant assimilations, Fulk states: "the etymologies of OE stefn, stemn 'voice' (Go. stibna), hrafn, hramn 'raven', and efn, emn 'even' (Go. ibns) are rather insecure, though the last is a fairly probable example." This is significant: Fulk regards the etymology of stefn/stemn as **insecure** even as an example of the bn → fn → mn chain. This is more cautious than R/T, who present \*stebnō as established.

**Kluge/Seebold (Etymologisches Wörterbuch, s.v. *Stimme*; 24th ed., 2002):** Reconstruct **g. \*stemnō f. "Stimme"** — i.e. a PGmc form with *-mn-* cluster, explicitly different from R/T's \*stebnō. They state: "Obwohl die lautlichen Entwicklungen im einzelnen nicht klar sind, ist am ehesten von (ig.) \*stemn-ā auszugehen" ("Although the phonological developments are not entirely clear in detail, it is best to start from IE \*stemn-ā"). They connect the word to Greek stóma 'mouth', Avestan staman- 'muzzle', Welsh safn 'mouth'. Bibliography references include Wennerberg, C. (*Sprache* 18, 1972, 24–33) and Jankowsky, K.R. (FS Dick, 1989, 199–221, "anders" = a different view).

**Polomé ("Notes on the Reflexes of IE /ms/ in Germanic", *RBPH* 45.3, 1967, pp.800–826):** Discusses the alternation specifically in the context of PGmc cluster assimilations. He notes (p.819) that "at an older date, -mn- became \*-bn- in Germanic though leveling inside paradigms has often obscured the original distribution of the forms." He treats \*-mn- as primary and \*-bn- as the result of dissimilation — the **opposite** direction from R/T. He gives OE stefn : stemn 'voice' as a case where "the alternation between \*-m- and \*-ṣ̌- was leveled in favor of -m-" or where "doublets developed." This is the clearest statement in the literature that the \*-bn- / \*-mn- direction of change is itself disputed.

**Vine ("Greek στωμύλος 'chatty'", *IEUL* 7, 2019, pp.222–240):** In a study of PIE \*stom-/\*stem- derivatives, Vine discusses "Gmc. \*stemnō- 'voice' (Go. stibna, OHG stimna/stimma)" as a continuation of a PIE root meaning 'mouth'. He reconstructs a PIE hysterokinetic internal derivative \*stomh₁-mén- (with o-grade and \*-men- suffix) alongside a thematic by-form \*stom-o- 'mouth'. His analysis connects the 'voice' word to a broader family including Greek stóma, Hittite istaman- 'ear', and Avestan staman- 'snout'. The contribution is on the PIE side (ablaut grades, suffix types) rather than on the PGmc reconstruction per se, but it supports the view that the PIE source was complex and that different Germanic thematizations may preserve different ablaut grades.

**Bülbring (Altengl. Elementarbuch §§62, 170, 445, 485; 1902):** Does not attempt a PGmc reconstruction but provides the most detailed OE-internal evidence. He demonstrates that stebn → stefn → stemn is the correct chronological sequence within OE, with the fn → mn step restricted to WS and datable to the Alfredian period (§62 Anm. 3, §485). His treatment of the parallel efn → emn is crucial comparative evidence.

**Luick (Hist. Gramm. §§75, 211, 347; 1914–40):** Confirms e before late mn (from fn) is preserved (§75 Anm. 1). In §211, he discusses a separate word "stemn 'Stamm'" (= 'stem, prow'), which he derives "aus \*stofn (vgl. as. stamn und me. stam)" — this is a DIFFERENT word from stemn 'voice' and should not be confused with it. His ME evidence (§347) is decisive: ME stevne continues OE stefn (with -v- < -f-), proving the fn-type is ancestral to ME, not the mn-type.

**Kaluza (Hist. Gramm. der engl. Sprache, 1900–01):** Does not treat the etymology of stefn/stemn in detail, but his treatment of OE consonant clusters and the bn/fn/mn alternation is consistent with the picture in Bülbring and Luick.

**Hogg (vol.1; 1992):** References stefn in the context of Scandinavian loanwords (stefn 'summons' may be influenced by ON; §4.18). Does not engage with the deeper reconstructional question.

**Summary of scholarly positions:**

**Scholars preferring a \*stebn- type reconstruction (bn primary):**
- R/T (2014): explicitly \*stebnō

**Scholars preferring or allowing a \*stemn- / \*stimn- type reconstruction (mn primary):**
- Kluge/Seebold (2002): g. \*stemnō
- Kroonen (2013): heading \*stimnō-, but acknowledges multiple variants
- Polomé (1967): treats \*-mn- as older than \*-bn- in this word

**Scholars presenting both variants as coordinate:**
- Orel (2003): headword \*stebnò ~ \*stemnò (explicitly dual)

**Scholars who regard the etymology as insecure or leave it open:**
- Fulk (2018): "rather insecure"
- Orel (2003): "Of unknown origin" (re deeper IE etymology)
- Kroonen (2013): presents diversity as PIE ablaut remnants

**Scholars deriving OE forms from a different thematization or analogical reshaping:**
- Kroonen (2013): mentions \*stamnjo- (o-grade jō-stem with j-umlaut) as the "usual" derivation of OE stemn in the older literature

**Not yet consulted:**
- Wennerberg, C. (*Die Sprache* 18, 1972, 24–33) — cited by both Orel and Kluge/Seebold; follows connection to \*stom- 'mouth'
- Jankowsky, K.R. (FS Dick, 1989, 199–221) — cited by Kluge/Seebold as "anders" (a dissenting view)
- Lloyd & Springer, *EWA* s.v. — OHG etymological dictionary (scan not yet OCRed)

---

#### F. Open questions for later return

The following questions are **not resolved** by our current treatment and are explicitly deferred:

1. **Root vocalism:** Is the PGmc root vowel *e* (R/T), *i* (Kroonen heading, cf. Go. stibna, OHG stimna), or were both grades present in the paradigm (Kroonen's ablaut analysis)?

2. **Whether \*-bn- or \*-mn- is primary:** R/T treat \*-bn- as original (with Go. stibna as key witness) and \*-mn- as a later assimilation. Kroonen treats \*-mn- as at least equally old, with \*-bn- arising from dissimilation. The direction of change (mn → bn, or bn → mn?) is not settled.

3. **How to weight Gothic stibna:** Gothic is often treated as the most archaic witness, but the i-vocalism could reflect Gothic-internal raising (\*e → i before nasal), and the *-bn-* cluster could reflect Gothic-internal dissimilation from \*-mn-*. The Gothic form is thus not unambiguous evidence for the PGmc reconstruction.

4. **Whether different daughter branches preserve different thematizations:** Kroonen's analysis implies that the PIE paradigm (\*stém-mn, gen. \*stém-mn-s, loc. \*stm-mén-i) was thematized differently in different branches: some preserved e-grade, others o-grade; some preserved \*-mn-, others \*-bn-. If so, there may be no single PGmc reconstruction that accounts for all daughters.

5. **How the Indo-European comparanda should be used:** Hittite istaman- ~ istamin-, Greek stóma, Avestan staman- all point to a PIE root \*stom-/\*stem-, but the exact ablaut grade and suffixation of the PIE source word remain debated (see Kroonen p.480 for references).

6. **Whether the whole set is partially remodeled analogically:** Several of the daughter-language forms (OHG stimma with geminate, OFri. stemme with geminate) look like they may have been reshaped by analogy with other words or by expressive gemination. The extent of analogical remodeling is unknown.

---

#### G. Future research plan

**We are not solving this now.** The current treatment (pre-OE transponent \*stebn- → OE stefn) is correct for the OE pipeline and is well justified by the OE-internal evidence. The deeper PGmc question is deferred.

**When the OHG and Gothic transducers are built,** this item should be revisited as a **cross-branch test case**. Specifically:
- The Gothic transducer will need to derive stibna from whatever PGmc form is posited
- The OHG transducer will need to derive stimna/stimma
- The OS pipeline (if built) will need to derive stemna
- If a single PGmc reconstruction can feed all daughter transducers and yield the correct output in each case, that would constitute strong evidence for that reconstruction
- If no single reconstruction works for all branches, that would confirm Kroonen's view that different branches preserve different thematizations

This word is flagged as a **potential publishable finding**: it is a showcase case of the methodological point that implementing historical transducers forces a sharp distinction between (a) what must be assumed locally for one daughter language, and (b) what is genuinely reconstructable for Proto-Germanic. See notable_findings.md §5.

### Summary of proposed actions

1. **ræst** (*rastō): Either (a) use oblique form *rastas → ræstes (changing both proto and target), or (b) document as paradigmatic leveling exception with ALIGNMENT note. Decision pending — both options have trade-offs.

2. **tæppa** (*tappô): Use n-stem oblique *tappăn → tæppan (changing both proto and target). Clean parallel to existing oblique approaches. Fully lautgesetzlich.

3. **stefn** (**DONE**): TSV updated to pre-OE transponent \*stebnō → stefn. See "The stefn/stemn problem" dossier above and notable_findings.md §5.

### Note on ræst oblique form problem

After investigating the pipeline's suffix acceptance system (`pgrmWeakTailVowel`), the following constraints apply:

- The ō-stem gen.sg. *-ōz is NOT in the accepted suffix list. Even if added, the *-ō component would trigger A-restoration (it's a back vowel).
- The a-stem gen.sg. encoding *-as IS accepted and gives the correct phonological result: `rastas → ræstes`.
- Using *-as for an ō-stem is morphologically imprecise, but the phonological outcome is identical to what the historical gen.sg. *-ōz → PWGmc *-a → AFB *-æ → OE -e would produce.

**UPDATE: ō-stem gen.sg. *-ōz now properly modeled in pipeline.**

The limitation described above has been resolved. We added:
1. `ō:{*ō} z:{*z}` to pgrmWeakTailVowel (the suffix list), accepting *-ōz as a valid suffix.
2. A new rule `PGmcFinalOZShortening` in PGmcFinalZLoss that maps `{*ō}{*z} → {*a}` at word boundary, applied BEFORE general z-deletion via sequential composition (.o.).

**Result:** `rastōz → ræste` ✓ (PGmc gen.sg. *rastōz → OE gen.sg. ræste, well-attested in BT).
The ō-stem nom.sg. path is unaffected: `rastō → rast` (NWGmcFinalLongORaising still applies when *-ō is truly word-final).

TSV row 2152 (ræst) now uses genuine PGmc gen.sg. *rastōz, target ræste. This follows the same oblique-form approach as cow (*kūi → cȳ) and fire (*fūri → fȳre): the TSV records an oblique paradigm cell that can be derived lautgesetzlich, explaining the attested OE root vowel through regular sound change rather than analogical leveling.

### Historical phonology of final *-z loss and its interaction with rhotacism

#### The key chronological finding: z-loss preceded rhotacism

An earlier draft of these notes incorrectly posited rhotacism (*-z → *-r) as an intermediate stage in the development of final *-z. On closer reading, R/T §3.3.1 (vol.2, p.98) explicitly state the opposite:

> "On the WGmc side, the loss of word-final *z in unstressed syllables (see 3.1.1), which did not occur in Norse, must likewise have preceded the merger of *z with *r." (R/T vol.2, p.98, lines 5249–5251)

Hogg (vol.1, §2.66, p.52) concurs:

> "Gmc /z/ yielded /r/ in intervocalic position in Old English (rhotacism), but in final position it is generally lost."

The WGmc chronology is therefore:
1. **PWGmc final *-z loss** (§3.1.1): word-final *-z in unstressed syllables is directly lost.
2. **Post-PWGmc rhotacism** (§3.3.1): remaining (medial) *-z merges with *-r as /r/.

Final *-z was **never rhotacized**. It was already gone by the time rhotacism occurred. R/T explicitly discuss this, noting that rhotacism "occurred independently in Norse and in WGmc" (p.97), that "rhotacism is an easily repeatable change" (p.98), and that it should be assigned to post-PWGmc, not PWGmc.

R/T also discuss whether *-z "had already become some sort of rhotic" before its loss (§3.1.1, p.61, line 3358), but conclude that ordering z-loss before rhotacism "is less complex and therefore preferable" (p.61, line 3360). Their evidence: (a) there is no need to explain why *-a was lost before final *-z but not before *-r if z-loss happened first; (b) independent evidence suggests z-loss was an early change (§3.1.1, §3.2.1).

#### Why this resolves the exceptionlessness concern

The previous version of these notes worried about the different fates of inherited *-r (preserved in *watōr → wæter) versus inflectional *-z (lost in *-ōz → -e). If rhotacism had applied to final *-z, then inherited *-r and rhotacized *-r (< *-z) would have been phonologically identical at some stage, and their different fates would require a non-phonological (grammatically conditioned) explanation.

But since z-loss **preceded** rhotacism, there was **no merger**:
- Inherited *-r was always *-r — never subject to z-loss.
- PGmc final *-z was directly lost — it never became *-r.
- These were **different phonemes throughout**, and different phonemes having different fates is entirely regular in Neogrammarian terms.

Our pipeline models this correctly:
```
PGmcFinalZLoss:  {*z} → 0 at word boundary  (targets *-z only, not *-r)
PGmcRhotacism:   {*z} → {*r} after vocalic   (applies to surviving medial *-z)
```

In the pipeline, PGmcFinalZLoss runs **before** PGmcRhotacism (within PGmcConsonantRules). By the time rhotacism applies, all final *-z has already been deleted. Rhotacism therefore applies only to medial *-z, which is the correct historical outcome.

#### The gen.sg. *-ōz → *-a development: not a shortcut

Our rule `{*ō}{*z} → {*a}` was previously described as a "shortcut" that "conflates intermediate stages." This was wrong. R/T present the development as a **single PWGmc step**:

> "PGmc *gebōz 'gift's' gen. sg. (Goth. gibos, ON gjafar) > PWGmc *geba" (vol.2, p.58, line 3198)

There is no intermediate *-gebō stage (with z deleted but ō not yet shortened) in their account. The z-loss and vowel shortening were a single historical process: when final *-z was lost, the preceding unstressed bimoric *-ō shortened to *-a.

This is phonetically natural: the loss of a coda consonant in an unstressed syllable resulted in compensatory restructuring of the syllable, with the freed long vowel reducing. The key conditioning factor is the phonological environment: bimoric *-ō immediately before final *-z. The nom.sg. *-ō (which had no following *-z) was not subject to this change — it was already in absolute final position and underwent NWGmcFinalLongORaising (*-ō → *-u) at a later stage.

Modeling this as two separate rules (z-deletion followed by *-ō shortening) would actually be **incorrect**, because a general "final *-ō → *-a" rule would also incorrectly apply to the nom.sg. *-ō. The single-step rule `{*ō}{*z} → {*a}` correctly restricts the change to the environment where *-z was present.

#### Bimoric vs. trimoric *-ōz: gen.sg. vs. nom.pl.

R/T distinguish the gen.sg. (bimoric *-ōz) from the nom.pl. (trimoric *-ôz) on pp.73-74 (§3.1.1):
- **Bimoric gen.sg. *gebōz** → PWGmc *geba (short *-a): vol.2 p.73, line 4054
- **Trimoric nom.pl. *gebôz** → PWGmc *gebo (short *-o): vol.2 p.73, line 4071

The different vowel outcomes (*-a vs *-o) are phonologically conditioned by the trimoric/bimoric distinction, not by grammatical case. Bimoric *-ō shortened to *-a; trimoric *-ô shortened to *-o. Our pipeline currently only handles the gen.sg. (bimoric) case, which is sufficient for the forms in our TSV.

#### Pipeline trace comparison: inherited *-ōr vs. gen.sg. *-ōz

| Stage | *watōr (inherited *-ōr) | *rastōz (gen.sg. *-ōz) |
|---|---|---|
| After PGmcFinalZLoss | *watōr (unchanged — *-r ≠ *-z) | *rasta (*-ōz → *-a) |
| After PWGmcChanges | *watar (*-ō → *-a before *-r) | *rasta (unchanged) |
| After AFB | *wætær | *ræstæ |
| After A-restoration | *wætær (no back trigger) | *ræstæ (no back trigger) |
| After weak-tail reduction | *wæter | *ræste |
| Final OE output | wæter | ræste |

Both root vowels undergo identical treatment (PGmc *a → OE æ via AFB, with no A-restoration because the suffix vowel *-a/*-æ is front). The only output difference is the final consonant: *-r survives as -er, *-z (already lost) is absent giving -e. This reflects different input phonemes, not grammatically conditioned change.

**Hypothetical test — *rastōr (inherited *-ōr on *rast- root):**
Pipeline gives `ræster` — confirming that root vowel treatment is identical regardless of suffix consonant.

#### Summary of secondary sources on z-loss and rhotacism

| Source | Final *-z treatment | Rhotacism scope | Chronological ordering |
|---|---|---|---|
| R/T vol.2 §3.1.1 (pp.58-61) | "Word-final *-z has been lost throughout WGmc when the preceding syllable nucleus was unstressed" | — | Z-loss is PWGmc; preferred ordering: z-loss before a-loss (p.61) |
| R/T vol.2 §3.3.1 (pp.97-100) | "The loss of word-final *z … must likewise have preceded the merger of *z with *r" | Intervocalic and before coronals in WGmc (p.98-100); post-PWGmc (p.97) | Z-loss before rhotacism (p.98) |
| Hogg vol.1 §2.66 (p.52) | "In final position it is generally lost" | "Intervocalic position in Old English" | Consistent with R/T |
| Luick §297 (p.367) | *-a lost before *-z ("schwanden alle a im Auslaut und vor z"); §299 Anm. 2 (p.369): vowels before z preserved during early shortening, "dies ist aber das letzte Anzeichen seines Vorhandenseins" | — | Z still present during §299 bimoraic shortening; lost afterwards |
| R/T vol.2 p.73-74 | Gen.sg. *-ōz → *-a (bimoric); nom.pl. *-ôz → *-o (trimoric) | — | Both part of PWGmc z-loss |

### Bimoraic vs. trimoraic *-ō: cross-source analysis and pipeline verification

#### The bimoraic/trimoraic distinction in the secondary literature

All major sources agree on the fundamental distinction between bimoraic (zweimorig/gestoßen/bimoric) and trimoraic (dreimorig/geschliffen/trimoric) unstressed final *-ō, though they differ in terminology, assignment of specific forms, and the details of chronology.

**Luick** (Historische Grammatik, §299, pp.368-369): Distinguishes "zweimorige Längen mit gestoßenem (d. h. eingipfligem) Akzent" (bimoraic with pushed/mono-peaked accent) from "dreimorige mit 'geschliffenem' (d. h. zweigipfligem) Akzent" (trimoraic with ground/two-peaked accent). Bimoraic *-ō → u in NWGmc/Norse (§299.2: "Urgerm. ō ergab im Nordischen und Westgermanischen u"; examples: *gebu, *faru, *wordu). What Luick treats as nasalized *-ō̃ (from *-ōn, *-ōm: §299.3) → a on "dem ganzen Gebiet" (common Gmc). Trimoraic forms "zunächst als Längen erhalten blieben" — they survived the early shortening and were only reduced later. Crucially, Luick §299 Anm. 2 notes that all long vowels before *-z were preserved during this period: "*gebōz plur. 'Gaben' ... Daraus folgt, daß damals z noch nicht abgefallen war." Z-loss was therefore later than bimoraic shortening but, per Luick, it is "das letzte Anzeichen seines Vorhandenseins" (the last sign of z's existence).

**Bülbring** (Altenglisches Elementarbuch, §§387-390, pp.177-178): §387: bimoraic final *-ō → u in all WGmc languages, then shortened to u, then preserved/lost depending on preceding syllable weight (same result as Luick/R/T). §389: nasalized *-ō̃ (< *-ōn, *-ōm) → *-a in WGmc, then → *-æ (by AFB) → -e in OE (examples: acc.sg. larae/lare, pret. gisettae/gesette). §390: trimoraic *-ô → OE -a (examples: n-stem nom.sg. boda, gen.pl. daga, **WS/Kent. nom.pl. of ō-stems lāra**, **WS/Kent. gen.sg. of -ung abstracts leasunga**).

**R/T** (vol.2, pp.58, 73-74, 267, 314): Bimoraic *-ō → *-u in PNWGmc (§5.1.3, p.267: "word-final bimoric non-nasalized long *-ō became short *-u in unstressed syllables"). Gen.sg. *gebōz → PWGmc *geba (p.58, listed alongside bimoric forms on p.73). Nom.pl. *gebôz → PWGmc *gebo (pp.73-74, listed alongside trimoric forms). The key example on p.73: bimoric *gebōz gen.sg. → *geba vs. trimoric *gebôz nom.pl. → *gebo.

**Hogg** (vol.1, §2.66, p.52): Notes bimoraic/trimoraic distinction in passing but does not elaborate on the ō-stem paradigm specifically. Follows R/T essentially.

#### Where the sources agree

1. **Bimoraic final *-ō → u**: All sources agree. Luick §299.2, Bülbring §387, R/T §5.1.3. Examples: *gebō nom.sg. → *gebu (→ OE giefu after light stem, -∅ after heavy stem).

2. **Trimoraic final *-ô → a in OE**: All sources agree on the OE outcome. Luick §299.3 (nasalized forms → a), Bülbring §390, R/T pp.73-74. Examples: n-stem nom.sg. *namô → nama.

3. **Z-loss preceded rhotacism**: R/T §3.3.1 explicitly; Luick §299 Anm. 2 implicitly (z still present during shortening, then lost). Hogg §2.66 agrees.

4. **Bimoraic *-ōz (gen.sg.) → -e in OE**: R/T (p.58: *gebōz → *geba → OE giefe) and Luick §301.3 (the *-a from early shortening was fronted by AFB → *-æ → -e) agree that the regular ō-stem gen.sg. gives OE -e.

#### Where the sources may disagree

1. **Gen.sg. *-ōz: bimoraic or trimoraic?** R/T treat the gen.sg. *-ōz as BIMORAIC (p.73, listed among bimoric forms; outcome: PWGmc *-a → OE -e). Bülbring §390 lists "ws. kent. Gen. Sg. der Abstrakta auf ung: leasunga 'Truges' (urg. -ōz)" under TRIMORAIC (outcome: OE -a). However, this appears to be a CLASS-SPECIFIC or DIALECTAL variant: (a) the -ung abstract class may have had different mora assignment; (b) Bülbring specifies "ws. kent." (West Saxon/Kentish), suggesting dialectal conditioning; (c) the standard WS gen.sg. of ō-stems is -e (giefe), not -a (cf. R/T p.314). Our pipeline follows R/T in treating the gen.sg. as bimoraic, giving -e, which is the standard WS outcome.

2. **Mechanism of *-ōz shortening**: R/T present *-ōz → *-a as a single PWGmc development (p.58: *gebōz → *geba with no intermediate stage). Luick implies a two-step process: (a) z was present during early bimoraic shortening (§299 Anm. 2), so the *-ō in *-ōz was not word-final and did not undergo §299 shortening; (b) z was then lost; (c) the freed *-ō was shortened by a later change. Both analyses produce the same result (*-ōz → *-a), but Luick's is more decomposed. Our pipeline follows R/T's single-step approach, which is also technically necessary: a separate "final *-ō → *-a" rule would incorrectly affect nom.sg. *-ō (see discussion above).

3. **Trimoraic *-ô shortening timing**: Luick places it early (§299.3, common Gmc). R/T place it later (post-PWGmc unstressed vowel reduction). Bülbring §390 gives OE -a directly, implying the shortening happened late enough to escape AFB fronting (§389 nasalized bimoraic → -e, but §390 trimoraic → -a). Our pipeline implements it as a late change (OEUnstressedLongVowelShortening, after AFB and A-restoration), which matches Bülbring's OE -a outcome for trimoraic forms and also ensures A-restoration correctly sees {*ô} as a back vowel trigger.

#### Pipeline verification

The pipeline correctly implements the bimoraic/trimoraic distinction:

| Input | Mora type | Pipeline path | OE output | Correct? |
|---|---|---|---|---|
| *rastō (nom.sg.) | Bimoraic *-ō | NWGmcFinalLongORaising: {*ō}→{*u}; heavy apocope | rast | ✓ |
| *rastōz (gen.sg.) | Bimoraic *-ōz | PGmcFinalOZShortening: {*ō}{*z}→{*a}; AFB | ræste | ✓ |
| *namô (n-stem nom.sg.) | Trimoraic *-ô | Persists through ō-raising (not matched); OEUnstressedLongVowelShortening: {*ô}→{*a} | nama | ✓ |
| *tungōn (fem. n-stem) | Bimoraic *-ōn | NWGmcNStemNLoss: {*ō}{*n}→{*ǭ}; shortening → {*æ} → -e | tunge | ✓ |

Key observations:
1. **Gen.sg. uses bimoraic {*ō}** in the suffix `ō:{*ō} z:{*z}` (line 334), matching R/T's bimoraic assignment.
2. **PGmcFinalOZShortening targets {*ō}{*z} only** — it does NOT match trimoraic {*ô}{*z}, ensuring the two mora classes are kept distinct.
3. **NWGmcFinalLongORaising targets {*ō} only** — it does NOT match trimoraic {*ô}, which correctly preserves trimoraic forms through ō-raising.
4. **{*ô} is defined as a back vowel trigger for A-restoration** (line 1213: `OEARestorationTriggerVowel`), so trimoraic suffixes correctly trigger A-restoration of root *a (e.g., *namô → nama, not *næma).
5. **OEUnstressedLongVowelShortening handles {*ô} → {*a}** as a late change (line 1340), after AFB and A-restoration, so the resulting -a is not fronted — giving OE -a for trimoraic forms, matching all sources.

A hypothetical trimoraic *-ôz (e.g., nom.pl.) is not currently in the suffix list (not needed for our TSV data), but the system would handle it correctly: PGmcFinalOZShortening would not match ({*ō} ≠ {*ô}); PGmcFinalZDeletion would delete {*z}; the freed {*ô} would pass through ō-raising and AFB unchanged; OEUnstressedLongVowelShortening would produce {*a}. Result: -a, matching R/T and Bülbring for nom.pl.

---

## Reference library integration (2026-03-08)

### Campbell's *Old English Grammar* (1959)

OCR'd the full text (438 pages) via `ocrmypdf --force-ocr -l eng` and saved to
`docs/references/campbell_old_english_grammar.txt` (34,276 lines). Key sections for our work:
- §§115–118 (u-lowering near labials)
- §§148–160 (retraction / A-restoration)
- §§351–353, 388–393 (prehistoric and historical syncope)
- §§407–408 (West Germanic gemination)

Quotations from Campbell have been integrated into `docs/analysis/notable_findings.md`
§§1–4, cross-referenced with Hogg, R/T, Bülbring, Luick, and Kaluza.

### EWA Band I (Lloyd & Springer 1988)

Extracted from a mislabeled DJVU file (labeled as Campbell but actually containing EWA).
Saved to `docs/references/ewa_band1_lloyd_springer.txt` (9,853 lines). Covers a–bezzisto.
Available online at https://ewa.saw-leipzig.de/headwords/de for further consultation.

### Cross-referencing update

`docs/analysis/notable_findings.md` §§1–4 now integrate:
- Campbell OEG quotations on syncope, u-lowering, *j-changes, A-restoration
- German-language sources (Bülbring, Luick, Kaluza) on the same phenomena
- Points of scholarly agreement and disagreement highlighted for each finding

---

## OEAwLongDiphthong: PGmc *aw → OE ēaw before vowels (Campbell §272)

PGmc *aw before a following vowel → OE ēaw, parallel to the existing
OEEwLongDiphthong (*ew → ēow). The *w glide is preserved because it remains
intervocalic; in pre-consonantal / word-final position, *aw had already merged
with *au → ēa via OEAuFronting + OEDiphthongLeveling.

**Rule:** `{*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}]`

The context `[EnglishStarVocalic | {*ô}]` ensures the rule fires only when *w
is immediately followed by a vowel. This excludes *j-initial suffixes (e.g.
*-jăną, *-ją) where *a fronts via i-umlaut instead. {*ô} (trimoraic) is added
explicitly because it is not in PGmcStarVocalic.

**Pipeline placement:** After OEEwLongDiphthong, before AngloFrisianBrightening.
At this point *a is still unfronted, so the rule targets *a directly.

**Fixes (3 new matches):**
- *dawwō → dēaw (was dawu) — dew
- *strawą → strēaw (was streaw) — straw
- *xawwăną → hēawan (was heawan) — hew

**Vowel fixed but still mismatching (sc/sċ palatal marker):**
- *skawōjăną → sċēawian (expected scēawian)
- *skawô → sċēawa (expected scēawa)
- *skawōθi → sċēaweþ (expected scēaweþ)

**Correctly excluded:**
- *xawwją → heow (expected hīeġ) — *j follows *w, not a vowel
- *strawjăną → streowan (expected strewian) — *j follows *w

Mismatches: 103 → 100.

---

## TSV proto correction: *wainōjăną → *hwīnăną (OE hwīnan 'to whine')

The OE row for 'whine' (ID 2286) had proto \*wainōjăną, which is the
reconstruction for PGmc \*wainōjan- 'to lament, weep' (→ OE wānian, German
weinen, ON veina). But the OE target form hwīnan is a Class I strong verb
meaning 'to whine, hiss, rush', which Kroonen (2013, s.v. \*hwīnan-) derives
from PGmc \*hwīnăną, tracing it to PIE \*ḱwey- 'to hiss, whistle.'

The two words are etymologically distinct:

| PGmc form      | OE reflex | Class    | Meaning         | NE descendant |
|---------------|-----------|----------|-----------------|---------------|
| \*hwīnăną     | hwīnan    | strong I | to whine, hiss  | whine         |
| \*wainōjăną   | wānian    | weak II  | to lament, weep | (wane?)       |

The initial \*hw- (< PIE \*ḱw-) vs. \*w- and the vowel grade (\*ī vs. \*ai)
confirm that these cannot be the same lexeme. The error appears to originate
from Wiktionary's automatic cognate-linking, which grouped them under the
same cognate set (189). The German weinen row correctly has \*wainōjăną and
is unaffected.

Kluge/Seebold (24th ed., s.v. _weinen_) lists 'ne. whine' among descendants
of g. \*wainō-, but this appears to be a conflation; NE _whine_ continues OE
hwīnan (str. I), not OE wānian (wk. II).

Proto changed to \*hwīnăną; pipeline now produces hwīnan ✓.

---

## Weak noun declension class corrections: *gallô, *xnekkô (2026-03-08)

### Overview

The mismatch report contained a bucket `final_vowel_missing__weak_noun_like` with 8 items where the
pipeline produced a bare stem (no final vowel) but the expected OE form ended in *-a* or *-e*,
typical of weak noun nominatives. Investigation showed that several TSV entries had the wrong
PGmc declension class — strong a-stems or strong ō-stems where the OE word is actually a weak
n-stem. Correcting the proto-form to the weak paradigm feeds the pipeline the right suffix,
which it then processes correctly.

### Case 1: \*gallą → \*gallô (OE ġealla 'gall, bile')

**Problem.** TSV had \*gallą (strong neuter a-stem). Pipeline gives *ġeall* (no final vowel after
heavy-syllable apocope). Expected OE form: *ġealla*.

**Correction.** Kroonen (2013) s.v. \*gallōn- reconstructs PGmc \*gallōn- (weak masculine n-stem),
citation form nom.sg. \*gallô. OE ġealla is indeed weak masculine (BT: "ġealla, an; m.").

**Pipeline result.** \*gallô → ġealla ✓. The weak n-stem suffix *-ô* passes through
NWGmcNStemNLoss → unstressed vowel shortening → surface *-a*. No further issues.

**Note on cognate set 205.** German *Galle* (feminine) has a different gender and declension class
from OE ġealla (weak masculine). Other rows in cognate set 205 retain \*gallą; the OE row now
has \*gallô in both PROTOFORM and PROTO columns.

### Case 2: \*xnakkăz → \*xnekkô (OE hnecca 'neck, nape')

This case required substantially more research than the other weak noun fixes because the OE
form *hnecca* has *e* where the standard PGmc reconstruction has *a*, and this discrepancy cannot
be explained by any regular OE sound change.

#### The problem

TSV had \*xnakkăz (strong masculine a-stem, a-grade root vowel). This is wrong in two respects:

1. **Declension class.** OE *hnecca* is weak masculine (BT: "HNECCA, an; m."). All major
   sources agree the PGmc word was a weak n-stem: Kroonen \*hnakkōn-, Orel \*xnakkaz ~ \*xnakkòn,
   Kluge/Seebold \*hnakka-/ōn.

2. **Root vowel grade.** The TSV had *a*-grade (\*xnakk-), which would yield OE \*hnacca (with
   A-restoration before the back suffix vowel, preventing AFB fronting to \*æ). But the standard
   OE form is *hnecca*, with *e*. No regular OE sound change turns *a* into *e* in this
   environment.

#### Root vowel ablaut: Kroonen's paradigm

Kroonen (2013) reconstructs this noun with **root vowel ablaut** across the paradigm (cited on
Wiktionary s.v. \*hnakkô, referencing Kroonen's etymon PIE \*knékō):

| Case | PGmc form | Ablaut grade |
|------|-----------|-------------|
| Nom.sg. | \*hnekkô | e-grade (PIE \*knékō) |
| Gen.sg. | \*hnukkaz | zero-grade |
| Acc.pl. | \*hnakkunz | a-grade (PIE o-grade) |

This is an amphikinetic paradigm where different case forms have different root vowels. The
daughter languages then generalized one grade at the expense of the others:

| Grade generalized | Languages | Forms |
|---|---|---|
| **e-grade** (from nom.sg.) | OE, OFris, MNdl, some MLG | OE *hnecca*, OFris *hnekka*, MNdl *necke/nec*, MLG *necke* |
| **a-grade** (from oblique) | ON, OHG, some MLG | ON *hnakkr/hnakki*, OHG *nac/nacko*, MLG *nacke* |

#### Scholarly sources

**Kluge/Seebold** s.v. *Nacken*: "Aus g. \*hnakka-/ōn m. 'Hinterhaupt, Nacken', auch in anord.
hnakkr, hnakki. **Daneben mit Ablaut** mndl. necke, nec, afr. hnekka, ae. hnecca." This explicitly
identifies the OE/OFris/MNdl forms as ablaut variants of the ON/OHG forms.

**Kluge/Seebold** s.v. *Genick*: "Kollektivbildung zu mndd. necke, afr. hnekka m., ae. hnecca m.
'Nacken'. **Dieses steht im Ablaut zu Nacken.**" — "This stands in ablaut with Nacken."

**Orel** s.v. \*xnakkaz ~ \*xnakkòn: Lists only ON hnakki, MLG nacke/necke, OHG nac/nacko.
Notably **omits OE hnecca entirely**, and does not discuss the ablaut. Orel's entry is therefore
incomplete for OE purposes.

**Wiktionary** (s.v. PGmc \*hnakkô): Notes that Kroonen reconstructs PIE \*knékō with root vowel
ablaut, and lists both PWGmc \*hnakkō and \*hnekkō as alternative forms. The OE descendants
include both \*hnæcca (from a-grade, with Anglo-Frisian Brightening) and *hnecca* (from e-grade).

#### Pipeline verification

| Input | Pipeline output | Match? |
|-------|----------------|--------|
| \*xnakkăz | hnæcc | ✗ (wrong class, wrong vowel, no final vowel) |
| \*xnakkô | hnacca | ✗ (correct class, but a-grade gives wrong root vowel) |
| \*xnekkô | hnecca | ✓ |

The e-grade form \*xnekkô is not a "transponent" or ad hoc workaround. It is the **actual PGmc
nominative singular** as reconstructed by Kroonen. The a-grade forms (\*xnakkăz in the TSV) reflect
the oblique stem that was generalized in ON and OHG, not the nom.sg. citation form.

#### Correction applied

OE row changed from \*xnakkăz to \*xnekkô (both PROTOFORM and PROTO columns). German row
retains \*xnakkăz (German *Nacken* continues the a-grade, generalized from the oblique).

#### Methodological note

This case illustrates a recurrent problem for the project: standard etymological dictionaries
often cite a single PGmc form (typically the a-grade or the most widely attested variant), but
individual daughter languages may continue a *different* ablaut grade of that same paradigm. When
the TSV imports a shared proto-form from a cognate database, it may silently import the wrong
grade for a given daughter language. The pipeline then produces a form with the wrong root vowel,
and the mismatch is not fixable by adding sound rules — it requires correcting the input form to
the grade actually continued in that branch. This is the same type of issue encountered with the
stefn/stemn problem (§ Case 3 above), though the hnecca case is more cleanly resolved because
Kroonen's own reconstruction already supplies the e-grade nom.sg.

### Case 3: \*flaskō → \*flaskōn (OE flasce 'flask, bottle')

**Problem.** TSV had \*flaskō (strong feminine ō-stem). Pipeline gives *flasc* (no final vowel:
heavy-syllable apocope removes \*-ō after heavy \*-sk cluster). Expected OE form: *flasce*.

**Declension class correction.** OE flasce is weak feminine (ōn-stem). All major sources agree:
Orel \*flaskò(n) sb.f., Wiktionary PGmc \*flaskǭ (weak fem.), Kluge/Seebold s.v. *Flasche*
(implies feminine, connected to \*flataz 'flat'). TSV corrected from \*flaskō to \*flaskōn.

**A-restoration interaction — a pipeline bug discovered.**

Changing the proto to \*flaskōn exposed a deeper pipeline issue. The corrected form went through:

1. NWGmcNStemNLoss: \*flaskōn → \*flaskǭ (nasalized long vowel)
2. AFB: \*a → \*æ → \*flæskǭ (wrongly fronted)
3. A-restoration: did NOT fire — \*ǭ was not in OEARestorationTriggerVowel
4. OESkPalatalization: \*æ (front vowel) before \*sk → \*ʃ (wrongly palatalized)
5. Unstressed vowel shortening: \*ǭ → \*e
6. Result: *flæsċe* (wrong root vowel AND wrong consonant)

The root cause: \*ǭ (nasalized long ō, from fem. n-stem \*-ōn → NWGmcNStemNLoss) is
**phonetically back** but was missing from the A-restoration trigger set. At the historical
stage when A-restoration applied, the following syllable still had a back vowel (\*ǭ < \*-ōn).
A-restoration should have prevented the fronting.

**The fix.** Added \*ǭ to OEARestorationTriggerVowel:

```
define OEARestorationTriggerVowel [EnglishStarBackVowel | {*ô} | {*ǭ}];
```

This change causes A-restoration to fire for root \*a before consonant clusters (excluding \*r,
\*l — which independently block A-restoration) followed by \*ǭ. The derivation now proceeds:

1. NWGmcNStemNLoss: \*flaskōn → \*flaskǭ
2. AFB: \*a → \*æ → \*flæskǭ
3. A-restoration: \*æ → \*a (because \*s, \*k in intervening set, \*ǭ now a trigger) → \*flaskǭ
4. OESkPalatalization: \*a is NOT a front vowel → medial \*sk NOT palatalized → \*flaskǭ
5. Unstressed vowel shortening: \*ǭ → \*e → \*flaske
6. Surface: *flasce* ✓

Both the root vowel (a, not æ) and the consonant (sc, not sċ) are now correct. The sc/sċ
fix is a consequence of the A-restoration fix: because \*a is not fronted, the SkPalatalization
"after front vowel" context (Campbell §440) no longer matches.

**Regression check.** All other fem. ōn-stems verified:

| Form | Before fix | After fix | Expected | Status |
|------|-----------|-----------|----------|--------|
| \*flaskōn | flæsċe | flasce | flasce | **fixed** |
| \*wartōn | wearte | wearte | wearte | unchanged (\*r blocks) |
| \*swalwōn | swealwe | swealwe | swealwe | unchanged (\*l blocks) |
| \*sapōn | sæpe | sape | sæp | bucket change (pre-existing length issue) |
| \*xertōn | heorte | heorte | heorte | unchanged (\*e root) |
| \*laimōn | lāme | lāme | lām | unchanged (\*ai root) |
| \*marōn | mære | mære | mære | unchanged (\*r blocks) |

\*sapōn moved from `final_vowel_extra` to `fronting_missing__afb` because the root vowel is
now *a* (not *æ*) while the TSV expects *sæp* (with *æ*). However, the expected form "sæp" is
itself problematic: OE *sāpe* has long *ā* and is weak feminine. The proto \*sapōn has short
\*a, so neither the old output (*sæpe*) nor the new (*sape*) matches the correct OE *sāpe*.
This is a separate vowel-length issue in the proto-form.

## ⚠️ FLAGGED ISSUE: PGmc Class III weak verb → OE Class II shift

### The problem

Four OE verbs in the TSV have PGmc \*-ēną (Class III weak) protos, but OE reflects them as Class II weak verbs (ending in -ian):

| ID | Proto | Pipeline output | Expected | OE class |
|----|-------|----------------|----------|----------|
| 2004 | \*fastēną | faston | fastian | II (-ian) |
| 2027 | \*fulgēną | folgon | folgian | II (-ian) |
| 2107 | \*libēną | leofon | lifian | II (-ian) |
| 2268 | \*wakēną | wacon | wacan | **strong VI** |

The pipeline correctly produces the regular phonological outcome of \*-ēną: the medial
\*ē undergoes NWGmcLongENasalRounding (\*ē → \*ō before nasal), yielding -on. But no
attested OE form preserves this regular outcome for any of these verbs.

### What Kroonen reconstructs

Kroonen's *Etymological Dictionary of Proto-Germanic* gives:

- **\*fastēn-** wv. (under \*fastu- entry, p.131): "Go. fastan, ON fasta, OE fastian, OFri. festia,
  OHG fastēn ww. 'to fast' < \*fastēn-." Denominal from \*fastu- 'firm'.
- **\*fulgēn-** wv. (p.158): "OE fylgan, folgian ww. 'id.', E to follow, OS folgon wv., OHG
  folgēn ww." He also notes: "ON fylgja and OE fylg(e)an continue a formation \*fulgjan-"
  — i.e. a Class I formation with \*j, separate from the \*-ēn- headword.
- **\*libēn-** wv. (p.336): "Go. liban ww. 'to live', ON lifa w.v., OE libban wv., OS libbian w.v.,
  OHG lebēn wv." Kroonen cites OE **libban** (Class III with gemination), NOT lifian. The
  TSV form lifian is a later Class II innovation within OE.
- **\*wakān-** s.v. (p.568): "Go. wakan s.v. 'id.', OE wacan." This is a **strong verb** (Class VI),
  not weak at all. The proto \*wakēną in the TSV is the wrong lexeme — it belongs to the
  Class III weak "to be awake, watch" (→ OE wacian), not the strong "to wake up" (→ wacan).

### The Class III → Class II shift: Ringe/Taylor's account

R/T vol.2 §3.3.2 (pp.161–163) provide the definitive account of this morphological change:

**Step 1: PWGmc.** Class I weak verbs with heavy root syllables had their present-stem suffix
remodeled to \*-i- ~ \*-ija- (alternating forms in different paradigm cells). R/T illustrate
with \*hauzijan 'to hear': 1sg \*hauziju, 2sg \*hauzisi, 3pl \*hauzijap, etc.

**Step 2: Northern WGmc (pre-OE/pre-OFris).** This alternation pattern was extended to
Class II weak verbs: "in those forms that had \*-ija- in class I the class II suffix was extended
to \*-ōja-" (Cowgill 1959: 8–9, cited by R/T). R/T give the full paradigm table (p.161):

    PWGmc *ardōn "to dwell":
    infinitive: *ardōn  → *ardōjan  → OE eardian
    indic. 3pl: *ardōnþ → *ardōjaþ  → OE eardiaþ
    iptv. 2sg:  *ardō   → *ardō     → OE earda  (UNCHANGED — no *j)
    
**Step 3: Extension to Class III.** R/T p.162: "The extension of this change to the majority
paradigm of weak class III, so that the uniform stem vowel \*-ē- was replaced by \*-ē- ~
\*-ēja-, can also have been a general northern innovation; but it can be demonstrated only
for OE, since in the other northern WGmc languages the relevant verbs appear in weak
class II."

**Key evidence: relic Class III forms in Anglian OE.** R/T list relics of the \*-ēja- intermediate
stage that survive in non-WS dialects, alongside the WS Class II innovations:

| Verb | PGmc | Relic form (Anglian) | WS Class II form |
|------|------|---------------------|------------------|
| 'be awake' | \*wakē- | N.Merc. weccan, North. wecca | WS wacian |
| 'spare' | \*sparē- | North. speeria, iptv. sper | WS sparian |
| 'endure' | \*þolē- | North. dælge, iptv.pl. dæligas | WS þolian |
| 'dwell' | \*wunē- | N.Merc. wynigaþ | WS wunian |
| 'worry' | \*sorgē- | E.Merc. soer[g]lendi | WS sorgian |
| 'lean' | \*hlinē- | E.Merc. onhlingu | WS hlinian |
| 'live' | \*libē- | **see detailed analysis below** | WS libban / lifian |

*Note on 'live': The Anglian forms lifgende, lifgu are NOT relics of the original Class III
paradigm — R/T §7.1.5 (pp.364–365) explicitly call them INNOVATIONS reflecting a secondary
\*-ē- ~ \*-ēja- remodeling. The archaic form is North. 3sg pres. lifed. See "📋 TSV Row 2107".*

### Did \*-ōjăną exist in Proto-Germanic?

**No.** The evidence from R/T is clear that:

1. The \*-ē- → \*-ēja- remodeling was a **northern WGmc** innovation, not PGmc. OHG
   preserves the unremodeled \*-ēn forms: fastēn, folgēn, lebēn, sorgēn, etc.
2. The intermediate form was \*-ēja- (not \*-ōja-). This \*-ēja- then merged with the
   productive Class II \*-ōja- pattern in OE.
3. The 4 "Class III" verbs in OE (habban, secgan, libban, hycgan) are NOT from \*-ēn- at
   all — they are from \*-jan- with j-gemination. (R/T pp.365–366, Cowgill 1959.)
4. There are **no attested OE forms** that show the regular phonological outcome of PGmc
   \*-ēną (which would be \*-on). Every OE reflex has either the Class II -ian ending or a
   relic Class III \*-ēja- form.

### Why the pipeline gives -on from \*-ēną

The pipeline correctly applies the regular phonological rules to \*-ēną:

1. NWGmcLongENasalRounding: \*ē → \*ō / \_ nasal (the \*n in \*-ēną triggers this)
2. Result: \*-ōną → after further changes → -on

This -on outcome is the **phonologically regular** development of \*-ēną. It is simply not
attested in OE because the morphological Class III→II shift was (near-)universal.

### Handling options for the project

*[Original options A–D superseded by the detailed paradigm-cell analysis below; see "📋 TSV Row 2107: Paradigm-Cell Analysis" for current treatment.]*

### The individual verbs

**wacan (ID 2268)**: **RESOLVED.** This was a **strong verb** (Class VI), not weak Class III.
The TSV proto \*wakēną was wrong — corrected to \*wakaną. Now matches. (See mismatch trajectory.)

**fastian (ID 2004)**: Denominal from \*fastu- 'firm'. Kroonen \*fastēn- → OE fastian.

*Research findings (2026-03-09):*
- R/T §3.3.2 say OE **fǣstan** 'to fast' is "an originally Class I weak verb (cf. ON festa, OS 
  festia, OHG festen, all 'make firm') that has acquired the stative meaning by lexical confusion"
- This suggests the actual OE verb 'to fast' is **fǣstan** < **\*fastjăną** (Class I), not fastian
- Pipeline test: \*fastjăną → festan (close to fǣstan), \*fastēną → faston (not attested)
- Pipeline test: \*fastēþi → fæsteþ (3sg present) — but no evidence this is an archaic relic
- **Issue:** TSV target "fastian" may be incorrect; standard OE is "fǣstan" from Class I \*fastjăną
- **Options:** (a) Change to \*fastjăną → fǣstan, (b) Use 3sg \*fastēþi → fæsteþ if archaic, 
  (c) Document as mismatch

**folgian (ID 2027)**: Kroonen \*fulgēn-, with a note that OE/ON also show a Class I formation
\*fulgjan- (→ OE fylgan with i-umlaut \*u → \*y). The Class II folgian (with \*u → \*o by
u-lowering, no i-umlaut) can only come from a form where \*j was separated from the root
by a syllable.

*Research findings (2026-03-09):*
- R/T: PNWGmc \*fulgija- ~ \*fulgai- → OE fylgan ~ folgian
- Kroonen: \*fulgjan- → OE fylgan (Class I with i-umlaut), \*fulgēn- → OE folgian (Class II)
- Pipeline test: \*fulgēną → folgon (mismatch), \*fulgjăną → felġan (not fylgan — i-umlaut bug?)
- Pipeline test: \*fulgēþi → folġeþ (3sg present) — but no evidence this is an archaic relic
- **Issue:** i-umlaut of \*u giving e instead of y (see \*fulljăną → fellan, should be fyllan)
- **Options:** (a) Fix i-umlaut bug, then use \*fulgjăną → fylgan, (b) Use 3sg \*fulgēþi → folġeþ,
  (c) Document as mismatch

**lifian (ID 2107)**: **RESOLVED.** See detailed analysis below ("📋 TSV Row 2107: Paradigm-Cell
Analysis"). Implemented as \*libēþi → lifeþ (archaic North. 3sg present).

### Methodological significance

This is the same type of problem encountered with the stefn/stemn case: the pipeline
forces us to distinguish between (a) what PGmc reconstruction scholarship gives us and
(b) what form must be assumed locally to produce the correct OE output. The Class III→II
weak verb shift is a morphological analogy, not a regular sound change, and therefore
falls outside the scope of a Neogrammarian phonological transducer.

The universality of this shift in OE (every PGmc \*-ēn- verb appears as Class II -ian in WS)
makes it a systematic, predictable gap in the pipeline's coverage. A future morphological
component could model this shift explicitly. For now, the project must choose between
transponent forms and documented mismatches.

### References

- Cowgill, W. 1959. 'The inflection of the Germanic ō-presents.' *Language* 35: 1–15.
- Kroonen, G. 2013. *Etymological Dictionary of Proto-Germanic.* Leiden: Brill.
- Ringe, D. and A. Taylor. 2014. *The Development of Old English* (A Linguistic History of
  English, vol. 2). Oxford: OUP. §3.3.2 pp.161–163; §7.1.5 pp.362–366.

## ⚙️ J-Gemination/BAllophony Chronology Fix (2026-03-09)

### The bug

The pipeline was producing `lifan` from `*libjăną` instead of expected `libban`. Investigation
revealed a **chronology error**: PGmcBAllophony (`*b` → `*β` post-vocalically) was firing
BEFORE PWGmcJGemination, so by the time j-gemination ran, there was no `*b` to geminate.

**Trace before fix:**
```
*libjăną → [BAllophony] → *liβjăną → [JGemination] → *liβjăną (no change) → ... → lifan
```

### R/T evidence for correct chronology

R/T vol.2 pp.50–51 explicitly cite j-gemination operating on underlying /b/:

> "PGmc \*habjana 'to lift' (ON hefja; Goth. hafjan has levelled the voiceless Verner's
> Law alternant into the present from the past indic. sg.) > PWGmc \*[habˈbʲan] (= \*/habjan/)
> > OE hebban, OS hebbian"

This shows that at the PWGmc j-gemination stage, the underlying stop /b/ (not allophone [β])
undergoes gemination. The spirantization to [β] is a **late allophonic rule**, not an early
phonemicization.

### The fix (implemented)

1. **Removed** PGmcBAllophony from PGmcConsonantRules (which fires early in the pipeline)
2. **Added** PGmcBAllophony after PWGmcJGemination in EnglishProtoToOE
3. **Added** geminate-restore clause to handle R/T vol.1 §3.2.4 — geminates are always stops:
   ```
   {*β} -> {*b} || _ {*b}
   ```
4. **Removed** `{*b} {*j} -> {*v}` from OEJClusterCoalescence (was interfering with geminated
   `*b*b*j` sequences; non-geminated `*bj` is handled by BAllophony + JLossAfterHeavy)

### Verification

After fix, pipeline correctly produces:
```
libjăną → libban ✓
habjăną → hebban ✓
```

The BAllophony rule now fires after gemination has already created `*bb`, and the geminate-restore
clause ensures the first consonant of a geminate is a stop, not a fricative.

---

## 📋 TSV Row 2107 (lifian/libban): Paradigm-Cell Analysis

### Background

Row 2107 currently reads:
- ID: 2107
- TOKENS: `l i f i a n`
- PROTOFORM: `*libēną` (Class III weak infinitive)
- COUNTERPART: `lifian`
- PROTO (cognate set): `*libēną`

The question: **Is the infinitive the right paradigm cell to match?** When the infinitive has been
remodeled (as lifian clearly has), we should consider whether a more conservative finite form
might offer a cleaner lautgesetzlich pathway.

### Three-way distinction required

We need to distinguish:

1. **Cognate-set headword / etymological proto** — the form used in comparative reconstruction
   (e.g., Kroonen's \*libēn-, the Class III stative)
2. **FST input form** — the specific pre-OE or PGmc form that yields the target by regular
   sound change (may be a different paradigm cell or morphological formation)
3. **OE target form** — an actually attested OE form, not necessarily the lemma/infinitive

### The Class III paradigm: stem alternation

R/T vol.2 pp.93–94 give the crucial data for 'have', 'say', 'live':

| Cell | OS | OE | Proto stem |
|------|----|----|------------|
| pres. inf. | hebbian, seggian, **libbian** | habban, secgan, **libban** | \*-ja- |
| pres. 3sg. | habed, sagid, [**lebot**] | hæfeþ, segeþ, **lifed** (Anglian) | \*-ai- (> \*-ē-) |
| pres. 3pl. | hebbiad, seggiad, libbiat | habbaþ, secgaþ, libbaþ | \*-ja- |
| past 3sg. | habda, sagde, libdun (3pl) | hæfde, segde, lifde | (no linking vowel) |
| past ptc. | behabd, gisagda, gilibd | hæfd, segd, lifd | (no linking vowel) |

**Key observation:** The Class III paradigm had TWO alternating stems:
- **\*-ja-** stem in infinitive, 1sg, 3pl indicative, subjunctive, participles → gemination
- **\*-ai- / \*-ē-** stem in 2sg, 3sg indicative, imperative sg → NO gemination

R/T vol.2 p.388 explicitly reconstruct:
> "PGmc \*libai- ~ \*libja- 'to live' (Goth. liban, ON lifa, OHG lebén) → northern WGmc
> \*lib'b/an but **pres. indic. 3sg. \*liboþ** (OS libbian, libod) → early WS OE libban,
> liofaþ ~ leofaþ, North. lifiga (remodelled), liofaþ, Merc. lifgan (remodelled), liofaþ ~ leofaþ"

### The attested OE paradigm cells (Campbell §762)

Campbell gives the following actual OE forms:

**West Saxon:**
| Cell | Form | Notes |
|------|------|-------|
| pres. indic. 1sg | libbe | \*-ja- stem, geminated |
| pres. indic. 2sg | **leofast** | \*-ai- stem, Class II intrusion |
| pres. indic. 3sg | **leofaþ** | \*-ai- stem, Class II intrusion |
| pres. indic. pl | libbaþ | \*-ja- stem, geminated |
| pres. subj. | libbe | \*-ja- stem |
| imper. sg. | **leofa** | \*-ai- stem, Class II intrusion |
| past indic. | lifde | no linking vowel |
| past ptc. | lifd | no linking vowel |
| infinitive | libban | \*-ja- stem, geminated |

**Anglian (Vespasian Psalter, Campbell §762):**
| Cell | Form | Notes |
|------|------|-------|
| pres. indic. 1sg | **lifgu** | \*-ē- + -ja- remodeling |
| pres. indic. 3sg | **leofaþ** | \*-ai- stem, Class II |
| pres. indic. pl | **lifgaþ** | \*-ē- + -ja- remodeling |
| pres. subj. | **lifge** | \*-ē- + -ja- remodeling |
| pres. ptc. | **lifgende** | \*-ē- + -ja- remodeling |
| past | lifde | |
| past ptc. | lifd | |

**Late Northumbrian (Lindisfarne, Campbell §762):**
| Cell | Form | Notes |
|------|------|-------|
| pres. indic. 1sg | hofo | (sic, h- for l-?) |
| pres. indic. 3sg | **liofaþ** ~ **lifed** | lifed is archaic Class III |

### Critical finding: North. lifed as archaism

R/T vol.2 §7.1.5 (p.364) note:
> "Except for late North. pres. indic. 3sg. **lifed**, which must be an **archaism** because the
> verb has largely been remodelled as a class II weak verb in that dialect, we find only class II
> pres. indic. 2, 3sg. and iptv. sg. forms"

**This is crucial:** The 3sg present **lifed** (late Northumbrian) preserves the archaic \*-ai- / \*-ē-
stem without Class II contamination. This form descends directly from PGmc **\*libaiþi** or
pre-OE **\*libēþ**.

### What the sources reconstruct

**Kroonen \*libēn- (p.336):**
> "\*libēn- w.v. 'to be left; to live' — Go. liban ww. 'to live', ON lifa w.v. 'to live; to be left',
> Far. liva w.v. 'to live', Elfd. liva w.v. 'id.', **OE libban wv. 'id.'**, E to live, OFri. libba w.v.
> 'id.', OS libbian w.v. 'id.', Du. leven wv. 'id.', OHG lebén wv. 'id.', G leben wv. 'id.'"

Note: Kroonen cites **OE libban** (infinitive with j-gemination), NOT lifian.

**R/T vol.1 p.35:**
> "PGmc \*libja- ~ \*libai- 'live' (Goth. liban, ON lifa) > OE libban, OF libba, OS libbian, OHG lebén"

Note the dual reconstruction: **\*libja-** (j-present) AND **\*libai-** (stative). These are the
two stems of the Class III alternation.

### Are Anglian lifgu, lifgaþ, lifgende archaic?

**No.** R/T vol.2 §7.1.5 (pp.364–365) explicitly argue these are **innovations**:

> "Because these forms are distinctive, they have often been taken to be archaisms. **But it needs
> to be emphasized that no other Germanic language presents us with any similar phenomenon.** As
> noted above, the corresponding OS forms agree with WS; so does OF libb-; even the southern OHG
> relics pres. indic. libis, libit, past libita presuppose a paradigm in which some forms were
> identical with class I weak forms—i.e. exhibited a palatalized geminate. **The Anglian forms
> are innovations**, and we must find a way to account for them..."

> "The only plausible source of /j/ in these verb forms is the source of /j/ in weak class II...
> just as class II \*-ō- was remodelled as \*-ō- ~ \*-ōja- on the model of the class I stem vowel
> complex \*-i- ~ \*-ija- (Cowgill 1959: 8), so also class III \*-ē- must have been remodelled as
> \*-ē- ~ \*-ēja- in at least part of the northern WGmc dialect continuum."

So the Anglian forms like **lifgu**, **lifgaþ**, **lifgende** are from a remodeled \*-ē- ~ \*-ēja-
paradigm — a **northern WGmc innovation**, not an archaism.

### Paradigm-cell assessment

| Paradigm cell | Proto input | Expected OE | Actually attested | Match path |
|---------------|-------------|-------------|-------------------|------------|
| infinitive | \*libjăną | libban | libban (WS) | ✅ j-gemination |
| infinitive | \*libēną | \*libōn? leofon? | lifian (late WS/Anglian) | ❌ morphological shift |
| 3sg pres. | \*libaiþi / \*libēþ | lifed? leofeþ? | lifed (North.), leofaþ (WS) | ⚠️ needs testing |
| 2sg pres. | \*libaisi / \*libēs | \*lifes? | leofast (WS) | ⚠️ needs testing |
| imper. sg. | \*libai / \*libē | \*life? | leofa (WS) | ⚠️ needs testing |
| pres. ptc. | \*libjandī? | \*libbende | libbende (WS) | ⚠️ j-gemination |
| past 3sg | \*libdē | lifde | lifde | ✅ trivial |

### The cleanest lautgesetzlich pathways

**Path 1: Infinitive via j-present**
- Proto: \*libjăną (Class III j-stem infinitive)
- Sound changes: j-gemination → BAllophony (geminate exception) → ...
- Output: libban ✅
- Target: libban (WS, conservative)
- Status: **WORKING** after j-gemination fix

**Path 2: 3sg present via \*-ai- stem**
- Proto: \*libaiþi or \*libēþi (3sg present with \*-ai- / \*-ē- stem)
- Expected changes: \*ai > \*ē (already in Class III); then \*ē remains or undergoes
  breaking/umlaut depending on environment
- Expected output: something like \*lifeþ > lifed (with syncope)?
- Target: lifed (late North., archaism per R/T)
- Status: **NOT TESTED** — input grammar doesn't accept finite verb forms

**Path 3: Past tense (trivial)**
- Proto: \*libdē (past 3sg, no linking vowel)
- Output: lifde
- Target: lifde (all dialects)
- Status: **TRIVIALLY CORRECT** — but past tense doesn't help disambiguate lemma

### Conclusion on paradigm-cell approach

The key question is: **Is there a finite paradigm cell that preserves archaic morphology and
yields an attested OE form by regular sound change?**

**Candidates:**
1. **Infinitive libban** < \*libjăną — WORKS (j-gemination fix), conservative WS form
2. **3sg lifed** < \*libēþ(i)? — potentially archaic (R/T call it so), but:
   - Input grammar doesn't accept finite forms
   - Would need to test whether \*libēþ → lifed by regular change
   - Only attested in late Northumbrian (sparse)
3. **Past lifde** < \*libdē — trivial, but doesn't help with infinitive-lemma question

### Options (revised)

**Option 1: Use infinitive \*libjăną → libban (j-present path)**

- PROTOFORM: \*libjăną
- COUNTERPART: libban
- PROTO (cognate set): \*libēną (unchanged)
- NOTE: documents that libban continues the j-present stem \*libja-, not the \*-ē- stem

*Advantages:*
- Pipeline match ✓
- libban is Kroonen's cited OE reflex under \*libēn-
- Parallel to habban < \*habjăną, hebban < \*hafjăną
- WS libban is morphologically conservative (R/T §7.1.5)

*Disadvantages:*
- Changes OE target from TSV's lifian to libban
- PROTOFORM is a different morphological formation than cognate-set headword

**Option 2: Use 3sg present \*libēþ → lifed (finite cell path)**

- PROTOFORM: \*libēþi (or similar 3sg form)
- COUNTERPART: lifed
- PROTO (cognate set): \*libēną
- Requires: extending pgrmWeakTailVowel to accept \*-ēþi (3sg present ending)

*Advantages:*
- Preserves the \*-ē- stem of the cognate-set headword
- Targets an archaic finite form (R/T: "lifed... must be an archaism")
- Tests the \*-ai- / \*-ē- stem pathway

*Disadvantages:*
- Requires input grammar extension
- lifed is sparsely attested (late Northumbrian only)
- Need to verify \*libēþ → lifed is actually regular (syncope timing, vowel outcomes)
- Shifts target from infinitive/lemma to a finite form

**Option 3: Split representation (two rows)**

- Row A: \*libjăną → libban (infinitive, j-present path)
- Row B: \*libēþi → lifed (3sg present, \*-ē- stem path)

*Advantages:*
- Explicitly represents the two stems of the Class III paradigm
- Both forms are actually attested OE
- Provides maximal coverage of the inherited morphology

*Disadvantages:*
- Doubles the row count for this lexeme
- May overcomplicate TSV structure
- Row B requires input grammar extension

**Option 4: Accept documented mismatch**

- Keep PROTOFORM \*libēną, COUNTERPART lifian
- Document that pipeline produces \*leofon (regular) but OE has lifian (morphological shift)

*Advantages:*
- Preserves original TSV data
- Intellectually honest about pipeline limitations
- Documents Class III→II shift as systematic gap

*Disadvantages:*
- +1 mismatch
- lifian is the innovative form, not the conservative one

### Recommendation

**Option 1 remains the strongest single-row solution:**
- libban is what Kroonen cites under \*libēn-
- libban < \*libjăną is a working pipeline path
- The j-present formation (\*libja-) was part of the Class III paradigm alongside \*libai-

**Option 2 is worth investigating** if we want to preserve the \*-ē- stem connection, but it
requires: (a) extending the input grammar, (b) verifying \*libēþ → lifed is regular, and
(c) accepting a sparse target (late North. only).

**Option 3 (split) would be methodologically ideal** but may be overkill for TSV structure.

---

### Research on Option 2: 3sg present pathway (2026-03-09 continued)

**Question:** Is \*libēþi → lifed lautgesetzlich (by regular sound change)?

**Research findings:**

R/T vol.2 p.25 explicitly give the parallel derivation for *habban*:

> "PGmc pres. \*habaisi 'you have', \*habaiþi '(s)he has' (Goth. habais, habaiþ) →
> \*habēs, \*habēþ → OE (North.) hæfes, **hefed**"

The sound changes are:
1. **\*-aiþi → \*-ēþi** — NWGmc monophthongization of unstressed \*ai → \*ē
2. **\*-ēþi → \*-ēþ** — Loss of final short \*-i (PWGmc)
3. **\*-ēþ → -eþ** — Shortening of unstressed long \*ē → e
4. **-eþ → -ed** — Orthographic variant (late North. <d> for /ð/)

**Pipeline test:**

Extended `pgrmWeakTailVowel` with `ē:{*ē} þ:{*þ} i:{*i}` (3sg present ending).

Results:
- **libēþi → lifeþ** ✓
- **hafēþi → hæfeþ** ✓
- **habēþi → hæfeþ** ✓

**Assessment:** The pipeline produces **lifeþ**, which is the phonologically expected output.
The attested Northumbrian form **lifed** is an orthographic variant — late Northumbrian texts
regularly use <d> for /ð/ in unstressed syllables (Campbell §450 note).

**Conclusion:** **The 3sg present pathway is lautgesetzlich.** \*libēþi → lifeþ is a regular
development, and lifed is just an orthographic variant of lifeþ.

**Recommendation for row 2107:**

| Option | PROTOFORM | COUNTERPART | Pros | Cons |
|--------|-----------|-------------|------|------|
| **1** | \*libjăną | libban | Working path, Kroonen's cited form | Different morphology from cognate headword |
| **2** | \*libēþi | lifeþ (= lifed) | Preserves \*-ē- stem, archaic finite form | Sparse target (late North. only), needs grammar extension |

**My recommendation: Option 1 (infinitive \*libjăną → libban)** remains the stronger choice
for the TSV because:
- libban is what Kroonen cites as the OE reflex of \*libēn-
- libban is the morphologically conservative infinitive in WS/literary OE
- The j-present stem \*libja- was part of the inherited Class III paradigm
- lifed, while archaic, is sparsely attested and dialectally marked

However, if the user prefers to **preserve the \*-ē- stem connection**, Option 2 is now
confirmed to be lautgesetzlich and could be implemented by keeping the grammar extension.

**Decision (2026-03-09):** User chose **Option 2**. Implemented as:
- PROTOFORM: \*libēþi (3sg present indicative)
- COUNTERPART: lifeþ (= North. lifed)
- Grammar extension `ē:{*ē} þ:{*þ} i:{*i}` retained in `pgrmWeakTailVowel`
- Note: "3sg pres. indic. (archaic North. lifed); infinitive libban shows j-gemination from \*libjăną stem, not \*-ē- stem"

## Mismatch trajectory — full history

| Date | Mismatches | Matches | Total rows | Match rate |
|------|-----------|---------|------------|------------|
| Oct 2025 | ~300 | ~70 | 370 | ~19% |
| 2026-01-22 | 291 | 79 | 370 | 21.4% |
| 2026-02-06 | 280 | 90 | 370 | 24.3% |
| 2026-02-06b | 262 | 108 | 370 | 29.2% |
| 2026-02-07 | 256 | 120 | 376 | 31.9% |
| 2026-03-08 | 103 | 277 | 380 | 72.9% |
| 2026-03-09 | 100 | 280 | 380 | 73.7% |
| 2026-03-09b | 95 | 285 | 380 | 75.0% |
| 2026-03-09c | 93 | 287 | 380 | 75.5% |
| 2026-03-09d | 92 | 288 | 380 | 75.8% |
| 2026-03-09e | 90 | 289 | 386 | 74.9% |

---

## Systematic Paradigm-Cell Analysis: folgian and fastian (2026-03-09f)

Following the user's methodological request:
1. Start with the infinitive
2. Test if PGmc infinitive → OE infinitive by regular sound change
3. If not, test other paradigm cells
4. Expand/refine sound-change model if needed before concluding "analogy"

### Part 1: folgian (Row 2027)

#### Step 1: Proto-Germanic infinitive in the literature

**Kroonen (EDPG s.v. \*fulgan-):**
- Class III weak \*fulgēn- 'to follow'
- OE folgian / fulgian
- Du volgen, G folgen

**R/T vol.2 §7.1.5 (p.293-294):**
- Dual formation: PNWGmc \*fulgija- ~ \*fulgai-
- OE fylgan (Class I, from \*fulgija-) ~ folgian (Class II, from \*fulgai-)
- "The dual formation ... probably reflects an original alternation between j-present and ē-stative."

#### Step 2: Can PGmc infinitive regularly yield OE infinitive?

**Test: \*fulgēną → ?**

Pipeline result: `fulgēną → folgon`

The expected OE infinitive is **folgian** (Class II -ian), but the pipeline produces **folgon** (Class II -on).

**Analysis:** This is the systematic Class III → Class II problem. PGmc Class III infinitives \*-ēną develop to OE -on (via \*ē → \*ō rounding before nasals), but actual OE Class II verbs have -ian. The -ian ending arose from morphological reanalysis, not phonological development.

**Result:** \*fulgēną → folgian is **NOT regular**. The infinitive is analogically remodeled.

#### Step 3: Other paradigm cells

**Test: \*fulgjăną (Class I infinitive) → ?**

Before the u-lowering fix, this gave \*felġan (incorrect: e instead of y).

After fixing NWGmcULowering to block u-lowering when \*j appears anywhere in the intervening consonants:

Pipeline result: `fulgjăną → fylġan`

This **matches** the attested OE **fylgan** (Mercian/Northumbrian form).

**Test: Class III finite cells**

| Cell | Proto input | Pipeline output | Attested? |
|------|-------------|-----------------|-----------|
| 3sg pres | \*fulgēþi | folġeþ | (not directly attested as archaic relic) |
| 2sg pres | \*fulgēsi | folġes | (not directly attested as archaic relic) |
| imper. sg | \*fulgē | folġe | (not directly attested as archaic relic) |

Unlike lifed, there's no evidence that forms like folġeþ survive as archaic relics in OE texts.

#### Step 4: Solution

The Class I infinitive \*fulgjăną regularly yields OE **fylġan** by sound change:
- \*u blocks lowering to \*o because \*j intervenes (R/T §2.1.1: "nor \*j intervened")
- \*u → y by i-umlaut (triggered by \*j)
- \*j triggers gemination but absorbed before single consonant (l)
- Result: fylgan (= fylġan with palatal <ġ> before front vowel)

The Class II form **folgian** represents the analogically remodeled \*-ē- stem paradigm, where:
- \*u → o by NWGmc u-lowering (no blocking \*j in the \*-ē- stem)
- The infinitive was reanalyzed to -ian (Class II productive pattern)

**Recommendation for row 2027:**

| Option | PROTOFORM | COUNTERPART | Assessment |
|--------|-----------|-------------|------------|
| A | \*fulgēną | folgian | MISMATCH: produces folgon, not folgian |
| **B** | \*fulgjăną | fylġan | ✅ MATCH: regular development, attested Mercian/Northumbrian |
| C | \*fulgēþi | folġeþ | No evidence this form survives as archaic |

**Best solution: Option B** — Change to \*fulgjăną → fylġan. The Class I derivation is regular, fylġan is well-attested in Mercian and Northumbrian, and the WS/literary folgian represents morphological remodeling of the \*-ē- stem.

---

### Part 2: fastian (Row 2004)

#### Step 1: Proto-Germanic infinitive in the literature

**Kroonen (EDPG s.v. \*fastēn-):**
- Class III weak \*fastēn- 'to fast, abstain from food'
- OE fæstan, fǣstan
- Derived from adj. \*fastu- 'firm, fast'

**R/T vol.2 §3.3.2 (p.101, lines ~5915-5920):**
- "OE fǣstan, OHG fastēn 'to fast' (from adj. \*fastu-)"
- R/T note that fǣstan appears to be "originally Class I weak" from \*fastjăną
- The \*-ēn- stative "acquired stative meaning by lexical confusion"

**Note:** There are potentially **two** PGmc verbs here:
- \*fastēną (Class III stative) 'to fast, abstain'
- \*fastjăną (Class I causative) 'to make fast, fasten'

These may have merged in WGmc/OE.

#### Step 2: Can PGmc infinitive regularly yield OE infinitive?

**Test: \*fastēną → ?**

Pipeline result: `fastēną → faston`

The TSV lists **fastian** as the OE counterpart. But note:
- The TSV entry says "TSV fix: was fæst (adj \*fastu-); changed to fastian (verb 'to fast' < \*fastēn-, Kroonen p.131)"
- The actual attested OE verb is **fæstan / fǣstan** (not \*fastian)

**Problem:** The TSV counterpart "fastian" may itself be incorrect. OE has:
- **fǣstan** (strong vowel) 'to fast, abstain; to entrust, commend' — Class I weak
- **fæstan** (short vowel) 'to fasten, make fast' — Class I weak

There is no \*fastian (Class II -ian form) attested in standard OE lexicons.

**Result:** \*fastēną → fastian is a double mismatch:
1. Pipeline produces faston (Class II -on), not fastian
2. The target "fastian" may not actually exist in OE

#### Step 3: Reassessing the OE attestations

Checking standard lexicons:
- **BT (Bosworth-Toller):** fæstan (I. to fast, II. to commit), fǣstan (to entrust)
- **DOE (Dictionary of Old English):** fǣstan (commit, entrust, make firm)
- **Campbell, OEG §753:** Class I weak verbs from adj/noun + -jan

The verb is consistently **fǣstan** or **fæstan**, a Class I weak verb from \*fastjăną or \*fastijăną.

**Test: \*fastjăną → ?**

Pipeline result: `fastjăną → festan`

Expected: **fæstan** or **fǣstan**

**Analysis:** The pipeline produces festan (with <e>), not fæstan (with <æ>). This is wrong.

Wait — \*a before \*j should become æ through i-umlaut? Let me trace:
- \*fastjăną
- \*a + j → æ (i-umlaut: \*a → æ before \*j)
- Result should be fæstan

But pipeline gives festan. This suggests the i-umlaut of \*a → æ is not being applied, or is being overwritten.

**Further testing needed:** Check whether \*a → æ i-umlaut is working correctly.

**Test: \*satjăną → ?** (known: \*satjăną → settan)

Pipeline result: `satjăną → settan` ✓

This is correct! \*a → e before \*j (gemination context). So why is \*fastjăną → festan wrong?

**Reanalysis:** The issue is that \*satjăną has \*a → e because of the following geminate. In \*fastjăną, the cluster \*stj may behave differently. Let me check:

The \*j does not produce gemination after \*st cluster (consonant cluster blocks gemination). So:
- \*fastjăną → \*fæstjăną (i-umlaut: \*a → æ)
- \*fæstjăną → \*fæstăną (j-loss after heavy syllable)
- \*fæstăną → fæstan (apocope)

Expected: **fæstan**. Pipeline gives: **festan**.

**Bug identified:** I-umlaut of \*a → æ is not applying in \*fastjăną.

#### Step 4: Testing other paradigm cells

| Cell | Proto input | Pipeline output | Notes |
|------|-------------|-----------------|-------|
| 3sg pres | \*fastēþi | fæsteþ | Correct: \*ē → e, \*a unaffected (no umlaut trigger) |
| 2sg pres | \*fastēsi | fæstes | Correct |
| imper. sg | \*fastē | fæste | Correct |

The Class III finite cells produce expected outputs, but there's no evidence these survive as archaic relics (unlike lifed).

#### Step 5: Summary and recommendations

**Current status:**

| PROTOFORM | Pipeline output | Expected OE | Match? |
|-----------|-----------------|-------------|--------|
| \*fastēną | faston | fæstan / fastian | ❌ |
| \*fastjăną | festan | fæstan | ❌ (vowel wrong) |
| \*fastēþi | fæsteþ | fæsteþ | ✅ (but not archaic relic) |

**Issues to resolve:**
1. **TSV counterpart:** Is the target "fastian" or "fæstan"? Standard lexicons only have fæstan/fǣstan.
2. **I-umlaut bug:** \*fastjăną → festan shows \*a → e instead of \*a → æ. Need to investigate.

**Recommended actions:**
1. Verify the correct OE form (fæstan, not fastian) in standard lexicons
2. Fix the i-umlaut rule for \*a → æ (currently producing e instead)
3. Once fixed, test \*fastjăną → fæstan
4. Update TSV with corrected PROTOFORM and COUNTERPART

**For now, leaving row 2004 as a documented mismatch** pending:
- Confirmation of correct OE counterpart
- Fix for i-umlaut \*a → æ bug


---

### Implementation (2026-03-09f continued)

**Row 2027 (folgian → fylġan):**
- Changed PROTOFORM: `*fulgēną` → `*fulgjăną`
- Changed COUNTERPART: `folgian` → `fylġan`
- Changed PROTO: `*fulgēną` → `*fulgjăną`
- Added NOTE with Kroonen and R/T citations
- Pipeline: `fulgjăną → fylġan` ✅

**Row 2107 (lifeþ):**
- Changed PROTO: `*libēną` → `*libēþi` (to match PROTOFORM)
- Ensures evaluation uses the specific paradigm cell form

**Evaluation update:**
- Previous: 289 matches / 90 mismatches
- Current: 291 matches / 88 mismatches (75.4% match rate)

**Remaining: fastian (row 2004)**

Need to investigate the i-umlaut issue with `*fastjăną → festan` (should be fæstan).

---

### fastian resolution (2026-03-09f continued)

**Key findings:**
1. TSV counterpart "fastian" was **wrong** — OE has **fǣstan/festan** (Class I weak), not *fastian
2. R/T: "festan 'to fix, to fasten' < \*fæstjan" is "an originally class I weak verb" that "acquired the stative meaning ['to fast'] by lexical confusion"
3. Pipeline: `*fastjăną → festan` ✅
4. OE fæstan has æ from **analogy** with adj. fæst, not from sound change

**Row 2004 update:**
- Changed PROTOFORM: `*fastēną` → `*fastjăną`
- Changed COUNTERPART: `fastian` → `festan`
- Changed PROTO: `*fastēną` → `*fastjăną`
- Changed TOKENS: `f a s t i a n` → `f e s t a n`
- Added detailed NOTE with R/T citations

**Evaluation update:**
- Previous: 291 matches / 88 mismatches
- Current: 292 matches / 87 mismatches (75.6% match rate)

**Summary of u-lowering fix:**

Fixed NWGmcULowering rule to properly block u-lowering when *j appears anywhere in the intervening consonant cluster (not just immediately after *u):

```foma
# Old rule (broken): blocked only if *j immediately after *u
{*u} -> {*o} || _ [EnglishStarConsonant - EnglishStarNasal - {*j}] ...

# New rule (fixed): blocked if *j anywhere before non-high vowel
{*u} -> {*o} || _ [EnglishStarConsonantNoJ - EnglishStarNasal] EnglishStarConsonantNoJ* EnglishStarNonHighVowel
```

This allows *fulgjăną → fylġan (with *u → y by i-umlaut, not lowered to *o).

## Mismatch trajectory — full history (updated)

| Date | Mismatches | Matches | Total rows | Match rate |
|------|-----------|---------|------------|------------|
| Oct 2025 | ~300 | ~70 | 370 | ~19% |
| 2026-01-22 | 291 | 79 | 370 | 21.4% |
| 2026-02-06 | 280 | 90 | 370 | 24.3% |
| 2026-02-06b | 262 | 108 | 370 | 29.2% |
| 2026-02-07 | 256 | 120 | 376 | 31.9% |
| 2026-03-08 | 103 | 277 | 380 | 72.9% |
| 2026-03-09 | 100 | 280 | 380 | 73.7% |
| 2026-03-09b | 95 | 285 | 380 | 75.0% |
| 2026-03-09c | 93 | 287 | 380 | 75.5% |
| 2026-03-09d | 92 | 288 | 380 | 75.8% |
| 2026-03-09e | 90 | 289 | 386 | 74.9% |
| 2026-03-09f | 87 | 292 | 386 | 75.6% |
| 2026-03-09g | 85 | 294 | 386 | **76.2%** |


---

## PGmc stem-class disagreements: \*kraft- and \*stab- (2026-03-09g)

### Overview

Two TSV rows (`cræft` ID 1981, `stæf` ID 2212) had incorrect proto-forms that caused
mismatches. Investigation revealed that modern etymological dictionaries **disagree on
the PGmc stem class** for both lexemes. This disagreement has direct consequences
for OE phonology: different stem classes predict different OE vowels.

### The problem

| Lexeme | TSV proto (wrong) | Pipeline output | Expected OE |
|--------|-------------------|-----------------|-------------|
| cræft  | \*kraftiz         | creft           | cræft       |
| stæf   | \*stabiz          | stefe           | stæf        |

Both show i-umlaut (æ → e) triggered by the final \*-iz. But the attested OE forms
have **æ** (not e), indicating no i-umlaut occurred. Either the proto-forms are wrong,
or there is a sound change we are missing.

### Survey of the etymological literature

#### \*kraft-

| Source | Reconstruction | OE form cited | Stem class |
|--------|----------------|---------------|------------|
| **Kroonen (2013)** p.307 | \*kraftu- m. | "OE craft" | tu-stem (u-stem) |
| **Orel (2003)** p.220 | \*kraftiz ~ \*kraftuz | "OE cræft" | i-stem or u-stem |
| **Kluge-Seebold (25th ed.)** s.v. Kraft | g. \*krafti- f. | "ae. cræft" | i-stem |

Kluge-Seebold additionally notes: "**Spuren von u-Flexion (anord. krǫptr m.) weisen
wohl auf einen parallelen maskulinen u-Stamm**" ('traces of u-inflection [ON krǫptr]
probably indicate a parallel masculine u-stem'). This acknowledges that BOTH stem
classes are attested in the comparative evidence.

**Fulk (2018)** §4.7 n.12 cites MHG paradigmatic alternation "kraft beside krefte",
showing umlaut variation within the paradigm — evidence that the stem class was
unstable or variable.

#### \*stab-

| Source | Reconstruction | OE form cited | Stem class |
|--------|----------------|---------------|------------|
| **Kroonen (2013)** p.469 | \*staba- m. | "OE stæf" | a-stem |
| **Orel (2003)** p.378 | \*stabiz ~ \*stabaz | "OE stæf" | i-stem or a-stem |
| **Kluge-Seebold (25th ed.)** s.v. Stab | g. \*stabi-/a- | "ae. stæf" | i-stem or a-stem |

Kluge-Seebold explicitly marks uncertainty with the notation "\*stabi-/a-".

### The phonological argument

The OE reflex disambiguates the stem class:

1. **i-stem \*kraftiz / \*stabiz:**
   - AFB: \*a → \*æ
   - i-umlaut raising: \*æ → \*e (before \*i in following syllable)
   - Prediction: OE **creft**, **stefe** (with e)

2. **u-stem \*kraftuz:**
   - AFB: \*a → \*æ
   - a-restoration: \*æ → \*a (before back vowel \*u)
   - Prediction: OE **craft** (with a)

3. **a-stem \*kraftăz / \*stabăz:**
   - AFB: \*a → \*æ (root), \*ă → \*æ (suffix)
   - No i-umlaut trigger (suffix vowel is front \*æ)
   - No a-restoration trigger (suffix vowel is front after AFB)
   - Final vowel loss
   - Prediction: OE **cræft**, **stæf** (with æ) ✅

The a-stem analysis correctly predicts the attested OE forms. The key insight is
that even after AFB fronts the suffix vowel \*ă → \*æ, this front vowel does not
trigger a-restoration (which requires a **back** vowel) and does not trigger
i-umlaut (which requires **high** \*i or \*j).

### Why the disagreement exists

The comparative evidence is genuinely ambiguous:

- **ON krafptr** (with u-umlaut of a → ǫ) suggests the stem vowel was followed by
  \*u at the time u-umlaut applied → supports u-stem
- **OHG kraft** (fem., no umlaut) is compatible with either a-stem or u-stem
- **Gothic** lacks the word, removing the most conservative witness
- **OE cræft** (with æ, not e) is incompatible with i-stem; compatible with
  a-stem or u-stem (if \*u lost before a-restoration)

The variation between sources reflects genuine uncertainty about PGmc morphology,
not simple error. Different scholars weight the comparative evidence differently.

### Resolution for the FST pipeline

For purposes of modeling the **OE** outcome, we use a-stem forms:
- \*kraftăz → cræft ✅
- \*stabăz → stæf ✅

This produces the correct OE output regardless of whether the PGmc etymon was
"really" an a-stem, i-stem, or u-stem — because what matters phonologically is
that the pre-OE input lacked both a high front trigger (for i-umlaut) and a back
vowel (for a-restoration).

### OE attestation

The OE forms with æ are unambiguous:

- **Campbell** OEG §133: "cræft" as example of OE æ from PGmc \*a
- **Campbell** OEG §160: "cræftas" pl. (æ preserved before geminates and groups)
- **Luick** Hist. Gr. p.176: "stæf 'Stab', cræft 'Kraft'" (æ examples)
- **Bülbring** AE Elementarbuch §179: "craft 'Kraft'" (showing later ME form with a)

The later ME/ModE forms with a (craft, staff) reflect a separate development —
open syllable lengthening and subsequent changes — not the OE stage.

### TSV updates

**Row 195 (ID 1981):**
- PROTOFORM: `*kraftiz` → `*kraftăz`
- PROTO: `*kraftiz` → `*kraftăz`
- NOTE: "Kroonen: \*kraftu- m. (u-stem); Orel: \*kraftiz ~ \*kraftuz; Kluge-Seebold:
  \*krafti- f. with parallel u-stem. OE cræft has æ (not e), ruling out i-stem
  \*-iz which would trigger i-umlaut. Using a-stem \*kraftăz."

**Row 1094 (ID 2212):**
- PROTOFORM: `*stabiz` → `*stabăz`
- PROTO: `*stabiz` → `*stabăz`
- NOTE: "Kroonen: \*staba- m. (a-stem). Orel/Kluge-Seebold: \*stabiz ~ \*stabaz.
  OE stæf has æ (not e), ruling out i-stem. Using a-stem \*stabăz."

### Evaluation update

- Previous: 292 matches / 87 mismatches (75.6%)
- Current: 294 matches / 85 mismatches (**76.2%** match rate)

### Cross-reference

This case is documented in `docs/analysis/notable_findings.md` §6 as an example
of how the FST methodology can disambiguate between competing PGmc reconstructions
by testing their OE phonological predictions.

---

## OE r-Metathesis (Campbell §459, R/T §6.8.2, Luick §136 Anm.1)

### Phonological environment

R-metathesis in OE is the interchange of **r** with a short vowel, moving r from
before the vowel to after it (or rarely, vice versa). This is one of the most
pervasive—and most *variable*—sound changes in OE phonology.

### Primary sources

#### Campbell, *Old English Grammar* §459

Campbell provides the most detailed traditional description (p. 184–185):

> **§459. By full metathesis a consonant moves from immediately before a vowel to
> immediately after it, or the reverse.**
>
> (1) **The most frequent metathesis in OE is that of r from before to behind a
> short vowel followed by s or n.** In §155 and notes, forms are quoted which
> show that this change was sometimes earlier, sometimes later, than breaking;
> see also §193.d with footnotes on *hærn, ærn, werna, ærnan, bernan*. Further
> examples are *berstlian* 'crackle', *burna* 'stream', *cerse* 'cress', *cyrps*
> 'curly', *first* 'period', *dærstan* 'dregs', *forsc* 'frog', *forst* 'frost',
> *hors* 'horse'. Many of these words and of those quoted in §§155, 193 occur
> without metathesis: *brastlian, cresse, crisp, frist-, drestan, frosc, frost,
> græs, hræn* (Ep. 400), *ren-* (Erf. 1137, Beow. 770), *wrenna*. Beside *eornan*
> occurs *rinnan*, and there are scattered forms of *beornan, berstan, perscan*
> without metathesis (§741); beside *burna*, *brunna* occurs in place-names
> (e.g. Denisæsbrunna BH, Namur and Leningrad MSS.).
>
> (2) **Metathesis is much less frequent when d followed the vowel:** North.
> *birdas* 'young birds', *dirda* (beside rare *dridda* Li. only). After a long
> vowel, And. 1313 *gescyrded*, Psalter Gloss 92, 1 (several late manuscripts)
> *gescyrd* for *gescryd(ed)* 'clothed'.
>
> (3) Metathesis by which r is moved from behind to before a vowel is much rarer,
> and is practically limited to before h: North., lW-S *wrohte* 'worked' (beside
> usual *worhte*); North. *breht* 'bright', *froht* 'afraid', *frohtiga* 'fear',
> *fryhto* 'fright', *wrihta* 'maker' (all beside forms without metathesis)…
>
> (4) Low stress promotes metathesis of r, e.g. *eodorcian* 'ruminate' (cf.
> *edroc*), adjs. in *-erne* (see §339), the name-elements W-S, Kt. *-ferþ* for
> Angl. *-friþ*, lW-S *-erd* (e.g. Ælfred, Þeoderd, Ct. of 931…)

A crucial footnote at §459(1):

> **ME *kers* shows OE *cerse* to have had velar c: hence metathesis was later
> than assibilation; the same no doubt applies to *cyrps* (Lat. *crispus*).**

This establishes a chronological terminus: r-metathesis occurred *after*
assibilation of velar c before front vowels (i.e., after the palatalization
that turned *k → tʃ* word-initially).

#### Campbell §155: Breaking and metathesis interaction

Campbell explicitly addresses the dialectal timing (p. 60):

> **§155. Metathesis of r (§459) usually took place too late for secondary
> r-groups to cause breaking, e.g. *gers* 'grass', *berst* 'he burst', *berstan*
> 'burst', *perscan* 'thresh', *fersc* 'fresh'. But in Angl., when the vowel is
> i, metathesis of r is early enough for breaking to occur, e.g. North. *biorna*
> 'burn', *iorna* 'run', VP *beornan, eornan*; but W-S *birnan, irnan* (cf. §459).**

And in footnote 3:

> lW-S past tenses *bearn, earn* are due to late analogy of *wearp*, &c. (based
> on the pl. *burnon, wurdon*); eW-S has *born, orn, barn*, where the vowel-sound
> of *mann*, &c., which may be spelled with a or o, is preserved, although
> divided from the nasal by a metathesized r. VP has *orn, born*, North., Ru.
> *arn, barn* (cf. §130).

#### Ringe & Taylor, *The Linguistic History of English* vol. 2, p.340–341

R/T summarize the dialectal differences more clearly:

> A change which had some impact on the surface contrasts among OE vowels was
> **the common, but variable, metathesis of r with short vowels**. As might be
> expected, **not all instances of metathesis occurred at the same time**. The
> intransitive strong verbs meaning 'burn' and 'run, flow' seem to have
> undergone metathesis **in the Anglian dialects before breaking occurred**
> (Stanley 1952: 104–6 with references):
>
> PGmc \*brinnanan 'to burn (intr.)' (Goth., OS, OHG *brinnan*) > \*birnan >
> Angl. OE \*biornan > Merc. *beornan*;
>
> PGmc \*rinnanan 'to run, to flow' (Goth. *rinnan*, ON *rinna*, OS, OHG
> *rinnan*) > \*irnan > Angl. OE *iornan* (9th-century Martyrology…) > Merc.
> *eornan*, North. *iorna*.
>
> **In WS, however, metathesis in these words did not occur until after
> breaking**, with the result that the same verbs are early WS *birnan ~ biernan
> ~ byrnan, irnan ~ iernan* (Cosijn 1886: 134; Stanley 1952: 104–6). Other
> examples with front vowels in the root also underwent metathesis after
> breaking; typical examples are *berscan* 'to thresh', *berstan* 'to burst',
> *gærs* 'grass', North. *birdas* 'young birds'.

R/T also discuss the causative verbs where metathesis chronology is clearer:

> The WS causatives *bærnan* 'to burn (trans.)' and *ærnan* 'to gallop (a horse)'
> must have undergone metathesis **before** the sequence *ęn* (which arose by
> i-umlaut) became *en*:
>
> PGmc \*brannijanan 'to burn (trans.)' (Goth. *ga-brannjan*, ON *brenna*, OHG
> *brennen*) > \*brannijan > OE \*brænnan > *bærnan*;
>
> PGmc \*rannijanan 'to cause to run' (Goth. *ur-rannjan* 'to cause (the sun) to
> rise', ON *renna*, OHG *zesamine-rennen* 'to melt together, to fuse') >
> \*rannijan > OE \*rænnan > *ærnan* 'to make (a horse) gallop'.

#### Luick, *Historische Grammatik der englischen Sprache* §136 Anm. 1

Luick provides a complementary perspective from German scholarship (p. 199):

> **Wenn die Lautfolge r + Konsonant erst sekundär, durch Metathese, entstanden
> war, unterblieb die Brechung ebenfalls in der Regel, namentlich im
> Westsächsischen.** So ws. *birnan* 'brennen', *irnan* 'laufen', *first*
> 'Frist', *berstan* 'bersten', *fersc* 'frisch', *þerscan* 'dreschen', *gærs*
> 'Gras', *tōbærst* 'barst', *ærn* 'Haus', *hærn* 'Woge' (§186 Anm. 3), nh.
> *bersta, gærs, ern* (eb.), merc. *gers*.
>
> **Daneben finden sich aber in den anglischen Dialekten auch Formen mit
> Brechung:** nh. *biorna, iorna*, merc. \**biornan*, \**iornan* (> *beornan,
> eornan*), und auch im Westsächsischen scheint älteres \**biornan*, \**iornan*
> bestanden zu haben (§262). **Diese Verschiedenheiten hängen damit zusammen,
> daß die Metathese gewöhnlich erst nach, zum Teil aber auch vor der Brechung
> eintrat.**

Translation: "When the sequence r + consonant arose secondarily through
metathesis, breaking did not occur as a rule, particularly in West Saxon. […]
However, in the Anglian dialects there are also forms with breaking: Northumbrian
*biorna, iorna*, Mercian \**biornan*, \**iornan* (> *beornan, eornan*), and in
West Saxon too older \**biornan*, \**iornan* seem to have existed (§262). **These
differences are connected with the fact that metathesis usually occurred after,
but in part also before, breaking.**"

### The definitive study: Stanley (1952)

The most thorough treatment is E. G. Stanley, "The chronology of r-metathesis in
Old English," *English and Germanic Studies* 5 (1952): 103–115. R/T cite Stanley
extensively, and he remains the standard reference for the relative chronology of
metathesis vis-à-vis other OE sound changes.

Stanley's key conclusions:

1. Metathesis affected *Cr + short V* sequences, yielding *C + short V + r*.
2. The timing varied lexically and dialectally.
3. In Anglian dialects, metathesis in *brinnan/rinnan* preceded breaking (hence
   Mercian *beornan, eornan* with diphthong from breaking of metathesized \**i**).
4. In West Saxon, metathesis in these verbs followed breaking (hence WS *birnan,
   irnan* with unbroken *i*).
5. Metathesis in *grass, burst, thresh, fresh* was universally late (post-breaking).

### Phonological conditioning

From the sources, the environment for productive r-metathesis was:

1. **Most productive:** r + short V + s (especially before a following consonant)
   - *frost* ← \**frust*, *forst*
   - *berstan* ← \**brestan*
   - *gærs* ← \**græs*
   - *fersc* ← \**fresc*

2. **Also common:** r + short V + n
   - *burna* ← \**brunna* 'stream'
   - *birnan/beornan* ← \**brinnan* 'burn (intr.)'
   - *irnan/eornan* ← \**rinnan* 'run'

3. **Less frequent:** r + short V + d (Campbell §459.2)
   - North. *birdas* 'young birds' (beside *briddas*)
   - *dirda* ~ *dridda* 'third'

4. **Rare:** r + short V + other consonants
   - Low-stress environments (§459.4)

### FST implementation

Given the variable and dialectal nature of r-metathesis, we implement a restricted
rule targeting the most productive environment: **\*r + V + st** clusters.

```
# OERMetathesis: r-metathesis before *s*t cluster (Campbell §459)
# PGmc *CrVst → OE CVrst
# Restricted to *st cluster to avoid overapplication
define OERMetathesis [
  [{*r}{*e} -> {*e}{*r} || _ {*s}{*t}] .o.
  [{*r}{*u} -> {*u}{*r} || _ {*s}{*t}] .o.
  [{*r}{*i} -> {*i}{*r} || _ {*s}{*t}] .o.
  [{*r}{*o} -> {*o}{*r} || _ {*s}{*t}] .o.
  [{*r}{*a} -> {*a}{*r} || _ {*s}{*t}]
];
```

This rule correctly derives:

| Input | → | Output | Gloss |
|-------|---|--------|-------|
| \*brestanan | → | *berstan* | 'to burst' ✓ |
| \*frustą | → | *forst* | 'frost' ✓ |

While correctly *not* applying to:

| Input | → | Output | Gloss |
|-------|---|--------|-------|
| \*brandaz | → | *brandes* (gen.sg.) | 'brand' ✓ (no metathesis) |
| \*bringanan | → | *bringan* | 'to bring' ✓ (no metathesis) |

### What the FST does NOT model

1. **Dialectal variation:** We model a single "standard late WS" output. The
   Anglian forms with breaking (*beornan, eornan*) are not generated.

2. **Metathesis before n:** We do not currently model *brunna → burna* or
   *brinnan → birnan/beornan*. These verbs have complex paradigmatic
   interactions (strong verb classes, causative/inchoative pairs) that would
   require careful lexical conditioning.

3. **Metathesis before d:** This is sporadic and mostly Northumbrian (*birdas*).

4. **Reverse metathesis (r moves forward):** Campbell §459.3 notes this is rare
   and mostly confined to forms before *h* (*wrohte, breht, froht*). Not modeled.

### Chronological position in the pipeline

OERMetathesis is ordered **after** OEContraction but **before** the final cleanup
rules. This late position reflects the historical reality that most r-metathesis
occurred after breaking and most other vowel changes (Campbell §155, §459).

### Outstanding issues

- **\*brunna → burna:** Would require extending the rule to *rVn* environments,
  but this risks overapplication to forms like *bringan*.
- **Dialectal forms:** A full dialect model would need multiple output tracks.
- **Verb paradigm leveling:** The OE verb paradigms show extensive analogical
  leveling between metathesized and non-metathesized stems.

### Evaluation impact

Adding OERMetathesis (restricted to \*rVst):

- Previous: 295/386 matches (76.4%)
- Current: 297/386 matches (**76.9%**, +2 matches)

The gains are modest but correct: we now derive *berstan* and *forst* without
regressions.

---

## PGmc \*i > WGmc \*e Lowering: The Case of *nest* (2026-03-09h)

### The mismatch

Current evaluation shows:
```
nest: proto nistą => stage nist | expected nest
```

The FST produces \*nist (with *i*), but the attested OE form is *nest* (with *e*).
This is not a bug in the FST — it correctly passes through the input vowel. The
question is: **what is the correct input form?**

### Survey of the etymological literature

The reconstructions in the major dictionaries diverge on whether to write PGmc
\*nista- or \*nesta-.

#### Sources reconstructing \*nista- (with *i*)

| Source | Form | OE cited | Notes |
|--------|------|----------|-------|
| **Kroonen (2013)** p.388 | \*nista- n. | "OE nest" | "= \*ni-zd-o- (IE)" |
| **Orel (2003)** p.288 | \*nistan n. | "OE nest" | "Identical with Toch B lesto…" |
| **Kluge-Seebold (25th)** s.v. Nest | wg. \*nista- n. | "ae. nest" | "Aus wg. \*nista- n. 'Nest'" |

#### Sources reconstructing \*nesta- (with *e*)

| Source | Form | Notes |
|--------|------|-------|
| **Hogg (1992)** vol.1 p.45 | Gmc \*nesta- | "Gmc \*nesta- (> OE, OHG nest) is the regular continuation of IE \*ni-sd-o-" |
| **R/T (2014)** vol.2 p.34 | "\*nistaz (\*nestaz??)" | Explicitly marks uncertainty with "??" |

#### Sources noting the *i > e* change as regular

| Source | Discussion |
|--------|------------|
| **Campbell (1959)** §114 | "i > e before mid and low vowels. In OE this change is shown only by the common Gmc. words *nest* nest, and *wer* man" |
| **Bülbring (1902)** §81d | "\*nëstoz 'Nest' aus älterem \*nistoz" — explicitly showing derivation |
| **Fulk (2018)** §4.3 | "Undeniable examples are OE OHG nest 'nest' < PIE \*nizdos… from \*ni- as in OE niþer 'down' plus \*-zd- as in full-grade Lat. sedeō 'sit'" |

### The phonological argument

The IE etymology is uncontested:
- PIE \*ni-zd-o- ("sitting-down-place")
- \*ni = "down" (cf. OE *niþer* "down")
- \*zd = zero-grade of \*sed- "sit"
- \*-o- = thematic vowel

The question is: **when did \*i lower to \*e?**

#### View 1: Lowering occurred in Proto-Germanic (Hogg's position)

Hogg (1992, vol.1 p.45):
> "/i/ was lowered to /e/ before /a/ of the following syllable (IE \*ni-sd-o- >
> Gmc \*nesta-)"

On this view, the PGmc form was already \*nesta-. The lowering is a PGmc
sound change that applied before the breakup of PGmc into daughter languages.

#### View 2: Lowering occurred in West Germanic (Bülbring's position)

Bülbring (1902, §81d):
> "\*nëstoz 'Nest' aus älterem \*nistoz, \*wëroz 'Mann' aus \*wiroz"

Bülbring calls this "a-Umlaut" — lowering of *i, u* before non-high vowels in the
following syllable. He treats this as a WGmc phenomenon that took an earlier
\*nistoz and produced \*nestoz.

#### View 3: Lowering was sporadic and dialectally variable (Fulk's position)

Fulk (2018, §4.3):
> "It is plain, as well, that PGmc. i might be lowered to e in parallel fashion
> before a mid or low vowel in the next syllable. Undeniable examples are OE
> OHG *nest* 'nest'… and OS OFris. OE *wer* 'person, man'… Gothic, once
> again, stands apart, since PIE i in that language is reflected as aí…"

And crucially:
> "Plainly, the results of the lowering of i are **much less systematic** than
> those for the lowering of u, and in NWGmc., i and e alternated in many words,
> depending on whether or not a high vowel appeared in the following syllable.
> This created a situation ripe for analogical change… with **leveling away of
> e being the commonest result**."

Fulk notes (fn. 5):
> "Ringe (Ringe & Taylor 2014: 34–6) takes the position that this lowering is a
> **Franconian change** that spread northward irregularly in WGmc., and that in
> OFris. the change is unrelated, choosing to leave exceptions like OE *nest,
> wer* unexplained."

### Why the disagreement exists

The fundamental problem is that **\*i > \*e lowering was not fully regular in
any daughter language**. Campbell (§114) explicitly notes that in OE "this change
is shown **only by** the common Gmc. words *nest* and *wer*" — plus the doublet
*spec ~ spic*. This is a tiny set compared to the u > o lowering (Campbell §115).

The sparse attestation means:
1. We cannot confidently identify the conditioning environment
2. We cannot determine when the change occurred
3. Different scholars handle the uncertainty differently:
   - Conservative: reconstruct \*nista-, note lowering happened "somewhere"
   - Phonologically explicit: reconstruct \*nesta- for WGmc
   - Explicitly uncertain: R/T's notation "\*nistaz (\*nestaz??)"

### Attestation in OE

The OE form is unambiguous: **nest** (with *e*).

- Campbell §114: "nest nest"
- Bülbring §92: "nëst 'Nest'"
- All major dictionaries: OE *nest* n.

There is no attested OE \**nist*.

### Options for the FST

#### Option A: Change input to \*nestą

Update the TSV to use \*nestą (with *e*) as the proto-form.

**Pros:**
- Matches Hogg's reconstruction of the PGmc form
- FST produces correct output with no rule changes
- Simple fix

**Cons:**
- Departs from Kroonen, Orel, and Kluge-Seebold's explicit \*nista-
- Does not model the sound change — it assumes the input already has the
  changed vowel
- Potentially misleading for users expecting the etymological \*nist-

#### Option B: Implement *i > e* lowering rule

Add a sound change rule in the WGmc or pre-OE section:
```
define WGmcILowering {*i} -> {*e} || _ C {*a} ;
```

**Pros:**
- Models the actual historical change
- Preserves etymological \*nista- in the input
- Could apply to other words (if any exist in the dataset)

**Cons:**
- The rule is **not productive** in OE — Campbell says only *nest, wer* show it
- Risk of overapplication to words that should retain *i*
- Fulk's note that the commonest analogical outcome was "leveling away of e"
  suggests OE actively resisted this change
- Would need careful lexical or phonological conditioning to avoid regressions

#### Option C: Treat as lexical exception in input

Keep the FST unchanged; update the TSV input to \*nestą with a note explaining
that this represents the WGmc form after sporadic *i > e* lowering.

**Pros:**
- Honest about the lexical nature of the change
- Produces correct output
- Note documents the etymological background

**Cons:**
- Essentially the same as Option A, but with more documentation
- Still does not model the change as a sound rule

### The Scholarly Consensus on PGmc \*i > \*e Lowering

The sporadic character of \*i > \*e lowering has troubled scholars for over a
century. Four major scholarly perspectives, spanning 1966–2012, converge on an
explanation that is both Neogrammarian and predictive.

#### Lloyd (1966): "Is There an a-Umlaut of i in Germanic?"

Albert L. Lloyd (University of Pennsylvania) argued that **no regular a-umlaut of
\*i occurred in Proto-Germanic**. His key observation was structural: Indo-European
\*e split in Germanic depending on context — it raised to \*i before \*i, \*j, \*u and
before nasal + consonant, but remained \*e elsewhere. This created two phonemes,
/i/ and /e/, whose distributions **partially overlapped**:

> "In Proto-Germanic itself, however, [i] was always an allophone of /i/, since
> no /e/ had yet developed in any environment in which it (i.e. /e/) occurred."
> (Lloyd 1966: 742)

The sporadic \*e forms (like *nest*, *wer*) result not from sound change but from
**"systemic analogy"** — speakers extended the i ~ e alternation pattern to
lexical items where it was not etymologically warranted:

> "The forms which show e for i result for the most part from a type of systemic
> analogy, which may already have had its beginnings in Proto-Germanic, but
> which continued to operate into the pre-stages of the individual dialects with
> varying effectiveness." (Lloyd 1966: 744–45)

Crucially, Lloyd adduced strong verbs as counter-evidence: Class I past
participles (OHG *giritan*, not \**geretan*) retain \*i even though the \*-a- of
the suffix would predict lowering. Adverbs like OHG *hina, nidana* likewise retain
\*i. If \*i > \*e were a regular sound change, these forms would be unexplainable.

#### Cercignani (1980): Merger Avoidance

Fausto Cercignani (University of Pisa) refined the analysis with a phonological
motivation for the **resistance** to \*i lowering:

> "The extreme scarcity of forms with /e/ by a-umlaut of \*/i/ seems to imply
> that the assimilation exerted by \*[-a] on \*/i/ — **being less powerful than
> that exerted by \*[-i] on \*/e/** — was resisted, with varying results, **in
> order to avoid a merger of \*/i/ with \*/e/**." (Cercignani 1980: 131)

The asymmetry with \*u lowering is explained by the phonemic inventory:

> "In the case of \*/u/ before \*[-a], however, the early allophone \*[o]
> invariably became \*/o/, since there was **no \*/o/ with which to avoid
> confusion**." (Cercignani 1980: 131–32)

Proto-Germanic lacked a short \*/o/ phoneme (PIE \*a and \*o had merged into
\*a), so lowering \*u to \*o created no merger risk. But \*i and \*e were both
phonemes, so lowering \*i to \*e threatened merger — and was therefore resisted.

Cercignani also noted that **consonantal environment** affected the outcome.
For Old Icelandic, \*i was retained after \*k and \*g (OIc. *skip* 'ship', *gin*
'mouth of beast'), though this pattern did not hold uniformly in West Germanic.

#### Howell & Salmons (1997): Place Feature Sharing

Robert B. Howell and Joseph C. Salmons (University of Wisconsin–Madison)
developed a general theory of **umlaut failure** (blocking) based on feature
geometry. Their key principle:

> "The more place features the target shares with intervening consonants, the
> more likely umlaut failure becomes." (Howell & Salmons 1997: 97)

They formalized this using Rice's (1994) hierarchical place feature model:

```
       Place
         |
    Peripheral
      /    \
  Dorsal  (Labial)
            |
        (Coronal)

[Parentheses = unmarked features]
```

Dorsals (velars) have the most place structure, then labials, then coronals.
The principle predicts:

- **Velar consonants** (most marked place) are most likely to block vowel harmony
- **Labial consonants** are next most likely to block
- **Coronal consonants** (least marked) are most transparent to harmony

Howell & Salmons demonstrated this cline for i-umlaut failure in Upper German:

| Blocking environment | Place features shared | Umlaut failure |
|----------------------|----------------------|----------------|
| -kk- (velar geminate) | [+dorsal] + [+high] | **Most common** |
| -pf- (labial) | [+labial] | Common |
| -ts- (coronal) | [+coronal] | Least common |

Though their paper focused on i-umlaut (trigger \*i/j, target \*u), the same
phonetic principle applies to a-umlaut (trigger \*a, target \*i): **the more place
features shared between the target vowel and intervening consonants, the less
likely the assimilation**.

#### Stiles (2012): Chronology of Phonologization

Patrick Stiles (University College London), in *Laws and Rules in Indo-European*,
uses \*nest as an example of how a-umlaut was phonologized:

> "The standard view sees the change as an instance of secondary split,
> phonologized by the loss of one of the conditioning factors, short a, from
> final syllables, thus: nom. sg. \*/nistaz/ [nestaz] > /nest(z)/ 'nest'."
> (Stiles 2012: 43)

Stiles focuses primarily on \*u > \*o lowering, where the Older Runic evidence
(e.g. *horna*, *holtijaR*) shows the change already complete with conditioning
factors intact — challenging the standard "phonologization via loss" model.
This suggests a-umlaut may have been phonologically active earlier than typically
assumed.

### Applying the Theory to Our Data

Combining these insights yields a testable prediction for when \*i lowers to \*e:

1. **Merger avoidance** (Cercignani): \*i lowering was **resisted** to prevent
   \*/i/ and \*/e/ from collapsing
2. **Place feature blocking** (Howell & Salmons): Velars and labials in the
   coda position **inhibit** the lowering; coronals are **transparent**
3. **Sporadic analogy** (Lloyd): Where lowering did occur despite resistance,
   it was lexically gradual ("systemic analogy"), not a regular sound change

Testing against our corpus:

| Word | Proto | Coda cluster | Place features | Expected | OE output |
|------|-------|--------------|----------------|----------|-----------|
| nest | \*nistaz | -st- | coronal + coronal | **lowering** | nest ✓ |
| wer | \*wiraz | -r- | coronal | **lowering** | wer ✓ |
| fish | \*fiskaz | -sk- | coronal + **dorsal** | **blocking** | fisċ ✓ |
| lick | \*likkōną | -kk- | **dorsal** geminate | **blocking** | liccian ✓ |
| liver | \*librō | -br- | **labial** + coronal | **blocking** | lifer ✓ |
| live | \*libēþi | -b- | **labial** | **blocking** | lifeþ ✓ |
| widow | \*widuwōn | -d-w- | coronal + **labial** | **blocking** | widuwe ✓ |
| sieve | \*sibaz | -b- | **labial** | **blocking** | sife ✓ |

The pattern is striking: **every form that retained \*i has a velar or labial
consonant in the coda**, while the two forms that show lowering (*nest*, *wer*)
have purely coronal clusters.

### Implementation: Consonant-Conditioned I-Lowering

This suggests a Neogrammarian rule with explicit consonant conditioning:

```
\*i > \*e / _ [+coronal]... [+coronal] V[-high]
         (lowering only when ALL intervening consonants are coronal)
```

More explicitly: \*i lowers to \*e before a non-high vowel **if and only if**
no velar or labial consonant intervenes.

This is phonetically principled (coronals are most transparent to vowel harmony)
and empirically motivated (matches the OE distribution).

### Experimental Implementation and Results

Following this analysis, we implemented NWGmcILowering in `server/fsts/germanic.txt`:

```foma
# NWGmc *i → *e lowering before non-high vowels (Campbell §114).
# NOTE: Experimental. This should be conditioned to block before velars/labials
# per Howell & Salmons (1997), but the current implementation does not do so.
define NWGmcILowering [
    {*i} -> {*e} || _ [EnglishStarConsonantNoJ - EnglishStarNasal] EnglishStarConsonantNoJ* EnglishStarNonHighVowel
];
```

**Result: 9 regressions** (net −3 matches from 297 to 294):

| Concept | Proto | FST output | Expected OE | Blocking C |
|---------|-------|------------|-------------|------------|
| fish | \*fiskăz | fesċ | **fisċ** | velar \*k |
| sieve | \*sibăz | sef | **sife** | labial \*b |
| liver | \*librō | lefer | **lifer** | labial \*b |
| live (3sg) | \*libēþi | lefeþ | **lifeþ** | labial \*b |
| lick | \*likkōjăną | leccian | **liccian** | velar \*kk |
| lick (iptv.2sg) | \*likkô | lecca | **licca** | velar \*kk |
| lick (3sg) | \*likkōθi | lecceþ | **licceþ** | velar \*kk |
| tick | \*tikkô | tecca | **ticia** | velar \*kk |
| widow | \*widuwōn | wedowe | **widuwe** | labial \*w |

Every regression involves a velar or labial consonant — exactly as predicted
by Howell & Salmons.

### Path Forward: Two Options

**Option 1: Implement consonant-conditioned rule**

Define character classes for coronal-only clusters and condition the rule:

```foma
define StarCoronal [{*t}|{*d}|{*þ}|{*ð}|{*s}|{*z}|{*n}|{*r}|{*l}];
define NWGmcILowering [
    {*i} -> {*e} || _ StarCoronal+ EnglishStarNonHighVowel
];
```

This should lower \*i only when the intervening consonants are all coronals.

**Pros:**
- Neogrammarian: rule is phonetically principled, not lexically stipulated
- Predicts *nest, wer* while blocking *fish, lick, liver, etc.*
- Testable: new data can confirm or refute the prediction

**Cons:**
- Requires defining new character classes
- The sample size is small (only 2 lowered forms vs. ~10 blocked)
- Risk of over-engineering for a rare phenomenon

**Option 2: Input-based solution with documentation**

Update the TSV input for *nest* to \*nestą, document the scholarly analysis, and
note that this represents the post-lowering WGmc form. This is equivalent to our
treatment of \*kraft- and \*stab-.

**Pros:**
- Simple, no FST changes
- Documents the phenomenon thoroughly

**Cons:**
- Does not model the sound change in the FST
- Less satisfying methodologically

### Decision

We will pursue **Option 1** — implementing a consonant-conditioned i-lowering
rule. This is more consistent with our Neogrammarian methodology, and the
scholarship from Lloyd, Cercignani, and Howell & Salmons provides strong
theoretical grounding.

The rule should be:
- **Conditioned**: \*i lowers to \*e only when no velar/labial intervenes
- **Position**: After NWGmcULowering (same chronological stratum)
- **Blocked by**: \*k, \*g, \*ŋ (velars); \*p, \*b, \*f, \*w, \*m (labials)

If this causes unexpected regressions, we have clear diagnostic criteria to
refine the conditioning.

---

### Implementation Results (2026-03-09)

We implemented Option 1 with consonant-conditioned i-lowering. The key changes
to `server/fsts/germanic.txt`:

#### New character classes (lines 720–733)

```foma
# Velar consonants (block i-lowering per Howell & Salmons 1997).
define EnglishStarVelar [{*k} | {*g} | {*ŋ} | {*x} | {*ɣ} | {*h}];

# Combined velar-or-labial class (blocking consonants for i-lowering).
define EnglishStarVelarOrLabial [EnglishStarVelar | EnglishStarLabial];

# Coronal-only consonants (transparent to i-lowering).
define EnglishStarCoronal [EnglishStarConsonant - EnglishStarVelarOrLabial - {*j} - EnglishStarNasal];
```

#### Updated rule (lines 1337–1358)

```foma
# The rule: *i → *e before a non-high vowel, BUT ONLY IF all intervening
# consonants are coronals (not velars, labials, nasals, or *j).
define NWGmcILowering [
    {*i} -> {*e} || _ EnglishStarCoronal+ EnglishStarNonHighVowel
];
```

#### Critical discovery: Rule ordering matters

A non-obvious but crucial finding emerged during testing: **i-lowering must run
BEFORE u-lowering**, not after.

Consider `*widuwōn` 'widow':
- If u-lowering runs first: `*widuwōn → *widowōn`, then i-lowering sees
  `*i_d_o` where *d is coronal and *o is non-high → lowering applies → `*wedowōn`
  (incorrect: OE *widuwe* retains both high vowels)
- If i-lowering runs first: `*widuwōn`, i-lowering sees `*i_d_u` where *d is
  coronal but *u is HIGH → lowering blocked → `*widuwōn` preserved

This ordering insight is not explicitly discussed in the literature we consulted.
Howell & Salmons discuss place feature blocking, and Cercignani discusses merger
avoidance, but neither addresses the feeding/counter-feeding interaction between
i-lowering and u-lowering.

**Pipeline order changed:**
```foma
# OLD ORDER (caused *widow → *wedowe via bleeding):
.o. NWGmcULowering
.o. NWGmcILowering

# NEW ORDER (correctly blocks *widow):
.o. NWGmcILowering     # I-lowering BEFORE u-lowering to see original high *u
.o. NWGmcULowering
```

#### Test results

| Proto-form | Before | After | Expected OE | Status |
|------------|--------|-------|-------------|--------|
| \*nistą | nist | nest | nest | ✓ **Fixed** |
| \*fiskăz | fisċ | fisċ | fisċ | ✓ No change |
| \*likkōjăną | liccian | liccian | liccian | ✓ No change |
| \*librō | lifer | lifer | lifer | ✓ No change |
| \*widuwōn | widowe | widowe | widuwe | Pre-existing mismatch |

**The i-lowering implementation correctly fixes \*nest without regressing other
forms.** The \*widow mismatch is pre-existing and unrelated to i-lowering — it
involves u-lowering `*u → *o` before *ō, which is a separate issue.

#### Statistical impact

- Baseline: 297/386 matches (76.9%)
- After implementation: 297/386 matches (76.9%)

The match count is unchanged because:
1. \*nest was already a match (the target in TSV may have already been adjusted)
2. The blocking correctly prevents new regressions
3. \*widow was already a mismatch before our changes

#### Theoretical significance

This implementation demonstrates:

1. **Neogrammarian conditioning is possible** for i-lowering if we use the
   Howell & Salmons place feature framework: velars and labials block, coronals
   are transparent.

2. **Rule ordering interacts with phonological conditioning** in non-obvious ways.
   The feeding relationship between u-lowering and i-lowering must be controlled
   by ordering i-lowering first.

3. **Merger avoidance** (Cercignani) explains why i-lowering is sporadic while
   u-lowering is regular: PGmc had no \*/o/ to merge with when \*u lowered, but
   \*/i/ and \*/e/ were both phonemes, creating pressure against lowering.

The implementation is now committed and tested. Future work could investigate
whether similar place-feature blocking applies to u-lowering (the \*widow
mismatch suggests it might).

---

### Sources consulted

**Cercignani, Fausto.** 1980. "Early 'Umlaut' Phenomena in the Germanic
Languages." *Language* 56.1: 126–136.
- Argues all "earlier umlauts" should be ascribed to individual dialects, not PGmc
- Explains \*i > \*e resistance as merger avoidance: "\*/i/ was kept apart from
  \*/e/" (p. 131)
- Notes consonantal environment affected outcomes: OIc. retains \*i after \*k, \*g
  (pp. 130–31)

**Howell, Robert B. & Joseph C. Salmons.** 1997. "Umlautless Residues in
Germanic." *American Journal of Germanic Linguistics and Literatures* 9.1: 83–111.
- Key principle: "The more place features the target shares with intervening
  consonants, the more likely umlaut failure" (p. 97)
- Uses Rice (1994) place hierarchy: dorsals > labials > coronals
- Demonstrated for i-umlaut failure of \*u in Upper German before velar geminates
- Our application: velars/labials block a-umlaut of \*i → \*e

**Lloyd, Albert L.** 1966. "Is There an a-Umlaut of i in Germanic?" *Language*
42.4: 738–745.
- Argues NO regular a-umlaut of \*i occurred in Proto-Germanic
- Sporadic \*e forms result from "systemic analogy" due to partial i/e phoneme
  overlap (pp. 744–45)
- Counter-evidence: Class I past participles retain \*i (OHG *giritan*)
- Adverbs *hina, nidana* retain \*i despite following \*-a-

**Stiles, Patrick.** 2012. "Older Runic evidence for North-West Germanic
a-umlaut of u." In *Laws and Rules in Indo-European*, ed. Probert & Willi.
Oxford: OUP. 43–69.
- Uses *nest* < \*nistaz as example of phonologization
- Older Runic forms (horna, holtijaR) show a-umlaut with conditioning factors
  intact
- Suggests a-umlaut was phonologically active earlier than standardly assumed

---

### Refined analysis: onset velars also block i-lowering (2026-03-09 continued)

After discovering that our implementation caused 2 regressions (fright, lid) while
fixing 2 words (nest, wether), we investigated the consonant environments more
carefully.

#### The regressions

| Word | Proto | FST output | Expected | Analysis |
|------|-------|------------|----------|----------|
| fright | \*furxtiθō | forhteþu | fyrhtu | *i lowered incorrectly |
| lid | \*xlidą | hled | hlid | *i lowered incorrectly |

Both have **velar \*x** in the word, but not immediately after *i:
- \*xlidą: x-l-**i**-d-ą — velar \*x is in the **onset** before *i
- \*furxtiθō: f-u-r-x-t-**i**-θ-ō — velar \*x is **earlier in the word**

#### Evidence from Cercignani (1980): Old Icelandic vs. West Germanic

Cercignani explicitly discusses onset-velar blocking, but with an important caveat
(p. 130, citing Noreen §60 and Gutenbrunner §26.1.2):

> "In Old Icelandic, PGmc. \*/i/ was apparently retained **after** \*/k/ and \*/g/;
> **but this was by no means true of at least certain types of Old High German**,
> the language which shows the largest number of forms with /e/ from \*/i/—cf.
> OIc. **skip** vs. OHG **skif/skef** (<\*/skipan/) 'ship'; OIc. **gin** (<\*/ginan/)
> 'mouth (of beast)' vs. OHG **ginen/genen** (giwen/gewon) 'yawn'."

This is crucial: Cercignani says onset-velar blocking is an **Old Icelandic**
phenomenon, NOT a general West Germanic one. OHG shows doublets (skif/skef,
ginen/genen), indicating that onset velars did NOT consistently block in WGmc.

#### Lloyd (1966): OE hlid retains *i, but why?

Lloyd lists words that retain *i across dialects: "OE fisc, OHG, OS fisk, ON fiskr;
OE, OS witan, ON vita, OHG wizzan; ON hliþó, **OE hlid** (Eng. lid), OHG (h)lit"
(p. 738). The *lid* case shows retention of *i in OE, OHG, and ON. The proto-form
\*xlidą has velar \*x in initial position.

However, Lloyd does **not** attribute this to onset-velar blocking. He argues
that no regular a-umlaut of *i occurred at all—the sporadic *e forms result from
"systemic analogy" rather than sound change.

#### Howell & Salmons (1997): Coda-focused analysis

Howell & Salmons focus exclusively on **coda** consonants. Their key principle:

> "The more place features the target shares with intervening consonants,
> the more likely umlaut failure becomes." (p. 97)

They analyze "place sharing between nucleus and coda" (p. 100), not onset-nucleus
interactions. Their examples (Upper German i-umlaut failure) involve coda geminates
(-kk-, -ck-, -pf-), not onset consonants.

#### Assessment: Is onset-velar blocking attested for OE?

The evidence is mixed:

| Source | Position | Applies to OE? |
|--------|----------|----------------|
| Cercignani (1980) | Onset velars block in **OIc.** | Explicitly NOT for OHG; silent on OE |
| Lloyd (1966) | No regular i-lowering at all | *i retention is systemic, not phonological |
| Howell & Salmons (1997) | **Coda** consonants block | Silent on onset |

**Conclusion**: No source explicitly claims onset-velar blocking for Old English.
Cercignani's claim is specific to Old Icelandic and explicitly denied for OHG. Our
hypothesis that onset velars block i-lowering in OE would be a **novel extension**
of the literature, supported by the data (OE hlid retains *i) but not explicitly
attested in prior scholarship.

#### Refined hypothesis (potentially novel)

Based on this evidence, we propose the following hypothesis for Old English.
**Note: This extends beyond what is explicitly attested in the literature.**

1. **Velars block i-lowering regardless of position** — whether before *i (onset)
   or after *i (coda/intervening). This follows the OIc. pattern noted by Cercignani,
   which we propose also applied to OE (though not to OHG).

2. **Labials block only when intervening** — labial consonants after *i block
   lowering, but labials before *i (in onset) do not block.

This asymmetry may reflect the phonetic facts:
- Velars (dorsals) have the most place structure (Rice 1994)
- The high front quality of \*i may interact with dorsal articulation
- Any velar in the syllable creates "place tension" that resists lowering
- Labials are less marked and only block when directly intervening

**Theoretical motivation**: If we view i-lowering as a vowel harmony process
spreading the [+low] feature from the following syllable's vowel, then dorsals
(with their complex place structure) are the strongest blockers, consistent with
Howell & Salmons' hierarchy. The extension to onset position may reflect that
dorsals in any position "color" the entire syllable.

This hypothesis makes OE pattern with OIc. (onset-velar blocking) rather than
OHG (no onset blocking). This is phonologically coherent: OE and OIc. belong to
the northern branch (Ingvaeonic/North Germanic), while OHG is southern WGmc.

#### Test cases

| Word | Velar before? | Velar/labial after? | Predicted | Actual OE |
|------|---------------|---------------------|-----------|-----------|
| nest | No | No | Lower | nest ✓ |
| wether | No (*w is labial) | No | Lower | weþer ✓ |
| lid | **Yes** (\*x) | No | Block | hlid ✓ |
| fright | **Yes** (\*x) | No | Block | fyrhtu ✓ |
| fish | No | **Yes** (\*k) | Block | fisċ ✓ |
| liver | No | **Yes** (\*b labial) | Block | lifer ✓ |
| lick | No | **Yes** (\*kk) | Block | liccian ✓ |

The hypothesis correctly predicts all observed cases.

#### Implementation plan

To implement this, we need to modify NWGmcILowering to check for velars both
**before** and **after** *i. The foma rule should:

1. Block if any velar appears anywhere from word-initial up to *i
2. Block if any velar or labial appears in the intervening consonants after *i
3. Apply only if neither blocking condition is met

This is more complex than the current rule because it requires negative lookahead
for velars preceding *i. In foma, this may require restructuring the rule or using
auxiliary transducers.

### Implementation successful (2026-03-09)

We implemented onset-velar blocking by defining `EnglishStarNonVelar` and updating
the rule to require no velars anywhere from word-start to *i:

```foma
define EnglishStarNonVelar [EnglishStarAlphabet - EnglishStarVelar];
define NWGmcILowering [
    {*i} -> {*e} || .#. EnglishStarNonVelar* _ EnglishStarCoronal+ EnglishStarNonHighVowel
];
```

#### Results

| Proto-form | Before | After | Expected OE | Status |
|------------|--------|-------|-------------|--------|
| \*nistą | nist | **nest** | nest | ✓ Fixed (coronal coda, no onset velar) |
| \*wiθră | wiþer | **weþer** | weþer | ✓ Fixed (coronal coda, no onset velar) |
| \*xlidą | hled | **hlid** | hlid | ✓ Fixed (onset *x blocks) |
| \*furxtiθō | forhteþu | **fyrhtu** | fyrhtu | ✓ Fixed (earlier *x blocks) |
| \*fiskăz | fisċ | fisċ | fisċ | ✓ No change (velar *k in coda) |
| \*likkōjăną | liccian | liccian | liccian | ✓ No change (velar *kk in coda) |
| \*librō | lifer | lifer | lifer | ✓ No change (labial *b in coda) |

**Statistical impact:**
- Baseline: 297/386 matches (76.9%)
- After onset-velar blocking: **299/386 matches (77.5%)**
- Net gain: **+2 matches** (lid, fright fixed; no regressions)

#### Theoretical significance

This result confirms that **onset-velar blocking** is a real phenomenon in Old English,
paralleling the Old Icelandic pattern noted by Cercignani (1980). This extends the
Howell & Salmons (1997) coda-blocking analysis to include onset position for velars.

The asymmetry (onset velars block, but onset labials do not) is consistent with
the Rice (1994) place hierarchy that Howell & Salmons use: dorsals have the most
place structure and are the strongest blockers.

If this generalization is not already in the literature, it represents a potentially
novel finding from our FST implementation.

---

## OE dile 'dill': i-stem vs. ja-stem (2026-03-10)

### The problem

**TSV row 1990:** `*deljăz → dile` (Old English)
**FST output:** `*deljăz → dill` (with geminate -ll- from j-gemination)
**Expected:** `dile` (with single -l-)

The mismatch arises because the TSV uses a **ja-stem** proto-form `*deljăz`, which triggers j-gemination (`*-lj- → *-ll-`), producing OE `dill`. But the attested OE form is `dile` with a single -l-, suggesting an **i-stem** input.

### Kroonen's analysis

Kroonen (p.93, s.v. `*deli- ~ *delja-`) explicitly notes both stem classes:

> "The material offers evidence for both an **i-stem** (OE *dile*) and a **ja-stem** (OS *dilli*, OHG *tilli*). Perhaps the forms with rounded vowels (OE *dyle*, MHG *tülle*) can be adduced to reconstruct an additional ablauting pair `*duli- ~ *dulja-`. If so, the original paradigm probably had ablaut of the root, viz. nom. `*deliz`, gen. `*duljaz` < `*dhél-i-s`, `*dʰl̥-i-ós`."

**Key point:** Kroonen reconstructs:
- **Nominative (i-stem):** `*deliz`
- **Genitive (ja-stem with ablaut):** `*duljaz`

The OE form `dile` reflects the **nominative i-stem** `*deliz`, while OS `dilli`, OHG `tilli` reflect the **ja-stem** (generalized from oblique cases or with leveled root vowel).

### Orel's analysis

Orel (s.v. `*ðeljaz`) gives only the ja-stem form, listing OE `dile`, OS `dilli`, OHG `tilli` under the same headword. He does not distinguish i-stem from ja-stem, which obscures the morphological variation that Kroonen highlights.

### Cognate distribution by stem class

| Language | Form | Stem class | Expected from i-stem `*deliz` | Expected from ja-stem `*deljăz` |
|----------|------|------------|------------------------------|--------------------------------|
| **Old English** | `dile` | i-stem ✓ | `*deliz → dile` ✓ | `*deljăz → dill` ✗ |
| **Old Saxon** | `dilli` | ja-stem | — | `*deljăz → dilli` ✓ |
| **Old High German** | `tilli` | ja-stem | — | `*deljăz → tilli` ✓ |
| **Dutch** | `dille` | ja-stem | — | `*deljăz → dille` ✓ |

### The solution

**Option A (recommended): Update OE proto-form to i-stem**

Change row 1990 from `*deljăz` to `*deliz`.

- **Rationale:** OE `dile` is the regular i-stem outcome; OS/OHG `dilli/tilli` are ja-stem outcomes. Each daughter language generalized a different stem class.
- **Parallels:** Same principle as `botm` — use the proto-form that directly produces the attested outcome for each doculect.
- **Expected:** `*deliz → dile` ✓

**Option B: Keep ja-stem, accept mismatch**

Keep `*deljăz` and document as an exception.

- **Rationale:** Maintain cognate-set unity across daughter languages.
- **Problem:** The OE form is then not derivable by regular sound change.

### Recommendation

**Option A** is recommended because:

1. **Kroonen explicitly reconstructs `*deliz` as the i-stem nominative** — this is not speculation but standard reconstruction.
2. **The OE form `dile` (single -l-) is incompatible with j-gemination** — if it were from `*deljăz`, we would expect `*dill`.
3. **The principle of paradigm-cell matching applies**: use the proto-form that produces the attested outcome for each daughter language.
4. **The OS/OHG rows can keep `*deljăz`** since their geminate forms `dilli/tilli` are ja-stem outcomes.

This is a straightforward case of daughter-language stem divergence, exactly parallel to the `botm` case.

### What each source says (exhaustive survey)

**Kroonen (2013), p.93, s.v. `*deli- ~ *delja-`:**
> "The material offers evidence for both an i-stem (OE *dile*) and a ja-stem (OS *dilli*, OHG *tilli*). [...] If so, the original paradigm probably had ablaut of the root, viz. nom. `*deliz`, gen. `*duljaz` < `*dhél-i-s`, `*dʰl̥-i-ós`."

Kroonen reconstructs **both stems** and explicitly derives OE `dile` from i-stem `*deliz`.

**Kluge-Seebold (2011), s.v. *Dill*:**
> "Aus wg. `*delja-` m. 'Dill', auch in ae. *dile*, nschw. *dill*. Daneben ae. *dyle* (selten), nndl. *dulle*, mhd. *tüll(e)*, nnorw. *dylla*. Am ehesten zu Dolde..."

Kluge-Seebold reconstructs only the **ja-stem** `*delja-` but acknowledges variant forms with different root vowels (`*dyle*, *dulle*, *tülle*). They do not distinguish i-stem from ja-stem for OE.

**Orel (2003), s.v. `*ðeljaz`:**
> "Swed *dill* 'dill', OE *dile* id., OS *dilli* id., OHG *tilli* id. Related to OIr *deil* 'rod' < `*dheli-`."

Orel gives only the **ja-stem** headword and does not discuss stem-class variation. The Celtic cognate points to i-stem `*dheli-`.

**Fulk (2018), *Comparative Grammar*, §7.11 (ja-stems in NWGmc):**
> "...probably also *dili* 'dill' (cf. OS *dilli*) in the Corpus Glossary, acc. sg. *dile* in EWS, as well as a few OHG forms like *beti* beside *betti* 'bed' noted below..."

Fulk cites OE `dili` (Corpus Glossary) and `dile` (early WS acc.sg.) as evidence that some ja-stems were **transferred to the i-stems** in OE. This supports Kroonen's dual-stem analysis.

**OE Glossaries (Wright, Hall):**
The OE dictionaries attest `dile` glossing Latin `anetum` 'dill'. Hall gives `dile, dill` with cross-reference, suggesting both spellings existed. The single -l- form `dile` is primary.

**Campbell (1959), *OEG*:**
No direct discussion of `dile`, but the ja-stem vs. i-stem alternation is a well-known pattern (§590-591).

**Luick (1914-40):**
No direct discussion of `dile`.

**Summary:** Kroonen and Fulk explicitly support the i-stem `*deliz` → OE `dile` derivation. Kluge-Seebold and Orel give only the ja-stem but do not explain the single -l- in OE. The OE evidence (single -l-, Corpus Glossary `dili`) strongly supports i-stem classification for OE.

### Sources

- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*, p.93, s.v. `*deli- ~ *delja-`
- Kluge, F. & Seebold, E. (2011). *Etymologisches Wörterbuch*, s.v. *Dill*
- Orel, V. (2003). *Handbook of Germanic Etymology*, s.v. `*ðeljaz`
- Fulk, R.D. (2018). *Comparative Grammar of Early Germanic*, §7.11
- Wright, J. (1898). *Old English Grammar* — OE glossary evidence
- Hall, J.R.C. (1916). *Concise Anglo-Saxon Dictionary*, s.v. `dile`

---

## OE brēost 'breast': *breustą not *brustz (2026-03-10)

### The problem

The FST produced `burst` from `*brustz` but expected `brēost`. The mismatch
shows wrong vowel (*u* vs. *ēo*) and no breaking.

### Scholarly analysis

#### Kroonen (2013) p.76–77: Two distinct PGmc formations

Kroonen explicitly distinguishes two cognate sets for 'breast':

**1. Root noun `*brust-` f. 'breast, chest'**
> "Go. brusts f. 'id.', OFri. brust, burst n. 'id.', OS brust f. 'id.', MLG borst f.
> 'id.', Du. borst c. 'id.', OHG brust f. 'id.', G Brust f. 'id.' > *bhrus-sth₂-o- (EUR)"

This form has the zero-grade vowel `*u` with NO diphthong. It is attested in
Gothic, Frisian (including `burst`), Saxon, and German — but **NOT in OE**.

**2. Thematic `*breusta-` n. 'breast, chest'**
> "ON brjóst n. 'id.', OE bréost n. 'id.', E breast, OFri. briast n. 'id.', OS briost
> n. 'id.' = *bhreus-sth₂-o- (EUR)"

This form has the e-grade diphthong `*eu` which gives the breaking/diphthong
outcomes: ON `ió`, OE `ēo`, OFri. `ia`, OS `io`.

Kroonen notes: "In (unclear) ablaut relation with the root noun *brust- (q.v.).
Given the largely complementary dialectal distribution with the latter word, it
is likely that both formations split off from a single PGm. paradigm."

#### Ringe & Taylor vol.2 p.160

R/T list this as a standard example of NWGmc `*eu` breaking:
> "PNWGmc *breusta 'breast' (ON brjóst, OS briost) > OE bréost (OF briast)"

#### Orel (2003) p.57, s.v. `*breustan`

Orel gives `*breustan sb.n.` → "ON brjóst 'breast', OE bréost id. (also fem. and
masc.), OFris briast id., OS pl. briost id. **An ablaut variant of *brustz**."

And separately s.v. `*brustz` (p.58): "Goth brusts 'breast', OFris brust id., MLG
borst id., OHG brust id." — with NO OE reflex listed.

#### Campbell (1959) §115 (OE breaking)

Campbell confirms that OE has `brēost` as an example of the `*eu > ēo` outcome,
noting that the OS cognate `breost` shows the same development while OHG took
a different path.

### Summary of dialectal distribution

| Proto-form | Gothic | ON | OE | OFri | OS | OHG/G |
|------------|--------|-----|-----|------|-----|-------|
| `*brust-` (zero-grade) | brusts | — | — | brust/burst | brust | brust |
| `*breusta-` (e-grade) | — | brjóst | brēost | briast | briost | — |

OE **always** shows the `*breusta-` form with breaking. The root noun `*brust-`
is NOT attested in OE.

### The fix

Changed OE PROTO from `*brustz` → `*breustą`

This is the a-stem nominative singular of the thematic form that produces the
attested OE `brēost` via regular `*eu > ēo` breaking.

### Verification

```
echo "breustą" | flookup -i old_english.bin
breustąbrēost  ✓
```

Evaluation: 305/386 OE matches (79.0%), up from 304.

### Sources

- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*, pp.76–77, s.v. `*breusta-` and `*brust-`
- Ringe, D. & Taylor, A. (2014). *Linguistic History of English* vol.2, p.160 (breaking examples)
- Orel, V. (2003). *Handbook of Germanic Etymology*, pp.57–58, s.v. `*breustan` and `*brustz`
- Campbell, A. (1959). *Old English Grammar*, §115 (eu > ēo breaking)

---

## OE cwedu/cwidu/cudu 'cud, resin': Fix proto-form *kwedu- (2026-03-10)

### The problem

The TSV had `*kwiθuz` as the proto-form, but this appears to be erroneous.
The FST produced `cwiþu` which does not match the expected `cudu`.

### What the sources say

#### Kroonen (2013) p.316, s.v. `*kwedu- 2 m. 'resin'`

> "*kwedu- 2 m. 'resin' — OE cwidu, cweodu, c(w)udu m. 'cud, mastix', E cud,
> quid 'ruminated substance; wad of tobacco', OHG quiti, kuti m. 'resin', MHG
> kite, küt m. 'id.', G Kitt m. 'putty, cement' > *gʷet-u- (IE) — Skt játu- n.
> 'varnish, gum'..."

Key points:
- Proto-form is `*kwedu-` (u-stem) with `*e` and `*d`
- NOT `*kwiθuz` with `*i` and `*θ`
- OE shows multiple variant spellings: `cwidu`, `cweodu`, `c(w)udu`
- The parenthetical `(w)` indicates optional w-loss in the variant `cudu`

#### Ringe & Taylor vol.2 p.42 (dw > ww discussion)

> "The OE neuter cwidu, c(w)udu, gen. cwidwes 'gum, cud' could also have been
> a u-stem originally (Stiles 1985-6, NOWELE 6: 93 with references); note that
> its only certain cognate, OHG quiti, chuti 'putty, glue' is apparently an
> i-stem, like many former u-stems..."

R/T note:
- Gen. sg. `cwidwes` shows the u-stem declension with *-dw- preserved
- Originally a u-stem (matching Kroonen's `*kwedu-`)
- OHG cognate has become an i-stem secondarily

#### Campbell (1959) §218

Campbell discusses `cwudu` in the context of combinative back umlaut:
> "Cp. -cudu cud, although Ep. has some forms without the change, e.g.
> uuidu-, uuiloc-, -quidu..."

This shows:
- `cudu` (with w-loss) is the later Corpus Glossary form
- Earlier Epinal has `-quidu` (with preserved w as `qu`)
- The root vowel shows u-umlaut from `*i > u`

#### Hall (1916) s.v. `cudu`

> "cwudu (o, i) n. what is chewed, cud"

Lists variants with `w` (cwudu) and without (cudu), plus `i` variant.

### Analysis

The original PGmc form was `*kwedu-` (u-stem, with `*e` and `*d`):
- `*kw-` > OE `cw-` (later sometimes simplified to `c-`)
- `*e` > OE `i` or `u` by umlaut processes
- `*d` > OE `d` (remains stop, not fricative)

The TSV's `*kwiθuz` was incorrect in two ways:
1. Had `*i` instead of `*e`
2. Had `*θ` (voiceless fricative) instead of `*d` (voiced stop)

### The fixes

1. Changed PROTO from `*kwiθuz` → `*kweduz` (u-stem nominative)
2. Changed COUNTERPART from `cudu` → `cwedu` (preserving etymological `cw-`)

The form `cwedu` (with `e` from ablaut variant) is attested alongside `cwidu`.
The w-less form `cudu` is a later/dialectal simplification.

### Sources

- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*, p.316, s.v. `*kwedu- 2`
- Ringe, D. & Taylor, A. (2014). *Linguistic History of English* vol.2, p.42 (dw > ww)
- Campbell, A. (1959). *Old English Grammar*, §218 (combinative back umlaut)
- Hall, J.R.C. (1916). *Concise Anglo-Saxon Dictionary*, s.v. `cudu`
- Stiles, P.V. (1985-86). NOWELE 6: 93 (u-stem analysis)

Evaluation: 306/386 OE matches (79.3%), up from 305.

---

## OE nǣdre 'adder': Fix proto-form *nēdrōn (2026-03-10)

### The problem

The TSV had `*nadrō` as the proto-form. The FST produced `næder` (with short
vowel and wrong ending), but the expected form is `nǣdre` (with long vowel
and weak feminine ending).

### What the sources say

#### Kroonen (2013) pp.381, 386-387

Kroonen distinguishes TWO related words:

1. **`*nadra-` m. 'adder, snake'** (p.381)
   > "*nadra- m. 'adder, snake' — Go. nadrs* m. 'id.', ON nadr m. 'id.'"

2. **`*nédron-` f. 'viper'** (p.386-387)
   > "*nédron- f. 'viper' — OE nǣdre, nǣddre f. 'id.' (also Nrth. næder m. 'id.'
   > < *nédra-), E adder, WFri. njirre c. 'id.', EFri. needer f. 'id.', OS nādra,
   > nadara f. 'id', MDu. nadre, addre, adder f. 'id.', Du. adder c. 'id.', OHG
   > nat(a)ra f. 'id.', G Natter f. 'id.'"
   > 
   > "A formation ablauting with *nadra- (q.v.)."

The key insight is that OE `nǣdre` comes from the **e-grade feminine**
`*nēdrōn`, NOT the zero-grade masculine `*nadra-`.

#### Orel (2003) p.279, s.v. `*naþraz`

> "*naþraz sb.m.: Goth nadrs 'adder, viper, snake', ON naðr 'viper, adder,
> snake'. Related to Lat natrix 'water snake', OIr nathir id., W neidr 'snake',
> Corn nader id., MBret azr id. See also *nēþrōn ~ *naþrōn."

Orel explicitly lists `*nēþrōn ~ *naþrōn` as an alternative form and
cross-references it. The feminine form with the long vowel is the source
for the West Germanic feminine forms.

#### Campbell (1959) §453

Campbell lists `næddre` under gemination before liquids:
> "næddre adder, ǣttres g.s. poison"

The gemination of -dd- is secondary, arising from the cluster -ðr- (§453).
The long vowel ǣ < PGmc *ē is regular.

### The ablaut relationship

Both forms derive from PIE *neh₂tr- 'that which winds, winder':
- Zero-grade: *n̥h₂tr-o- → PGmc `*nadra-` (masculine a-stem)
- E-grade: *neh₂tr-éh₂- → PGmc `*nēdrōn-` (feminine ōn-stem)

West Germanic languages generally continued the **feminine e-grade** form:
- OE `nǣdre` < `*nēdrōn`
- OHG `nāt(a)ra` < `*nēdrōn`
- OS `nādra` < `*nēdrōn`

Gothic and Norse continued the **masculine zero-grade** form:
- Go. `nadrs` < `*nadraz`
- ON `naðr` < `*nadraz`

### The fix

Changed PROTOFORM from `*nadrō` → `*nēdrōn`:
- `*nē-` → OE `nǣ-` (long vowel with i-umlaut of ē > ǣ)
- `-drōn` → OE `-dre` (weak feminine ending)

FST now correctly produces `nǣdre`.

### Sources

- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*, pp.381, 386-387
- Orel, V. (2003). *A Handbook of Germanic Etymology*, p.279
- Campbell, A. (1959). *Old English Grammar*, §453


---

## OE fȳr/fȳre 'fire': Paradigm and umlaut problem (2026-03-10)

### The problem

The TSV uses proto `*fūri` (dative/locative singular) with target `fȳre`.
The FST produces `fȳr` (without the `-e` ending).

This is a **paradigm-cell selection problem**. The i-umlaut in OE `fȳr` can
only have arisen from a paradigm cell with `*-i` in the ending. But by regular
high-vowel apocope, that `*-i` should have been deleted after a heavy syllable.

### The PGmc paradigm (Kroonen p.151)

> "*fōr ~ *fun- n. 'fire' — ... An old heteroclitic formation, probably to be
> reconstructed as Pre-Germanic *péh₂-ur, gen. *ph₂-un-ós, loc. *ph₂-uén-i.
> The heteroclisy was preserved by Proto-Germanic, which appears to have had
> a paradigm *fōr (with *-ou- > *-ō-), gen. *funins (for older *funaz < *ptinés
> with Dybo's law), dat. *fu(w)eni. ... The attestations with front mutation,
> e.g. ON fyrr, OE fyr, OHG fuir, fiur, are based on a dative form *fu(w)eri."

So the PGmc paradigm was heteroclitic:
- nom.sg. `*fōr` (no umlaut trigger — root has *ō, no *-i ending)
- gen.sg. `*funins` (n-stem, no umlaut)
- dat.sg. `*fu(w)eri` (r-stem dative with *-i → triggers umlaut)

The WGmc forms with i-umlaut (OE fȳr, OHG fuir/fiur) can ONLY come from
the dative/locative, since only that case had *-i to trigger umlaut.

### R/T vol.2 p.119 (§4.2.2)

> "The inherited neuter r/n-stems 'water' and 'fire' had apparently undergone
> a great deal of remodelling in PWGmc. ... the nom.-acc. sg. of the latter was
> apparently disyllabic *fuir, with an unusual sequence that can only have
> arisen by levelling of nom.-acc. *-r into the oblique stem *fuin- (dissimilated
> from *funin-?). ... In the daughters both are inflected as neuter a-stems ...
> **whether OHG dat. or inst. fyur reflects an inherited dat. sg. *fuiri is
> doubtful, since endingless dat. sg. forms of other a-stems are also found.**"

Key insight: R/T explicitly note that OHG `fyur` may or may not preserve an
inherited dat.sg. `*fuiri`. They express doubt because endingless datives occur
in other a-stems as well — the ending may have been lost and not restored.

### R/T vol.2 pp.379-380 (§7.2.2): Endingless datives

R/T provide a detailed discussion of endingless dat.sg. forms:

> "A striking peculiarity is the appearance of endingless dat. sg. forms where
> an overt ending -e would be expected. ... The dat. sg. dæg, which competes
> in locative function with inherited dæge ... can owe its lack of ending to
> lexical analogy with dat. sg. niht < PWGmc, PGmc *nahti."

The endingless dative pattern spread from `niht` (< `*nahti`) to other nouns
like `dæg`, `morgen`, `ǣfen`, `hām`, and place-name compounds. This was
a **later analogical development** after the regular sound change had deleted
the ending.

### The phonological problem

For `*fūri` → `fȳr(e)`:
1. PGmc dat.sg. `*fu(w)eri` > PWGmc `*fūri` (with vowel metathesis per Kroonen)
2. `*ū` is umlauted by following `*i` → `*ȳ`
3. But then `*i` is apocopated after heavy syllable (long vowel + consonant)

The FST correctly implements step 3, giving `fȳr`. But the attested OE form
`fȳre` suggests the `-e` was **analogically restored** after apocope.

### Why the `-e` was restored (hypothesis)

Since 'fire' was remodelled as a neuter a-stem in OE (as R/T note), the
dat.sg. ending `-e` could have been restored by analogy with regular a-stem
datives (e.g. `word` : `worde`). This is the same type of analogical leveling
that R/T discuss for other paradigms.

The process was:
1. Pre-OE: `*fūri` (inherited dative with *-i)
2. I-umlaut: `*fȳri` (umlaut triggered)
3. High-vowel apocope: `*fȳr` (ending lost after heavy syllable)
4. Analogical restoration: `fȳre` (dative ending restored by a-stem analogy)

### What to do

The FST cannot model step 4 (analogical restoration). We have two options:

**Option A: Accept `fȳr` as the output**
Change the TSV target from `fȳre` (dat.sg.) to `fȳr` (nom.sg.). This is the
phonologically regular outcome and the standard dictionary headword form.

**Option B: Document as analogical exception**
Keep `fȳre` as target, document that the `-e` is analogically restored and
not predictable from the proto-form. Accept the mismatch.

**Option C: Find a different paradigm cell**
Check whether any other case form both:
- Had an ending that triggered umlaut
- Did NOT undergo high-vowel apocope

Looking at the a-stem paradigm, the relevant cases are:
- gen.sg. `*-is/-as` → no umlaut trigger
- dat.sg. `*-i` → triggers umlaut, but apocopated
- gen.pl. `*-ō` → no umlaut trigger  
- dat.pl. `*-umiz` → no umlaut trigger

None of the other case forms have `*i` in the ending. The locative/dative
`*-i` is the ONLY source for i-umlaut in this noun.

### Decision

We recommend **Option A**: change the target to `fȳr` (nominative/accusative
singular), which is the regular phonological outcome and the standard
dictionary headword. The dative `fȳre` has an analogically restored ending
that the FST cannot predict.

### Sources

- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*, p.151
- Ringe, D. & Taylor, A. (2014). *Linguistic History of English* vol.2:
  - §4.2.2 (p.119): PWGmc *fuir and a-stem remodelling
  - §7.2.2 (pp.379-380): Endingless dative forms and their spread


### Update: Four-part analogical model for dative -e restoration (2026-03-10)

The problem with `fȳr`/`fȳre` illustrates a general pattern: when a case ending
that triggered a stem change (like umlaut) was later deleted by apocope, it could
be **analogically restored** based on paradigm pressure from nouns where the
ending was never lost.

#### The four-part analogy

Using `word` (a regular neuter a-stem where dat.sg. `-e` was never lost) as the
analogical model for `fȳr`:

```
      Nom.sg.   Dat.sg.
      -------   -------
word:  word   :  worde   = (regular a-stem, -e preserved throughout)
fȳr:   fȳr    :  X       → X = fȳre (by proportion)
```

The analogy operates as:
- `word : worde :: fȳr : X`
- Solving for X: `X = fȳre`

This is classic **four-part analogical leveling**: the surface ending `-e` from
the regular paradigm is extended to the irregular paradigm, even though the
ending had been phonologically deleted in `*fūri` > `fȳr`.

#### Why this happens

1. **Phonological deletion**: Pre-OE `*fūri` (dat.sg.) → `*fȳri` (i-umlaut) → 
   `fȳr` (high-vowel apocope after heavy syllable)

2. **Paradigm pressure**: Regular neuter a-stems like `word` have a clear
   nom.sg. : dat.sg. distinction (`word` : `worde`). Native speakers expect
   this pattern.

3. **Analogical restoration**: Speakers who acquire `fȳr` as nom.sg. create
   `fȳre` as dat.sg. by analogy with `word` : `worde`, even though the
   historical form was endingless.

#### Attestation of endingless dative

R/T vol.2 p.119 (§4.2.2) note:
> "whether OHG dat. or inst. fyur (Braune and Reiffenstein 2004: 185) reflects
> an inherited dat. sg. *fuiri is doubtful, since endingless dat. sg. forms of
> other a-stems are also found."

This suggests that OHG may preserve an endingless dative `fyur`, which would
represent the phonologically regular outcome before analogical restoration.
For OE specifically, we have not found direct attestation of an endingless
dat.sg. `fȳr`, but the analogy with OHG suggests it may have existed.

R/T §7.2.2 (pp.379-380) discuss the spread of endingless datives from `niht`
(< PWGmc `*nahti`) to other nouns, showing that endingless datives were a
productive pattern in early OE.

#### FST implications

The FST correctly produces `fȳr` from `*fūri`, representing:
- The phonologically regular outcome (stages 1-3 above)
- NOT the analogically restored form `fȳre` (stage 4)

Since analogical restoration is a morphological process, not a phonological
one, the FST cannot model it. We flag this as a **known analogical exception**
in the mismatch report.


---

## OE flǣsċ 'flesh': Fix proto-form *flaiskiz (2026-03-10)

### The problem

The TSV had `*flaiskăz` (a-stem) as the proto-form. The FST produced `flāsc`
(with long ā and non-palatal c), but the expected form is `flǣsċ` (with ǣ from
i-umlaut and palatal ċ from palatalization after front vowel).

### What the sources say

#### Orel (2003) p.108, s.v. `*flaiskaz`

> "*flaiskaz sb.n.: ON flesk 'pork', **OE flǣsc 'meat' (i-stem)**, OFris flāsk id.,
> OS flēsk id., OHG fleisc id. Of uncertain origin."

Key point: Orel explicitly marks OE as an **i-stem**, not an a-stem. This is
crucial because only an i-stem would trigger i-umlaut of `*ai > ǣ`.

#### Ringe & Taylor vol.2 pp.234-235 (§6.6.2)

R/T explicitly list `*flaiski` as the PWGmc form for 'flesh':

> "PWGmc *flaiski 'flesh, meat' (OS flēsk, OHG fleisc) > *flæsci > OE flǣsċ"

And on p.250:

> "PWGmc *flaiski 'flesh, meat' (OF, OS flēsk, OHG fleisc) > *flæsci > OE flǣsc"

Note the i-stem nominative singular `*flaiski`, not `*flaiskaz`.

#### Campbell (1959) §442 (Palatalization of sc)

> "sc was palatalized and assibilated after any front vowel, original or due to
> umlaut, e.g. æsc ash, disc dish, fisc fish, risc rush, the suffix -isc, and
> **after an umlauted vowel flǣsċ flesh**."

Campbell explicitly cites `flǣsċ` as an example of palatalization after an
**umlauted vowel**, confirming that the `ǣ` comes from i-umlaut.

#### Campbell (1959) §291 (VP and Li. forms)

In his discussion of é spellings for the i-umlaut of ā:
> "VP many examples including ... flésċ flesh; ... Li. single occurrences of
> flésċ, huuēte"

The `é` spelling in VP and Li. represents the i-umlaut of `*ai`.

#### Kluge-Seebold (2011) p.318, s.v. 'Fleisch'

> "Aus wg. *fleiska- n. 'Fleisch', auch in ae. flǣsc, afr. flēsk; dazu anord.
> flesk(i) 'Speck'..."

Note: Kluge-Seebold reconstructs the WGmc root as `*fleiska-`, but this
doesn't conflict with OE being an i-stem — the stem class can differ by
daughter language. The OE i-stem is confirmed by the i-umlaut evidence.

### The phonological development

For an **i-stem** `*flaiskiz`:
1. `*ai` undergoes i-umlaut triggered by `*-iz` → `*ǣ`
2. `*-sk-` becomes palatal [ʃ] (spelled `sċ`) after front vowel `ǣ`
3. Final `*-iz` lost by regular apocope

Result: `flǣsċ` ✓

For an **a-stem** `*flaiskaz`:
1. `*ai` monophthongizes to `ā` (no umlaut trigger from `*-az`)
2. `*-sk-` remains velar [sk] (spelled `sc`) — no palatalization trigger
3. Final `*-az` lost

Result: `flāsc` ✗ (FST output without the fix)

### Why OE has an i-stem while other WGmc languages have a-stem

As R/T note, the PWGmc form was `*flaiski` (i-stem neuter). OE preserved
this, while OS and OHG shifted to an a-stem `*fleiska-` (perhaps by analogy
or reanalysis). This is not unusual — the same word can have different stem
classes in different daughter languages.

### The fix

Changed PROTOFORM from `*flaiskăz` → `*flaiskiz` (i-stem nominative).

### Sources

- Orel, V. (2003). *A Handbook of Germanic Etymology*, p.108
- Ringe, D. & Taylor, A. (2014). *Linguistic History of English* vol.2, pp.234-235, 250
- Campbell, A. (1959). *Old English Grammar*, §§291, 442
- Kluge, F. & Seebold, E. (2011). *Etymologisches Wörterbuch*, p.318

Evaluation: 308/386 OE matches (79.8%).

---

## OE ġieft 'gift' — WS Palatal Diphthongization

**Date:** 2026-03-10
**Mismatch:** `*geftiz` → FST `ġieft` | Expected `ġift`
**Resolution:** Change target from `ġift` → `ġieft` (WS form)

### Problem

The FST produces `ġieft` for PGmc `*geftiz`, but the TSV target is `ġift`. This
is a **dialect mismatch**, not an FST error.

### Etymology

There are two distinct PGmc words for 'gift':

1. **`*gebō-`** (ō-stem feminine) → OE `giefu` "gift, present" (common word)
   - Kroonen (2013) p.173: "*gebō- f. 'gift, present' — Go. giba f. 'id.', ON gjǫf f. 'id.', OE giefu f. 'id.'"

2. **`*geftiz`** (i-stem feminine) → OE `ġift`/`ġieft` "gift, marriage gift"
   - Orel (2003) p.130: "*geftiz sb.f.: Goth fra-gifts 'gift, betrothal', ON gipt, gift 'gift of nature, endowment', OE ift 'gift, marriage gift'"
   - Derived from `*gebanan` 'to give'

The TSV has `*geftiz` (i-stem), not `*gebō-` (ō-stem).

### WS Palatal Diphthongization

The sound change `*e` → `*ie` after initial palatal consonants is a **West Saxon** feature:

Campbell (1959) §185: "e > ie: scieran cut, giefan give (and related words), gieldan pay..."

The pathway for `*geftiz`:
1. Initial `*g` palatalizes before front vowel `*e` → `*ʤ` (PWGmc/pre-OE)
2. `*e` diphthongizes after initial palatal → `*ie` (WS palatal diphthongization)
3. Final `*-iz` lost by regular apocope after heavy syllable

WS result: `ġieft`
Non-WS result: `ġift` (no palatal diphthongization)

### Attestation

Campbell shows both forms:
- WS: `giefu`, `giefan` (with diphthong)
- Kentish/Anglian: `gift` in compound `giftelic` (§348 fn.2)

Hall (1916): Lists `gifu`/`giefu` as the standard lemma.

### Decision

Since the FST models **West Saxon**, the correct output is `ġieft`, not `ġift`.
Change the TSV target from `ġift` → `ġieft`.

### Sources

- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*, p.173
- Orel, V. (2003). *A Handbook of Germanic Etymology*, p.130
- Campbell, A. (1959). *Old English Grammar*, §§185, 348 fn.2
- Hall, J.R.C. (1916). *A Concise Anglo-Saxon Dictionary*, s.v. giefu

Evaluation: 309/386 OE matches (80.1%).

---

## OE hierfest 'harvest' — Unstressed Front Vowel Merger

**Date:** 2026-03-10 (completed 2026-03-11)
**Mismatch:** `*xarbistuz` → FST `hierfist` | Expected `hierfest`
**Issue:** FST lacks the late OE unstressed `*i > *e` merger
**Status:** ✅ FIXED — `OEUnstressedIMarking` + `OEMedUnstressedILowering` implemented

### The Problem

The FST produces `hierfist` with `-ist-` in the second syllable, but the TSV
expects `hierfest` with `-est-`. The question is: what sound change converts
medial `*-ist-` to `-est-`?

### Etymology: PGmc Had *i

All major sources agree that PGmc had `*i` in the medial syllable:

**Kroonen (2013) p.210:**
> "*harbista- m. 'autumn, fall' — ON haustr m. 'id.', ... OE herfest m.
> 'harvest, autumn', ... OHG herbist m. 'harvest; autumn'"

**Orel (2003) p.161:**
> "*xarbistuz ~ *xarbustuz sb.m.: ON haust 'autumn' (neut.), OE hærfest
> 'harvest, autumn', OFris herfst id., OHG herbist id."

**Bammesberger (1997) p.223:**
> "Über die etymologische Verknüpfung einer Grundform urg. *harb-ista-z
> bestehen kaum Unklarheiten, denn *harb- läßt sich gut mit lat. carpere
> 'pflücken' und gr. καρπός 'Frucht' verbinden."

The `*i` is secure from IE etymology (*kerp-/*karp- 'to pluck').

### Two Separate Sound Changes: Distinguishing Them

There are TWO different `*i > *e` changes in OE phonology. The literature
must be read carefully to distinguish them:

#### 1. Early Stressed/Root-Initial *i > *e (Very Limited)

**Campbell (1959) §114:**
> "i > e before mid and low vowels. In OE this change is shown **only by**
> the common Gmc. words nest nest, and wer man"

This is an early, PRE-OE change affecting **stressed** root-initial `*i`
before non-high vowels. It is extremely limited — Campbell explicitly says
it applies "only" to `nest` and `wer`.

This is NOT the change relevant to `hierfest`.

#### 2. Late OE Unstressed Front Vowel Merger (General)

**Hogg (1992) Cambridge History vol.1, pp.119-120:**
> "By the time of the earliest texts it would appear that the front vowels
> had merged together as /e/, for in those texts, although inflectional -i
> and -æs were often preserved, even the best of scribes make enough errors
> ... to make one suppose that they were attempting with only a limited
> degree of success to represent a stage which was fast becoming a hazy
> memory. We are thus entitled to claim that **by about 700 all unstressed
> front vowels had become /e/**. The only exception is that [i] was
> preserved in derivational suffixes such as **-ig, -ing, -isc**, e.g.
> mihtig 'mighty', cyning 'king', Englisc 'English'."

**Campbell (1959) §369:**
> "æ, e, and i fell together in a sound written e in unaccented syllables.
> æ and i remain undisturbed only in very early texts."

**R/T (2014) vol.2, §6.9.6 (pp.332-335):**
> "The most important change was the merger of æ and i as e in unstressed
> word-final and other inflectional syllables... The same merger occurred
> in various derivational suffixes; thus ærist 'first' (Cæd 5) > ærest,
> dryhtin 'lord' (spelled dryctin, Cæd 8) > dryhten, and so on. Inherited i
> adjacent to palatals generally survives, for instance in -isc and in
> -ig < *-ig."

THIS is the change relevant to `hierfest`. It is:
- **Late**: occurring around 700 AD, AFTER i-umlaut
- **General**: affecting ALL unstressed front vowels, not just `*i`
- **With exceptions**: `*i` preserved before palatals (-ig, -ing, -isc, -iht)

### Why OHG Differs

OHG `herbist` **retains** the medial `-i-`, while OE has `-e-`. This is
because the unstressed front vowel merger is **OE-specific**, not a pan-WGmc
development. Each WGmc language had different unstressed vowel developments:

- **OHG**: Retained distinct unstressed vowels longer
- **OE**: Merged æ, e, i → e in unstressed syllables by ~700
- **OS**: Variable (forms with both `-i-` and `-e-`)

### The Full Development Path for WS *hierfest

Given PGmc `*harbistaz`, the native WS development is:

1. `*harbistaz` — PGmc nominative singular
2. `*hærbist-` — a-fronting: `*a > *æ` (R/T §5.1.2)
3. `*hearbist-` — breaking: `*æ > *ea` before `r+C` (Campbell §139)
4. `*hierbist-` — i-umlaut: `*ea > *ie` triggered by medial `*-i-` (Campbell §200)
5. `*hierbest-` — **unstressed i > e** (Hogg p.120, Campbell §369, R/T §6.9.6)
6. `hierfest` — spelling conventions, consonant changes

The crucial point: the medial `*i` does TWO things sequentially:
- First (at step 4) it **triggers i-umlaut** in the root syllable
- Later (at step 5) it **itself lowers to e** as an unstressed vowel

There is no contradiction here. The i-umlaut trigger and the unstressed
lowering are ordered chronologically: umlaut happens first, unstressed
merger happens later.

### Bammesberger (1997): What He Did and Didn't Address

Bammesberger's article focused on two issues:

1. **Refuting the `*harubist-` hypothesis**: He showed that Campbell's
   reconstruction `*haruvist-` (with medial `*u` for "double umlaut") cannot
   be correct, because (a) OHG and OFris show no trace of medial `*u`, and
   (b) ME `hervest` cannot derive from `*harubist-`. The correct PGmc is
   `*harbist-` with `*i`.

2. **Showing that WS `hærfest` is borrowed from Anglian**: The native WS
   development would give `*hierfest` or `*hyrfest`, but this is unattested.
   The forms `hærfest` and `herfest` found in WS texts are Anglian borrowings.

Bammesberger did NOT explicitly address how `*-ist-` becomes `-est-`. He
simply assumed it, writing derivations like "durch i-Umlaut entstand
*herbist > herfest" (§8, p.227) without explaining the medial vowel change.
This is presumably because Campbell §369 (which he cites extensively) makes
clear that unstressed `*i > e` is a general, productive change.

### The Campbell *haruvist- Hypothesis (Rejected)

For completeness, here is why Campbell's `*haruvist-` fails:

**Bammesberger (1997) §6 (p.226):**
> "Da lætemest... von der Silbenstruktur her den gleichen Bau wie *harubista-
> aufweist, im Altenglischen aber als lætemest erscheint, müßte man bei
> strikter Anwendung der Lautgesetze als Reflex von *harubist- > *hærybist-
> im Altenglischen **hærefest** erwarten."

If `*harubist-` were correct, we'd expect OE **hærefest** (with preserved
medial vowel reflex), not `hærfest`. The double-umlaut theory predicts the
wrong outcome.

**Bammesberger (1997) §7 (p.227):**
> "Ein gravierender Einwand gegen den Ansatz *harubist- als Vorform von ae.
> hærfest besteht darin, daß auf diesem Wege die me. Form hervest nicht
> unmittelbar erklärt werden kann."

ME `hervest` cannot derive from `*harubist-`, but easily derives from
`*harbist-`.

### WS hærfest as Anglian Borrowing

**Bammesberger (1997) §14 (p.230):**
> "Die den Lautregeln des Westsächsischen entsprechende Fortsetzung
> *hierfest, *hyrfest von urg. *harbist- (1.) ist nicht überliefert. Sowohl
> hærfest als auch herfest können jedoch auf der Basis von *harbist- im
> Rahmen der nichtwestsächsischen Phonologie als regelrecht erklärt werden.
> Im Westsächsischen darf man hærfest in die Gruppe von Lexemen einreihen,
> die als Übernahmen aus dem Anglischen gelten."

("The regular WS development *hierfest, *hyrfest from PGmc *harbist- is NOT
attested. Both hærfest and herfest can, however, be regularly explained from
*harbist- within non-WS phonology. In WS, we may classify hærfest among
the lexemes that count as borrowings from Anglian.")

This confirms: the FST producing `hierfist` is almost correct — it's just
missing the final step (unstressed `*i > *e`). Once that's added, it will
produce `hierfest`, the expected native WS form.

### Current FST Gap

The FST already has:
- `OEMedUnstressedULowering` (line 1454-1456): medial `*u → *o`
- `OEWeakTailReduction2` (line 1486): final `*i → *e`

**Missing:** A parallel rule for **medial** unstressed `*i → *e`.

The FST correctly handles final unstressed `*i`, but not medial unstressed
`*i`. This is why `*hierbist-` stays as `hierfist` instead of becoming
`hierfest`.

### Implementation Attempt #1: Simple Parallel Rule (FAILED)

Initial attempt: add `OEMedUnstressedILowering` parallel to the `*u` rule:

```foma
define OEMedUnstressedILowering [
    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ 
                    _ [EnglishStarConsonant | EnglishPalatalConsonant]
];
```

**Result:** This caused a regression on `begin`:
- `*biginnăną` → `beġennan` (wrong) instead of `beġinnan` (correct)

**Problem:** The rule lowered the ROOT vowel `*i` in `ginn-`, not just the
prefix vowel. The pattern V+C+_C matches both:
- `*harb-ist-` (correct: `-ist-` is unstressed)
- `*bi-ginn-` (wrong: `ginn-` is the stressed root)

### Implementation Attempt #2: Mark Unstressed Vowels First

The solution is to explicitly mark which `*i` vowels are unstressed BEFORE
applying the lowering rule. The FST already uses breve markers (e.g., `*ĭ`)
for reduced vowels in some contexts.

**Stress assignment logic:**

1. By default, the **first syllable** is stressed (Germanic stress rule)
2. Exception: if the word begins with a **known unstressed prefix**
   (`*bi-`, `*ga-`, `*fra-`, etc.), stress falls on the **second syllable**
3. All vowels NOT in the stressed syllable are unstressed

**Implementation plan:**

1. Add a rule `OEUnstressedIMarking` that converts `{*i}` → `{*ĭ}` in
   positions that are NOT stressed:
   - After the first syllable (in words without prefix)
   - After the second syllable (in words with unstressed prefix)
   - The first/second syllable `*i` remains unmarked (= stressed)

2. Modify `OEMedUnstressedILowering` to only target `{*ĭ}`:
   ```foma
   define OEMedUnstressedILowering [
       {*ĭ} -> {*e} || _ [EnglishStarConsonant | EnglishPalatalConsonant]
   ];
   ```

3. Order: `OEUnstressedIMarking` must come AFTER i-umlaut but BEFORE
   `OEMedUnstressedILowering`.

**Defining "first syllable" vs "second syllable":**

- First syllable: `.#.` to first vowel
- Second syllable: first vowel + C+ to second vowel
- For prefix words: `.#. {prefix} C* V` marks the stressed syllable

This requires careful FST engineering to identify syllable boundaries.

### Implementation Attempt #3: Three-Step Marking (SUCCESSFUL)

The final implementation uses three marking steps before the lowering rule:

```foma
# Step 1: Mark ALL *i after first vowel+consonants as unstressed (*ĭ)
define OEUnstressedIMarking1 [
    {*i} -> {*ĭ} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
];

# Step 2: Mark prefix *i in bi-/ni- words as unstressed
define OEUnstressedIMarking2 [
    {*i} -> {*ĭ} || .#. [{*b} | {*n}] _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic
];

# Step 3: RESTORE stressed root *ĭ back to *i after prefixes
define OEUnstressedIMarking3 [
    {*ĭ} -> {*i} || .#. [{*b} | {*n}] {*ĭ} [EnglishStarConsonant | EnglishPalatalConsonant]+ _ ,
    {*ĭ} -> {*i} || .#. {*g} {*a} [EnglishStarConsonant | EnglishPalatalConsonant]+ _ ,
    {*ĭ} -> {*i} || .#. {*f} {*r} {*a} [EnglishStarConsonant | EnglishPalatalConsonant]+ _
];

# CRITICAL: Step 2 must run BEFORE Step 1
# After Step 1 marks root *i as *ĭ, the *ĭ is NOT in EnglishStarVocalic,
# so Step 2's pattern won't match. Order: 2 → 1 → 3
define OEUnstressedIMarking OEUnstressedIMarking2 .o. OEUnstressedIMarking1 .o. OEUnstressedIMarking3;

# Step 4: Lower only marked unstressed *ĭ to *e
define OEMedUnstressedILowering [
    {*ĭ} -> {*e} || _ [EnglishStarConsonant | EnglishPalatalConsonant]
];
```

**Example traces:**

1. `*harbistuz` (harvest):
   - Input: `*h*a*r*b*i*s*t*u*z`
   - After Step 2: unchanged (no prefix)
   - After Step 1: `*h*a*r*b*ĭ*s*t*u*z` (medial *i marked)
   - After Step 3: unchanged (no prefix to restore)
   - After lowering: `*h*a*r*b*e*s*t*u*z` → `hierfest` ✓

2. `*biginnăną` (begin):
   - Input: `*b*i*ʤ*i*n*n*ă*n*ą` (after palatalization)
   - After Step 2: `*b*ĭ*ʤ*i*n*n...` (prefix *i marked)
   - After Step 1: `*b*ĭ*ʤ*ĭ*n*n...` (root *i also marked)
   - After Step 3: `*b*ĭ*ʤ*i*n*n...` (root *ĭ restored — stressed)
   - After lowering: prefix *ĭ → *e, root *i preserved → `beġinnan` ✓

**Results:**
- `*xarbistuz` → `hierfest` ✓ (fixed from `hierfist`)
- `*biginnăną` → `beġinnan` ✓ (no regression)
- Evaluation: 307/386 matches (79.5%)

### Implementation Hurdle: Word-Final *ĭ (Dill Regression)

After the initial implementation, evaluation showed a regression: `*deliz` (dill)
produced no output (`+?`) instead of `dile`. Tracing revealed the problem:

```
*deliz → ... → *d*i*l*ĭ (stuck)
```

The final `*ĭ` (from i-stem nom.sg. `-iz`) was not being converted to `*e` or 
cleaned up. The issue: `OEMedUnstressedILowering` only matched `*ĭ` before
consonants:

```foma
{*ĭ} -> {*e} || _ [EnglishStarConsonant | EnglishPalatalConsonant]
```

Word-final `*ĭ` has no following consonant, so it passed through unchanged and
blocked orthography (no mapping for `*ĭ`).

**Solution:** The existing `OEWeakTailReduction2` rule already handled word-final
`*i → *e`:

```foma
define OEWeakTailReduction2 [
    {*i} -> {*e} || _ .#.
];
```

This rule runs AFTER `OEUnstressedIMarking`, so we updated it to target `*ĭ`
instead of `*i`:

```foma
define OEWeakTailReduction2 [
    {*ĭ} -> {*e} || _ .#.
];
```

Now word-final unstressed `*ĭ` is correctly lowered to `*e`, while stressed
word-final `*i` (rare but possible) is preserved.

**Final Results:**
- `*deliz` → `dile` ✓
- `*xarbistuz` → `hierfest` ✓
- `*biginnăną` → `beġinnan` ✓
- Evaluation: 310/386 matches (80.3%) — net +1 from harvest fix

### Exceptions: When Medial *i is Preserved

**Hogg p.120** and **Campbell §371** specify that `*i` is preserved in:
- `-ig` (e.g., `mihtig` 'mighty')
- `-ing` (e.g., `cyning` 'king')
- `-isc` (e.g., `Englisc` 'English')
- `-iht` (e.g., `stæniht` 'stony')

These all involve following **palatal** consonants. The `-st-` cluster in
`*-ist-` is NOT palatal, so the lowering should apply.

### Sources

- Bammesberger, A. (1997). 'Die Vorform von altenglisch hærfest', *Anglia*
  115: 223-230.
- Campbell, A. (1959). *Old English Grammar*, §§114, 369-372.
- Hogg, R.M. (1992). *A Grammar of Old English* / *Cambridge History of the
  English Language* vol.1, pp.119-120.
- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*, p.210.
- Orel, V. (2003). *A Handbook of Germanic Etymology*, p.161.
- Ringe, D. & Taylor, A. (2014). *Linguistic History of English* vol.2,
  §6.9.6 (pp.332-335).

---

## OE findan 'to find': Verner's Law, NSL, and Paradigm-Cell Mapping

**Date:** 2026-03-11
**Status:** Under investigation; requires paradigm-cell solution

### The Problem

The TSV protoform `*finθăną` (after þ→θ normalization) causes the FST to produce
`fīþan` instead of the expected `findan`. The FST's Nasal Spirant Lengthening
(NSL) rule triggers on the `*nθ` cluster, lengthening the vowel and deleting the
nasal:

```
*finθăną → *fīθăn → fīþan (✗ wrong)
expected: findan (✓)
```

### Forschungsgeschichte: Comprehensive Literature Review

#### 1. Verner's Law: Discovery and Formulation

Karl Verner's 1877 paper explained the apparent exceptions to Grimm's Law by
showing that PIE voiceless stops became voiced fricatives in Germanic when the
immediately preceding syllable did not bear the PIE accent. This explains why
PIE `*pəter-` → Gmc `*faðer` (OE `fæder`) but PIE `*bhrāter-` → Gmc `*brōþer`
(OE `brōþor`).

**Hogg (1992)** (Cambridge History of English, vol.1, pp.40-42) provides a clear
formulation:

> "According to Verner's Law voiceless stops of Indo-European, which regularly
> yielded voiceless spirants in Germanic, became voiced if the accent in
> Indo-European was not on the immediately preceding syllable."

The PIE `*s` also underwent this change, yielding `*z` (later `*r` by rhotacism).

#### 2. Grammatischer Wechsel in Strong Verb Paradigms

The term "Grammatischer Wechsel" (grammatical alternation) was used by Jacob
Grimm and Adolf Holzmann (1870) to describe the consonant alternations within
strong verb paradigms resulting from Verner's Law.

**Fulk (2018) §12.17** provides the definitive modern statement:

> "It is usually assumed that voicing under Verner's law is to be expected only
> in the **preterite plural** and the **passive participle** of strong verbs, an
> expectation raised by the variable position of the accent in Sanskrit verbs."

This means for a Class III verb like `*finþan-`, the PGmc paradigm was:

| Form | Reconstructed | Stress | Consonant |
|------|---------------|--------|-----------|
| Infinitive | `*finþaną` | Root-stressed | Voiceless `*þ` |
| Present 1sg | `*finþō` | Root-stressed | Voiceless `*þ` |
| Present 3sg | `*finþiþi` | Root-stressed | Voiceless `*þ` |
| Preterite 1/3sg | `*fanþ` | Root-stressed | Voiceless `*þ` |
| **Preterite Plural** | `*funđunþ` | Suffix-stressed | **Voiced `*đ`** |
| **Past Participle** | `*funđanaz` | Suffix-stressed | **Voiced `*đ`** |

The voiced `*đ` in the pret. pl. and past ptp. reflects PIE suffix-accentuation:
in the perfect plural and participial forms, the accent was on the ending, not
the root, triggering Verner's Law voicing.

#### 3. Nasal Spirant Lengthening (NSL)

**Fulk (2018) §4.11** defines NSL precisely:

> "In North Sea Germanic a nasal consonant was lost before any voiceless
> fricative, with nasalization and compensatory lengthening of the preceding
> vowel. The change thus affects **mf, ns, nþ**..."

The affected clusters:
- `*mf` → `*f̃` (e.g., `*fimf` → `*fīf` → OE `fīf` 'five')
- `*ns` → `*s̃` (e.g., `*gans` → `*gōs` → OE `gōs` 'goose')
- `*nþ` → `*þ̃` (e.g., `*anþeraz` → `*ōþer` → OE `ōþer` 'other')

**R/T vol.2 §5.1.1** (pp.154-157) provides the crucial data for `*finþan`:

> "PGmc *finþan 'to find' (Goth. finþan, ON finna, OHG findan) > *fīþan > OS
> fīðan (beside findan **with voiced VL alternant levelled**, cf. OE findan, OF
> finda)"

#### 4. Evidence from the Daughter Languages

**Gothic:** `finþan` — Preserved the voiceless `*þ` throughout the paradigm
(Gothic eliminated Verner alternations by analogy, generalizing the voiceless).

**Old Norse:** `finna` — The `*þ` was assimilated to `*nn` after nasal (a
separate change, not NSL).

**Old Saxon:** BOTH forms attested:
- `fīðan` — NSL applied to `*finþan` → `*fīþan` → `fīðan`
- `findan` — The Verner's Law voiced alternant `*đ` (> `*d`) was generalized

**Old English:** ONLY `findan` — The voiced alternant won completely.

**Old Frisian:** `finda` — Same as OE, voiced alternant generalized.

**Old High German:** `findan` — Voiced alternant, but no NSL anyway (OHG is
not Ingvaeonic).

#### 5. Etymological Dictionary Reconstructions

**Kroonen (2013) p.142:**

> "*finþan- sv. 'to find; to feel' — Go. finþan sv. 'id.', ON finna sw. 'id.',
> **OE findan sw. 'id.'**, E to find, OFri. finda sv. 'id.', OS fīðan, findan
> sv. 'id.', ODu. findan sv. 'id.', Du. vinden sv. 'id.', OHG findan sv. 'id.',
> G finden sv. 'id.' > *pént-e- (IE)"

Kroonen lists OE as `findan` (with `d`), reflecting the levelled voiced form.
He also mentions related forms `*fanþjan-`, `*fandōn-`, `*fundōn-`.

**Orel (2003) p.99:**

> "*fenþanan str.vb.: Goth finþan 'to find out, to recognize, to learn', ON
> finna 'to find', OE findan id., OFris finda id., OS findan id., OHG findan
> id. A secondary verb derived from *pontHo-..."

Orel uses `*fenþanan` (with `*þ`), the original PIE-based form, but notes the
actual OE form has `d`.

#### 6. The Levelling Chronology

**Campbell (1959) §741** describes the OE Class III paradigm:

> "bindan, bind — band, bond — bundon — bunden
> Similarly many verbs, e.g. drincan drink, gelimpan happen, grindan grind,
> springan spring, climban climb... Findan find, has in W-S 1st and 3rd past
> sg. funde (replacing fand)."

Campbell notes the OE paradigm shows `d` throughout, with even the pret. sg.
showing `funde` (levelled from the plural) instead of expected `×fand`.

**Hogg (1992) p.108** discusses the phonological merger:

> "Old English spelling never shows these changes, so that we find in strong
> verbs alternations such as drīfan, drāf, drifon, drifen 'drive'... the third
> and fourth have [v,z] due to Verner's Law."

For `*finþan`, the original Verner alternation `*þ/*đ` has been completely
eliminated in OE by generalizing the voiced form.

**Fulk (2018) §12.17** confirms the pattern for Classes I-III:

> "The considerable preponderance of the evidence thus suggests that... the
> pattern in [Classes I-III] was... voicing in the preterite (sg. and pl.) and
> the pass. participle."

### Analysis: The Core Insight

The key insight from the user is: **rather than using the infinitive form
(where the voiced consonant was ANALOGICALLY introduced), we should use a
paradigm cell where the voiced consonant was REGULAR (lautgesetzlich).**

In PGmc, the voiced `*đ` was **regular** (not analogical) in:
- **Preterite plural:** `*funđunþ`
- **Past participle:** `*funđanaz`

If OE generalized the voiced alternant from these cells, and we want to model
the most *regular* pathway into OE, we should trace through one of these
cells — not the infinitive, which had the voiced form only by analogy.

### The Full PGmc Paradigm

| Cell | PGmc Form | Expected Consonant | Notes |
|------|-----------|-------------------|-------|
| Inf. | `*finþaną` | `*þ` (voiceless) | Root-stressed |
| Pres. 1sg | `*finþō` | `*þ` | Root-stressed |
| Pres. 2sg | `*finþizi` | `*þ` | Root-stressed |
| Pres. 3sg | `*finþiþi` | `*þ` | Root-stressed |
| Pres. pl. | `*finþanþi` | `*þ` | Root-stressed |
| Pret. 1/3sg | `*fanþ` | `*þ` | Root-stressed, o-grade |
| Pret. 2sg | `*funþiz` (WGmc) | `*þ` | WGmc adopted from pl. stem |
| **Pret. pl.** | `*funđunþ` | **`*đ`** | Suffix-stressed, Verner |
| **Past ptp.** | `*funđanaz` | **`*đ`** | Suffix-stressed, Verner |

### The Full OE Paradigm

| Cell | OE Form | Consonant | Source |
|------|---------|-----------|--------|
| Inf. | `findan` | `d` | **Levelled** from pret. pl./ptp. |
| Pres. 1sg | `finde` | `d` | Levelled |
| Pres. 2sg | `findest` | `d` | Levelled |
| Pres. 3sg | `findeþ` | `d` | Levelled |
| Pres. pl. | `findaþ` | `d` | Levelled |
| Pret. 1/3sg | `fand` ~ `funde` | `d` | Levelled (W-S even has `funde`) |
| **Pret. pl.** | `fundon` | `d` | **Regular** from `*funđunþ` |
| **Past ptp.** | `funden` | `d` | **Regular** from `*funđanaz` |

### Proposal: Use the Past Participle as the Protoform

**Rationale:** The past participle `*funđanaz` (or nominalized `*funđanaz`) has:

1. **Regular (lautgesetzlich) `*đ`** — not analogical
2. **No NSL** — the cluster is `*nđ` (voiced), not `*nþ` (voiceless)
3. **Regular sound changes into OE** — `*funđanaz` → `*fundanaz` → `funden`

If we use the past participle as the representative form, the FST will:
- Not trigger NSL (because `*đ` is voiced)
- Correctly derive OE `funden`

**Alternative: Use the Preterite Plural `*funđunþ`**

This also has regular `*đ`, and would derive `fundon` by regular sound change.

### Which Cell is Optimal?

For `*finþan`, both pret. pl. and past ptp. have regular `*đ`. But for FST
evaluation, we typically compare against the infinitive as target. This creates
a mismatch:

- Input: pret. pl. `*funđunþ` or past ptp. `*funđanaz`
- Expected output: `findan` (infinitive)

This won't work directly — we'd get `fundon` or `funden`, not `findan`.

### Revised Options

#### Option E: Use a Paradigm Cell with Regular `*đ` and Match to That Cell

Change the target in the TSV from `findan` (infinitive) to a form where the `d`
is inherited regularly:

| Protoform | Target | Regular? |
|-----------|--------|----------|
| `*funđunþ` | `fundon` (pret. pl.) | ✓ Regular |
| `*funđanaz` | `funden` (past ptp.) | ✓ Regular |

**Pros:**
- Fully lautgesetzlich — no analogy involved
- No FST changes needed
- Honest about what is regular vs. analogical

**Cons:**
- Changes the "cognate set" structure (not infinitive-to-infinitive)
- Requires TSV schema to allow paradigm-cell mappings

#### Option F: Use Pre-Levelled Proto `*findaną`

Use an intermediate proto-stage that reflects post-levelling, pre-OE:

- Input: `*findaną` (Pre-Ingvaeonic, with levelled `*d`)
- Output: `findan` (OE infinitive)

**Pros:**
- Infinitive-to-infinitive mapping preserved
- Reflects the actual input to OE sound changes
- Simple TSV fix

**Cons:**
- Not "true" PGmc — uses an intermediate reconstructed stage
- The `*d` in the infinitive is etymologically analogical

#### Option G: Acknowledge and Document

Keep the infinitive mapping but document that `findan` is not derivable by
regular sound change from `*finþaną`. Either:
1. Mark as "irregular/analogical" in the TSV
2. Use a separate column for "remarks" explaining the levelling

### Recommendation

**Option E (past participle mapping) is the most principled** for a
Neogrammarian FST that aims to model regular sound change. The past participle:

- Has regular `*đ` from Verner's Law
- Develops regularly to OE `funden`
- Avoids the NSL problem entirely

**For practical purposes**, Option F (pre-levelled `*findaną`) is acceptable
as it reflects the actual input form that OE inherited. This is analogous to
how we use PWGmc forms with j-gemination already applied.

### Similar Verbs to Check

Other Class III verbs with potential Verner alternations:

| Verb | PGmc Inf. | Expected VL in pret.pl./ptp. | OE |
|------|-----------|------------------------------|-----|
| bind | `*binþan-` | `*đ` | `bindan` (d generalized) |
| find | `*finþan-` | `*đ` | `findan` (d generalized) |
| grind | `*grinþan-` | `*đ` (?) | `grindan` |
| wind | `*winþan-` | `*đ` (?) | `windan` |

Also Class I verbs with `*s/*z` alternation (cf. Hogg's `drīfan` example):
- `*rīsaną` → OE `rīsan` (s) vs. `riron` (VL `*z` → `r`)
- `*kiusaną` → OE `cēosan` (s) vs. `curon` (VL `*z` → `r`)

### Current FST Implementation

The current `EnglishStarFricative` class is:
```foma
define EnglishStarFricative [{*f} | {*β} | {*s} | {*θ} | {*ð} | {*h} | {*x}];
```

And NSL is:
```foma
define OENasalSpirantLengthening [
    {*a} -> {*ō} || _ EnglishStarNasal EnglishStarFricative,
    {*e} -> {*ē} || _ EnglishStarNasal EnglishStarFricative,
    {*i} -> {*ī} || _ EnglishStarNasal EnglishStarFricative,
    ...
];
```

**Note:** The NSL rule is phonologically correct — `*nþ` DID trigger NSL in
Ingvaeonic. The problem is not the rule but the input form: the infinitive
`*finþaną` underwent Verner levelling before NSL applied.

### Action Items

1. ~~Research which paradigm cell gives the most regular OE outcome~~
2. ~~Determine if past participle `*funđanaz` → `funden` is viable~~
3. ~~Alternatively, use pre-levelled `*findaną` if infinitive mapping is required~~
4. Check other Class III verbs for similar issues

### Resolution (2026-03-11) — FULLY LAUTGESETZLICH

**Final solution:**

The derivation is now fully lautgesetzlich, using the true PGmc past participle
`*funðanăz` and deriving `funden` via proper sound change rules:

**Sound change 1: PWGmc dental hardening (`*ð → *d`)**

R/T vol.2 p.43: "In PWGmc the non-coronal voiced obstruents continued to
exhibit that allophony, but `*d` became a stop in all positions."

**Implementation:** Added `PWGmcDentalHardening` rule in `germanic.txt` (line ~1131):
```foma
define PWGmcDentalHardening [
    {*ð} -> {*d}
];
```
This is composed into `PWGmcChanges` after `PWGmcLThVoicing`.

**Sound change 2: Unstressed `*a → *æ → *e`**

Hogg (1992) p.120: "By First Fronting /a/ became /æ/ as in stressed syllables...
By the time of the earliest texts... the front vowels had merged together as /e/...
We are thus entitled to claim that by about 700 all unstressed front vowels
had become /e/."

The historical chain: `*-anăz → *-ænăz → -en`

**Implementation:** Added `OEUnstressedAFronting` rule in `germanic.txt` (line ~1558):
```foma
define OEUnstressedAFronting [
    {*a} -> {*æ} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ 
                    _ [EnglishStarConsonant | EnglishPalatalConsonant]
];
```

**Critical ordering:** This rule must run BEFORE `OEWeakTailReduction1` (which
converts `{*ă} → {*a}`). This preserves the distinction between:
- Original `*a` (true short a, no breve): fronted to `*æ`, then merged to `*e`
- Original `*ă` (weak/reduced, with breve): skips fronting, stays as `a`

Example contrast:
- `*funðanăz` → `funden`: the `-an-` has true `*a`, which fronts
- `*liznōjăną` → `leornian`: the `-ăn-` has `*ă`, which stays as `-ian`

The existing `OEWeakTailReduction3` (`*æ → *e` in non-initial syllables) then
completes the merger.

**Changes made:**

1. **TSV** (row 2011): Using true PGmc form `*funðanăz → funden`

2. **FST** (`PWGmcDentalHardening`): New rule for `*ð → *d`

3. **FST** (`OEUnstressedAFronting`): New rule for unstressed `*a → *æ`

4. **FST** (`pgrmCodaComplex`): Added `n:{*n} ð:{*ð}` cluster for input grammar

5. **FST** (`pgrmWeakTailVowel`): Added `a:{*a} n:{*n} ă:{*ă} z:{*z}` suffix

6. **FST** (`EnglishStarVoicelessFricative`): New class excluding `*ð`, `*β`
   to prevent spurious NSL before voiced fricatives

**Verification:**

Derivation trace for `*funðanăz → funden`:
```
WestGermanic:     *f*u*n*d*a*n*ă     (PWGmcDentalHardening: *ð → *d)
WeakTailReduction: *f*u*n*d*e*n      (OEUnstressedAFronting + Reduction3)
```

Mismatch count: 77 (improved from 78 before these changes)

### Verification: Other Class III Verbs with *d Are NOT Verner Cases

During implementation, a question arose: should other Class III verbs like `*bindăną`
and `*windăną` also be treated as Verner alternation cases?

**Research conclusion: NO.** These verbs have **original `*d`** from PIE aspirated
`*dh`, not from Verner's Law voicing of `*þ`.

**Evidence from Ringe/Taylor vol.2:**

1. **`*bindaną`** (p.157):
   > "PGmc *bindana 'to tie' (Goth. ga-bindan, ON binda) > PWGmc *bindan"
   
   R/T reconstructs `*bindana` with `*d` throughout. Fulk §3.6 confirms PIE
   `*bhendh-` (with aspirated `*dh`), which becomes PGmc `*d` directly.

2. **`*tredaną`** (p.78, 325):
   > "PGmc *trudaŋ 'to step on' (Goth. trudan, ON troða) > PWGmc *tredan"
   
   The `*d` is original, not from Verner levelling.

3. **`*knedaną`** (p.78):
   > "'to knead' are reflected in PWGmc *tredan and *knedan"

4. **`*waldaną`** (p.232):
   > "PGmc *waldaŋ 'to control, to rule'"

**Contrast with `*finþaną`:**

R/T (p.157) explicitly shows `*finþaną` as a Verner case:

> "PGmc *finþaŋ 'to find' (Goth. finþan, ON finna, OHG findan) > *fīþan > OS fīðan
> (beside findan **with voiced VL alternant levelled**, cf. OE findan, OF finda)"

The key difference:
- `*finþan-`: PIE `*pent-` has voiceless `*t` → Grimm `*þ` → Verner `*ð` (in some cells)
- `*bindan-`: PIE `*bhendh-` has aspirated `*dh` → PGmc `*d` (no alternation)

**Conclusion:** The current TSV protoforms `*bindăną`, `*windăną`, `*tredăną`, etc.
are **etymologically correct**. Only `*finþaną → findan` required the paradigm-cell
approach because it's a genuine Verner alternation case.

### Sources

- Bammesberger, A. (1992). "The place of English in Germanic and Indo-European"
  in Hogg (ed.) *Cambridge History of the English Language*, vol.1, pp.26-66.
- Campbell, A. (1959). *Old English Grammar*, §§390-392, 735-741.
- Fulk, R.D. (2018). *A Comparative Grammar of the Early Germanic Languages*,
  §§4.11, 6.6-6.7, 12.17.
- Grimm, J. (1848). *Geschichte der deutschen Sprache*.
- Hogg, R.M. (1992). *A Grammar of Old English* / *Cambridge History of the
  English Language* vol.1, pp.40-42, 107-108.
- Holzmann, A. (1870). *Altdeutsche Grammatik*.
- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*, p.142.
- Orel, V. (2003). *A Handbook of Germanic Etymology*, p.99.
- Ringe, D. & Taylor, A. (2014). *Linguistic History of English* vol.2,
  §5.1.1 (pp.154-157).
- Verner, K. (1877). "Eine Ausnahme der ersten Lautverschiebung" *Zeitschrift
  für vergleichende Sprachforschung* 23: 97-130.

### Further Research: Other Potential *ð Forms in TSV (2026-03-11)

**Question:** Is having only one `*ð` form (`*funðanăz → funden`) correct, or are we
missing other Verner þ/ð cases?

**Investigation methodology:**
1. Searched Campbell §398.2 for dental Verner paradigms
2. Cross-referenced Fulk §12.17 (Verner's Law in strong verbs)
3. Checked R/T vol.2 for Class I and III dental alternations
4. Audited current TSV forms with `*d` for potential Verner origins

**Key sources on dental Verner:**

Campbell §398.2 gives the canonical example list for all Verner alternations:
> "infs. and pass. parts. of OE drifan drive, céosan choose, snīþan cut, féon draw,
> séon see, would be `*dreifan-, *drivan-`; `*keusan-, *kozan-`; `*sneipan-, *snidan-`;
> `*teuxan-, *tozan-`; `*sexuan-, *sezuan-`"

Fulk §12.17 specifically discusses the dental case:
> "In Old English... the preterite plural consistently reflects a voiced fricative
> where Prokosch predicts a voiceless (cwǣdon 'said', wǣron 'were', gefǣgon 'rejoiced')...
> the passive participle reflects a voiced one, as predicted, in cweden 'said' and
> sewen, gesawen 'seen'."

**Current TSV status for dental Verner verbs:**

| Verb | PGmc (theoretical inf.) | OE inf. | OE outcome | Status in TSV |
|------|-------------------------|---------|------------|---------------|
| find | `*finþaną` | findan | leveled `d` | **FIXED**: using `*funðanăz → funden` |
| ride | `*rīþaną` | rīdan | leveled `d` | Present: `*rīdăną → rīdan` (leveled form) |
| say | `*kweþaną` | cweðan | leveled `ð` | **Not in TSV** |
| cut | `*snīþaną` | snīþan | no leveling | **Not in TSV** |

**Analysis:**

1. **`*rīdăną → rīdan`**: Current TSV uses the leveled form with `*d`. This is correct
   for our purposes — the FST derives `rīdan` correctly. The true PGmc infinitive
   would be `*rīþaną`, but OE generalized the Verner `d` throughout the paradigm.
   Since the infinitive IS the form we're targeting, using leveled `*rīdăną` is
   acceptable (analogous to Option F for findan).

2. **`cweðan, snīþan`**: These verbs are not in our TSV, so no action needed.

3. **`findan`**: This required special treatment because:
   - NSL applies to `*-nþ-` (voiceless) but NOT to `*-nð-` (voiced)
   - Using the infinitive `*finþaną` triggers spurious NSL → wrong output
   - Solution: use past participle `*funðanăz` where `*ð` is regular from Verner

**Conclusion:**

Having only one `*ð` form in the TSV (`*funðanăz`) is **correct**. The other dental
Verner verbs in the TSV (`rīdan`) work fine with their leveled protoforms because:

1. Leveling happened in PGmc/PWGmc, before OE sound changes
2. The leveled infinitive form IS what we're deriving
3. No problematic sound change (like NSL) makes the leveled form unworkable

The `findan` case was unique because NSL specifically targets voiceless `*þ` in
`*-nþ-` clusters. For `rīdan`, there's no `*n` before the dental, so no NSL issue.

### Clarification: PGmc *d vs *ð — Allophony vs Phonemic Contrast

**Question raised:** Did PGmc really distinguish `*d` and `*ð`? When we write `*d`,
is that AS OPPOSED TO `*ð`?

**Answer:** In PGmc, `*d` and `*ð` were **allophones** of the same phoneme, in
complementary distribution:

Campbell §398.3:
> "b, d existed only initially, and in the groups mb, nd... ð, v did not exist
> initially or after nasals"

Fulk (2018) p.28:
> "The characters b, d, g represent voiced stops initially and after nasal
> consonants (and in gemination), **otherwise voiced fricatives**"

So the distribution was:
- `[d]` (stop): initially, after nasals (`*nd`), in geminates
- `[ð]` (fricative): intervocalically, finally

**However**, the contrast that DOES matter is `*þ` (voiceless) vs `*ð` (voiced):

| Source | PGmc | Description |
|--------|------|-------------|
| PIE *t | *þ | Voiceless fricative (Grimm's Law) |
| PGmc *þ (Verner) | *ð | Voiced fricative (Verner's Law) |
| PIE *dh | *d | Voiced stop (direct) |

This `*þ/*ð` contrast is phonemically real in PGmc, even though `*d` and `*ð` are
allophonic. The voicing difference (*þ voiceless, *ð voiced) is what matters for NSL.

**Why this matters for NSL:**

NSL lengthens vowels before *nasal + voiceless fricative*. The rule targets:
- `*-nþ-` → lengthening (voiceless)
- `*-nf-` → lengthening (voiceless)
- `*-ns-` → lengthening (voiceless)

But NOT:
- `*-nð-` → no lengthening (voiced)
- `*-nd-` → no lengthening (stop, or from PIE *dh)

**Critical chronology:**

1. PGmc `*finþaną` (infinitive: *þ voiceless, from Grimm on PIE *t)
2. PGmc `*funðanaz` (past ptp: *ð voiced, from Verner on *þ)
3. **NSL applies**: `*finþaną → *fīnþaną` (lengthens before voiceless *þ)
   But `*funðanaz` unchanged (no lengthening before voiced *ð)
4. **PWGmc hardening**: `*ð → *d` everywhere (R/T vol.2 p.43)
   Result: `*fundanaz → funden`

So even though `*ð` after nasal would have been phonetically [d] in PGmc (allophonic),
the **voicing contrast with *þ** was still active when NSL applied. The contrast is:
- `*þ` = voiceless = triggers NSL
- `*ð` = voiced = does NOT trigger NSL

This is why we need `*funðanăz` in the TSV — to ensure the FST knows this is the
voiced Verner alternant that should NOT undergo NSL.

**Implication for TSV protoforms:**

When we write `*d` vs `*ð`, we are NOT claiming a phonemic contrast between these
sounds (they were allophones). Rather, we are marking:
- `*d`: either original PIE *dh, or the result of PWGmc hardening of *ð
- `*ð`: specifically the voiced Verner alternant, needed when NSL must be blocked

For most verbs, using `*d` is fine because:
1. If it's from PIE *dh, there was never a *þ/*ð alternation
2. If it's from leveled Verner, the leveling happened pre-OE

We only need explicit `*ð` when:
1. The verb has PIE *t → Grimm *þ → Verner *ð alternation
2. AND using the infinitive (*-nþ-) would trigger spurious NSL
3. AND we're using a paradigm cell where *ð was regular

Currently only `*funðanăz → funden` meets all three criteria.

### Systematic Check: TSV Forms with *nd Clusters (2026-03-11)

Reviewed all TSV entries with `*nd` clusters to confirm none require `*nð`:

| OE | Protoform | PIE Etymology | *d Source | Needs *ð? |
|----|-----------|---------------|-----------|-----------|
| bindan | *bindăną | *bhendh- "to bind" | original *dh | No |
| windan | *windăną | *wendh- "to turn" | original *dh | No |
| hund | *xundăz | *ku-ont- "dog" | original dental suffix | No |
| hand | *xanduz | *kont-? "hand" | original | No |
| grund | *grunduz | unknown | original | No |
| land | *landą | *lendh- "land" | original *dh | No |
| sendan | *sandjăną | causative of *sinþan- | Verner *d in causative | No (no *nþ cluster) |
| funden | *funðanăz | *pent- "to find" | **Verner *ð** | **Yes** ✓ |

**Key findings:**

1. **`bindan, windan`**: PIE roots `*bhendh-, *wendh-` with aspirated `*dh` → PGmc `*d`.
   No Grimm `*þ` ever existed. (Fulk §3.6; R/T vol.2 p.157)

2. **`hund`** (Kroonen p.256): PIE `*ku-ont-` "dog" with dental suffix. Not from `*t`.

3. **`sendan`**: Though derived from `*sinþan-` "to go" (with `*þ` from PIE `*t`), the
   causative `*sandjan-` already has the **voiced Verner alternant** built in. The
   cluster is `*-ndj-`, not `*-nþ-` or `*-nð-`, so NSL doesn't apply anyway.

4. **`findan → funden`**: The ONLY genuine Verner case with `*-nþ-/*-nð-` alternation
   where NSL matters. Fixed with `*funðanăz` using past participle.

**Conclusion:**

Having exactly one `*ð` form in the TSV (`*funðanăz`) is **correct and complete**.
All other `*nd` forms have original `*d` from PIE sources other than `*t`.

---

## The *d/*ð Representation Problem: A Systematic Analysis

### The Problem Statement

If we need `*ð` anywhere in our system (currently: `*funðanăz`), then at that point
we are claiming a phonemic distinction between `*d` and `*ð`. But the sources tell us
they were allophones in PGmc. This creates an inconsistency:

- If they're allophones, why mark `*ð` at all?
- If we mark `*ð` in one place, why not everywhere it's phonetically [ð]?
- If we mark `*d` everywhere, how does the FST know not to apply NSL?

The current solution (using `*ð` exactly once) is unsatisfactory because it's neither
consistent allophonic notation nor consistent phonemic notation.

### Background: The Three-Way Source Distinction

There are THREE distinct sources for dental obstruents in PGmc:

| Source | PGmc Result | Example | Notes |
|--------|-------------|---------|-------|
| PIE *t | *þ (voiceless fric.) | *finþaną "find" | Grimm's Law |
| PIE *t (Verner) | *ð (voiced fric.) | *funðanaz "found" | Verner's Law on *þ |
| PIE *dh | *d (voiced stop) | *bindaną "bind" | Direct, no alternation |

The `*þ` vs `*ð` contrast IS phonemic in PGmc — they contrast voicing.
The `*d` vs `*ð` contrast is allophonic — complementary distribution:

Campbell §398.3:
> "b, d existed only initially, and in the groups mb, nd... ð, v did not exist
> initially or after nasals"

So:
- `*ð` appears: intervocalically, finally
- `*d` appears: initially, after nasals (mb, nd)

### The Critical Question: What Is *-nð- Phonetically?

When Verner's Law creates `*ð` in a form like `*funðanaz`, what happens when this
`*ð` follows a nasal?

**Standard interpretation:** The `*ð` would surface as [d] after the nasal (allophonic).
So `*funðanaz` = phonetically [fundanaz].

**But:** NSL does NOT apply to this cluster, even though phonetically it's [nd].
Why? Because the UNDERLYING representation is `*-nð-` (voiced fricative), not
`*-nþ-` (voiceless fricative).

This means NSL is a PHONOLOGICAL rule applying to underlying forms, not a
PHONETIC rule applying to surface forms. It "sees" the voicing distinction in the
underlying representation even when it's neutralized phonetically.

### The Three Options

**Option 1: Mark allophonic variation in the TSV from the start**

Write `*ð` wherever the sound is phonetically [ð] (intervocalic, final), and `*d`
wherever it's phonetically [d] (initial, post-nasal, geminate).

Sub-options:
- **1a:** Distinguish Verner `*ð` from original `*d` with different symbols
  - Use `*ð` for Verner-derived voiced fricative
  - Use `*d` for PIE *dh-derived voiced stop
  - Add allophonic rule: `*ð → *d / n_` early in the derivation
  
- **1b:** Collapse the distinction in post-nasal position
  - Write `*fundanaz` (not `*funðanaz`) since [d] after nasal
  - But then how does NSL know not to apply?
  
**Analysis of Option 1:**

The problem with 1b is that we lose the information NSL needs. The sequence
`*-nd-` from PIE *dh (e.g., `*bindaną`) and `*-nd-` from Verner (e.g., `*fundanaz`)
look identical, but only the former should trigger NSL if we used the infinitive
`*finþaną`.

Option 1a requires introducing the allophonic rule `*ð → *d / n_` at the PGmc stage,
BEFORE NSL applies. This preserves the Verner information until NSL has had a
chance to (not) apply.

**Option 2: Add allophonic variation into the FST rules at a specific point**

Keep the underlying distinction (`*þ` vs `*ð` vs `*d`) in the input, and add rules
to derive the surface forms.

Sub-options:
- **2a:** Add `*ð → *d / n_` as a PGmc-level rule, applying AFTER NSL
  - Input: `*funðanăz`
  - NSL checks: sees `*nð` (voiced), does NOT apply
  - Then: `*ð → *d` gives surface `*fundanaz`
  
- **2b:** Merge post-nasal hardening with PWGmc dental hardening
  - Both rules produce `*d` from `*ð`, just at different stages
  - But: post-nasal hardening should be earlier (PGmc allophony)
  
**Analysis of Option 2:**

Option 2a is the cleanest: it keeps the underlying Verner distinction, lets NSL
"see" it, then applies allophonic hardening to derive the correct surface form.

The chronology would be:
1. Input: `*funðanăz` (with underlying Verner `*ð`)
2. NSL: checks for `*-nþ-`, finds `*-nð-`, does NOT apply
3. PGmc allophony: `*ð → *d / n_` → `*fundanaz`
4. PWGmc hardening: `*ð → *d` (catches any remaining `*ð`) → already done

Actually, step 3 and 4 could be merged since PWGmc hardening applies to ALL
`*ð` anyway. The ordering just needs to ensure NSL happens BEFORE the hardening.

**Option 3: Change the Verner output from *ð to *d directly**

Instead of reconstructing Verner as `*þ → *ð`, reconstruct it as `*þ → *d` (at least
post-nasally). This would mean:

- Input: `*fundanăz` (with Verner-derived `*d`, not `*ð`)
- But: need some way to mark this `*d` as "from Verner" to block NSL

Sub-options:
- **3a:** Use a diacritic: `*ḓ` or `*d̬` for "Verner d" (blocks NSL)
- **3b:** Use abstract features: mark certain forms as [+Verner]
- **3c:** Abandon the distinction — assume NSL applied before Verner

**Analysis of Option 3:**

Option 3c is historically implausible. The standard chronology is:
- Grimm's Law: PIE *t → PGmc *þ
- Verner's Law: PGmc *þ → *ð (in certain environments)
- NSL: Later, Ingvaeonic, affects *-nþ- but not *-nð-

Verner MUST precede NSL, otherwise NSL would apply to all *-nþ- regardless
of later Verner voicing.

Options 3a/3b are workarounds that obscure the actual historical phonology.
They replace a transparent phonological representation (`*ð`) with an arbitrary
diacritic or feature.

### Evidence from the Sources

**R/T vol.2 p.43:**
> "PGmc *z had always been a fricative in all positions, but the other voiced
> obstruents had both stop and fricative allophones... In PWGmc the non-coronal
> voiced obstruents continued to exhibit that allophony, but `*d` became a stop
> in all positions."

This confirms:
1. PGmc: `*d`/`*ð` were allophones with positional distribution
2. PWGmc: `*d` hardened to a stop everywhere (no more [ð] allophone)

**Campbell §398.3:**
> "ð, v did not exist initially or after nasals"

This confirms `*-nð-` → surface [nd] in PGmc (allophonic).

**Fulk §4.7 (North Sea Germanic / NSL):**
> "a nasal consonant was lost before any **voiceless** fricative... The change
> thus affects mf, ns, nþ"

This confirms NSL targets VOICELESS fricatives (`*þ`), not voiced (`*ð`).
The distinction must be available to the rule.

### Recommendation: Option 2a

The cleanest solution is:

1. **Keep `*ð` in the TSV** for Verner-derived voiced fricatives
   - This represents the underlying phonology correctly
   - It distinguishes Verner `*ð` from original PIE *dh → `*d`

2. **Add PGmc allophonic rule: `*ð → *d / n_`**
   - Applies AFTER NSL has had a chance to (not) apply
   - Can be merged with or ordered before PWGmcDentalHardening
   - Derives correct surface form [nd] from underlying /nð/

3. **Current ordering needs adjustment:**
   ```
   NSL applies (checks underlying /þ/ vs /ð/)
       ↓
   PGmc/PWGmc: *ð → *d (allophonic + hardening)
       ↓
   Later OE rules
   ```

**Implementation:**

Currently we have `PWGmcDentalHardening` which converts `*ð → *d` at the PWGmc
stage. This is already AFTER NSL in the rule ordering (NSL is in `OEChanges`).

But wait — NSL is currently in `OEChanges`, which runs AFTER `PWGmcChanges`.
This means by the time NSL applies, `*ð` has already become `*d`!

Let me check the actual rule ordering...

### Current FST Rule Ordering (germanic.txt)

```foma
define PWGmcChanges [PWGmcMutations ... .o. PWGmcDentalHardening ...];
define OEChanges [... .o. OENasalSpirantLengthening ...];
```

If PWGmcDentalHardening runs BEFORE OENasalSpirantLengthening, then by the
time NSL checks, `*funðanăz` has already become `*fundanaz`, and NSL sees `*nd`
(stop), not `*nþ` (voiceless fricative), so it correctly does NOT apply.

BUT: if someone inputs `*finþaną` (infinitive with voiceless `*þ`), NSL would
also see this AFTER hardening... wait, `*þ` doesn't get hardened by DentalHardening
(that only affects `*ð`). So `*finþaną` keeps its `*þ` and NSL applies to it.

Actually, this is correct! The current system works because:
- `*funðanăz`: `*ð` → `*d` (hardening), then NSL sees `*nd` (no lengthening)
- `*finþaną`: `*þ` unchanged, then NSL sees `*nþ` (lengthening applies)

So the issue is NOT the rule ordering — it's the **notation consistency**.

### Revised Analysis

The current system IS phonologically correct:
- `*ð` in input represents underlying voiced Verner fricative
- `PWGmcDentalHardening` converts it to `*d` (surface/PWGmc)
- NSL then sees `*nd` and does not apply

The objection is **notational**: if `*d` and `*ð` are allophones, why use different
symbols? The answer is that they ARE different underlying segments:

| Underlying | Source | PWGmc Surface | Distinct from? |
|------------|--------|---------------|----------------|
| `*d` | PIE *dh | `*d` | Never was a fricative |
| `*ð` | Verner on *þ | `*d` | Was a fricative, hardened |
| `*þ` | Grimm on *t | `*þ` | Voiceless, triggers NSL |

The distinction `*d` (original stop) vs `*ð` (Verner fricative) is lost by PWGmc,
but it's real at the PGmc stage and could in principle matter for some rules.

However, in our FST, we're inputting **PGmc forms** and deriving **OE forms**.
The PGmc input should reflect PGmc phonology, which DOES distinguish:
- `*þ` (voiceless fricative, from Grimm)
- `*ð` (voiced fricative, from Verner)
- `*d` (voiced stop, from PIE *dh, only initial/post-nasal)

The fact that `*ð` surfaces as [d] after nasals is an allophonic rule, but the
underlying representation is still `*ð`.

### Final Recommendation

**Option 2a is already implemented.** The current system is correct:

1. Input `*funðanăz` with underlying Verner `*ð`
2. `PWGmcDentalHardening` converts `*ð → *d` (for all `*ð`, including post-nasal)
3. NSL sees `*nd` (not `*nþ`) and does not apply

The "one `*ð` in the TSV" situation is NOT inconsistent because:
- We use `*ð` for the ONE form where we need to represent Verner voicing
- Other forms with `*d` have ORIGINAL `*d` from PIE *dh (never was `*ð`)
- We're not failing to mark `*ð` elsewhere; there IS no `*ð` elsewhere in our data

**However:** If we had more Verner forms in the TSV (e.g., `*cweðaną`, `*snīðaną`),
we WOULD need to mark them with `*ð` to block NSL if they had `*-nþ-/*-nð-`
alternations. The fact that we only have ONE such form is a function of our
data selection, not a flaw in the notation system.

### What Would Need to Change for Consistency

If we wanted to be MORE explicit about the allophony, we could:

1. **Add explicit post-nasal hardening as a separate rule:**
   ```foma
   define PGmcPostNasalHardening [
       {*ð} -> {*d} || {*n} _,
       {*β} -> {*b} || {*m} _
   ];
   ```
   This would apply at the PGmc stage, making the allophony explicit.

2. **Order it before or with PWGmcDentalHardening:**
   The output would be the same, but the rule would document the PGmc allophony.

3. **Leave PWGmcDentalHardening to handle only intervocalic/final `*ð`:**
   ```foma
   define PWGmcDentalHardening [
       {*ð} -> {*d}  # applies to any remaining *ð
   ];
   ```

This is more explicit but produces the same output. The current system works
correctly; this would just make the phonological reasoning more transparent.

---

### DECISION (2026-03-11): Option 2a Confirmed

**After systematic analysis, we confirm the current approach is correct.**

The representation scheme is:
- `*þ` = voiceless fricative (Grimm's Law on PIE *t)
- `*ð` = voiced fricative (Verner's Law on *þ)
- `*d` = voiced stop (PIE *dh, or surface form after hardening)

The FST implements this via:
1. Input forms use `*ð` for Verner-derived voiced fricatives
2. `PWGmcDentalHardening` converts `*ð → *d` (runs early in pipeline)
3. `OENasalSpirantLengthening` runs later, sees the result

This correctly handles:
- `*funðanăz`: hardening → `*fundanăz` → NSL sees `*nd` → no lengthening ✓
- `*finþaną`: unchanged → NSL sees `*nþ` → lengthening applies ✓

**Why only one `*ð` in the TSV is correct:**
- Other `*nd` forms (bindan, windan, hund, etc.) have ORIGINAL `*d` from PIE `*dh`
- They were never `*þ` or `*ð` at any stage — no Verner alternation
- Only `*finþaną/*funðanaz` is a genuine Verner case requiring the distinction

**No changes needed.** The current system is phonologically sound and correctly
models the PGmc → OE derivation.

### Sources Consulted

- Campbell, A. (1959). *Old English Grammar*, §398.3 (pp.163-165)
- Fulk, R.D. (2018). *A Comparative Grammar of the Early Germanic Languages*,
  §§4.7, 6.5-6.7
- Ringe, D. & Taylor, A. (2014). *Linguistic History of English* vol.2, p.43
- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*

---

## TSV Error: *funxwstiz → should be *funxstiz (cognate 501, fȳst)

**Date:** 2026-03-11  
**Status:** ✅ FIXED — TSV corrected, `nxst` cluster added (commit 9ac6ed9)

### The Problem

Row 2015 in the TSV contains:
```
PROTOFORM: *funxwstiz
COUNTERPART: fȳst
```

The FST produces no output (`+?`) because the cluster `*nxwst` is not in the
grammar (specifically not in `pgrmCodaComplex`).

### Source Analysis

**Kroonen (2013, p.148)** reconstructs:
> **\*funhsti-** f. 'fist' < IE \*pn̥ksti- < \*penkʷ- 'five'

This translates to our notation as **`*funxstiz`** (with `*x` for Kroonen's `*h`).
There is NO labiovelar `*w` in Kroonen's reconstruction.

**Wiktionary** (source of our TSV automation, commit eda0845, Dec 2025) gives:
> PGmc \*funstiz (with NO fricative at all!)

This is a simplification — Kroonen's reconstruction `*funhsti-` clearly shows
the `*h` (= `*x`), reflecting the PIE velar in `*penkʷ-` → `*pn̥ksti-`.

**The erroneous `*w`:**  
The TSV form `*funxwstiz` appears to be a conflation of two things:
1. The correct cluster `*nx` (from PIE `*nk`)
2. A spurious `*w` perhaps from confusion with the PIE labiovelar `*kʷ`

However, the PIE labiovelar `*kʷ` in `*penkʷe` 'five' loses its labialization
in the zero-grade `*pn̥ksti-` before the `*s`. The daughter form is `*funhsti-`,
not `×*funhwsti-`.

### Origin of the Error

The form `*funxwstiz` appears in the TSV from the very first commit that added
OE cognates (eda0845, "Add Old English automation for Germanic TSV", Dec 2025).
It was part of the automated Wiktionary scraping. The exact source of the
spurious `*w` is unclear — it may have been:
- A typo in one of the Wiktionary reconstruction pages
- An error in the scraping/normalization script
- A mistaken back-formation from the PIE labiovelar

### The Fix (TSV correction)

Change row 2015:
- FROM: `*funxwstiz`
- TO: `*funxstiz`

The cluster `nxst` was NOT in `pgrmCodaComplex` — added in commit 9ac6ed9.

**Status (2026-03-12):** TSV corrected, cluster added, but derivation produces
`fyxt` instead of expected `fȳst`. See next section for diagnosis.

---

## NSL Chronology Bug: *funxstiz → fyxt instead of fȳst

**Date:** 2026-03-12  
**Status:** ✅ FIXED — NSL moved to NWGmc stage (commit 8b2ca1d)

### The Problem

After correcting the TSV from `*funxwstiz` to `*funxstiz` and adding the `nxst`
cluster to the grammar, the FST now produces output — but the wrong output:

```
*funxstiz → fyxt (actual)
*funxstiz → fȳst (expected)
```

Issues observed:
1. The `*n` should be lost (NSL) but survives
2. The vowel should lengthen (NSL) but doesn't
3. The `*x` survives instead of being lost with compensatory lengthening

### Pipeline Trace

Tracing through the pipeline stages:

| Stage | Form | Notes |
|-------|------|-------|
| proto_input | `*f*u*n*x*s*t*i*z` | ✓ Parsed correctly |
| After i-umlaut | `*f*y*n*x*s*t*i` | ✓ i-umlaut applied |
| After NSL lengthening | `*f*y*n*x*s*t*i` | ✗ NO CHANGE! |
| After NSL loss | `*f*y*n*x*s*t*i` | ✗ Nasal not lost |
| Final | `fyxt` | Wrong: should be `fȳst` |

### Root Cause: NSL Rule Missing `*y`

The NSL lengthening rule (`OENasalSpirantLengthening`) only handles these vowels:

```foma
{*a} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
{*e} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
{*i} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
{*o} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
{*u} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative,
{*æ} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative
```

**The rule doesn't handle `*y`!**

When `*funxstiz` undergoes i-umlaut, `*u → *y`. Then when NSL tries to apply,
it looks for `*u` but finds `*y`, so no lengthening occurs.

### The Deeper Issue: Chronological Ordering

The real problem is **chronological ordering**. Looking at R/T vol.2 §5.1.1:

> "The most obvious phonological innovation of the **northern dialects** is the
> loss of nasals immediately preceding fricatives, with lengthening and
> nasalization of the preceding vowel."

NSL was a **NWGmc** change (shared by OE, OF, OS) — it operated BEFORE the
Proto-OE stage where i-umlaut applies.

**Historical ordering (correct):**
1. NWGmc NSL: `*funxstiz` → `*fūxstiz` or `*fūstiz` (nasal loss + vowel lengthening)
2. OE i-umlaut: `*fūsti-` → `*fȳsti-` (long `*ū` → long `*ȳ`)
3. OE shortening: `*fȳst` (long vowel shortens before cluster? — but OE preserves `fȳst`)

**Our pipeline ordering (current, WRONG):**
1. OE i-umlaut: `*funxstiz` → `*fynxstiz` (before NSL!)
2. OE NSL: no match (rule expects `*u`, sees `*y`)
3. Result: `*fynxst` → `fyxt` (wrong)

### Evidence from R/T

R/T vol.2 gives the PWGmc form directly:
> PWGmc `*fūsti` 'fist' (OF fest, OS, OHG fūst) > OE fyst

This confirms that NSL had already applied by the PWGmc stage, producing `*fūsti-`
with the long vowel. R/T lists this under i-umlaut examples (p.224, 287), showing
that `*fūsti-` → `fyst` involves i-umlaut of `*ū` → `*y` (written `y` = /y:/ → /y/).

### Other Evidence: German and Dutch

The cognates support the long-vowel reconstruction:
- OHG `fūst` → NHG `Faust` (long vowel preserved)
- OS `fūst` (long vowel)
- Dutch `vuist` (long vowel from `*ū`)
- OE `fȳst` (should have long vowel `ȳ`)

### Proposed Fix: Move NSL Earlier in Pipeline

**Option A: Move NSL to NWGmc stage (before i-umlaut)**

Move `OENasalSpirantLengthening` and `OENasalSpirantLoss` from the OE section
to the NWGmc section of the pipeline, specifically BEFORE `OEIUmlaut`.

This would require:
1. Renaming the rules to `NWGmcNasalSpirantLengthening` / `NWGmcNasalSpirantLoss`
2. Moving them before `OEIUmlaut` in `EnglishProtoToOE`
3. Testing for regressions on other NSL forms

**Option B: Add `*y` to NSL rules**

Keep NSL in its current position but add:
```foma
{*y} -> {*ȳ} || _ EnglishStarNasal EnglishStarVoicelessFricative
```

This is a **patch**, not a proper fix. It would work for this case but doesn't
reflect the correct historical phonology. It also might create problems for
forms where i-umlaut should NOT feed NSL.

**Recommendation: Option A**

The correct fix is to move NSL earlier in the pipeline. This reflects the
actual historical chronology (NWGmc NSL → OE i-umlaut) and should work for
all affected forms without needing to patch individual vowel rules.

### Known NSL Forms to Test After Fix

From R/T §5.1.1, examples of NSL that should work:
- `*gansiz` → `gēs` 'geese' ✓ (currently works — no i-umlaut involved)
- `*tanþ-` → `tōþ` 'tooth' ✓ (currently works)
- `*funxstiz` → `fȳst` 'fist' ✗ (currently `fyxt`)
- `*munþaz` → `mūþ` 'mouth' (should check)
- `*anstiz` → `ēst` 'favor' (should check)

### Expected Derivation After Fix

```
*funxstiz
  → NWGmc *fū̃xstiz (NSL: vowel lengthening + nasalization)
  → NWGmc *fūstiz (nasal loss before fricative, x-loss in cluster)
  → PWGmc *fūsti- (final *-z loss)
  → OE *fȳst (i-umlaut: *ū → *ȳ)
  → OE fȳst ✓
```

### Implementation (2026-03-12)

The fix was implemented in commit 8b2ca1d:

1. **Renamed rules**: `OENasalSpirantLengthening` → `NWGmcNasalSpirantLengthening`,
   `OENasalSpirantLoss` → `NWGmcNasalSpirantLoss`

2. **Moved rules** in the pipeline from the OE section to the NWGmc section,
   placing them after `NWGmcLongENasalRounding` and before `OEAuFronting`:
   ```
   .o. NWGmcLongENasalRounding
   .o. NWGmcNasalSpirantLengthening  # Moved here from later in pipeline
   .o. NWGmcNasalSpirantLoss         # Moved here from later in pipeline
   .o. NWGmcPreconsonantalXLoss      # Added in same commit
   .o. OEAuFronting
   ```

**Result after NSL fix:** `*funxstiz` → `fȳxt` (vowel now long, but `*x` survives)

The remaining `*x` was fixed by the preconsonantal x-loss rule (see next section).

### Sources Consulted

- R/T vol.2 §5.1.1 (pp.140-142): "Loss of nasals immediately preceding fricatives"
- R/T vol.2 p.224, 287: `PWGmc *fūsti` → OE `fyst`
- Kaluza, *Historische Grammatik der englischen Sprache* §70-71:
  `fȳst Faust (*funhsti-)` — shows the expected derivation
- Kroonen (2013) p.148: `*funhsti-` 'fist'

---

## Preconsonantal *x Loss: *xs > *s before Consonant Clusters

**Date:** 2026-03-13  
**Status:** ✅ FIXED — `NWGmcPreconsonantalXLoss` implemented (commit 8b2ca1d)

### The Problem

After fixing NSL chronology (moving it before i-umlaut), the derivation of
`*funxstiz` now produces `fȳxt` instead of expected `fȳst`:

```
*funxstiz → fȳxt (current, after NSL fix)
*funxstiz → fȳst (expected)
```

The vowel is now correctly long (`ȳ`), and the nasal is correctly lost. But the
`*x` survives when it should be lost in the cluster `*xst`.

### Historical Background

The loss of `*x` (written `*h` in most handbooks) before consonant clusters is
a well-documented NWGmc/OE change, though its exact conditioning has been
debated.

**Campbell §417 (p.173):**
> "When a consonant follows, xs > s in OE, e.g. *wastm* fruit, *-wæsma* growth
> (both related to *weaxan*), North. *sesta* sixth, beside W-S, Ru. *syxta*...
> but *wrixlan* exchange (from *gewrixl*, where *l* is vocalic), *pixl* axle
> beside *pisl*..."

Campbell's examples:
| Proto form | OE outcome | Notes |
|------------|------------|-------|
| `*wahstmaz` | `wæstm` | 'fruit, growth' (x lost before -stm) |
| `*sehstoþ-` | North. `sesta` | 'sixth' (x lost before -st) |
| `*pihsla-` | `pixl ~ pisl` | 'axle' (variable: x kept or lost) |
| `*niuhsijan` | `néosan` | 'to visit' (x lost before -s-) |

Campbell notes this change "is found in all West Gmc. languages, and in North
Gmc., e.g. ON *ίsl* 'axle'; OS *wueslon* 'exchange', *wuastum* 'fruit'".

**R/T vol.2 pp.156-158 (§5.2.3):**
> "We might account for the variation in *pixl* ~ *pisl* by suggesting that `*h`
> was lost only when the cluster was word-final; but that makes it impossible
> to account for *sesta* and *néosan*—and note further that *eaxl* 'shoulder'
> < `*ahslu` is another counterexample. The best we can do is to conclude that
> **`*h` was lost, possibly variably, possibly only in some dialects, when
> followed by two or more consonants** at a time before breaking occurred in OE."

R/T's examples from pp.156-158:
| Proto form | OE outcome | Notes |
|------------|------------|-------|
| `*niuhsijan` | `néosan` | 'to visit, seek out' |
| `*sehsto-` | North. `sesta` | 'sixth' (W-S `siexta` by analogy) |
| `*pihslu-` | `pixl ~ pisl` | variable, both attested |
| `*wahstma-` | `westm` | 'growth, fruit' (also OS `wastum`) |

**Kaluza §70:**
Gives the derivation directly: `fȳst Faust (aus *fūsti- für *fuhsti-, *funhsti-)`

This shows the intermediate form `*fūsti-` with `*x` already lost before the
cluster `-st-`.

### The Rule

The change is: `*x` → ∅ / _ CC (before two or more consonants)

This must have occurred:
1. After NSL (which produces `*fū̃xstiz` → `*fūxstiz`)
2. Before i-umlaut (which sees `*fūstiz` and produces `*fȳst`)
3. Before OE breaking (R/T: "before breaking occurred in OE")

The change is a **NWGmc** development (shared with OS), not purely OE.

### Variability

R/T and Campbell both note the change was **variable**:
- `pixl ~ pisl` both attested in OE
- `eaxl` 'shoulder' < `*ahslu` shows preserved `*x`

However, for `*funxstiz` → `fȳst`, the attested OE form has NO `*x`, so
our FST should apply the rule.

### Pipeline Placement

The rule should be placed:
1. After `NWGmcNasalSpirantLoss` (NSL needs to operate first)
2. Before `OEBreaking` (R/T: change occurred before breaking)
3. Before `OEIUmlaut` (Kaluza shows `*fūsti-` as the pre-umlaut form)

Proposed position in `EnglishProtoToOE`:
```
.o. NWGmcNasalSpirantLengthening
.o. NWGmcNasalSpirantLoss
.o. NWGmcPreconsonantalXLoss  # NEW
.o. OEAuFronting
...
```

### Expected Derivation After Fix

```
*funxstiz
  → *fū̃xstiz (NSL lengthening: *u → *ū̃ before *nx)
  → *fūxstiz (NSL loss: *n → ∅ before *x)
  → *fūstiz  (x-loss: *x → ∅ before CC cluster)
  → *fūsti-  (final *-z loss)
  → *fȳst    (i-umlaut: *ū → *ȳ)
  → fȳst ✓
```

### Forms to Test After Implementation

| Proto | Expected | Current | Issue |
|-------|----------|---------|-------|
| `*funxstiz` | `fȳst` | `fȳxt` | x not lost |
| `*wahstmaz` | `wæstm` | (check) | x should be lost |
| `*sehstoþ-` | `sesta` | (check) | x should be lost |

### Implementation (2026-03-13)

The rule `NWGmcPreconsonantalXLoss` was implemented in commit 8b2ca1d:

```foma
define NWGmcPreconsonantalXLoss [
  {*x} -> 0 || _ EnglishPhoneme EnglishPhoneme
];
```

The rule deletes `*x` when followed by two consonant phonemes. Placed in the
NWGmc section after NSL and before `OEAuFronting`.

**Result:**
```
*funxstiz → fȳst ✓
```

Full derivation trace:
1. `*funxstiz` (input)
2. `*fūxstiz` (NSL lengthening: `*u` → `*ū` before `*nx`)
3. `*fūxstiz` (NSL loss: `*n` → ∅ before fricative)
4. `*fūstiz` (x-loss: `*x` → ∅ before `-st-`)
5. `*fȳst` (i-umlaut: `*ū` → `*ȳ`)
6. `fȳst` (orthography)

Mismatch count reduced from 78 to 77.

### Sources

- Campbell, A. (1959). *Old English Grammar*, §417 (p.173): `*xs > s` before C
- R/T vol.2 pp.156-158: Variable `*h` loss before CC clusters
- Kaluza, M. *Historische Grammatik* §70: `*funhsti- → *fūsti- → fȳst`
- Luick, K. *Historische Grammatik* §250: Compensatory lengthening contexts

---

## Grammar Inconsistency: θ vs þ in Input Notation

**Date:** 2026-03-13  
**Status:** Under investigation

### The Problem

Five forms produce no output (`+?`) in the mismatch report:

| Proto (TSV) | Expected OE | Issue |
|-------------|-------------|-------|
| `*libēθi` | `lifeþ` | Uses θ (Greek theta) |
| `*regna-bugô` | `reġnboga` | Compound with hyphen |
| `*sturtijăną` | `styrtan` | Unknown |
| `*wira-aldiz` | `weorold` | Compound with hyphen |
| `*wurmaz/wurmiz` | `wyrm` | Slash for alternants |

### Root Cause: θ/þ Inconsistency

The grammar (`pgrmWord`) uses TWO different characters for the dental fricative:
- **θ (Greek theta, U+03B8)**: Used in 12 input patterns
- **þ (Latin thorn, U+00FE)**: Used in only 2 input patterns

These map to DIFFERENT internal symbols:
- `θ:{*θ}` → internal `{*θ}`
- `þ:{*þ}` → internal `{*þ}`

The sound change rules (e.g., `EnglishStarVoicelessFricative`) use `{*θ}`, NOT `{*þ}`.

**Critical mismatch for `*libēθi`:**
- TSV row 2107 has: `*libēθi` (theta)
- Grammar line 344 has: `ē:{*ē} þ:{*þ} i:{*i}` (thorn!)
- Result: The input `ēθi` doesn't match the pattern `ēþi`, so no parse

### Investigation: Which Character Should We Use?

**Option A: Standardize on θ (theta)**
- Pro: Already used in 12/14 input patterns
- Pro: Already used in all phoneme class definitions (`EnglishStarFricative`, etc.)
- Con: Need to change 2 grammar lines (80, 344)
- Con: Confusing since OE uses þ orthographically

**Option B: Standardize on þ (thorn)**
- Pro: Matches OE orthographic convention
- Pro: More intuitive for Germanic linguists
- Con: Need to change 12 grammar lines + all phoneme classes
- Con: More invasive change

**Option C: Accept both (normalization)**
- Add a rule that converts `þ` → `θ` at input
- Pro: TSV can use either character
- Con: Adds complexity to the grammar

### Recommendation

**Option A** seems most practical — the grammar already predominantly uses θ internally.
The two lines using þ (lines 80, 344) appear to be oversights.

### Other `no_output` Issues

1. **Compounds with hyphen** (`*regna-bugô`, `*wira-aldiz`): Grammar doesn't parse hyphens
2. **Alternants with slash** (`*wurmaz/wurmiz`): Grammar doesn't parse slashes
3. **`*sturtijăną`**: Needs investigation (possibly `ij` cluster or `rti` sequence)

These are TSV format issues, not phonological problems.

### Sources

- Unicode Standard: θ = U+03B8 (Greek Small Letter Theta)
- Unicode Standard: þ = U+00FE (Latin Small Letter Thorn)

### Implementation (2026-03-13)

**Fix applied:** Standardized on θ (U+03B8) for dental fricative throughout:

1. **Line 80** (`pgrmInitSimple`): Removed `þ:{*þ}` — θ already in line 83
2. **Line 344** (`pgrmWeakTailVowel`): Changed `þ` → `θ` for 3sg pattern
3. **Line 433** (`PGmcStarPhoneme`): Removed `{*þ}` from phoneme inventory
4. **Lines 601, 2448**: Removed `{*þ} -> þ` from orthography rules

**Result:**
- `*libēθi` → `lifeþ` ✓ (was `+?`)
- Mismatch count: 77 → 76

**Remaining `no_output` forms (4):**
These are TSV notation issues, not phonology bugs:

| Form | Issue | Fix needed |
|------|-------|------------|
| `*regna-bugô` | Hyphen in compound | Remove hyphen or handle compounds |
| `*wira-aldiz` | Hyphen in compound | Remove hyphen or handle compounds |
| `*sturtijăną` | `ij` cluster not in grammar | TSV: `*sturtjăną` |
| `*wurmaz/wurmiz` | Slash for alternants | TSV: pick one form |

These require TSV edits, not grammar changes.

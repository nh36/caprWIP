# Investigation: Four Complex TSV Items

## Overview

Four TSV items remain in the "complex TSV fix" category. Each has problems with
the proto-form, the OE target, or both, and each would require pipeline changes
to resolve fully. This document analyzes each item in detail.

Current pipeline results:
| Proto | Pipeline output | TSV target | Status |
|-------|----------------|------------|--------|
| `*xlaxjăną` | hliehan | hlæhhan | Mismatch |
| `*skellinăz` | sċiellen | sċilling | Mismatch |
| `*furxtīn` | fyrhten | fryhtu | Mismatch |
| `*taixwō` | tāhw | tā | Mismatch |

---

## 1. *xlaxjăną → hlæhhan "laugh" (ID 2092)

### Proto-form assessment

The TSV has `*xlaxjăną`. Kroonen (p. 228, line 14373) gives **\*hlah(j)an-** s.v.
'to laugh', noting the suffix alternation between ON hlæja < \*hlahjan- and OS
hlahan < \*hlahan-. R/T consistently reconstruct **\*hlahjana**.

The TSV encoding `*xlaxjăną` uses `x` for the velar fricative and `j` for the
glide — this is the correct encoding for our pipeline's alphabet (where `x` maps
to `{*x}` and `h` maps to `{*h}`).

**Proto form is approximately correct** — *xlaxjăną represents *hlahjanan.

### OE target assessment

The TSV has `hlæhhan`. R/T give the WS form as **hliehhan** (lines 3674, 10264,
13896, 19594) and the Anglian poetic form as **hlehhan** (line 13897). The form
`hlæhhan` is not specifically given by R/T.

R/T's derivation (line 10264):
> PGmc \*hlahjana > PWGmc \*hlahh'an > \*hlehh'an > \*hleahh'an > OE hliehhan

The stages are:
1. **WGmc j-gemination**: \*hlahjan → \*hlahhjan (x+j → xx, gemination)
2. **Anglo-Frisian brightening**: \*a → \*æ before hh
3. **Breaking**: \*æhh → \*eahh
4. **i-Umlaut**: \*eahh → \*ieahh → hiehh (WS palatal diphthong umlaut)

The form `hlæhhan` represents stage 2 only (brightening without breaking or
umlaut). It's not attested as a standard OE form in R/T. The TSV note says
"R/T: PGmc *hlahjanan > OE hlæhhan/hliehhan" — this appears to be inaccurate;
R/T do NOT give hlæhhan as a standard form.

**TSV target should be `hliehhan`** (WS) or `hlehhan` (Anglian).

### Pipeline issues (2 independent problems)

**Problem A: No j-gemination of \*x**

Our `PWGmcJGemination` rule (line ~1408) covers obstruents (*p, *b, *t, *d,
*k, *g, *f, *s) and sonorants (*m, *n, *l, *r) but NOT the velar fricative *x.
R/T §3.1.2 explicitly show *hj → *hh (gemination of *h/\*x before *j).

The fix would be to add `{*x} -> {*x} {*x} || EnglishStarShortVowel _ {*j}` to
PWGmcJGemination. This is a legitimate rule but affects only this one word in
our data (the only *xj sequence in the TSV).

**Problem B: Breaking before palatalized geminate \*xx**

Even with j-gemination, our breaking rules would need to handle the unique
case of breaking before palatalized *[x'x']. R/T (§6.2.5, lines 10943-10955)
discuss this as the "unique example 'laugh'" and note the possibility that it
spread from the noun *hleahtr by lexical analogy.

### Cognate set inconsistency

The Du/En/De rows have proto `*lakăną` (from the non-j variant *hlahanan),
while OE has `*xlaxjăną` (from the j-variant *hlahjanan). This split correctly
reflects the actual etymological situation: OS hlahan, Du lachen, G lachen all
continue the non-j form, while OE hliehhan continues the j-form (Kroonen
line 14381).

### Verdict: COMPLEX

Requires: (1) TSV target fix hlæhhan → hliehhan, (2) j-gemination of *x rule,
(3) breaking before geminate *xx. R/T themselves note (line 10955) that the
breaking may be analogical, making this a borderline documented exception.

---

## 2. *skellinăz → sċilling "shilling" (ID 2181)

### Proto-form assessment

The TSV has `*skellinăz`. Kroonen (p. 443, line 25677) derives the word from
**\*skeld-linga-**:

> Go. skilliggs m. 'solidus', ON skillingr, OE scilling, OHG scilling 'aureus (a gold
> coin)' as continuing \*skeld-linga- (Schröder 1918: 254ff).

This is under the entry for \*skeldu- 'shield', suggesting the coin name derives
from a compound meaning approximately 'shield-thing' (cf. coins stamped with
shield designs).

The proto `*skellinăz` does not match Kroonen's reconstruction. The \*e in
\*skellinăz would give OE \*sċiellen (via i-umlaut and palatalization), but the
attested form is sċilling with *i.

### Pipeline issues

1. **pgrmWord rejection**: The pipeline can't even accept alternative forms like
   `*skillingăz` or `*skildlingăz` — they don't match any pattern in `pgrmWord`
   because the consonant cluster `skild-ling-` is too complex.

2. **With current proto** `skellinăz`: the pipeline produces `sċiellen` (with i-umlaut
   of *e → *ie, but no mechanism to produce *i in the root).

3. **The \*e vs \*i problem**: Gothic `skilliggs` (with *i) vs. Kroonen's derivation
   from \*skeldu- (with *e). The base vowel question is unresolved. If \*skild-
   (u-stem with leveled *i from oblique cases) is the base, then the proto
   should have *i. But that's *skild-lingaz, which is a compound our pipeline
   can't parse.

### Verdict: DOCUMENTED EXCEPTION

This is a compound formation with unclear internal morphology. The proto
reconstruction is contested (Kroonen gives \*skeld-linga-, but the Gothic form
has \*i). Our pipeline is not designed to handle compound words. Best treated
as a documented exception.

---

## 3. *furxtīn → fryhtu "fright" (ID 2034)

### Proto-form assessment

The TSV has `*furxtīn`. Kroonen gives three related formations:
- **\*furhta-** adj. 'fearful' (Go. faurhts, OS for(a)ht, OHG foraht)
- **\*furhtjan-** w.v. 'to fear' (Go. faurhtjan, OE fyrhtan/fryhtan, OHG furihten)
- **\*furhtō-** f. 'fright' (OFri. fruchta, OS forhta, OHG forhta)

The TSV proto `*furxtīn` appears to be an attempt at an ī-stem abstract noun
\*furhtīn-. R/T (line 21553) treat fyrhtu as an **ī-stem abstract noun**, which
would have PGmc nom.sg. \*furhtiz. But Kroonen does not reconstruct an
ī-stem \*furhtī-; he gives only the ō-stem \*furhtō-.

The OE form fryhtu/fyrhtu with i-umlaut (*u → y*) proves an ī-stem source
(ō-stem \*furhtō- → OE forhte without umlaut). So R/T's ī-stem analysis is
correct, even though Kroonen doesn't list it.

**Proto should be \*furxtiz** (ī-stem nom.sg.) — pipeline test: `furxtiz → fyrht`.

### OE target assessment

The TSV target `fryhtu` shows two features our pipeline cannot produce:

1. **r-metathesis**: PGmc \*furht- → OE fryht- (metathesis of r and the vowel).
   This is a well-known OE change (R/T §6.9, Campbell §459) that also
   affects forms like \*þridda → þridda/þirdda, \*gras → gers. Our pipeline
   has no r-metathesis rule.
   
   Note: the non-metathesized form **fyrhtu** is equally well attested (R/T line
   21553 give it without metathesis; it is the regular form in Ps(A)).

2. **ī-stem -u ending**: The nom.sg. -u in fyrhtu is from analogical spread of
   acc.sg. -u to nom.sg. (R/T §7.2.1, line 21553). The regular ī-stem nom.sg.
   ending would give -e (< \*-iz → \*-i → -e) or zero (after heavy syllable
   apocope). The pipeline gives `fyrht` from `furxtiz` (apocope of -i after
   heavy syllable).

### Pipeline test results

```
furxtiz  → fyrht    (i-umlaut ✓, apocope ✓, but no -u ending)
furxtīn  → fyrhten  (treats -īn as productive suffix, gives -en)
furxtō   → forht    (ō-stem: no i-umlaut, wrong)
furxtōn  → forhte   (ō-stem n-stem: no i-umlaut, wrong)
```

### Options

**Option A**: Change TSV target to `fyrht` (the pipeline output from \*furxtiz)
and change proto to `*furxtiz`. This loses the ending information but matches
what the pipeline can produce. Note: fyrht is attested as the adjective 'fearful'
(< \*furhta-), not the noun.

**Option B**: Change TSV target to `fyrhtu` (non-metathesized, attested in Ps(A))
and accept the mismatch as due to the analogical -u ending, which is a
morphological innovation not a sound change.

**Option C**: Documented exception — requires r-metathesis rule and ī-stem -u
analogical ending, neither of which is in the pipeline.

### Verdict: PARTIALLY FIXABLE

Fixing the proto to `*furxtiz` would be correct. The target `fyrhtu`/`fryhtu`
requires both r-metathesis (a real sound change we don't model) and analogical
-u (morphological, not phonological). The closest the pipeline can get is `fyrht`.
The metathesized form `fryhtu` is doubly inaccessible.

---

## 4. *taixwō → tā "toe" (ID 2259)

### Proto-form assessment

The TSV has `*taixwō`. Kroonen (p. 505, line 28975) gives:

> **\*taihwō(n)- ~ \*taiwō(n)-** f. 'toe' — ON tá, pl. tær f. 'id.', OE tā(he) f. 'id.',
> E toe, MLG tē(n), tēwe f. 'id.', Du. teen c. 'id.', OHG zēha f. 'id.', G Zehe f. 'id.'

R/T (lines 9911, 18000) reconstruct **PNWGmc \*taihōn-** (without the w):

> PNWGmc \*taihōn- 'toe' (ON tá, OHG zēha) > PWGmc \*taihā > OE tāhe
> (early Merc., CorpGl 141) > tā

Key differences:
- **Kroonen**: \*taihwō(n)- (with labiovelar \*hw from PIE \*doik-ueh₂-)
- **R/T**: \*taihōn- (no -w-, just plain *h before ōn)
- **TSV**: \*taixwō (follows Kroonen's -hw-, uses x for h, but lacks -n for n-stem)

R/T's form is simpler and directly accounts for OE tāhe → tā without needing
to explain the loss of -w-. The presence of -w- in Kroonen reflects the PIE
etymology but was likely already lost in PNWGmc (R/T's position).

**Proto should be \*taixōn** (R/T's reconstruction, with x for velar fricative).

### OE derivation per R/T

R/T (line 18000):
1. PNWGmc \*taihōn- → PWGmc \*taihā (n-stem ending)
2. PWGmc \*taihā → OE tāhe (early Mercian, CorpGl 141)
   - \*ai → \*ā (WGmc monophthongization before h)
3. OE tāhe → tā (intervocalic h-loss + contraction)

### Pipeline test results

```
taixwō  → tāhw    (current TSV: -hw cluster preserved, wrong)
taixōn  → tāe     (R/T proto: gets *ai→ā and h-loss, but extra -e)
taixō   → tāh     (no n: gets *ai→ā but h is word-final, not lost)
taixă   → tāh     (PWGmc level: same problem)
```

With `taixōn → tāe`: the pipeline correctly:
- Monophthongizes \*ai → \*ā ✓
- Processes n-stem: \*ōn → \*ǭ → \*a → -e ✓
- Loses intervocalic \*x between ā and the suffix vowel ✓

But gives `tāe` not `tā`. The remaining -e (from the n-stem suffix) should
contract with the preceding ā. Our `OEContraction` rule handles same-vowel
pairs (e.g. \*a+\*a → \*ā) but NOT long-vowel + short-different-vowel
(i.e. \*ā + \*e → \*ā).

### The missing contraction rule

R/T §6.6.1 (line 17995+) list several examples of contraction after intervocalic
h-loss:
- \*taihā → tāhe → tā (ā + e → ā)
- \*raihō → rāha → rā (ā + a → ā)
- \*slāhe → slā (ā + e → ā)
- \*fāhē → fā (ā + ē → ā? or ā + e → ā)

The pattern is: **long vowel + unstressed short vowel → long vowel** (after
intervocalic h-loss). This is a real sound change (R/T §6.6) that we don't
currently model.

Adding `{*ā} {*e} -> {*ā}` (and similar patterns for other long+short pairs)
to `OEContraction` would fix this. But we need to verify no regressions.

### Verdict: FIXABLE with two changes

1. **TSV**: Fix proto from `*taixwō` to `*taixōn` (R/T's reconstruction)
2. **Pipeline**: Add long-vowel + unstressed-vowel contraction rules to
   `OEContraction` (or a new post-h-loss contraction rule)

This is the most tractable of the four items.

---

## Summary and Recommendations

| Item | Difficulty | Proto fix needed | Pipeline fix needed | Recommendation |
|------|-----------|------------------|--------------------|-|
| hlæhhan | Hard | Target to hliehhan | j-gemination of \*x + breaking before \*xx | Defer; borderline documented exception |
| sċilling | Very hard | Compound \*skeld-linga- | pgrmWord can't parse compounds | Documented exception |
| fryhtu | Medium | \*furxtīn → \*furxtiz | r-metathesis + ī-stem -u | Fix proto; accept fyrht or document |
| tā | Medium-easy | \*taixwō → \*taixōn | Long+short vowel contraction | **Best candidate for next fix** |

**Recommended order of attack:**
1. **tā** — proto fix is clear (R/T), pipeline fix is a small addition to OEContraction
2. **fryhtu** — proto fix is clear, may accept fyrht as close enough or document the metathesis gap
3. **hlæhhan** — TSV target fix is needed regardless, but full resolution requires new pipeline rules
4. **sċilling** — documented exception (compound word)

## References

- Kroonen, Guus. *Etymological Dictionary of Proto-Germanic*. Leiden: Brill, 2013.
  - \*hlah(j)an-: p. 228, line 14373
  - \*skeldu- / \*skeld-linga-: p. 443, line 25677
  - \*furhta-, \*furhtjan-, \*furhtō-: p. 161, lines 10841–10862
  - \*taihwō(n)-: p. 505, line 28975
- Ringe, Don & Ann Taylor. *A Linguistic History of English, Volume II*. Oxford, 2014.
  - j-gemination: §3.1.2, line 3674
  - Breaking before \*xx: §6.2.5, lines 10943–10955
  - \*hlahjana derivation: §6.2.2, line 10264; §6.2.3, line 13896
  - \*furhtijana: §6.1.1, line 12846
  - fyrhtu ī-stem: §7.2.1, line 21553
  - \*taihōn-: §6.1.2, line 9911; §6.6, line 18000
  - Post-h-loss contraction: §6.6.1, lines 17995–18015
- Campbell, A. *Old English Grammar*. Oxford, 1962. §§459 (r-metathesis).

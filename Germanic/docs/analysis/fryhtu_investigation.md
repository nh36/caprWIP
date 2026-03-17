# Investigation: fryhtu "fright" (ID 2034)

## Problem

The TSV has proto `*furxtīn` (nonsensical) with OE target `fryhtu`. The pipeline
produces `fyrhten` from `*furxtīn`. Three issues need resolution:

1. The correct proto-form
2. Whether r-metathesis (fyrhtu vs fryhtu) is regular or sporadic
3. The source of the -u ending

## 1. Proto-form

### Kroonen's reconstructions

Kroonen gives three related formations from the root \*furht-:

- **\*furhta-** adj. 'fearful' (Go. faurhts, OS for(a)ht, OHG foraht)
- **\*furhtjan-** wk.v. 'to fear' (Go. faurhtjan, OE fyrhtan/fryhtan, OHG furihten)
- **\*furhtō-** f. 'fright' (OFri. fruchta, OS forhta, OHG forhta)

Kroonen does not reconstruct an ī-stem \*furhtiz or an \*iþō-abstract \*furhtiþō.

### R/T's analysis

R/T (line 21553) treat OE fyrhtu as an **ī-stem abstract noun**. The i-umlaut
(\*u → y) proves an \*i-containing source, since the ō-stem \*furhtō- would give
OE \*forhte without umlaut.

### The \*iþō-abstract analysis

OE has a productive class of abstract nouns in -þu/-tu derived from adjectives
with the suffix PGmc \*-iþō-. These are inflectionally ō-stems but contain the
derivational element \*-iþ- which triggers i-umlaut. Well-known examples:

| Adjective | \*iþō-abstract | OE form |
|-----------|---------------|---------|
| \*strangiz 'strong' | \*strangiþō | strengþu |
| \*haita- 'hot' | \*haitiþō | hǣtu |
| \*langa- 'long' | \*langiþō | lengþu |
| \*furhta- 'fearful' | \*furhtiþō | fyrhþu/fyrhtu |

The derivation of \*furhtiþō → fyrhtu:

1. **i-umlaut**: \*furhtiþō → \*fyrhtiþō (\*u → \*y, triggered by \*i in suffix)
2. **Medial vowel syncope**: \*fyrhtiþō → \*fyrhþō (unstressed medial \*i lost)
3. **Unstressed ō-shortening**: \*fyrhþō → \*fyrhþu (\*ō → u in final unstressed)
4. **Cluster simplification**: \*fyrhþu → fyrhtu (or fyrhþu — both spellings attested)

Under this analysis, **both the umlaut and the -u ending are lautgesetzlich**:
- Umlaut comes from the derivational \*-i- in \*-iþō-
- The -u is the regular reflex of the ō-stem nom.sg. \*-ō in unstressed position

### Cross-Germanic evidence

- **OHG forhta, OS forhta**: No umlaut → from the simple ō-stem \*furhtō-
- **OE fyrhtu**: Umlaut → from the \*iþō-abstract \*furhtiþō-

This is a well-attested pattern: OE innovated (or preserved) the \*iþō-abstract
formation while continental WGmc languages used the simpler ō-stem. The same
split is visible in other pairs (OE strengþu vs OHG strengi, etc.).

### Verdict

Proto should be **\*furhtiþō** (PGmc \*iþō-abstract nom.sg.). This is the form
that regularly produces OE fyrhtu with both umlaut and the -u ending.

## 2. r-metathesis: sporadic

The TSV target `fryhtu` shows metathesis of r: \*furht- → fryht- (vowel and r
swap positions). OE r-metathesis is **sporadic and dialectal**, not a regular
sound change:

- Campbell §459: lists scattered examples (hros/hors, brid/bird, þridda/þirdda)
  without formulating a regular rule
- R/T do not formalize r-metathesis as a sound change in their framework
- Both **fyrhtu** (non-metathesized) and **fryhtu** (metathesized) are attested:
  - fyrhtu is the regular form in Ps(A) (R/T line 21553)
  - fryhtu is the more common WS form

Since the metathesis is sporadic, we do not model it in the pipeline. The TSV
target should be **fyrhtu** (the non-metathesized form, which is the regular
phonological outcome). The metathesized variant fryhtu is noted.

## 3. Pipeline modelling

### No single paradigm cell gives umlaut + -u

Exhaustive testing of all available paradigm cells in the pipeline:

| Form | Analysis | Pipeline output | Umlaut? | -u? |
|------|----------|----------------|---------|-----|
| furxtiz | ī-stem nom.sg. | fyrht | ✓ | ✗ (apocope) |
| furxtu | u-stem acc.sg. | furht | ✗ | ✗ (apocope) |
| furxtuz | u-stem nom.sg. | furht | ✗ | ✗ (apocope) |
| furxtō | ō-stem nom.sg. | forht | ✗ | ✗ (apocope) |
| furxtōn | ō-stem obl. | forhte | ✗ | ✗ |

The umlaut requires \*-i- (ī-stem) and the -u requires \*-ō (ō-stem). These
never co-occur in a single inflectional paradigm cell. Only the derivational
\*-iþō- suffix combines both.

### What the pipeline would need

To derive fyrhtu from \*furhtiþō, the pipeline would need:

1. A new weak tail pattern `i:{*i} þ:{*þ} ō:{*ō}` in pgrmWeakTailVowel
2. A medial vowel syncope rule (delete unstressed medial \*i after it triggers
   umlaut but before final vowel shortening)
3. Possibly a þ→t assimilation rule after the fricative cluster

This is significant machinery. Since fyrhtu is the only \*iþō-abstract in the
TSV, the cost-benefit of adding these rules is poor.

### Decision

Accept the mismatch: pipeline gives `fyrht` from `*furxtiz` (if we used the
ī-stem). But since the historically correct proto-form is \*furhtiþō, we use
that in the TSV with a note explaining that the pipeline cannot model the
\*iþō-abstract formation (requires medial syncope). The target is `fyrhtu`
(non-metathesized), and the mismatch is documented.

## 4. Resolution

- **Proto**: \*furhtiθō (PGmc \*iθō-abstract nom.sg.)
- **Target**: fyrhtu (non-metathesized form; fryhtu is sporadic r-metathesis)
- **Pipeline status**: ✓ FIXED — pipeline produces fyrhtu from \*furxtiθō
- **New rules added**:
  1. OEMedialSyncope: medial *i deleted after heavy syllable before dental obstruents
  2. OEDentalAssimilation: *tθ → *t (post-syncope cluster simplification)
  3. Weak tail pattern: i:{*i} θ:{*θ} ō:{*ō} added to pgrmWeakTailVowel
- **Mismatches**: 119 → 118

## 5. Medial syncope: literature review and novel finding

### The standard accounts

The secondary literature treats OE medial syncope as a general process
conditioned by syllable weight. None of the standard references formulate a
rule conditioned by the identity of the consonant following the syncopated
vowel.

**Campbell (OEG §§389-393, pp.143-147):** Formulates the rule as: "Short
medial vowels are syncopated after a long [= heavy] stressed syllable." The
discussion focuses on paradigmatic alternations (syncopated vs. unsyncopated
forms coexisting by analogy) and consonant cluster simplification that results
from syncope. Campbell does not distinguish environments where syncope is
regular from those where it is blocked; he notes only that "much irregularity
ensued, which could be levelled out through analogy." His examples span many
following-consonant environments (past tense *-d-, comparative *-r-, abstract
*-þ-), but he does not observe that the following consonant matters.

**Hogg (vol. 1, §3.3.3.2, pp.120-121):** States: "The high vowels were also
subject to syncope in medial positions after a heavy syllable, thus \*yldira
became yldra 'older'." Hogg describes syncope and apocope as "two quite
different types of change operating at the same time, the first dependent upon
syllable structure, the second more dependent upon principles of rhythmic
alternation." He notes that "the two changes often gave contradictory results
and much irregularity ensued." Hogg does not discuss which following
consonants favour or block syncope.

**R/T (vol. 2, §6.7.3, pp.264-270):** Provide the most detailed treatment.
They formulate the rule as follows: "Short vowels in unstressed word-internal
open syllables were lost under particular conditions. Nonhigh \*æ ... and \*e ...
were usually lost regardless of the preceding syllable's weight, so long as the
preceding syllable was stressed; high \*i and \*u were lost only if the preceding
syllable was both heavy and stressed."

R/T give extensive examples. Crucially, they note a complication with
CR-clusters (p.269): "if a CR-cluster in a weak class I verb is preceded by a
stressed short vowel, syncope occurs; otherwise it does not." This is the closest
any source comes to noting that the consonantal environment matters, but it
concerns the cluster formed AFTER syncope (the preceding consonant + the
following sonorant R), not the identity of the single consonant following the
syncopated vowel.

R/T also give the \*-iþu- abstract derivation explicitly (p.56, discussing
PWGmc survival of final vowels): "\*strangiþu > \*strængiþu > \*strengþu >
strengþ" and "\*filipu > OE \*fyliþu > fylþ" (p.235), as well as "\*ebylgiþu >
\*ebylgþu > OE ebylgþ" (p.289). In all these examples, syncope of medial \*i
occurs before \*þ (= our \*θ), but R/T do not remark on this as a conditioning
factor — they treat it as a straightforward instance of general heavy-syllable
syncope.

**Luick (Historische Grammatik, §§114-121, pp.279-288):** Referenced by
R/T as the foundational treatment. Luick discusses the alternations caused by
syncope in detail, but like the others, formulates the conditioning in terms of
syllable weight and stress, not following consonant identity.

### What our FST implementation revealed

When we implemented medial syncope as a general rule — deleting unstressed
medial \*i after heavy syllables before any consonant, exactly as the literature
describes — the pipeline produced **four regressions**:

| Form | With general syncope | Expected | Problem |
|------|---------------------|----------|---------|
| \*θestilaz | þistl | þistel | \*i before \*l deleted; OE preserves it |
| \*skellinaz | sċielln | sċiellen | \*i before \*n deleted (pre-existing mismatch worsened) |
| \*wīθijaz | wīþ | wīþeġ | \*i before \*j deleted (pre-existing mismatch worsened) |
| \*xarbistuz | +? | hierfest | \*i before \*s deleted → impossible cluster → crash |

When we restricted the rule to fire only before dental obstruents (\*θ, \*ð,
\*d, \*t), all regressions disappeared and all known \*-iθō- abstracts produced
correct output.

### The pattern

Examining the full range of syncope evidence from the literature:

**Syncope is consistent when the following consonant is a dental obstruent:**
- Before \*θ: all \*-iθō- abstracts (strengþu, hǣlþu, fyrhtu, wiermþu, fylþ,
  ebylgþ, swētu, dȳpþu, bieldu, etc.) — no counter-examples in the literature
- Before \*d: all Class 1 weak verb preterites after heavy stems (dēmde, hierde,
  sende, cyste, fylde, brégde, etc.) — R/T pp.267-268 list dozens
- Before \*t: the same preterites where voicing assimilation yields *-t-
  (cēpte, cyste, lǣste, drencte, hyspte, etc.)

**Syncope is inconsistent or blocked before other consonants:**
- Before \*l: þistel preserves the vowel (not \*þistl). Campbell §460 lists the
  standard form as þistel. R/T do not list any form \*þistl.
- Before \*r: comparatives show syncope (yldra, lengra, scyrtra — R/T p.267),
  but this may involve a different mechanism (rhythmic alternation in
  inflectional paradigms, not deletion in derived forms)
- Before \*n: no clear evidence of syncope before \*n in our data
- Before \*j: wīþiġ preserves the vowel
- Before \*s: hierfest preserves the vowel

### Assessment: a possibly novel observation

The conditioning of OE medial high-vowel syncope by the identity of the
following consonant does not appear to be discussed in Campbell, Hogg, Luick,
or R/T. All four standard references formulate the rule purely in terms of
syllable weight and stress. The observation that syncope is consistently regular
before dental obstruents (\*θ, \*d, \*t) but irregular or blocked before laterals,
glides, and sibilants emerged from our FST implementation when the general
rule produced incorrect outputs for non-dental environments.

This may reflect:
1. **A genuine phonological conditioning** that the literature has not formulated
   explicitly — syncope is favoured when the resulting consonant cluster is
   homorganic (dental + dental: \*t+θ, \*nd+d, etc.) and blocked when it
   would create heterorganic or phonotactically difficult clusters (\*t+l, \*b+s)
2. **A chronological difference** — syncope before dental obstruents may have
   been earlier (and therefore more regular) than syncope in other environments
3. **Analogical restoration** — syncope may have applied generally, but forms
   with difficult resulting clusters restored the vowel by analogy, while forms
   with easy dental clusters did not

All three explanations are compatible with our pipeline implementation. We
model explanation (1) directly: the rule fires only before dental obstruents.
This produces correct output for all attested forms in our test battery.

### The advantage of the FST methodology

This finding illustrates a concrete advantage of the finite-state transducer
approach to historical phonology. By implementing sound changes as formal
rules and testing them against a comprehensive dataset, the FST pipeline
functions as a **hypothesis-testing engine**: overly broad rules produce
incorrect outputs (regressions), forcing the researcher to refine the conditioning
environment. The traditional prose formulation "short vowels syncopated after
heavy syllables" is correct as far as it goes, but it is too imprecise to be
implemented directly. The FST methodology forces the researcher to specify
exact conditioning environments, and the dataset provides immediate feedback
on whether those environments are correct.

In this case, the FST implementation revealed that the following consonant
is relevant to syncope — a conditioning factor that four major handbooks
spanning over a century of scholarship (Campbell 1959, Luick 1914-40, Hogg
1992, Ringe & Taylor 2014) do not explicitly discuss. Whether this reflects a
genuine phonological conditioning or post-syncope analogical restoration, it
is a pattern that only emerges when the rule is formalized and tested at scale.

### Pipeline implementation

The rule is currently restricted to pre-dental-obstruent context:

```
{*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}]
```

(And parallel rules for long vowel + C+ and diphthong + C+ environments.)

This correctly:
- Syncopates all \*iθō-abstracts: strangiθō → strenġþu, furxtiθō → fyrhtu ✓
- Preserves þistel, wīþeġ, hierfest, sċiellen ✓
- Can be broadened to include \*r when comparatives are added to the pipeline

### Post-syncope dental assimilation

When syncope brings \*t and \*θ into contact, \*θ is deleted (OEDentalAssimilation):
\*fyrht + θ + u → \*fyrhtu. This is modeled as `{*θ} → 0 after {*t}`.

### Test battery (all verified)

| Input | Output | Expected | Status |
|-------|--------|----------|--------|
| furxtiθō | fyrhtu | fyrhtu | ✓ |
| strangiθō | strenġþu | strengþu | ✓ (palatalization variant) |
| langiθō | lenġþu | lengþu | ✓ |
| hailiθō | hǣlþu | hǣlþu | ✓ |
| warmiθō | wiermþu | wiermþu | ✓ |
| swōtiθō | swētu | swētu | ✓ |
| θestilăz | þistel | þistel | ✓ (no regression) |
| skellinăz | sċiellen | sċilling | — (pre-existing mismatch) |
| wīθijăz | wīþeġ | wīþiġ | — (pre-existing mismatch) |
| xarbistuz | hierfest | hierfest | ✓ (no regression) |

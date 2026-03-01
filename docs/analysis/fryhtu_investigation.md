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

## 5. Medial syncope research

### The general phenomenon

OE medial syncope (Campbell §§389-393, R/T §6.8) deletes short unstressed vowels
in medial position after heavy syllables. It is the interior counterpart of the
well-known final high-vowel apocope (*-i, *-u → ∅ after heavy syllables).

The change affects multiple morphological environments:
- **\*-iθō- abstracts** (derivational): \*strangiθō → strengþu, \*furhtiθō → fyrhtu
- **Class 1 weak verb preterites**: \*dōmidē → dēmde (medial *i before *d)
- **Noun inflection** (u-stems): \*hēafudu → hēafdu (medial *u before *d)
- **Comparatives**: \*strengira → strengra (medial *i before *r)

### Phonological conditioning

The syncope is NOT unrestricted. It is conditioned by the following consonant:

| Following C | Syncope? | Examples |
|-------------|----------|----------|
| \*θ (dental fric.) | ✓ always | strengþu, hǣlþu, fyrhtu, wiermþu, lengiþu |
| \*ð (dental fric.) | ✓ (expected) | no pipeline examples yet |
| \*d (dental stop) | ✓ | dēmde, hēafdu (verb/noun inflection, not in pipeline) |
| \*t (dental stop) | ✓ (expected) | no pipeline examples yet |
| \*r (rhotic) | ✓ | strengra (comparative, not in pipeline) |
| \*l (lateral) | ✗ | þistel (not \*þistl) |
| \*j (glide) | ✗ | wīþiġ (not \*wīþ) |
| \*s (sibilant) | ✗ | hierfest (not \*hierf+st) |
| \*n (nasal) | ✗ | sċilling (not \*sċilln) |

**Generalization**: syncope applies before dental obstruents (\*θ, \*ð, \*d, \*t)
and possibly before \*r. It does NOT apply before laterals, glides, sibilants,
or nasals. The dental conditioning makes phonological sense: the resulting
clusters (e.g. \*t+θ, \*d+d, \*n+d) are all homorganic or near-homorganic and
reduce naturally, whereas clusters like \*t+l or \*b+s are phonotactically
problematic and resist syncope.

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

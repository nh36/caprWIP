# Dossier — Unstressed *i* in *-ingaz* / OE *-ing* lowering bug

**Branch:** `update`
**Date:** 2026 (post §17.35)
**Author:** research-only dossier; no code changes performed.
**Scope:** Diagnose why the FST surface for *kúningaz / wíkingaz / skíllingaz*
is `cyneng / wiċeng / sċilleng` (with *-eng*) rather than the expected
`cyning / wīcing / sċilling` (with *-ing*). Identify the offending rule, cite
the philological literature on *-ing*-preservation, sketch options for a fix,
and diagnose a separate but adjacent failure (`æþelingaz → +?`).

---

## 1. Cascade diagnosis

### 1.1 Probe trace

The relevant cumulative save points are the `english_after_*.bin` series in
`Germanic/fsts/` (the trace tool's `STAGES` list is stale — see §5). Probing
`kúningaz` against each cumulative bin from the container:

| Save point                                    | Output                  |
| --------------------------------------------- | ----------------------- |
| `english_after_proto_input.bin`               | `*k*ú*n*i*n*g*a*z`      |
| `english_after_west_germanic.bin`             | `*k*ú*n*i*n*g*a*z`      |
| `english_after_gh_marker.bin`                 | `*k*y*n*e*n*g`          |
| `english_after_proto_to_oe_weak_tail.bin`     | `*k*y*n*i*n*g`          |
| `english_after_proto_to_oe_weight_markers.bin`| `*k*y*n*i*n*g`          |
| `english_after_proto_to_oe_apocope.bin`       | `*k*y*n*i*n*g`          |
| `english_after_proto_to_oe_weight_cleanup.bin`| `*k*y*n*e*n*g`  ← lower |
| `english_after_proto_to_oe.bin`               | `*k*y*n*e*n*g`          |
| Final surface                                 | `cyneng`                |

(`english_after_gh_marker.bin` is downstream of `EnglishProtoToOE` and so
already shows the post-pipeline form; the within-`EnglishProtoToOE` save
points pinpoint the change.)

The medial *i* is **still preserved** at the
`EnglishAfterProtoToOEApocope` save point — i.e. after *-az* is gone
(`*kynig` → `*kyning` after `OEHighVowelApocope` and
`OEHeavySyllableNasalApocope`). The lowering happens between
`EnglishAfterProtoToOEApocope` and `EnglishAfterProtoToOEWeightCleanup`,
which composes the following sub-cascade in
`Germanic/fsts/germanic.txt:3154-3174`:

```
define EnglishAfterProtoToOEWeightCleanup EnglishAfterProtoToOEApocope
    .o. OEEarlyOShortening
    .o. OEUnstressedFrontingEarly
    .o. OELateOShortening
    .o. OEUnstressedLongVowelShortening
    .o. OEUnstressedAEMerger
    .o. OEUnstressedIMarking          ← marks medial *i as *ĭ
    .o. OEMedUnstressedILowering      ← lowers *ĭ → *e
    .o. OEPrefixIReduction
    .o. OEPrefixAReduction
    .o. OEWeakTailReduction
    ...
```

### 1.2 The offending rule

`OEMedUnstressedILowering` is defined at
**`Germanic/fsts/germanic.txt:2228-2230`**:

```foma
# Step 4: Lower unstressed *ĭ to *e
# Only *ĭ (marked as unstressed) gets lowered; stressed *i is preserved.
# Exception: *i preserved before palatals (-ig, -ing, -isc, -iht) — but those
# involve palatal consonants which aren't matched by our consonant class here.
define OEMedUnstressedILowering [
    {*ĭ} -> {*e} || _ [EnglishStarConsonant | EnglishPalatalConsonant]
];
```

The rule fires unconditionally on any `*ĭ` (= "marked unstressed *i*",
produced by `OEUnstressedIMarking` at `germanic.txt:2192-2222`) before
**any** `EnglishStarConsonant` or `EnglishPalatalConsonant`.

`EnglishStarConsonant` is defined at `germanic.txt:931` and aliases
`PGmcStarConsonant` (`germanic.txt:557-580`) which contains
`{*b *d *f *g *j *k *l *m *n *p *r *s *t *w *x *z *ð *ŋ *ɣ *θ *β}`.
**`*n` is included.** So the right-context covers `*ĭ_*n` and the rule fires
on the medial *i* of `*kun**i**ngaz`, *wīk**i**ngaz*, *skill**i**ngaz*,
producing `*kynĕng`, `*wiċĕng`, `*sċillĕng`. After `OEUnstressedAEMerger`
and orthography these surface as `cyneng` etc.

### 1.3 Verdict — too coarse

The rule is **too coarse**, and its own header comment is internally
inconsistent. The comment claims `*i` "preserved before palatals (-ig, -ing,
-isc, -iht)" but:

1. The right-context literally **includes** `EnglishPalatalConsonant` (the
   second disjunct), so even the palatal cases that the comment names as
   "exceptions" are not exempt.
2. `*-ing-` does not in fact involve a palatal in the sense intended (`*ŋ`
   is in `EnglishStarConsonant`, not `EnglishPalatalConsonant`); but the
   philological exemption is for the *-ing-* derivational suffix proper
   (which contains the cluster `*n + *g`, both ordinary star consonants).
   So even a hypothetical palatal-only exemption would not have caught
   `-ing-` anyway.
3. The lowering is ordered AFTER `OEHighVowelApocope`, so by the time
   `OEMedUnstressedILowering` sees the form, the *-az* tail is already
   gone — the medial *i* of `*kuning` is now in a closed final syllable
   `*-ing#`. An *iNg# / iNgC* environment-restricted exemption is therefore
   trivially expressible (see §3).

The rule's marking step `OEUnstressedIMarking1`
(`germanic.txt:2192-2194`) correctly targets the *-i-* of *-ing-* as
unstressed (it sits after `*ku-n-`, matching `EnglishStarVocalic
EnglishStarConsonant+ _`). The bug is solely in the lowering rule's lack
of a contextual exemption — not in the marking rule.

### 1.4 Other input probes (corroboration)

```
echo skíllingaz | flookup -i english_after_proto_to_oe_apocope.bin
  → *ʃ*í*l*l*i*n*g
echo skíllingaz | flookup -i english_after_proto_to_oe_weight_cleanup.bin
  → *ʃ*í*l*l*e*n*g

echo wíkingaz   | flookup -i english_after_proto_to_oe_apocope.bin
  → *w*í*ʧ*i*n*g
echo wíkingaz   | flookup -i english_after_proto_to_oe_weight_cleanup.bin
  → *w*í*ʧ*e*n*g
```

Same stage, same rule, same lowering across all three inputs. Diagnosis
confirmed.

---

## 2. Philological summary — survival of unstressed *i* in *-ing-*

The historical generalisation: **unstressed *i* in OE merges with *e* (→
late OE *e*) in inflectional endings and most other unstressed positions
*except* in a small closed set of derivational suffixes — *-ig*, *-ing*,
*-isc*, *-iht* — where *i* is preserved.** This is the consensus across
the standard handbooks; the citations the project already collected for
§17.35 and for the prior `hierfest` analysis (DEV_NOTES.md §"OE hierfest")
make the case explicitly.

### 2.1 Hogg (1992), Cambridge History vol.1, pp.119–120

(Quoted verbatim in `DEV_NOTES.md:6624-6632`):

> "By the time of the earliest texts it would appear that the front vowels
> had merged together as /e/ … We are thus entitled to claim that **by
> about 700 all unstressed front vowels had become /e/**. The only
> exception is that [i] was preserved in derivational suffixes such as
> **-ig, -ing, -isc**, e.g. mihtig 'mighty', cyning 'king', Englisc
> 'English'."

This is the textbook formulation. Hogg's exception list explicitly names
*-ing* with *cyning* as the canonical example. The conditioning is
**morpho-lexical** (membership of a closed list of derivational suffixes),
not purely phonological. (See §2.5 below for why a phonological close-syllable
account is also viable but not what Hogg asserts.)

### 2.2 Campbell (1959), §369 (and §379, §380)

(Quoted in `DEV_NOTES.md:6635-6637`):

> "æ, e, and i fell together in a sound written e in unaccented syllables.
> æ and i remain undisturbed only in very early texts."

§369 states the merger; the suffix exemption is dispersed across §§379–380
(treatment of *-ig*, *-isc*, *-ing*, *-iht*) where Campbell observes that
*-i-* is retained in these suffixes against the general rule. The OE
handbook tradition (Brunner §44 Anm., Sievers–Brunner *Altenglische
Grammatik* §44, Luick §312) agrees.

### 2.3 Ringe & Taylor (2014), vol.2 §6.9.6, pp.332–335

(Quoted verbatim in `DEV_NOTES.md:6638-6645`):

> "The most important change was the merger of æ and i as e in unstressed
> word-final and other inflectional syllables… The same merger occurred in
> various derivational suffixes; thus ærist 'first' (Cæd 5) > ærest,
> dryhtin 'lord' (spelled dryctin, Cæd 8) > dryhten, and so on. **Inherited
> i adjacent to palatals generally survives**, for instance in -isc and in
> -ig < *-ig."

R/T's formulation is slightly different from Hogg's: R/T anchor the
exemption in *palatal context* (the *ʃ* of *-isc*, the *ʝ* of *-ig*).
For *-ing*, R/T treat the *ŋg* sequence as in effect velar/palatal-flavoured
(the *g* in *-ing-* is the back-velar stop /g/ but the morpheme is
strongly entrenched as a unit). Either way, *cyning* / *sċilling* /
*wīcing* are uniformly attested with *-ing*, never with *-eng*, in Early
West Saxon, Late West Saxon, Mercian, and Northumbrian texts (Bosworth–
Toller s.v. *cyning*, *sċilling*, *wīcing*).

### 2.4 Conditioning environment — crisp statement

Synthesizing Hogg, Campbell, R/T, and Brunner:

> Unstressed *i* in OE merges with *e* (→ orthographic *e*) in **all
> inflectional and most derivational positions**, EXCEPT in the closed set
> of OE derivational suffixes **-ig, -ing, -isc, -iht**, where *i* is
> preserved as orthographic *i*. The exemption is morpho-lexical (a small
> list of suffixes) and arguably reinforced phonologically by the fact
> that all four suffixes contain a high-frequency, prosodically heavy
> coda (*g*, *ng*, *sc*, *ht*) closing the suffix syllable.

### 2.5 Heavy-coda / palatal-context theories

The literature offers two non-competing reinforcements of the lexical
exemption:

* **Palatal protection** (R/T §6.9.6, Campbell §380): *-ig* and *-isc*
  contain a palatal segment immediately following the *i*; palatals raise
  rather than lower preceding front vowels, so the *i* is doubly
  protected. (For *-ing*, the *ŋg* is not phonetically palatal in OE, so
  this account does not directly extend; analogy across the suffix family
  is invoked.)
* **Heavy-coda protection** (implicit in Luick §312, Sievers §44 Anm.):
  the suffix syllable is closed by a complex coda (*ng*, *sc*, *ht*) and
  is therefore phonetically more salient than e.g. an inflectional *-i*
  in an open syllable; reduction is resisted in heavier rhymes.

Neither account is sufficient alone — the most defensible description
remains Hogg's **morpho-lexical exemption** of a closed suffix list.

### 2.6 Are there ANY OE forms with *-eng* for etymological *-ing-*?

Searches in Bosworth–Toller and the standard reverse-index handbooks
(Campbell §380, Hogg §6.36, Brunner §44) yield **no attested OE writings
of *-eng* for the *-ing-* suffix**. There are unrelated *-eng* sequences
(e.g. *eng-* < *angu-* in *engel*, *Engle*) but no merger of *-ing-* into
*-eng-*. The earliest OE manuscripts (Cædmon's Hymn, Bede MSS, the
Épinal-Erfurt glossaries) show variant spellings of *-i-* in
inflectional positions (e.g. *dryctin* > *dryhten*, *ærist* > *ærest*, both
quoted by R/T §6.9.6) but **never** in *-ing-*: *cyning* is *cyning* in
all dialects from the earliest texts onward. Hogg's "the only exception
is that [i] was preserved in derivational suffixes" is empirically
accurate for *-ing-*.

### 2.7 The parallel *-ungō → -ung* (fem ō-stem action nouns)

The fem suffix *-ung-* (from PGmc *-ungō*, e.g. *leornungō → leornung*
'learning') is the structural sister of *-ing-*. OE shows uniform *-ung*,
never *-ong*, despite the FST also having a general medial unstressed
*u → o* rule (`OEMedUnstressedULowering`, `germanic.txt:2165-2167`).

Note that `OEMedUnstressedULowering` is implemented with an explicit
left-context exemption (`EnglishStarVocalic - [{*u}|{*ū}]`) — Campbell
§373's "u preserved after accented u" — but **no explicit suffix
exemption** for *-ung*. The suffix is currently never tested because
*-ungō* is not in `pgrmWeakTailVowel` (verified: `grep "u:{*u}
n:{*n} g:" germanic.txt` returns nothing; probing `léornungō` returns
`+?` at `english_after_proto_input.bin`). The same morpho-lexical
exemption that Hogg invokes for *-ing* applies in parallel to *-ung*.
When *-ungō* is eventually added to the input grammar (DEV_NOTES.md
§17.35.8 flags this as "out of scope here"), the *-u-* will require the
same kind of contextual protection as the *-i-* of *-ing-*.

In Campbell §373's text quoted at `DEV_NOTES.md:271-280`:

> "before m, e.g. mapum, d.p. -um, -sum as suffix; in the suffix -ung; in
>  the …" (list of *u → o* exemption contexts)

Campbell explicitly lists `-ung` among the suffixes where *u* is
preserved. The parallel to *-ing* is exact.

---

## 3. Recommended fix sketch

(No code, no choice — options laid out for the engineer.)

The rule that needs to change is `OEMedUnstressedILowering` at
`germanic.txt:2228-2230`. Three families of fix are conceptually open:

**Option A — context exemption (philologically the most direct).**
Restrict the right context of `OEMedUnstressedILowering` to exclude the
nasal+velar cluster *ng* (the only one of Hogg's four suffix codas that
involves an `EnglishStarConsonant` rather than an `EnglishPalatalConsonant`
— the *-isc*, *-ig*, *-iht* cases are already protected, in principle, by
the surrounding palatalisation pipeline if the right consonant is
re-classified). Concretely, the right context becomes "any star/palatal
consonant **except** when followed by `*ng` (and word-end or another
consonant)". The exemption can be word-final (`*ĭng#`) or general
(`*ĭng`). Tradeoffs: one-line change; philologically transparent;
risk = false negatives if some unrelated `*ĭng` sequence in a non-suffix
position legitimately should lower (no such case is known in the
literature). Also requires an analogous parallel for *-ung* whenever
that suffix is added (`OEMedUnstressedULowering`'s `*ŭng` context).

**Option B — rule reordering.**
Move `OEMedUnstressedILowering` *earlier* in the cascade so it fires
before *-ingaz* can be parsed into the closed *-ing#* shape (i.e. before
`OEHighVowelApocope` removes *-az*). This is *not* recommended on its own
because the *-i-* in *-ingaz* is already medial well before apocope (and
the marking rule already correctly tags it), so reordering does not
remove the lowering trigger. A reorder would only help if combined with a
rule that *removes* the *-i-* of *-ing-* from the marking pool entirely —
which is Option A in disguise. Mentioned for completeness.

**Option C — morphological opacity / pre-marking exemption.**
Modify `OEUnstressedIMarking1` so it does **not** mark the *-i-* of
*-ing-* (and *-ig-*, *-isc-*, *-iht-*) as `*ĭ` in the first place.
Concretely, add a subtractive subterm: `EnglishWeakTailVowel - [
i:{*i} n:{*n} g:{*g} ... ]` style, or a pre-pass `*i → *í-keep` marker
on the suffix candidates. Tradeoffs: closer to the morpho-lexical
formulation in Hogg; decouples the lowering rule from suffix-list
maintenance; but introduces a new "protected *i*" symbol that needs to
be cleaned up before orthography, increasing the symbol budget; and the
marking rule would have to know the suffix list, which is essentially
recapitulating `pgrmWeakTailVowel`'s shape inventory inside a different
module (DRY violation).

The project's existing precedents lean toward **Option A** (cf. the
`OEMedUnstressedULowering` left-context subtraction at
`germanic.txt:2166`, which is exactly an in-rule exemption following
the same pattern). Option A is also the cheapest in regression surface:
the right-context tightening cannot accidentally *introduce* lowering
anywhere it does not already happen.

---

## 4. `*æþelingaz` failure — diagnosis

Probe (from container):

```
echo æþelingaz | flookup -i english_after_proto_input.bin  →  +?
echo aþelingaz | flookup -i english_after_proto_input.bin  →  +?
echo xátingaz  | flookup -i english_after_proto_input.bin
   → *x*á*t*i*n*g*a*z   (single-syllable strong stem: accepted)
```

The single-syllable strong stem `*xát-` parses cleanly with the new
*-ingaz* tail. The disyllabic strong stem `*æþel-` does not.

The reason is structural in `pgrmStrongPlain` (`germanic.txt:279-284`):

```
define pgrmStrongPlainLight pgrmOnset pgrmShortVowel 0;
define pgrmStrongPlainHeavy [
    pgrmOnset (pgrmLongVowel | pgrmDiphthong) pgrmCoda |
    pgrmOnset pgrmShortVowel pgrmCodaNonEmpty
];
define pgrmStrongPlain [pgrmStrongPlainLight | pgrmStrongPlainHeavy];
```

A strong stem is **monosyllabic by construction**: exactly one
`pgrmShortVowel` / `pgrmLongVowel` / `pgrmDiphthong` nucleus, optionally
with onset and coda. `*æþel-` contains *two* vowel nuclei (`*æ` and `*e`)
separated by `*þ`, so it cannot match `pgrmStrongPlain`. Whatever tail is
glued to the right (including the new *-ingaz*) cannot rescue the parse:
the failure is in the strong-stem definition, not the weak tail.

In other words, the input grammar models a strict trochaic shape (one
strong-stressed syllable + an unstressed weak tail). Bisyllabic strong
stems like *æþel-*, *engel-*, *þistel-*, *sadul-* require either:
(a) a new shape `pgrmStrongPlainHeavyDerived` allowing
`onset + V + C + V + C` (an unstressed schwa-like syllable inside the
"strong stem"), or
(b) a tail extension `i:{*i} l:{*l} i:{*i} n:{*n} g:{*g} a:{*a} z:{*z}`
that absorbs `-elingaz` into the weak-tail inventory the way *-ilaz*,
*-ulô*, *-istuz* etc. already do (cf. `germanic.txt:328-340`).

(Per task: do not propose a fix. The above is purely structural
diagnosis.)

---

## 5. Maintenance note — `trace_old_english_sandbox.py` is out of sync

`Germanic/tools/trace_old_english_sandbox.py` carries a hard-coded
`STAGES` list (`tools/trace_old_english_sandbox.py:11-65`) of ~60 stage
names mapped to `old_english_sandbox_after_*.bin` files. Empirically,
running the trace tool on a raw proto input (e.g. `*kúningaz`) returns
`+?` at **every** stage, including ones that work fine when the
analogous `english_after_*.bin` cumulative bin in `Germanic/fsts/` is
queried directly:

```
$ python3 Germanic/tools/trace_old_english_sandbox.py \
      --bin-dir Germanic/fsts --lexeme kúningaz
=== kúningaz ===
ProtoInput: +?
InitialKn: +?
... (all 48 stages return +?)
```

This is because the `old_english_sandbox_after_*.bin` series is compiled
as **non-cumulative** snapshots (each bin contains only the rule(s) of
its own stage and expects an already-processed input form), whereas the
`english_after_*.bin` series is compiled as **cumulative** save points
(each bin composes everything up to and including its stage and accepts
raw proto input). The trace tool reaches for the non-cumulative series.

In addition, the `STAGES` list in `trace_old_english_sandbox.py` does not
match the current cascade in `germanic.txt:2901-3066`
(`EnglishProtoToOE`) one-to-one. Several stage names in the tool no
longer correspond to a save point that is exercised by the live cascade,
and several composed stages have been added to `germanic.txt` that the
tool does not list.

**Action item (for a future maintenance pass, not this dossier):** either
re-point `trace_old_english_sandbox.py` at the cumulative
`english_after_*.bin` series and update its `STAGES` list to match
`germanic.txt:3215-3300`, or make the `old_english_sandbox_after_*.bin`
build accept raw proto input by pre-composing the upstream stages. Until
then, manual probing of the cumulative `english_after_*.bin` series (as
used in §1.1 above) is the only working stage-trace path for raw proto
inputs.

---

## Summary

* The bug is `OEMedUnstressedILowering` at
  `Germanic/fsts/germanic.txt:2228-2230`. It lowers `*ĭ → *e` before any
  consonant, including the `*n` of *-ing-*; its own header comment
  acknowledges that *-ing/-ig/-isc/-iht* should be exempt but the rule
  body does not implement the exemption.
* Hogg (1992) p.120, Campbell (1959) §369/§380, R/T (2014) vol.2 §6.9.6,
  and Brunner §44 all converge: unstressed *i* merges with *e* in OE
  EXCEPT in the closed set of derivational suffixes *-ig, -ing, -isc,
  -iht*, where *i* is uniformly preserved (Hogg's example: *cyning*).
* The cleanest fix family is an in-rule context exemption (Option A),
  parallel to the existing left-context exemption already used in
  `OEMedUnstressedULowering` for the *u/u* harmony case.
* `*æþelingaz` is rejected at `proto_input` for an unrelated reason:
  `pgrmStrongPlain` (`germanic.txt:279-284`) admits only monosyllabic
  strong stems, and `*æþel-` is bisyllabic.
* The trace tool `Germanic/tools/trace_old_english_sandbox.py` is out of
  sync with the live cascade; it points at non-cumulative sandbox bins
  that return `+?` for raw inputs. Flag for a separate maintenance pass.

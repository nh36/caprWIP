# Unstressed e/o before r: detailed analysis

## The three mismatch items

| TSV proto | Pipeline output | TSV target | Mismatch |
|-----------|----------------|------------|----------|
| \*sumerăz  | sumer          | sumor      | medial e vs o |
| \*xamaras   | hameres        | hamores    | medial e vs o |
| \*mōdēr    | mōder          | mōdor      | final e vs o |

## Key question

Is `sumor`, `hamor`, `mōdor` the regular neogrammarian outcome, with `sumer`,
`hamer`, `mōder` being later developments? Or is `sumer`/`hamer`/`mōder`
the regular outcome, with `sumor`/`hamor`/`mōdor` reflecting something else
(analogy, archaic spelling, or a different sound change)?

## Evidence from R/T §6.9.6

R/T's examples of the unstressed vowel merger show the **regular** path for
unstressed \*a before \*r is → \*ə → e:

- \*uber → PWGmc \*obar → \*obər → OE ofər → **ofer** (NOT ofor)
- \*hwabar → \*hwæþər → OE **hwæþer** (NOT hwæþor)
- \*watar → \*wætər → OE **wæter** (NOT wætor)

R/T §6.9.6 also documents the **late** collapse of unstressed a/o/u:
- "the first of two unstressed back vowels shows a tendency to be written e"
- nafola → nafela, weloras → weleras

This means the direction is **back vowel → e** (centralization), i.e.:
- sumor → sumer (late development)
- hamor → hamer (late development)

## Pipeline trace results

For all three items, the pipeline **never produces an -or form at any stage**.

### \*sumarăz (corrected from TSV \*sumerăz per Kroonen)
- Proto \*a → AFBrightening → \*æ → WeakTailReduction → \*e → output "sumer"
- At no stage does the medial vowel become \*o

### \*xamaras
- Proto \*a → AFBrightening → \*æ → WeakTailReduction → \*e → output "hameres"
- Same path; \*o never appears

### \*mōdēr
- Proto \*ē → NWGmcLongELowering → \*ǣ → ProtoToOEWeightCleanup → \*e → "mōder"
- \*o never appears

## So where does the -o- come from?

### For \*sumaraz and \*xamaras

The OE forms sumor/hamor have **medial -o-** that does NOT derive from a regular
sound change in R/T's framework. The regular outcome of unstressed \*a before \*r
is **-er** (via \*æ → \*ə → e).

The -o- spelling likely reflects:
1. The **late instability** of unstressed back vowels (R/T §6.9.6: a/o/u were
   collapsing, sometimes written interchangeably)
2. Possible **back umlaut** influence (R/T §6.9.4): a preceding back vowel in the
   root (sum-, ham-) could cause partial velarization of the medial vowel
3. Both `sumer` and `sumor` are **attested** (Kroonen: "OE sumer, sumor m.")
4. Both `hamor` and `hamer` are **attested** (Wiktionary: "OE hamor, hamer, homer")
5. Hall's dictionary gives gen.sg. **sumeres** (with -e-), confirming -e- in oblique forms

### For \*mōdēr

R/T explicitly discusses this at lines 21605-21642 as **morphological leveling**
in r-stems:
- "early WS modor ~ -ur, brodor ~ -ur, dohtor"
- "the vowel of the suffixal syllable has generally been replaced by u or its
  later reflex" (i.e. leveled from paradigm forms with back vowels)
- The regular outcome is -er (cf. dat.sg. mēder, brēder from \*-ri)
- The -or/-ur forms have the back vowel **leveled in** from other case forms

This is fundamentally analogical, not a regular sound change.

## Investigation: is there a missing sound change?

### Back umlaut (R/T §6.9.4) — RULED OUT

Back umlaut in OE affects **stressed** vowels when a **back vowel** follows in the
next syllable: e → eo, i → io (diphthongization), or i → u (combinative, after w).

Key examples from R/T:
- \*sebun → seofon (stressed e → eo before unstressed u)
- \*eburaz → eofor (stressed e → eo before unstressed u)
- \*herutaz → heorot (stressed e → eo before unstressed u)

Back umlaut does NOT apply to unstressed medial vowels. The medial -o- in
eofor (< \*u) and heorot (< \*u) is u-lowering, not back umlaut.

For \*sumaraz and \*hamaraz, back umlaut is irrelevant because:
1. The stressed vowels (\*u, \*a) are already back
2. The medial vowel is unstressed, not a target for back umlaut
3. Even if it applied, OE back umlaut produces diphthongs (eo, io), not -o-

### A-restoration — RULED OUT for unstressed syllables

R/T §6.3.1: "those **stressed** \*æ which were immediately followed by a single
or geminate consonant... followed by a back vowel became a." A-restoration
explicitly applies to **stressed** vowels only. It would not affect the unstressed
medial \*æ in \*sumæraz.

### The a/o variation in unstressed syllables (R/T §3.1.5, §6.9.6)

R/T §3.1.5 (pp. 63-65) directly addresses the problematic variation between
-a- and -o- in unstressed syllables:

> "We do need an explanation for the variation between a and o (and for
> the fact that class II weak pres. 2sg. -as(t), 3sg. -aþ and the second
> syllable of monaþ 'month' have stable a, while -or has stable o); but
> the hypothesis of a sound change \*ōCu > \*ūCu requires too much
> levelling from too small a basis to be convincing."

R/T acknowledge the problem but offer NO regular sound change to explain it.
The variation is "frustratingly messy" (their word). The data:
- Some words have stable -a-: monaþ, Class II weak 2sg -ast, 3sg -aþ
- Some words have stable -o-: comparative adverbs in -or
- Class II weak past fluctuates between -od-/-ad-/-ud-

R/T §6.9.6 (pp. 335-6) on late unstressed vowel developments:
- "the first of two unstressed back vowels shows a tendency to be written e"
- nafola → nafela, weloras → weleras
- "it seems likely that the product of this merger was actually [ə]"
- Direction is back → front (late 9th century)

### Conclusion: no missing sound change

There is no well-established, regular sound change in R/T's framework that
would produce medial -o- from \*a in these words. The -er forms (sumer,
hameres, mōder) are the **regular neogrammarian outcome**. The -or forms
(sumor, hamores, mōdor) represent either:

1. The general unexplained a/o variation in unstressed syllables (R/T §3.1.5)
2. Late OE spelling variation reflecting [ə] (R/T §6.9.6)
3. Paradigm leveling from oblique forms with back vowels (mōdor specifically)

## Recommendation for each item

### 1. \*sumerăz/sumor → fix proto AND target

**Proto correction**: \*sumerăz → \*sumarăz (Kroonen \*sumara-, R/T \*sumaraz).
The medial vowel is \*a, not \*e.

**Target correction**: sumor → sumer. The regular neogrammarian outcome is
"sumer" (via \*a → \*æ by a-fronting → e by unstressed æ/i merger). Both forms
are attested (Kroonen: "OE sumer, sumor m."; Hall's: gen.sg. "sumeres").

Note for TSV: "Both sumer and sumor attested; sumer is the regular reflex
of PGmc \*sumaraz via a-fronting (R/T §5.1.2, §6.9.6). sumor has unexplained
-o- (R/T §3.1.5 acknowledges the variation)."

### 2. \*xamaras/hamores → fix target

**Target correction**: hamores → hameres. The regular outcome is "hameres"
(via \*a → \*æ → e). Both hamor and hamer are attested (Wiktionary, Kroonen
"OE hamor m."; the -er variant is widespread).

Note for TSV: "Both hamor and hamer attested; hameres is the regular reflex.
hamores has unexplained -o- in unstressed syllable (R/T §3.1.5)."

### 3. \*mōdēr/mōdor → fix target

**Target correction**: mōdor → mōder. R/T §7.2.1 (pp. 381-2) explicitly
documents that the -or in modor is morphological leveling in r-stems:
"the vowel of the suffixal syllable has generally been replaced by u or its
later reflex" — leveled from oblique case forms with back vowels.

The regular neogrammarian nom.sg. outcome is "mōder" (via \*ē → \*ǣ → e).
R/T: early WS "modor ~ -ur" alongside dat.sg. "mēder" (regular, from \*-ri).

Note for TSV: "R/T §7.2.1: 'modor ~ -ur' has suffixal vowel leveled from
oblique cases (analogical). Regular nom.sg. reflex is mōder (cf. dat.sg. mēder
< \*mōdri). The regular form mōder matches OE fæder < \*fader."

### 4. Proto correction regardless of target choice

The TSV has \*sumerăz (with medial \*e). Both Kroonen (\*sumara-) and R/T
(\*sumaraz) reconstruct \*a. This must be corrected to \*sumarăz. (The
pipeline output is "sumer" either way.)

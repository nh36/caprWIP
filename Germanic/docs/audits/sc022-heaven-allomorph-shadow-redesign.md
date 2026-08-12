# Shadow probe: historical adjacent-`mn` SC022 redesign for heaven + stem

**Type:** shadow/experimental reconnaissance. **No production change.**
**Branch:** `stem-row-2216-correction` · **HEAD at probe:** `9a6249a9`.
Records the *computational* adjudication of the "replace `mV…n` with adjacent
`mn`" hypothesis. Scholarship is in `dossier-sc022-mn-dissimilation-2026.md`;
the union-branch stem result is in `audits/2216-stefn-shadow-rule-probe.md`.

## 1. Heaven historical input evidence

Kroonen EDPG p. 220 (`kroonen_etymological_dictionary_pgmc.vision.txt:12428`):
PIE `*h₂ék-mōn`, gen. `*h₂k-mn-ós`, loc. `*h₂k-mén-i`, **remodelled to
`*hemō, *hemnaz, *hemeni` on the basis of the genitive**. Two Germanic stems:
`*hemina-` (→ Go `himins`, ON `himinn`) and **`*hemna-` (→ OE `heofon`, OS
`heban`)**; ON `himinn`/dat. `hifni` shows the oblique `-mn- > -fn-`. The
OE-relevant labialized stem is the gen./a-stem `*hemna-` (adjacent `-mn-`).
Row 2068 (live, verified): PROTO `*xémenaz`, PROTOFORM `*xémonų` (acc.sg.,
**intervocalic** `m`), COUNTERPART `heofon`, class `late_analogy`.

**Critical structural observation:** OE `heofon` = h‑**eo**‑f‑**o**‑n has (a)
a back-umlaut diphthong `eo` and (b) a medial vowel `-o-` between the labial
and final `n`. Both require a vowel *following* the labial at back-umlaut time —
i.e. an **intervocalic `mV…n`** shape. A fully-adjacent `-mn-` input has no such
vowel.

## 2. Candidate CAPR heaven inputs (source-grounded, adjacent-`mn`)

| Candidate | Morphology / source | Rationale |
| :-- | :-- | :-- |
| `*xémnaz` | gen.sg./a-stem `*hemnaz` (Kroonen p. 220) | strongest — the genitive the paradigm was remodelled on; `*hemna-` is the OE stem |
| `*xémna` | bare oblique a-stem `*hemna-` | Kroonen: OE `heofon` < `*hemna-` |
| `*xémniz` | hypothetical i-variant | weak (heaven is not an i-stem); probe only |
| `*xémnō` | thematized ō | weak; probe only |

## 3. Adjacent-mn-only shadow rule (replaces the `mV…n` branch)

```foma
define PNWGmcMnDissimilation [
    {*m} -> {*β} || EnglishStarVocalic _ {*n}
];
```
No lexical conditioning; the sole trigger is post-vocalic `m` immediately before
`n`. The production `mV…n` branch is **removed** in this shadow (the whole point
of the "replace" hypothesis).

## 4. Heaven experiments (A–D)

| Cond. | Input | Rule | Output | Note |
| :-- | :-- | :-- | :-- | :-- |
| A (prod control) | `*xémonų` | production `mV…n` | `heofon` | correct |
| B (rule-only) | `*xémonų` | adjacent-mn | `heomon` | rule doesn't fire (m intervocalic) → `m` survives |
| C (cand/prod) | `*xémnaz`/`*xémna`/`*xémnō` | production `mV…n` | `hemn` | adjacent `m` not intervocalic → no dissimilation |
| C | `*xémniz` | production `mV…n` | `himn` | — |
| D (cand/adjacent) | `*xémnaz`/`*xémna`/`*xémnō` | adjacent-mn | **`hefn`** | `m→β→f` fires, but **no medial vowel, no `eo`** |
| D | `*xémniz` | adjacent-mn | **`hifn`** | same defect |

**No candidate yields `heofon`.** `HEAVEN_BEST = null`. The adjacent-`mn`
allomorphs collapse to `hefn`/`hifn`: labialization succeeds but `heofon`'s
medial `-o-` and back-umlaut `eo` are unrecoverable, because those require the
intervocalic `mV…n` shape that the "replace" rule discards.

## 5. Stem experiments (same shadow rule)

| Input | Output | Mult | Trace (changed stages) |
| :-- | :-- | :-: | :-- |
| `*stámnaz` | `stæfn` | 1 | `*stámna → SC022 *stáβna → PWGmcFinalBareALoss *stáβn → EAFBrightening *stæβn → stæfn` |
| `*stámniz` | **`stefn`** | 1 | `*stámni → SC022 *stáβni → EAFBrightening *stæβni → OEIUmlaut *steβni → OEHighVowelApocope *steβn → stefn` |

Stem works perfectly: adjacent `mn` supplies the `f`; the i-stem supplies the
i-umlaut environment; the two decisions are independent. (`stæfn` is the
attested Anglian variant.)

## 6. Blast radius (adjacent `mn` at the pre-SC022 stage)

Under current data, **only row 2216 (stem)** has adjacent `mn` at the pre-SC022
stage. Heaven's `*xémonų` has **intervocalic** `m` (not adjacent), so it is not
exposed to an adjacent-`mn` rule at all — which is exactly why the replace
breaks it.

## 7. Three corpus states

| State | Configuration | accepted | matched | mismatched | ambiguous |
| :-- | :-- | :-: | :-: | :-: | :-: |
| **P** production | current data + current SC022 | 380 | **372** | 8 | 0 |
| **R** replace-only | current data + adjacent-mn SC022 | 380 | **371** | 9 | 0 |
| **H** proposed | adjacent-mn SC022 + stem `*stámniz` (+ heaven best = none) | 380 | **372** | 8 | 0 |

- State R loses `heaven` (heofon→heomon): matched 372→371 — the direct cost of
  removing the `mV…n` branch.
- State H merely **trades** heaven for stem (heaven breaks, stem fixes): matched
  stays 372. It does **not** reach the ideal (373/7), because no heaven
  adjacent-`mn` input exists to keep heaven matched.

## 8. Complete State-H semantic diff (vs production)

| ID | concept | prod input | shadow input | old out | new out | old mult | new mult | cp | old match | new match |
| :-- | :-- | :-- | :-- | :-- | :-- | :-: | :-: | :-- | :-: | :-: |
| 2068 | heaven | `*xémonų` | `*xémonų` | `heofon` | `heomon` | 1 | 1 | `heofon` | ✓ | ✗ |
| 2216 | stem | `*stámnaz` | `*stámniz` | `stamn` | `stefn` | 1 | 1 | `stefn` | ✗ | ✓ |

Two rows change; **heaven regresses**, stem improves. No other row changes.

## 9. Multiplicity / integrity

All outputs remain multiplicity 1; no ambiguity introduced anywhere. The only
integrity failure is heaven: its output changes (`heofon → heomon`) and its
match status regresses. Every non-heaven, non-stem row is unchanged.

## 10. Future heaven data recommendation

- **PROTO:** keep `*xémenaz`.
- **PROTOFORM:** **keep `*xémonų`** (the vowel-retaining acc.sg.). It is a
  *segmental proxy*: CAPR derives `heofon` from this intervocalic form via the
  `mV…n` branch because the historically primary labialized allomorph is the
  *leveled* stem (labial from the oblique `-mn-` cluster **plus** the medial
  vowel from the full-grade nom.), which no single un-leveled input reproduces.
- **DERIVATION_CLASS:** keep `late_analogy` — the OE form reflects paradigm
  levelling/generalization of the labial into a vowel-retaining stem; that is
  exactly what `late_analogy` should denote. Do not reclassify.
- **NOTE (future):** may add that the `mV…n` treatment is a deliberate segmental
  proxy for mn-stem allomorphy (oblique labial + full-grade vowel), per the
  SC022 dossier. **Do not edit now.**

## 11. Future stem data recommendation (unchanged from prior probes)

- PROTO `*stámnaz`; PROTOFORM `*stámniz`; COUNTERPART `stefn`; class
  `early_analogy`/pre-OE stem selection. i-stem selection and `mn > βn` are
  independent; `stefn` is the archaic comparator; OE `fn > mn` (`stemn`) is a
  lexical/book matter; `*stab-` is a lexical caveat. **But this depends on the
  adjacent-`mn` branch existing in production — which the replace design does
  not provide (it breaks heaven).**

## 12. Future SC022 recommendation: UNION, not replace

**Replace is rejected.** Heaven's `heofon` genuinely requires the intervocalic
`mV…n` branch (its medial vowel + back-umlaut cannot arise from an adjacent
`-mn-` input), while stem requires adjacent `mn`. These are two distinct
*surface reflexes* of the one historical `-mn- > -βn-` change (heaven = leveled
vowel-retaining allomorph; stem = surviving cluster). The only architecture
that serves both is the **UNION**: **retain the current `mV…n` branch and ADD an
adjacent-`mn` branch** (the union was already shown clean in
`audits/2216-stefn-shadow-rule-probe.md`: stem→stefn, heaven preserved, zero
collateral). Do **not** replace `mV…n`.

## 13. Deferred (name/stage)

`PNWGmc` vs Common-Germanic staging, final SC number/name, and dissimilation-
vs-allomorphy prose remain later reconciliation issues; nothing here forces
them.

## 14. Deferred work

Production implementation (the **union** SC022, if pursued); SC022 name/staging;
row 2068 mutation (none recommended); row 2216 mutation (`*stámniz`/`stefn`,
pending union rule); baseline; reader-facing SC022 cleanup; deletion of residual
SC058 book material; final heaven and stem lexical entries.

## 15. Production integrity

`germanic.txt` unchanged (sha256 `10c61d2c…`); `germanic-aligned-final.tsv`
unchanged; baselines, manifests, book/index unchanged; row 2068 and row 2216
unchanged. All shadow work ran in the container's ephemeral `/root`.
`git diff --check` clean.

## Gate conclusion

Hard-gate conditions **fail**: (1) no source-grounded heaven allomorph yields
`heofon`; (4) the `mV…n` branch **is** required for heaven; (7,8,9) heaven's
output/match regresses under the replace. Stem passes (5,6) but cannot justify
discarding the heaven-critical branch. The scientifically correct next step is
the **union** design, not the replace.

`HISTORICAL SC022 SHADOW REDESIGN FAILS — RETAIN CURRENT SC022 FOR NOW`

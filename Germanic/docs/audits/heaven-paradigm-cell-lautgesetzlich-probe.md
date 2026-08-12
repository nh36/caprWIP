# Probe: heaven paradigm-cell (Lautgesetzlich-span) test of adjacent-`mn` SC022

**Type:** research + shadow reconnaissance. **No production change.**
**Branch:** `stem-row-2216-correction` · **HEAD at probe:** `c92f2ddb`.
Companion to `dossier-sc022-mn-dissimilation-2026.md`,
`audits/sc022-heaven-allomorph-shadow-redesign.md`,
`audits/2216-stefn-shadow-rule-probe.md`.

## 1. Research question

Applying CAPR's **longest-defensible-uninterrupted-Lautgesetzlich-span**
principle: is there a **PGmc paradigm cell → attested OE paradigm cell** pairing
for `heaven` that derives cleanly under a genuine adjacent-`mn` (`mn > βn`)
sound change — so the ahistorical surface `mV…n` proxy is unnecessary?

## 2. Reconstructed PGmc paradigm

Kroonen EDPG p. 220 (`kroonen_etymological_dictionary_pgmc.vision.txt:12428`):
PIE `*h₂ék-mōn`, gen. `*h₂k-mn-ós`, loc. `*h₂k-mén-i`, **remodelled to nom.
`*hemō`, gen. `*hemnaz`, dat. `*hemeni` on the basis of the genitive**. OE
`heofon`/OS `heban` continue the thematized **a-stem `*hemna-`** (adjacent
`-mn-`); Go `himins`, ON `himinn` continue `*hemina-`; ON dat. `hifni` shows the
oblique `-mn- > -fn-`.

| Cell | PGmc form | adjacent `mn`? | confidence | CAPR notation |
| :-- | :-- | :-: | :-- | :-- |
| nom.sg (a-stem `*hemna-`) | `*hemnaz` | yes | STRONG (Kroonen: OE `< *hemna-`) | `*xémnaz` |
| gen.sg | `*hemnas`/`*hemnaz` | yes | STRONG | `*xémnas` |
| dat.sg | `*hemni` (syncopated) | yes | PLAUSIBLE (dat. `*hemeni` unsyncopated has intervocalic m) | `*xémni` |
| dat.pl | `*hemnum(iz)` | yes | PLAUSIBLE | `*xémnum` |
| acc.sg (current CAPR) | `*hemonų` | **no** (intervocalic m) | — | `*xémonų` |

## 3. Attested OE paradigm

- **nom/acc.sg `hefen` = `heofon`** (Clark Hall 1960 p. …,
  `clark_hall_concise_anglo_saxon_dictionary.vision.txt:21259` "hefen … II. =
  heofon"; `:21485` "heofon (e) mf."). Campbell §381 (p. 135,
  `campbell_old_english_grammar.txt:10332`): **"heofon is for older hefen (CH)"**.
  Campbell §210 (`:6318`): `hefen` (front-suffix, **no** back-mutation) vs
  `heofon` (W-S u-/back-umlaut). So `hefn`/`hefen` is the **pre-back-mutation**
  form; `heofon` is the back-mutated citation form.
- **gen.sg `heofnes`** (Bosworth–Toller
  `bosworth_toller_anglo_saxon_dictionary.vision.txt:5170`), **dat.sg `heofne`**
  (`:67495`), **dat.pl `heofnum`** (`:6389`) — syncopated, `-fn-` cluster, with
  analogically-levelled W-S `eo`.

The `-fn-` outcome is exactly the CAPR **`hræfn`/`stefn`/`ofn` class** (syllabic
`-Cn` targets; the "unbroken early/Anglian" forms). Control: CAPR derives
`*xrábnaz → hræfn` (verified).

## 4. Cell-to-cell candidate matrix

| PGmc cell | OE cell | attested OE | rank | note |
| :-- | :-- | :-- | :-- | :-- |
| nom.sg `*xémnaz` | nom.sg | `hefn`/`hefen` | **STRONG** | pre-back-mutation nom, Clark Hall + Campbell §381 |
| gen.sg `*xémnas` | gen.sg | `hefnes`/`heofnes` | STRONG | eo in W-S is analogical |
| dat.pl `*xémnum` | dat.pl | `hefnum`/`heofnum` | PLAUSIBLE | eo analogical |
| dat.sg `*xémni` | dat.sg | `hefne`/`heofne` | PLAUSIBLE | i-umlaut interference (→`hifn`) |

## 5. Shadow SC022 (adjacent-mn only)

```foma
define PNWGmcMnDissimilation [
    {*m} -> {*β} || EnglishStarVocalic _ {*n}
];
```
Replaces the production `mV…n` environment (no other rule changed).

## 6. Probe results (adjacent-mn shadow)

| PGmc cell | input | prod out | shadow out | OE target | match (shadow) |
| :-- | :-- | :-- | :-- | :-- | :-: |
| nom.sg | `*xémnaz` | `hemn` | **`hefn`** | `hefn`/`hefen` | ✓ |
| gen.sg | `*xémnas` | `hemnes` | **`hefnes`** | `heofnes` (Angl. `hefnes`) | ✓ (non-WS) |
| dat.pl | `*xémnum` | `hemnum` | **`hefnum`** | `heofnum` (Angl. `hefnum`) | ✓ (non-WS) |
| dat.sg | `*xémni` | `himn` | `hifn` | `hefne` | ✗ (i-umlaut) |
| n-stem | `*xémniz` | `himn` | `hifn` | — | ✗ |

Under the **production** rule the same adjacent-`mn` inputs keep `m`
(`hemn`/`hemnes`) — the production `mV…n` proxy cannot labialize an adjacent
cluster. The adjacent-mn rule is required for the cluster.

## 7. Best successful derivation (nom.sg, full trace)

`*xémnaz` (PGmc a-stem nom `*hemnaz`) → OE nom `hefn`:
`ProtoInput *xémnaz → EAFFinalZDeletion *xémna → **SC022 PNWGmcMnDissimilation
*xéβna** → PWGmcFinalBareALoss *xéβn → OEVelarFricativePalatalization *çéβn →
OldEnglishOrthography héβn → hefn`. Every step is a real production sound change;
the `f` arises from the **literal** adjacent `mn > βn`. Corroboration: gen.sg
`*xémnas → *xéβnas → EAFBrightening *xéβnæs → OEUnstressedAEMerger *xéβnes →
hefnes`; dat.pl `*xémnum → *xéβnum → hefnum` — the whole `-fn-` oblique paradigm
falls out regularly.

## 8. Longest-span ranking

The nom.sg `*hemnaz → hefn` pairing is preferred: (1) both cells secure and
morphologically identical (nom→nom); (2) the endpoint `hefn`/`hefen` is attested
and is the historically **prior** form (Campbell §381); (3) the derivation is
entirely regular with **no analogy inside the span**; (4) it is the exact
structural analogue of the modelled `*xrábnaz → hræfn`. The later W-S
back-mutation + medial-vowel restoration (`hefn/hefen → heofon`) is the
analogical/dialectal restructuring that legitimately lies **outside** the span.

## 9. Current model vs proposed model

| | Current | Proposed |
| :-- | :-- | :-- |
| PROTOFORM | `*xémonų` (acc.sg., intervocalic m) | `*xémnaz` (nom.sg. a-stem, adjacent mn) |
| COUNTERPART | `heofon` | `hefn` (attested; = `hefen`) |
| `m→β` mechanism | **proxy** `mV…n` (ahistorical) | **literal** adjacent `mn > βn` |
| analogy inside span | back-mutation modelled, but on a proxy-labialized form | none; back-mutation left outside |
| morphology | acc.sg → nom-shape citation | nom.sg → nom.sg (clean) |
| fidelity to real SC022 | low (proxy) | high (literal cluster change) |

The proposed model is **more faithful to CAPR's longest-Lautgesetzlich-span
methodology**: literal sound change, clean cell correspondence, endpoint an
attested archaic form, analogy excluded — exactly as with `hræfn`, `find`,
`cow`, `fright`.

## 10. Outcome

**OUTCOME A — CLEAN CELL-TO-CELL SOLUTION.** A secure PGmc nom.sg `*hemnaz`
derives the attested OE nom `hefn` under the historically correct adjacent-`mn`
rule, multiplicity 1, with the oblique cells corroborating.

## 11. Corpus result (three states)

| State | Config | accepted | matched | mismatched | ambiguous |
| :-- | :-- | :-: | :-: | :-: | :-: |
| **P** | production | 380 | 372 | 8 | 0 |
| **R** | adjacent-mn rule, current data/targets | 380 | 371 | 9 | 0 |
| **H** | adjacent-mn rule + heaven(`*xémnaz`/`hefn`) + stem(`*stámniz`/`stefn`) | 380 | **373** | **7** | 0 |

**State H = the ideal 380/373/7/0.** Semantic diff vs P — **exactly two rows**:

| ID | concept | prod in→out (cp) | H in→out (cp) | P match | H match |
| :-- | :-- | :-- | :-- | :-: | :-: |
| 2068 | heaven | `*xémonų`→`heofon` (`heofon`) | `*xémnaz`→`hefn` (`hefn`) | ✓ | ✓ |
| 2216 | stem | `*stámnaz`→`stamn` (`stefn`) | `*stámniz`→`stefn` (`stefn`) | ✗ | ✓ |

Heaven stays matched (now via a historically clean model); stem becomes matched;
every other row unchanged; no multiplicity/ambiguity change. Remaining 7
mismatches: buck, fire, fowl, rust, tap, wolf, wool.

State R shows the cost of the adjacent-mn rule **without** retargeting heaven
(heaven 372→371) — i.e. the proxy is only needed while heaven targets `heofon`.

## 12. Consequence for SC022

**The cell-to-cell evidence supports eventually deleting the `mV…n` proxy and
retaining only the literal adjacent `mn > βn`.** This *reverses* the narrower
finding of `sc022-heaven-allomorph-shadow-redesign.md` (which fixed heaven's
target at `heofon` and therefore required the proxy / a union). Once heaven is
retargeted to its regular adjacent-`mn` outcome `hefn`, the pure adjacent-mn
rule serves **both** heaven and stem with zero collateral (State H). The
"replace" architecture becomes viable — **conditional on the row-2068
retargeting** and a full production regression at implementation time.

## 13. Consequence for row 2068 (future, do not edit)

- **PROTO:** could remain `*xémenaz` (lexeme citation) or move to `*xémnaz`;
  recommend keeping the citation `PROTO` and setting the derivational
  `PROTOFORM`.
- **PROTOFORM:** `*xémnaz` (PGmc a-stem nom `*hemnaz`, adjacent `mn`).
- **COUNTERPART:** `hefn` (attested pre-back-mutation nom, Clark Hall/Campbell
  §381; CAPR `-fn` class as `hræfn`/`stefn`/`ofn`). `heofon` becomes a
  comparison form (back-mutated citation).
- **DERIVATION_CLASS:** **`regular`** — under this model `hefn` is the regular
  Lautgesetzlich outcome; the current `late_analogy` reflected the proxy. The
  analogical back-mutation to `heofon` is now outside the modelled span.
- **NOTE (future):** PGmc mn-stem; a-stem nom `*hemnaz` → `hefn` by adjacent
  `mn > βn` (+ regular changes); W-S back-mutation `hefn/hefen → heofon` is a
  later analogical/dialectal restructuring left unmodelled (cf. `hræfn`).

## 14. Consequence for row 2216

`*stámniz → stefn` (mult 1) is independently reconfirmed under the same
adjacent-mn rule; `*stámnaz → stæfn`. i-stem selection (i-umlaut environment)
and `mn > βn` (the `f`) remain independent. Unchanged from prior probes.

## 15. Production integrity

`germanic.txt` unchanged (sha256 `10c61d2c…`); `germanic-aligned-final.tsv`,
baselines, manifests, book/index unchanged; rows 2068 and 2216 unchanged. All
shadow work ran in the container's ephemeral `/root`. `git diff --check` clean.

## Gate

A secure PGmc nom.sg cell derives the corresponding attested OE nom cell under
literal adjacent `mn > βn`, multiplicity 1, and the full corpus reaches the
ideal 380/373/7/0 with zero collateral.

`HEAVEN CELL-TO-CELL SOLUTION FOUND — HISTORICAL SC022 CLEANUP IS VIABLE`

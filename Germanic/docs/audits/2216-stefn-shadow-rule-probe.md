# Experimental probe: adjacent-`mn` dissimilation shadow rule for `stefn` (row 2216)

**Status:** experimental / non-production reconnaissance. **No production change made.**
**Branch:** `stem-row-2216-correction` · **HEAD at probe:** `4510f316`
**Production `germanic.txt` sha256 (unchanged):**
`3646acc6a4d69d64a7585bb4a7f6bff9693f15a9e42e52a6b71ed998fc5bf29f`

This documents a controlled shadow-FST experiment testing whether a minimal,
historically-motivated extension of `PNWGmcMnDissimilation` to adjacent `mn`
would derive attested OE `stefn` from the source-supported i-stem input
`*stámniz`, and what it would do to the rest of the corpus. Cross-references:
`dossier-stem-2026.md`, `dossier-stem-consonant-variation-2026.md`.

## 1. Current production rule

`Germanic/fsts/germanic.txt:2151-2153`, **SC022** `PNWGmcMnDissimilation`
("Proto-Northwest Germanic Mn Dissimilation", cascade order 22), between
SC021 `PNWGmcUnstressedORaising` and SC023 `PNWGmcNStemNLoss`
(`germanic.txt:3136-3138`). Cited: Fulk §6.14 (germanic.txt comment; the
quoted passage is actually §6.11, p. 121), Kluge–Seebold s.v. Himmel.

```foma
define PNWGmcMnDissimilation [
    {*m} -> {*β} || EnglishStarVocalic _ EnglishStarVocalic EnglishStarConsonant* EnglishStarNasal
];
```

- Output symbol: `{*β}` (voiced bilabial fricative). Surface `f` is produced
  later by the orthography rule `{*β} -> f` (`germanic.txt:902`).
- Environment: **`V m V C* N`** — `m` must be **intervocalic**, with a nasal
  (`{*m}|{*n}`) later in the word. This is the `heofon` (`*xemonų`) pattern.
- **Why `*stámniz` does not meet it:** in `st-á-m-n-i-z` the `m` is
  immediately followed by `n` (a consonant), so the right context
  `_ EnglishStarVocalic` (vowel immediately after `m`) fails. The rule cannot
  fire on the adjacent `-mn-` cluster; the production cascade keeps `mn` and
  yields `*stámniz -> stemn`.

### Existing production applications (stage-diff, all 380 OE rows)

Comparing the prod stage bins immediately before vs after SC022:

| Row | Concept | PROTOFORM | before SC022 | after SC022 |
| :-- | :-- | :-- | :-- | :-- |
| 2068 | heaven | `*xémonų` | `*xémunų` | `*xéβunų` |

**Exactly one** corpus row currently triggers SC022: `heaven`. Full prod trace:
`*xémonų → PNWGmcUnstressedORaising *xémunų → PNWGmcMnDissimilation *xéβunų →
OEMedUnstressedULowering *xéβonų → OEVelarFricativePalatalization *çéβonų →
OEBackMutation *çéoβonų → OEHighVowelApocope *çéoβon → OldEnglishOrthography
héoβon → heofon`. The `m→β` step is SC022; surface `f` is `{*β} -> f`
at OldEnglishOrthography. No separate voicing/normalization step is involved.

## 2. Historical plausibility (source adjudication)

- **A. General process — YES.** Polomé 1967 (pp. 818–819): Germanic
  `-mn- > *-bn-`. Fulk §6.11 (p. 121): "In the cluster mn, the first
  consonant tends to lose its nasality by dissimilation." Kroonen 2011
  (p. 183): OE `stefn`/`heofon` show "vocalization of the m".
- **B. Existing CAPR env — YES.** The intervocalic `heofon` environment is
  the canonical example (Fulk §6.11; Kluge–Seebold s.v. Himmel).
- **C. Adjacent `mn` — YES, explicitly.** Polomé 1967 (p. 819) cites
  **OE `stefn : stemn` 'prow'** (vs ON `stafn`, OS `stamn`) as an instance of
  the very same `-mn- ~ -bn-` alternation — the adjacent-cluster case.
- **D. Regularity — WEAK / lexically levelled.** Fulk: "the results are
  hardly regular," and the reverse `bn > mn` "is well attested in NWGmc";
  the `stefn/stemn` etymology is "rather insecure." Broad tendency with
  paradigm leveling, not an exceptionless law.
- **E. Row 2216 — DEFENSIBLE TO TEST.** The word is a genuine `-mn-` cluster
  in the right family; a controlled experiment is warranted (not a proof).
- **F. Alternative — RECORDED.** Torp (via Orel p. 371; Polomé p. 819 n. 2)
  links ON `stafn`/OE `stefn` to a separate root `*stab-` 'staff, post',
  under which the `f` is root-etymological and mn-dissimilation is *not* the
  explanation. This must be resolved before any production rule.

## 3. Blast radius (stage-level, empirical)

Rows whose form contains adjacent `mn` at the input to SC022 (all 380 OE rows
scanned via the prod `after_pnwgmc_unstressed_o_raising` stage bin):

| Row | Concept | PROTOFORM | form before SC022 |
| :-- | :-- | :-- | :-- |
| 2216 | stem | `*stámnaz` | `*stámna` |

**Exactly one** OE row is exposed to an adjacent-`mn` branch. No other corpus
form develops adjacent `mn` by that stage.

## 4. Candidate shadow rule (minimal test)

Only the second (adjacent) branch is added; the existing branch is untouched:

```foma
define PNWGmcMnDissimilation [
    {*m} -> {*β} || EnglishStarVocalic _ EnglishStarVocalic EnglishStarConsonant* EnglishStarNasal ,
    {*m} -> {*β} || EnglishStarVocalic _ {*n}
];
```

Rationale: it is a **phonological** environment (post-vocalic `m` directly
before `n` → `β`), parallel to the existing rule's post-vocalic left context,
not a lexical hack; it is the smallest addition that lets a `-mn-` cluster
undergo the same `m→β` the rule already performs intervocalically.

## 5. Row-2216 result (`*stámniz`)

- **Accepted; output set `{stefn}`; multiplicity 1.** Critical success
  condition met: unique `stefn`.

Shadow trace (changed stages only):
`*stámniz → EAFFinalZDeletion *stámni → **SC022 PNWGmcMnDissimilation *stáβni**
→ EAFBrightening *stæβni → SC055 OEIUmlaut *steβni → SC063 OEHighVowelApocope
*steβn → OldEnglishRemoveStars stefn` (surface `{*β} -> f`).

Stage roles: (1) form before SC022 = `*stámni`; (2) dissimilation output
`*stáβni`; (3) i-mutation `*a→*e` at SC055; (4) final `*z` removed earlier at
SC020; (5) final high vowel `*i` lost at SC063; (6) intermediate `*β → f` at
OldEnglishOrthography/RemoveStars; (7) final `stefn`.

Production trace for contrast (mn retained): `*stámni → SC055 *stemni →
SC063 *stemn → stemn`.

## 6. Existing-rule control (`heaven`)

`heaven` (`*xémonų`) is **identical** under prod and shadow — same output
`heofon` and byte-identical stage trace (SC022 fires via the *intervocalic*
branch; the adjacent branch is not reached). The extension does not disturb
the currently-modelled environment.

## 7. Full-corpus shadow semantic diff (prod vs shadow, 380 OE rows)

**Every** changed row (no omissions):

| Row | Concept | PROTOFORM | prod out | shadow out | prod mult | shadow mult | counterpart | prod match | shadow match |
| :-- | :-- | :-- | :-- | :-- | :-: | :-: | :-- | :-: | :-: |
| 2216 | stem | `*stámnaz` | `stamn` | `stæfn` | 1 | 1 | `stefn` | no | no |

**Totals (identical):** prod = shadow = accepted 380, matched 372,
mismatched 8, ambiguous 0.

Note: the corpus row uses the **production PROTOFORM `*stámnaz`** (a-stem,
no i-trigger), so the shadow yields `stæfn` (brightening `a→æ` after `m→β`,
no i-umlaut), *not* `stefn`. Deriving `stefn` requires the shadow rule **plus**
the researched i-stem input `*stámniz`. The two changes are entangled.

## 8. Scientific classification of the one changed row

- **Row 2216, `*stámnaz → stæfn` (production input): SUPPORTED / PLAUSIBLE.**
  `stæfn` is an **attested** (non-WS / Rushworth¹-Anglian) shape of the
  family (Campbell §484, p. 195; Bülbring §485, p. 191, "Ru.¹ hat stemn neben
  stæfn"). The shadow does not produce any historically wrong form. It merely
  fails to equal the *selected* WS comparator `stefn` because the production
  input is the a-stem, not the i-stem.
- **No PROBLEMATIC or UNKNOWN collateral rows** — the blast radius is a single
  word and heaven is untouched.

## 9. Open questions for a future sound-change dossier

1. Regularity/exceptions of adjacent `mn > βn`: the corpus exposes only one
   word, so regularity **cannot** be established computationally — needs
   source adjudication (Fulk: "hardly regular").
2. Are adjacent `mn` and intervocalic `mVn` (heaven) **one** sound change
   (unifying SC022) or two? Rule name/formulation depends on the answer.
3. Chronology (Common Gmc vs PNWGmc vs Anglo-Frisian) and **ordering vs
   EAFBrightening**: the shadow shows brightening applying after `m→β` (giving
   `æ` from the a-stem) — is that ordering historically correct?
4. The `*stab-` (Torp) alternative: if `stefn` is from 'staff', this rule is
   the wrong explanation for the word.
5. Which is the correct selected comparator — WS `stemn` (mn-retention,
   current cascade), general/base `stefn` (shadow rule), or Anglian `stæfn`?
   The variation dossier argues `stefn` is the base and `stemn` the WS
   secondary.
6. Exact conditioning: require preceding vowel? before `n` only vs any nasal?
   geminate-`nn` and cluster interactions?
7. Entanglement with the PROTOFORM decision: rule-alone → `stæfn`;
   rule + i-stem `*stámniz` → `stefn`. The dossier must treat them together.
8. Is "dissimilation" still the right label if the adjacent case is modelled?

## 10. Production integrity (verified)

- `Germanic/fsts/germanic.txt` — **byte-unchanged** (sha256 `3646acc6…bf29f`).
- `Germanic/data/germanic-aligned-final.tsv` — unchanged (`b685b849…7faf`).
- `Germanic/fsts/old_english_sandbox.txt` — unchanged (`12faa355…88d15`).
- Baselines, manifests, book/Index Verborum, row 2216, `PNWGmcMnDissimilation`
  — unchanged. All shadow work ran in the container's ephemeral `/root`
  (never a mounted repo path). Working tree clean; `git diff --check` passes.

## 11. Reproducibility

Inside the backend container, on ephemeral copies (never the repo):
1. `cp fsts/germanic.txt` + `fsts/old_english_sandbox.txt` to `/root/prod` and
   `/root/shadow`.
2. In the shadow `germanic.txt`, replace the single-branch SC022 body with the
   two-branch rule in §4.
3. Build each: `foma -q -l fsts/germanic.txt -e quit` then
   `foma -f fsts/old_english_sandbox.txt` (writes bins to that CWD).
4. `flookup -i <tree>/old_english.bin` per normalized PROTOFORM; diff prod vs
   shadow output sets; trace via `oe_full_trace_report.trace_lexeme`.

## 12. Recommendation

The shadow experiment is the strongest possible positive result: `*stámniz`
→ `stefn` uniquely (multiplicity 1); the entire blast radius is a single
corpus row (2216); heaven and all other rows are untouched; global totals are
unchanged; and the only collateral output (`stæfn` from the production a-stem)
is itself an attested variant. Historically the extension is source-motivated
(Polomé, Fulk, Kroonen) but its **regularity and the `*stab-` alternative are
unresolved**, which is exactly what a dedicated sound-change dossier must
settle before any production rule change.

`SHADOW STEFN HYPOTHESIS PASSES — RESEARCH THE SOUND CHANGE NEXT`

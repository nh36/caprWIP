# `*skúldrō → *skúldru` ('shoulder'): is it a sound law, or a paradigm‑class transfer?

A focused follow‑up to `Germanic/docs/dossier-shoulder-2026.md`. The
prior dossier surveyed the philology, the project precedents, and the
five fix options. This dossier asks the *single, narrow* question
that the prior dossier deferred:

> Is the change `*skúldrō (fem. ō‑stem nom.sg.) → *skúldru (the input
> form that yields OE `sculdor` lautgesetzlich)` a **regular sound
> law** of (P)NWGmc, or is it a **morphological / analogical** change
> (paradigm‑class transfer, back‑formation from the plural cell)?
>
> If the latter, does this lexeme belong in the project's "wontfix"
> bin alongside `wool, wolf, fugol, bucca, rust`, where Neogrammarian
> phonology is known to fail and the project explicitly does not chase
> the mismatch?

The answer determines which of three remediation options the project
should adopt for TSV row 2183.

> ## RETRACTION (2026-04-28, post-NH review)
>
> **The "Option Y (cell-switch)" recommendation below — PROTOFORM
> `*skúldru` (NApl) → COUNTERPART `sċuldor` (NSg) — is withdrawn.**
>
> NH pointed out that this is a **cross-cell** mapping
> (PNWGmc plural input → OE singular output) with no project
> precedent. Verified: existing non-NSg rows are cell-consistent
> (`*xámaras` GenSg → `hameres` GenSg; `*spéru` NApl → `speoru`
> NApl; `*wúndrą` NSg → `wundor` NSg). The dossier below assumes
> a policy of "PROTOFORM names whatever paradigm cell yields the
> COUNTERPART by sound change" — that is not the project's
> policy.
>
> The lautgesetz analysis itself (§§1–7) is unaffected and
> remains valid: the PNWGmc *-ō > *-u shortening rule
> (`NWGmcFinalLongORaising`) is in the cascade but cannot be
> reordered before u-lowering without regressing
> `*nosu / sorg / sċofl`; `*skuldrō` is not in R/T §2.3.1's
> labial-adjacency wontfix bin; the /uRCr/ cluster is not
> promoted to a Neogrammarian rule by any source. What changes
> is the conclusion. With Option Y withdrawn:
>
> * **Option Y' (plural-to-plural, cell-consistent)** —
>   PROTOFORM `*skúldru` → COUNTERPART `sċuldru`. Cell-consistent
>   and well-attested (Luick §247). FST currently apocopates *-u
>   after the heavy stem and produces `sċuldor`, so this is a
>   mismatch unless a /uRCr/ apocope blocker is added — which
>   the present dossier already showed lacks Neogrammarian
>   support. Future work, not a current fix.
> * **Option X (wontfix)** — now reinstated as the principled
>   answer. The reasoning is amended: the rejection in the body
>   of this dossier rested on R/T §2.3.1 not listing the lexeme,
>   but R/T §2.3.1 is not the only entry criterion. The actual
>   criterion is "no cell-consistent reconstruction yields the
>   attested form by regular sound change in the cascade." That
>   criterion *is* satisfied here:
>   * Empirical probe confirms `*skúldrą` and `*skúldraz` both
>     u-lower to `sċoldor`. *wúndrą's escape relies on its
>     nasal+C, which shoulder lacks.
>   * The `*skúldru` plural cell yields `sċuldor` lautgesetzlich
>     but only by violating cell-consistency — i.e. by a
>     paradigm-class transfer (back-formation of NSg from NApl)
>     that is morphological, not phonological, and outside the
>     cascade's scope.
> * **Option Z (add /uRCr/ rule)** — unchanged: lacks source
>   support and would regress other rows.
>
> **Recommendation post-retraction:** Option X (wontfix). Add
> shoulder to the exception column of
> `Germanic/docs/debug_snapshots/oe_known_problems_report.txt`
> with rationale "no cell-consistent PGmc/PWGmc reconstruction
> yields the attested NSg `sċuldor` by regular sound change;
> NSg /u/ is preserved by post-Neogrammarian morphological
> back-formation from the *skúldru-class plural (Luick §247),
> which is outside the cascade's scope."
>
> Sections below are preserved for historical record. Sections
> 1–7 (the lautgesetz analysis) remain accurate; only the
> Option-Y recommendation in §8 is wrong.

The dossier is organised in eight sections plus an executive summary
and a sources block:

1.  The PNWGmc *‑ō > *‑u shortening: rule, sources, status in the
    cascade.
2.  Empirical trace of `*skúldrō` and the counter‑feeding problem.
3.  Reordering test: would shortening‑before‑lowering save us, and at
    what cost?
4.  Relative chronology in the literature.
5.  The "wool / wolf / fugol" wontfix bin: what it is, why it is what
    it is.
6.  Is `*skuldrō` in that bin, in a different bin, or in no bin at
    all?
7.  Classification of the change: which of (a)–(d) best fits?
8.  Recommendation across Options X, Y, Z.

Citations follow the prior dossier's conventions; where a citation
could not be verified in the session a `[citation needed]` marker is
used rather than an invented page number.

---

## 1.  The PNWGmc *‑ō > *‑u shortening

### 1.1  The rule, in our cascade

`Germanic/fsts/germanic.txt` line 2008, defining
`NWGmcFinalLongORaising`:

```foma
# R/T vol.2 p.267: "word-final bimoric non-nasalized long *-ō became
# short *-u in unstressed syllables in PNWGmc."
# Examples: PGmc *gebō > PNWGmc *gebu, PGmc *feþrō > PNWGmc *feþru.
# This does NOT apply to: nasalized *ǭ (fem. n-stem), trimoric *ô (masc. n-stem).
define NWGmcFinalLongORaising [
    {*ō} -> {*u} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

The structural description is: `*ō → *u` after `V C+` at the right
edge of the word (`.#.`).  By construction:

*   Monosyllables (`*bō, *kō, *twō, *xwō`) are excluded — they have no
    pre‑nuclear vowel to satisfy `EnglishStarVocalic` and are handled
    instead by `NWGmcStressedMonosyllableORaising` at line 1993
    (`*ō → *ū`, the "lengthening" branch of Campbell §122 / Fulk
    §4.11 / R/T §3.1.4).
*   The nasalised *ǭ* of fem. n‑stem nom.sg. (`*tungǭ`) and the
    trimoric *ô* of masc. n‑stem nom.sg. (`*gumô`) are distinct
    symbols, not matched by `{*ō}`.
*   The rule fires bluntly on every other final `*‑ō`.

### 1.2  Source authority

*   **Ringe & Taylor, *Linguistic History of English* vol. 2** p.
    266–267 (per the prior dossier's citation; cross‑checked against
    the FST comment block at line 1997–2010): "It is clear that PGmc
    word‑final bimoric non‑nasalized long *‑ō became short *‑u in
    unstressed syllables in PNWGmc."  R/T explicitly date this to
    PNWGmc, *before* the WGmc node.  See also their PWGmc inventory at
    vol. 2 p. 142, which already cites `*skuldru` (with stem‑final
    `‑u`) as the PWGmc reconstruction.
*   **Campbell §331(5)** "n.s.f. of weak nouns, *tunge* < *‑ōn"
    (referenced inline in the FST comment block at line 2071) — the
    same phenomenon for n‑stems via *‑ōn → *‑æ → *‑e.
*   **Fulk §5.2 / §4.11** parallel coverage of the
    apocope / shortening rule in his *Comparative Grammar* (cross‑
    referenced in the FST comment block at line 2004 and in
    DEV_NOTES §17.31).
*   **Brunner §§143–149** on apocope and shortening of long final
    vowels in the West Germanic branch (cross‑referenced at line
    2005).

### 1.3  Pipeline outputs that depend on the rule

Empirically, the rule is essential to every ō‑stem nom.sg. and every
neuter‑stem nom.acc.pl. derivation in the cascade.  Sample derivations
that **succeed** because this rule fires:

| PROTOFORM | After `NWGmcULowering` | After `NWGmcFinalLongORaising` | Surface | Attested |
|---|---|---|---|---|
| `*xornō` | `*xornō` (no lowering trigger; nasal in cluster) | `*xornu` | `horn` | ✓ |
| `*gebō` | `*gebō` (next syll is the suffix; e is high‑ish, but lowering env. requires non‑high *next*) | `*gebu` → `giefu` | `giefu` | ✓ |
| `*feþrō` | `*feθrō` | `*feθru` → `feder` | `feder` | ✓ |
| `*núsō` | `*nósō` (← lowering fires!) | `*nósu` → `nosu` | `nosu` | ✓ |
| `*súrgō` | `*sórgō` (← lowering fires) | `*sórgu` → `sorg` | `sorg` | ✓ |
| `*skúflō` | `*skóflō` (← lowering fires) | `*skóflu` → `sċofl` | `sċofl` | ✓ |

In other words, the rule is correct, well‑sourced, and load‑bearing.
It is **not** missing from the cascade.

---

## 2.  Empirical trace of `*skúldrō` and the counter‑feeding problem

### 2.1  Live trace

```
$ python3 Germanic/tools/trace_old_english_sandbox.py \
      --lexeme '*skuldrō' --bin-dir Germanic/fsts
=== *skuldrō ===
…
BreakingLengthening: *s*k*o*l*d*r*u
…
WeightCleanup:        *ʃ*o*l*d*r
…
Surface:              sċoldor
```

(The intermediate stages between `ProtoInput` and `BreakingLengthening`
return `+?` for this proto in the bundled trace tool because the
sandbox bins are partial; the full pipeline rebuild gives the same
endpoint.  See `oe_known_problems_report.txt` line 51:
`*skúldrō → sċoldor (expected sċuldra)`.)

### 2.2  What the cascade does, step by step

1.  Composition order (`germanic.txt` line ~2886 onwards):

    ```
    NWGmcILowering
        → OEWsPalatalGlide
        → NWGmcULowering              ← line 2893
        → NWGmcStressedMonosyllableORaising
        → NWGmcFinalLongORaising      ← line 2904
        → PGmcFinalZDeletion
        → …
    ```

2.  When `NWGmcULowering` (line 1920) sees `*s k ú l d r ō`, the
    structural description is satisfied:
    `.#. EnglishStarConsonant* _ [EnglishStarConsonantNoJ - EnglishStarNasal] EnglishStarConsonantNoJ* EnglishStarNonHighVowel`.
    The `*ú` is preceded only by consonants (`sk‑`); the right context
    is `l d r ō` — a non‑nasal consonant `l`, more non‑j consonants
    `d r`, and the non‑high vowel `*ō`.  Lowering fires:
    `*skúldrō → *skóldrō`.

3.  When `NWGmcFinalLongORaising` (line 2008) then sees
    `*s k ó l d r ō`, the structural description is also satisfied:
    `EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.`.
    Final long `*ō` shortens: `*skóldrō → *skóldru`.

4.  Apocope, sonority repair (`d r → d V r`), palatalisation of
    `sk‑ → sċ‑`, and orthography then yield surface `sċoldor`.

### 2.3  The counter‑feeding diagnosis

The two PNWGmc rules **could in principle** have applied in either
order.  In the actually applied order:

```
*skúldrō   --[ULowering]-->   *skóldrō   --[ORaising]-->   *skóldru   →   sċoldor   ✗
```

In the hypothetical reverse order:

```
*skúldrō   --[ORaising]-->   *skúldru   --[ULowering]-->   (vacuous: next-syll *u is HIGH)   →   sċuldor   ✓
```

The reverse order *would* derive an attested OE form (`sċuldor`,
strong masc.; or, with appropriate paradigm cell, `sċuldru` plural).
This is the user's hypothesis, and at first glance it looks
attractive.  §3 examines whether we can actually reorder.

---

## 3.  The reordering test

### 3.1  Collateral damage

The prior dossier §10.3 enumerates the OE rows whose PROTOFORM matches
the schema `*[uú]Cō`:

```
2034   *fúrxtiθō    fyrhtu
2114   *lúnganjō    lungen
2143   *núsō        nosu
2162   *rústō       rust          (already wontfix)
2183   *skúldrō     sċuldra       (this dossier)
2185   *skúflō      sċofl
2200   *súrgō       sorg
2300   *wúllō       wull          (already wontfix)
```

I have spot‑checked rows 2143, 2185, 2200 in the live TSV
(`Germanic/data/germanic-aligned-final.tsv`):

| ID | PROTOFORM | OE COUNTERPART (col 6) | Modern gloss |
|---|---|---|---|
| 2143 | `*núsō` | `nosu` | nose |
| 2185 | `*skúflō` | `sċofl` | shovel |
| 2200 | `*súrgō` | `sorg` | sorrow |

All three attest the **lowered** root vowel `o`, *plus* a high‑vowel
suffix in *nosu* (or apocope after a heavy syllable in *sorg, sċofl*).
That is exactly the pattern of "lowering THEN shortening": the suffix
is allowed to do its quantity work *after* the root vowel has already
been a‑mutated.

If we swap the order, the predicted outcomes regress:

| Proto | Reordered output | Attested | Status |
|---|---|---|---|
| `*núsō` | `*nusu → nusu` | `nosu` | REGRESSION |
| `*súrgō` | `*surgu → surg` | `sorg` | REGRESSION |
| `*skúflō` | `*skuflu → scufl` | `sċofl` | REGRESSION |

These are not minor lexemes.  *Nosu* is the standard NWGmc nose word;
*sorg* is the Christian‑poetic abstract; *sċofl* is the Bald's
Leechbook implement.  They are well‑attested and the FST currently
gets them right *because* lowering bleeds into shortening, not the
other way around.

### 3.2  Verdict on reordering

Reordering is not on the table.  The current order (lowering first,
shortening second) is **forced by the OE data** as it stands in the
TSV.  Whatever the historical chronology was, the cascade has to
produce the lowered form for *nosu/sorg/sċofl*; if the formal
description of `NWGmcULowering` requires the suffix `*ō` to still be
present at the moment lowering applies, then the shortening must come
later.  This is a constraint on the **FST architecture**, not on the
historical phonology.

---

## 4.  Relative chronology in the literature

> Is there *any* scholar who orders shortening **before** a‑mutation?

A focused source check.  None of the four standard handbooks the
project leans on commits to a strict ordering of the two rules; what
they say is consistent with the FST's data‑driven order.

### 4.1  Campbell

*   **§§115–118** (a‑mutation of *u, i*).  Campbell describes
    a‑mutation as a NWGmc/early‑OE change conditioned by a non‑high
    vowel in the following syllable, and lists the standard
    blocking environments (nasal+C in §116; single *m* in §117;
    single *n* in §118).  He does not relate it explicitly to *‑ō
    > *‑u shortening.
*   **§331ff.** (apocope and shortening).  §331(5) explicitly
    derives weak‑noun nom.sg. *tunge* from *‑ōn via shortening;
    quantity reduction of *‑ō, *‑ē in unstressed final position is
    treated as a late PWGmc/OE event.  Campbell does not give a
    chronology relative to a‑mutation.
*   **§122** parallel monosyllabic lengthening (*ō > *ū) — used by
    `NWGmcStressedMonosyllableORaising`, no bearing here.

Campbell is silent on the relative ordering.

### 4.2  Hogg

*   **§§5.10–5.16** of *A Grammar of Old English* vol. 1 cover
    a‑mutation and the OE vowel system more generally.  Hogg
    (following Campbell) treats a‑mutation as a NWGmc innovation
    and places `‑ō > ‑u` (where it occurs) within the same NWGmc
    period.  Hogg does **not** give a chronological ordering of the
    two rules and uses the term "lautgesetzlich" precisely for
    cases where the OE outcome is regular: *full, wulf, fugol* are
    flagged as exceptions, not as products of a competing rule
    ordering.  [Page references not verified in this session;
    treat as `[citation needed]` for the exact subsection numbers.]

### 4.3  Brunner

*   **§§29ff.** (PGmc / PWGmc final‑vowel history).  Brunner
    treats the shortening of long final *‑ō to *‑u as a
    pre‑literary West Germanic event ("vorhistorisch im
    Westgermanischen geschehen"), prior to the documented OE
    period.  §63 (a‑umlaut of *u) is described in OE‑internal
    terms.  Brunner does **not** explicitly order the two rules
    relative to each other; in his discussion of `wulf ~ wolf`
    (§68) he attributes the divergence to the influence of
    inflected forms with a high vowel in the next syllable
    (*wulfes, wulfi*) — i.e. an **analogical** explanation, not a
    rule‑ordering one.

### 4.4  Ringe & Taylor

*   **vol. 2 §3.1**.  R/T treat *‑ō > *‑u shortening as a
    PNWGmc innovation (vol. 2 p. 267).  The *immediately preceding*
    discussion of a‑mutation (vol. 2 §2.3.1, pp. 27–33) treats it
    as also PNWGmc, but the two changes are described in separate
    subsections without a stated mutual order.  The closest R/T
    come to a chronology is:

    > "the sequence of changes would have been: 1. word‑final *‑ō
    > > *‑ū; 2. word‑final long high vowels were shortened in
    > unstressed syllables." (vol. 2 p. 267, quoted in the prior
    > dossier §10.5)

    R/T's PWGmc inventory (vol. 2 p. 142) cites `*skuldru` with
    stem‑final `‑u` already in PWGmc — i.e. for *this lexeme* they
    reconstruct the post‑shortening form as the inherited
    starting‑point.  They do **not** explain why; they list it
    side‑by‑side with the unproblematic items.

*   **vol. 2 §2.3.1 pp. 32–33** lists the labial‑adjacency
    exceptions to a‑mutation: `*fullaz, *wulfaz, *fuglaz,
    *tulga‑`, *ofer / ufan(e)*.  R/T conclude: "We do not really
    know why *u* failed to lower in these forms" (DEV_NOTES line
    85; cross‑referenced in `germanic.txt` line 1911).  **The
    inventory does not include `*skuldrō / *skuldru.`**

### 4.5  Luick

*   **§188** (a‑mutation), **§247** (Dehnung in /uRCr/ clusters).
    Luick handles a‑mutation in §78ff. and rejects Bülbring's
    "labial + long/closed l" rule on the basis of `wolcen, folc,
    folde, folm, bolla, bolt, molde, smolt`.  His own account
    (§78 Anm. 3) is paradigmatic levelling.
*   §247 enumerates a different cluster of items where
    *Dehnung unterblieb* in heavy clusters: *cildru, sculdru,
    wundru, gyrdlas, englas, fyrðran, hundred, timbrian,
    wundrian, heardre*. This is the cluster that interests us;
    Luick describes it for the lengthening rule, not for
    a‑mutation, but the lexemes involved are exactly those where
    high *u* survives in the plural cell.

### 4.6  Verdict on ordering

No scholar in the standard handbooks I have access to **explicitly**
orders shortening before a‑mutation.  R/T's bare list of two PNWGmc
events is the closest, and it does not commit to a single ordering.
The FST cascade's order (a‑mutation first, shortening second) is
**compatible with** the standard chronology and is **forced by the
OE data** for *nosu, sorg, sċofl*.

Therefore: `*skuldrō`'s mismatch is **not** a case of "the cascade has
the wrong rule order"; it is a case where the data requires the
attested order, and `*skuldrō` is the *one* row of the
`/[uú]Cō/` schema where the attested order produces the wrong
result.

---

## 5.  The "wool / wolf / fugol" wontfix bin

### 5.1  Where the bin lives in the project

*   **`Germanic/docs/debug_snapshots/oe_known_problems_report.txt`**
    lines 66–94, the `WONTFIX (6)` block.  Five of the six entries
    are the `u_lowering_near_labial` cluster:
    * `*búkkaz → bocc (expected bucc)`
    * `*fúglaz → fogol (expected fugol)`
    * `*rústō → orst (expected rust)`
    * `*wúlfaz → wolf (expected wulf)`
    * `*wúllō → woll (expected wull)`

    Each entry cites Luick §105–6 and R/T vol. 2 §2.3.1.  The sixth
    wontfix entry (`*ráukaz → rēac`, expected `rēc`) is unrelated
    (Anglian smoothing).

*   **`Germanic/docs/DEV_NOTES.md`** §17.10.34 ("Cluster: u‑lowering
    'exceptions' (wulf, fugol, bucc, rust, wull) — paradigm‑cell
    switch for 4/5") at line 25838 documents the strategy.  The
    section's source audit (lines 25855–25920) collects:
    *   **Stiles 2012 §4.1.1.2**: the only blocking environment for
        a‑mutation is a nasal‑initial intervening cluster.
        Geminates, labials, liquids do **not** block.
    *   **Campbell §115**: lists `full, fugol, bucca, wulf` by name
        as exceptions; explicitly notes OHG has the regular lowered
        forms `foll, fogal, boch, wolf`.
    *   **Brunner §68**: same exceptions; attributes them to
        analogical levelling from oblique cells with a high vowel
        in the next syllable (instr.sg. *wulfi*, gen.sg. *wulfes <
        *‑is*).
    *   **Luick §105–6** (cited at `germanic.txt` line 1911): "u
        retained near labials in specific lexical items, but this
        is irregular."
    *   **R/T §2.3.1** (vol. 2 pp. 32–33): "We do not really know
        why *u failed to lower in these forms."

### 5.2  Why the project's bin is "wontfix" and not "fix‑with‑a‑rule"

DEV_NOTES §17.10.34 lays out the explicit reasoning at lines
25921–25935.  Adding a labial‑ or geminate‑conditioned blocker to
`NWGmcULowering` would:

*   Contradict Stiles 2012 §4.1.1.2 explicitly.
*   Contradict Campbell §§115–116 explicitly.
*   Cause regressions in correctly‑derived forms with similar
    environments — notably the regular class II/III/IV strong‑verb
    past participles `boren, coren, holpen` (Campbell §115 cites
    these as the textbook regular outcomes).  A "block before
    labials" rule would break `boren`.
*   Violate `skills/be-lautgesetzlich.md`: "favour the consensus
    over a workaround that contradicts the consensus."

The chosen approach for 4 of the 5 cases (DEV_NOTES line 25936ff.) is
**paradigm‑cell switch**: change the per‑row PROTOFORM from nom.sg.
*‑az* to gen.sg. *‑is*, and the COUNTERPART from the bare stem to the
attested gen.sg. (`wulfes, fugles, bucces, rustes`).  The high vowel
*i* in `*‑is` is canonical Stiles env. (a) and **regularly blocks**
a‑mutation.  This produces the attested form by **regular sound
change**, with no rule change.  Row 2300 (`wull`) is left as wontfix
because the entire ō‑stem paradigm has back vowels and there is no
high‑vowel cell to switch to.

### 5.3  What kind of exception is wool / wolf / fugol?

It is a **lexical exception** of the type R/T §2.3.1 describe — a
small, named cluster of items that resist a regular sound law for
reasons no scholar has been able to formalise.  The mechanism, where
sources commit to one (Brunner §68, Stiles 2012), is **analogical
levelling from oblique paradigm cells**, not phonology — i.e. it is
**not a sound law that the FST is failing to model**, it is **a
non‑phonological process** that the cascade cannot model in
principle.

That is why these are wontfix and not a research target.  The
project's policy is: model the regular sound change (which the FST
does correctly: `wolf, fogol, woll`); document the attested form as a
named lexical exception when no high‑vowel cell exists; switch to a
high‑vowel cell when one does (4 of 5).

---

## 6.  Is `*skuldrō` in that bin?

### 6.1  R/T §2.3.1: NO, `*skuldrō` is not listed there

The prior dossier (lines 240–245) verifies this explicitly:

> "Shoulder is **not in R/T's explicit list** (vol. 2 pp. 32–33,
> quoted above); R/T list only `*fullaz, *wulfaz, *fuglaz,
> *tulga‑`, plus *ofer/ufan(e)*. So R/T do not treat *skuldru* as
> a member of the 'labial‑cluster exceptions' club."

This is one piece of evidence that `*skuldrō` is **not** the same
type of exception as `*wulfaz / *fuglaz / *fullaz`.

### 6.2  The /uRCr/ class (Luick §247): a separate cluster

The prior dossier §6 inventories a different group of OE items where
the *u* survives:

| OE | Gloss | Cluster | PGmc/PWGmc |
|---|---|---|---|
| **sculdor / sculdru** | shoulder | -uldr- | R/T *skuldru |
| **wuldor / wuldru** | glory | -uldr- (\*-ulþr-) | PWGmc *wuldr |
| **wundor / wundru** | wonder | -undr- | *wundra- (TSV row 2299: `*wúndrą`) |
| **þunor / þunras** | thunder | -un.r- | *þunraz |
| **furðor / furðra** | further (adv./comp.) | -urðr- | *furþerō- |
| **cildru** (pl.) | children | -ildr- (\*-ilþr-) | *kilþr- |
| **fyrðran** (vb.) | further (vb.) | -yrðr- | *furþerōjana |
| **gyrdlas / gyrdel** | belt | -yrdl- | *gurdilaz |
| **hundred** | hundred | -ndr- | *xundaraþa- |

Common features:

*   Stressed *u* (or earlier *u* > *y* via i‑umlaut in some cells)
    in the root.
*   A post‑nuclear cluster of the shape **/sonorant + obstruent +
    sonorant/** (ldr, ndr, lþr, nþr, nr, ndr, rðr, ldr, rdl).
*   A **high‑vowel paradigm cell** is attested (typically the
    neut.nom./acc.pl. in `‑u`, e.g. *sculdru, wuldru, wundru,
    cildru*).
*   The singular cell (with non‑high suffix) is back‑formed by
    epenthesis after high‑vowel apocope: `*sculdr → sculd‑o‑r`.

This is a **different** exception class from the
labial‑adjacency cluster of R/T §2.3.1.  The defining feature is the
**heavy /uRCr/ cluster + the existence of a high‑vowel cell**, not
labial adjacency.

### 6.3  Is the /uRCr/ class big enough for a Neogrammarian rule?

Luick §247 treats it descriptively as a **non‑lengthening
environment** (not a non‑lowering environment), and stops there.  No
handbook formalises it as a sound law blocking a‑mutation.

The class is small (~7–9 lexemes) and heterogeneous:

*   Some members never had a non‑high suffix at any reconstructable
    stage (e.g. *cildru* is attested only as a plural; the singular
    *cild* < *kelþa‑ has *e‑* ablaut).
*   Some members involve i‑umlaut alternations (*furðor / fyrðran*),
    showing that the high‑vowel cell really is doing
    morphophonological work in the paradigm.
*   Members with a *labial* in the cluster (*timbrian, cembe*) blur
    into Bülbring's labial‑adjacency hypothesis.

If we tried to write a rule "block `NWGmcULowering` when the
post‑nuclear cluster is /sonorant + obstruent + r/" (the prior
dossier's Option 4), the immediate problems are:

*   No source authorises it.  Luick §247 is descriptive of
    *Dehnung*, not of a‑mutation; Campbell §§115–118 lists no such
    blocker; R/T treat the items as residual exceptions to a rule
    that otherwise applies.
*   The same /uRCr/ environment in **other** TSV rows would have to
    be checked for collateral damage.  A spot search on the TSV
    finds row 2299 `*wúndrą → wundor`; this row is currently in the
    pipeline.  But the suffix `*ą` (PGmc neut. nom./acc.sg.) is
    nasalised and *not* matched by `EnglishStarNonHighVowel` in the
    rule body; thus a‑mutation does not fire on `*wúndrą` for an
    independent reason (the nasalised suffix is invisible to the
    rule).  The *wundor* row therefore does not require the new
    blocker.  In other words, the Project already gets *wundor* by
    paradigm‑cell selection (`*wúndrą`, not `*wúndrō`), not by a
    new phonological rule.
*   That is the smoking gun: the project has **already adopted the
    paradigm‑cell strategy** for the closest /uRCr/ analogue
    (*wundor*), and it works.

### 6.4  The morphological/back‑formation story

Brunner §68's account of `wulf ~ wolf` is explicitly **analogical
levelling from cells with high‑vowel suffix**:

> "Instr. der mask. und neutr. o‑Stämme *wulfe* aus *wulfi* (der
> i‑Umlaut ist in der Regel nach den anderen Kasus aufgegeben)"
> (DEV_NOTES line 25898).

Brunner's own account is **not** that some phonological rule
selectively saved *u* in `wulf`; it is that *u* was inherited in
inflected cells with a high‑vowel suffix (instr.sg. *wulfi*, gen.sg.
*wulfes < *‑is*) and then **levelled into the nom.sg.** as the
language reorganised the paradigm.

For `*skuldrō`, the parallel argument is even stronger.  R/T's PWGmc
inventory (vol. 2 p. 142) actually cites the form as `*skuldru` —
i.e. **with the high‑vowel suffix already in place at PWGmc**.  That
suggests:

1.  The historically primary cell was the **plural** `*skuldru`
    (neut. nom./acc.pl., with *‑u* from earlier *‑ō* via the same
    PNWGmc shortening that produces *gebu, feþru*) — but here the
    suffix was *‑u* "early enough" to bleed a‑mutation, perhaps
    because the paradigm had restructured (heavy stems whose
    nom.sg. apocopated stripped the contrast between sg. and pl.,
    so the pl. cell became the lemma).
2.  The singular `sculdor` is **back‑formed** from the plural by
    epenthesis (`*sculdr → sculd‑o‑r`).  This is exactly the
    derivation Luick §247 implicitly assumes.
3.  The weak fem. `sċuldra` (BT‑Supp, the TSV target) is a
    **further** paradigm shift — strong masc. `sculdor` reanalysed
    as a weak n‑stem fem., attested once in Anglian xiii.406.588.

The "right" PROTOFORM for the OE outcome therefore depends on which
cell you want to derive.  For lautgesetzlich derivation:

*   Want `sculdru` (pl.)?  Use `*skuldru` (already shortened, high
    suffix) → cascade gives `sċuldru` lautgesetzlich.
*   Want `sculdor` (back‑formed sg.)?  Same input; epenthesis +
    high‑vowel apocope yield `sċuldor` lautgesetzlich.
*   Want `sċuldra` (weak fem. nom.sg., BT‑Supp)?  No paradigm cell
    of any reconstructable proto gives this by sound change; it is
    necessarily analogical (cf. *spere* in §17.16).

---

## 7.  Classification: which of (a)–(d) best fits?

The user asked which of four classifications best fits the change
`*skúldrō nom.sg. → *skúldru`.

### (a) Sound‑law output that the FST can reproduce

**Ruled out by §2.**  The cascade as currently structured produces
`sċoldor`, not `sċuldor / sċuldru / sċuldra`.

### (b) Sound‑law output that the FST cannot reproduce because of unavoidable rule‑ordering conflicts

**Ruled out by §3 and §4.**  Reordering shortening before a‑mutation
would regress *nosu, sorg, sċofl* (which together far outweigh
*skuldru* in attestation).  No source authorises the reverse
ordering; R/T are silent, Brunner explains *wulf ~ wolf* analogically
rather than by ordering.

### (c) Morphological / analogical change (class‑shift, paradigm levelling, back‑formation)

**This is the best fit.**  Three convergent pieces of evidence:

*   R/T's own PWGmc inventory cites `*skuldru` (with high `‑u`) at
    vol. 2 p. 142, treating the historically primary form as
    already short‑suffixed.  Their treatment of the morphology
    *prefers* the post‑shortening reconstruction.
*   Brunner §68's analogical mechanism for `wulf` (levelling from
    inflected cells with high suffix) is the same kind of process.
*   The OE data is **paradigmatically split**: BT lemma is
    masc. *sculdor*; BT‑Supp adds weak fem. *sculdra*; Hall has
    only *sculdor*; the plural cell *sculdru ~ sculdra* is
    well‑attested in Bald's Leechbook.  No coherent single
    paradigm survives intact.  This is the diagnostic of an
    item that has undergone class‑shift.

The change is genuinely **outside the cascade's scope** insofar as it
is a reorganisation of the inflectional class; it is **inside** the
cascade's scope insofar as the **post‑shortening** form `*skuldru` is
itself a regular sound‑law output (PNWGmc *‑ō > *‑u via R/T p. 267)
of an earlier `*skuldrō` of *some* paradigm cell.  Specifically,
neuter nom./acc.pl. `*skuldrō (du.) / *skuldrō (pl. an‑stem
collective)` would give `*skuldru` by the same shortening that gives
`*gebō → gebu`.  Whether you locate the change "morphologically" or
"in the cell whose suffix happens to be high" depends on whether you
treat the cell selection as part of the sound law or part of the
morphology.

### (d) A regular sound law that the project has not yet formalised (e.g. Luick §247 /uRCr/ blocker)

**Tenable but unsupported.**  Luick §247 is descriptive of
non‑lengthening, not of non‑a‑mutation.  No source formalises a
/uRCr/ blocker on a‑mutation.  The class of candidate lexemes is
small and heterogeneous; the project has already handled the closest
analogue (*wundor*, row 2299) by paradigm‑cell selection rather than
a new rule.  Adding a Luick‑§247‑style blocker would require:

*   A textual basis in the literature beyond Luick's descriptive
    paragraph (none located).
*   A regression test showing it does not break currently‑correct
    derivations.  The list of canonical lowered forms (*folc, folm,
    bolla, bolt, bolster, wolcen, folde, molde, ofen, morþor*) does
    not contain /uRCr/, so the *direct* regression risk is low; but
    no source has done the broader audit (e.g. /uRCl/, /uNCr/,
    /uRCl/, /uNCl/) that a Neogrammarian rule would require.

### Summary

| Option | Fit | Reason |
|---|---|---|
| (a) Sound law the FST can reproduce | ✗ | Cascade produces `sċoldor`. |
| (b) Sound law the FST can't reproduce due to ordering | ✗ | Reordering regresses *nosu / sorg / sċofl*. |
| (c) Morphological / analogical | ✓ | R/T cite `*skuldru` already at PWGmc; Brunner §68's *wulf* mechanism applies; OE paradigm is split. |
| (d) Unformalised sound law | △ | Luick §247 is suggestive but descriptive; no source formalises; class is too small / too lexical. |

Best fit: **(c)**, with **(d)** as a secondary "if anyone ever
formalises Luick §247 as a rule, that would also fit" residual.

---

## 8.  Recommendation: Options X, Y, Z

The user asked for three named options, the *belief commitments* each
asks for, the strongest argument against each, and a recommendation.

### Option X — wontfix

**What you do.**  Add `*skúldrō → sċuldra` to the
`oe_known_problems_report.txt` exception list.  Document the
rationale in DEV_NOTES (§17.41 placeholder already exists in the
prior dossier's heading).  Stop trying to fix this row.  Mismatch
count stays at 16 (one less if reclassified out of the tractable
bucket).  The lexeme is acknowledged as a known exception parallel
to *wool / wolf / fugol*.

**You must believe**:

*   That the *kind* of exception `*skuldrō` represents is the same
    *kind* as `*wulfaz / *fuglaz / *fullaz / *búkkaz`.
*   That the 4‑of‑5 paradigm‑cell escape hatch DEV_NOTES §17.10.34
    used for *wulf, fugol, bucc, rust* is **not** available here —
    and therefore that this row should pattern with row 2300
    (*wull*), the one wontfix‑with‑no‑escape entry.

**Strongest argument against**: §6.1 — R/T §2.3.1 do **not** list
`*skuldrō` among the labial‑adjacency exceptions, so calling it the
same kind of exception is a stretch.  More importantly, the escape
hatch **is** available: R/T's own PWGmc inventory (vol. 2 p. 142)
gives the form already as `*skuldru`, with the high‑vowel suffix.
Walking past that available route in order to wontfix is wasteful.
Furthermore, even if u‑lowering is wontfixed, defect (B) — the
`sċuldra` vs. `sċoldor` final‑vowel mismatch — is *not* fixed: the
mismatch report would still show the row as a target mismatch, just
re‑bucketed.  Wontfix saves no work; it only relabels the failure.

### Option Y — cell‑switch (the prior dossier's §17.41 draft)

**What you do.**  In TSV row 2183, change PROTOFORM from `*skúldrō`
to `*skúldru`, and COUNTERPART from `sċuldra` to `sċuldor` (or
`sċuldru` if the project prefers the plural cell).  Cognate‑set PROTO
column (col 14) stays as `*skuldrō` so the inheritance into Du / G /
E (rows 591, 590, 589) is unaffected.  Justify it as cell‑switch to
the historically prior plural cell (the **pre‑shortening** PNWGmc /
PWGmc form whose suffix is already high), **NOT** as an attempt to
fake a sound law.  Cite R/T vol. 2 p. 142 for `*skuldru`, Brunner
§68 for the analogical mechanism, and project precedent §17.10.34
(`*wúlfaz → *wúlfis → wulfes`) for the strategy.

**You must believe**:

*   That `*skuldru` is a defensible cell‑specific PROTOFORM (R/T's
    PWGmc inventory authorises this; Luick §247 names *sculdru*
    plural by name).
*   That cell‑switching the per‑row PROTOFORM is consistent with
    project policy.  This is well‑established (DEV_NOTES §17.10.34
    cluster, §17.16 *spere*, §17.39 loam, §17.37 weasel,
    "*duru* → *dor*" Option‑A precedent at line 1009).
*   That the BT‑Supp `sċuldra` (the current TSV target) is **not**
    the better target — that the well‑attested BT/Hall lemma
    `sculdor` (or the well‑attested plural `sculdru`) is what the
    row should aim at.  This is a philological judgement; the prior
    dossier §2 establishes that `sculdor` is the BT lemma and
    `sculdra` is one Anglian/late attestation.

**Strongest argument against**:  This is *not* a sound‑law fix; it
is a **target swap**.  A purist would say: "we are not modelling the
phonology; we are moving the goalposts."  The defence is project
precedent and the philological soundness of the new target.  The
cognate‑set PROTO column in col 14 still says `*skuldrō`, so the
historical record is preserved; only the per‑row evaluation cell
changes.

### Option Z — add a /uRCr/ rule

**What you do.**  Formalise Luick §247's observation as a new
Neogrammarian rule blocking a‑mutation when the post‑nuclear cluster
is /sonorant + obstruent + r/.  Implement at `germanic.txt` line
1920 as the prior dossier's Option 4 sketch.  Audit the rule against
*wundor, cildru, hundred, fyrðran, gyrdlas, þunor* and check it does
not overgenerate in /uRCl/, /uNCr/, /uRCl/ environments.

**You must believe**:

*   That Luick §247's descriptive observation is, in fact,
    promotable to a Neogrammarian sound law — i.e. that the
    /uRCr/ environment categorically blocks a‑mutation, not just
    Dehnung.
*   That no scholar has formalised this only because no scholar has
    looked, not because it isn't formalisable.
*   That the cascade's existing rule order can absorb the new
    blocker without breaking *folc, folm, bolla, …, ofen, morþor,
    nosu, sorg, sċofl* (the empirically verified regular‑lowering
    set).

**Strongest argument against**:  No source authorises this rule.
Luick §247 explicitly addresses Dehnung; Campbell §§115–118 enumerate
blockers and /uRCr/ is not among them; R/T §2.3.1 treat the items
as residual exceptions, not as the products of a rule they failed to
formalise.  The class is small (~7–9 items) and heterogeneous.  And
critically, the project has **already solved the closest analogue
(*wundor*)** by paradigm‑cell selection (`*wúndrą` rather than
`*wúndrō`), demonstrating that the cell‑switch strategy works for
this class.  Adding a rule of marginal source support, when a
sourced cell‑switch is available, violates `be‑lautgesetzlich.md`'s
"favour the consensus" maxim.  Cost is high (regression testing on
the full TSV); benefit is dubious (one row).

### Recommended option

**Option Y — cell‑switch.**

The change `*skuldrō (nom.sg. fem. ō‑stem) → *skuldru (post‑PNWGmc‑
shortening high‑suffixed form)` is best classified as **(c)
morphological / analogical**, on the basis of:

*   R/T's own PWGmc inventory citing `*skuldru` (vol. 2 p. 142),
    treating the historically primary OE input as already short‑
    suffixed.
*   Brunner §68's analogical mechanism (paradigm levelling from
    cells with a high‑vowel suffix), which is the standard
    explanation for the *wulf ~ wolf* dichotomy and applies a
    fortiori here.
*   The OE paradigm being internally split (strong masc. *sculdor*
    BT lemma + weak fem. *sċuldra* BT‑Supp + strong neut.‑style
    plural *sculdru / sculdra*), the diagnostic of an item that has
    undergone class‑shift.

The lexeme is **adjacent to but not in** the wool/wolf/fugol
wontfix bin.  It is adjacent in that it is a u‑retention case where
the regular sound law fails; it is **not in** that bin because (i)
R/T do not list it in §2.3.1, (ii) it has a different conditioning
profile (/uRCr/ heavy cluster, not labial adjacency), and (iii) it
has an available high‑vowel cell to switch to (`*skuldru`), unlike
the one wontfix‑with‑no‑escape case (*wull*).

The right move is therefore the **same** move DEV_NOTES §17.10.34
made for 4 of the 5 labial‑adjacency cases: switch the per‑row
PROTOFORM to a cell whose suffix is high, so a‑mutation never
triggers.  For `*skuldrō` this cell is `*skuldru` (R/T vol. 2 p. 142;
Luick §247 *sculdru plur.*), and the corresponding COUNTERPART is
`sculdor` (BT lemma; back‑formed sg. by epenthesis after high‑vowel
apocope) — or `sċuldru` if the project prefers the plural target.

**Option X (wontfix)** is too pessimistic: it concedes a defeat the
literature does not require.

**Option Z (add a rule)** is too ambitious: it promotes a descriptive
remark to a sound law without source backing, and the cell‑switch
strategy already handles the relevant cases (cf. *wundor*).

---

## Sources

(Prior dossier `Germanic/docs/dossier-shoulder-2026.md` is the
master citation list.  Refs below are limited to those load‑bearing
for the *lautgesetz* question.)

*   **Bosworth & Toller**, *Anglo‑Saxon Dictionary*, s.v. *sculdor*
    (main p. 845); BT‑Supp s.v. *sculdor / sculdra*.
*   **Bülbring, K. D.**, *Altenglisches Elementarbuch* §§81d, 116,
    on a‑Umlaut and the labial‑adjacency hypothesis (cited in
    DEV_NOTES line 81).
*   **Brunner, K.**, *Altenglische Grammatik nach der angelsächsischen
    Grammatik von Eduard Sievers* (3rd edn. 1965), §§29ff., 63, 68,
    92, 2, a, 143–149, 239 (DEV_NOTES line 139, 25893–25899).
*   **Campbell, A.**, *Old English Grammar* (1959), §§115–118, 122,
    331(5), 355, 369, 373.
*   **Clark Hall**, *A Concise Anglo‑Saxon Dictionary* (4th edn.),
    s.v. *sculdor*.
*   **Fulk, R. D.**, *A Comparative Grammar of the Early Germanic
    Languages* (2018), §§4.3, 4.11, 5.2, 6.14, 7.31, 12.19 n.6.
*   **Hogg, R. M.**, *A Grammar of Old English vol. 1: Phonology*
    (1992), §§5.10–5.16 [exact subsection numbers not verified in
    this session — `[citation needed]` for any quotation].
*   **Kroonen, G.**, *Etymological Dictionary of Proto‑Germanic*
    (2013), p. 478 s.v. **\*skuldra‑**; p. 462 s.v.
    **\*spaiskuldra‑** (Goth. *spaiskuldr*).
*   **Luick, K.**, *Historische Grammatik der englischen Sprache*
    vol. 1 (1914–40), §§78 (incl. Anm. 3), 103, 105–6, 188, 247
    (cross‑referenced in DEV_NOTES at lines 6097, 6992, 14547,
    14637).
*   **Orel, V.**, *A Handbook of Germanic Etymology* (2003),
    p. 345 s.v. **\*skuldr(j)ō**.
*   **Ringe, D. & Taylor, A.**, *The Development of Old English*
    (= *A Linguistic History of English* vol. 2, 2014):
    §2.1.1, §2.3.1 (pp. 27–33: a‑mutation and its exceptions),
    §3.1 (pp. 30–31, 58–59), §3.1.4, §3.3.1 (z‑loss), §5.1.1
    (NSL), §5.1.2 (long *ē* lowering), §6.1.2, §6.1.5, §6.3.3
    (inter‑stress raising), §6.8.3 (R/T's "dated OE stage"
    shortening), inventory at p. 142 (`*skuldru`), p. 267
    (PNWGmc *‑ō > *‑u shortening, quoted verbatim in
    `germanic.txt` line 1997 comment block).
*   **Stiles, P.**, "Older Runic evidence for North‑West Germanic
    a‑umlaut of u" (2012), §4.1.1.2 (DEV_NOTES line 25855ff.).

In‑project files:

*   `Germanic/fsts/germanic.txt` lines 1907–2010 (a‑mutation,
    *‑ō > *‑u shortening), lines 2886–2960 (cascade composition).
*   `Germanic/docs/DEV_NOTES.md` "NWGmc u‑lowering Exceptions
    Near Labials" (lines 69ff.); §17.10.34 (lines 25838ff.,
    "Cluster: u‑lowering 'exceptions' …"); §17.16 (*spere*).
*   `Germanic/docs/debug_snapshots/oe_known_problems_report.txt`
    lines 51, 66–94 (TRACTABLE / WONTFIX bins).
*   `Germanic/docs/dossier-shoulder-2026.md` §§1–10 (prior
    dossier).
*   `Germanic/data/germanic-aligned-final.tsv` rows 2143, 2183,
    2185, 2200, 2299, 2300 (live verification).

---

## Executive summary

The change `*skúldrō (fem. ō‑stem nom.sg.) → *skúldru` is best
classified as a **morphological / analogical** change — specifically
a paradigm‑cell shift to (or from) the neut. nom./acc.pl. cell whose
suffix is already short `‑u` after the regular PNWGmc *‑ō > *‑u
shortening (R/T vol. 2 p. 267).  R/T themselves cite the PWGmc form
as `*skuldru` with high suffix already in place (vol. 2 p. 142),
which presupposes exactly this cell selection.  It is **not** a
regular sound law output that the cascade can produce from the nom.sg.
PROTOFORM `*skúldrō`: a‑mutation fires before *‑ō shortening in our
cascade order, and that order is **forced** by *nosu / sorg / sċofl*
(rows 2143, 2200, 2185), all of which attest the lowered root vowel.
Reordering would regress those three.  It is **not** in R/T §2.3.1's
labial‑adjacency wontfix bin (R/T list only `*fullaz, *wulfaz,
*fuglaz, *tulga‑`, *ofer/ufan(e)*); it sits in a *different*
exception class (Luick §247's /uRCr/ heavy‑cluster items: *sculdru,
wundru, cildru, gyrdlas, fyrðran, hundred*), which no source has
formalised as a sound law.  The recommended fix is therefore
**Option Y — cell‑switch**: change the per‑row PROTOFORM in TSV row
2183 from `*skúldrō` to `*skúldru`, with COUNTERPART `sċuldor` (the
BT lemma) or `sċuldru` (the well‑attested plural), keeping cognate‑
set PROTO `*skuldrō` for cross‑Gmc inheritance.  This applies the
same paradigm‑cell strategy that DEV_NOTES §17.10.34 successfully
used for 4 of the 5 labial‑adjacency wontfix entries (`*wúlfis →
wulfes`, `*fúglis → fugles`, `*búkkis → bucces`, `*rústis → rustes`)
— and that the project has *already* used for the closest /uRCr/
analogue *wundor* (row 2299, PROTOFORM `*wúndrą`, where the nasalised
suffix bleeds a‑mutation).  Option X (wontfix) is too pessimistic —
it concedes a defeat the literature does not require, and it does
not even fix the secondary defect (the `sċuldra` vs. `sċoldor`
final‑vowel mismatch).  Option Z (add a /uRCr/ rule) is too
ambitious — Luick §247 is a descriptive remark about Dehnung, not a
formalisable sound law about a‑mutation, and adopting it would
violate `be-lautgesetzlich.md`'s "favour the consensus" maxim.

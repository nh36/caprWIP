# Dossier: OE `stemn ~ stefn ~ stefna ~ stofn` consonant variation (2026)

## 1. Research question

For the Germanic 'stem, trunk, prow' lexeme (CAPR row 2216), the Old English
reflexes appear as `stemn`, `stefn`, `stefna`, and `stofn`, beside cognates
OS `stamn`, ON `stafn`, OHG/G `stam(m)`. This dossier adjudicates, from the
sources, the historical relationship among those forms, and in particular the
direction, regularity, and chronology of the `mn ~ fn` alternation. It does
**not** presuppose that `mn -> fn` is the relevant development; both directions
are tested against the literature.

This dossier is the **historical-variation** companion to
`Germanic/docs/dossier-stem-2026.md` (which established the i-stem input
hypothesis). It does not repeat that dossier; it cross-references it.

## 2. Prior CAPR result (unchanged in this task)

From the earlier investigation and the committed probe artifact
(`Germanic/docs/audits/2216-stem-candidate-probe.md`), at HEAD
`9f236dd2` with the unchanged production FST:

- `*stámniz` is accepted; the cascade yields exactly one output, `stemn`
  (multiplicity 1).
- Path: SC020 `EAFFinalZDeletion` (`*stámni`) -> SC055 `OEIUmlaut`
  (`*stemni`) -> SC063 `OEHighVowelApocope` (`*stemn`).
- No `mn -> fn` rule fires; the `-mn-` cluster is retained throughout.
- `PROTO = *stámnaz` is retained as the citation reconstruction.

The present dossier asks whether the attested variation weakens `*stámniz`
or `stemn` as the selected CAPR path. It does not.

## 3. Source inventory (local corpus first)

All paths under `/Users/nathanhill/Code/capr/docs/references/`. OCR line
numbers are given for reproducibility; scientific citations use the
publication locator.

| Source (publication locator) | Local file | What it contributes |
| :--- | :--- | :--- |
| Orel 2003, *Handbook of Germanic Etymology*, pp. 371, 373 | `orel_handbook_germanic_etymology.vision.txt` (`:41239`, `:41519`; page markers `:37025`, `:37242`) | Reconstructs `*stamnaz *stamniz` (stem/prow) and separately `*stebnō ~ *stemnō` (voice); cognate lists; Torp's `*stabnaz` separation |
| Kroonen 2013, *EDPG*, p. 480 | `kroonen_etymological_dictionary_pgmc.vision.txt` (`:24696`, `:1738`) | Voice etymon `*stimno-`/`*stebnō-`; explicit Germanic `*-mn- > *-bn-` |
| Kroonen 2011, *The Proto-Germanic n-stems*, pp. 183, 286 | `kroonen_2011_n_stems.vision.txt` (`:8286`, `:12975`) | OE `stefn`/`heofon`/`levene` as `*-mn-` with "vocalization of the m"; `stofn` = `*stubna/ō-` in the `*stub-` 'stub' family |
| Kroonen 2006, "Gemination and allomorphy in the PGmc mn-stems" (*ABäG* 61: 17–25) | `kroonen_2006_mn_stems_bottom_rime.txt` (`:1`) | PIE `*-Cmn- > *-Cn-` after labial roots; mn-stem allomorphy / Kluge's law framework |
| Polomé 1967, "Notes on the Reflexes of IE /ms/ in Germanic", pp. 818–819 | `polome_1967_reflexes_ie_ms.txt` (`:867`) | Germanic `-mn- > *-bn-`; OE `stefn : stemn` 'prow' and 'voice' as **doublets**; Torp `*stab-` alternative |
| Fulk 2018, *A Comparative Grammar of the Early Germanic Languages*, §6.14 (+ n. 6) | `fulk_comparative_grammar_early_germanic.vision.txt` (`:7365`, `:7403`) | "In the cluster mn, the first consonant tends to lose its nasality by dissimilation... the reverse change (of bn to mn) is well attested in NWGmc"; "hardly regular"; stem/voice etymologies "rather insecure" |
| Campbell 1959, *Old English Grammar*, §§193.d n.4, 484, 328 | `campbell_old_english_grammar.txt` (`:5504`, `:12570`, `:15225`) | `fn > mn` as *sporadic West-Saxon* assimilation; explicitly `stemn stem (beside stefn)`; rejects Luick on the vowel |
| Luick 1914–40, *Hist. Gramm.*, §75 Anm. 1; §186 | `luick_historische_grammatik.txt` (`:5988`, `:11332`, `:16996`) | "e vor jüngerem mn aus fn" (mn is younger, from fn); tentative `stemn Stamm aus *stofn` |
| Brunner 1965 (Sievers–Brunner), *Altenglische Grammatik*, §193.2; §201 | `brunner_1965_altenglische_grammatik.vision.txt` (`:8044`, `:4016`) | WS "fn ... geht ... oft in mn über": `stemn Stimme, stemn Stamm ... für ... stefn` |
| Bülbring 1902, *Altenglisches Elementarbuch*, §485 | `bulbring_altenglisches_elementarbuch.txt` (`:9012`) | WS "f vor n + Vokal in m über": `stemn 'Stimme', stemn 'Steven'` |
| Ringe & Taylor 2014, vol. 2, p. 346 | `ringe_taylor_linguistic_history_vol2.txt` (`:18934`) | Voice chain `*stebno > *stebnu > OE stebn > stefn > stemn` |
| Clark Hall 1960, *Concise A-S Dictionary*, pp. 276, 341 | `clark_hall_concise_anglo_saxon_dictionary.vision.txt` (`:38045`, `:38341`) | Lemmas: `stefn` I 'voice'; `stefn` III 'stem, trunk, prow/stern'; `stefna` 'prow/stern'; `stofn` 'trunk, stem, branch, shoot' |
| Bosworth–Toller (+ Supp.) | `bosworth_toller_anglo_saxon_dictionary.vision.txt` | Attestations: prow compounds (`brand-stefn`, `bundenstefna`, `hringedstefna`, `forþ-stefna`); voice `stemne` dat.sg. abundant |

Not directly probative for this word but inspected: Bammesberger 1990,
Seebold *Vergleichendes Wörterbuch*, Kluge–Seebold (no dedicated `Stamm` s.v.
locator recovered), Pokorny IEW pages, Bright/Sweet readers.

## 4. Old English stem/trunk/prow form inventory

| Form | Gender / class | Morphological shape | Sense(s) | Status in the lexeme | Lexeme assignment | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `stefn` (III) | m., strong (a-stem) | `stefn` (`fn`) | 'stem, trunk, root; prow/stern; foundation' | primary/base dictionary form for stem/prow | **A (stem/prow)** | Clark Hall p. 276; Campbell §484 |
| `stemn` | m. (stem/prow); homonym also f. 'voice', m. 'period' | `stemn` (`mn`) | 'stem, trunk; prow' | variant beside `stefn`; WS assimilation and/or retained `mn` | **A**, but graphically shared with B/period | Campbell §484 ("stemn stem beside stefn"); Brunner §193.2 |
| `stefna` | m., weak (n-stem) | `stefn` + `-a` | esp. nautical 'prow or stern of a ship' | related n-stem specialization | **A**, nautical sub-sense | Clark Hall p. 341; Orel p. 371 (OE `stefna`) |
| `stofn` | mf. | `stofn` (`o`-vocalism, `fn`) | 'trunk, stem, branch, shoot'; (ON `stofn` 'stub') | related but distinct ablaut formation | **A**, but separate stem (`*stub-`) | Clark Hall p. 341; Kroonen 2011 p. 286 |

Homonym control (do **not** use as evidence for A): `stefn`/`stemn` **f.**
'voice, sound' (Clark Hall p. 276, Campbell §328/§484), and `stefn` **m.**
'summons, turn, period' (Campbell §484). Attestations of dat.sg. `stemne`
'with a voice' are extremely common in Bosworth–Toller and are **category B**.

## 5. `stemn ~ stefn`: the central alternation

**What the grammars explicitly say about `fn ~ mn` in OE — direction, environment, chronology:**

- **Campbell §484** (`:12570`): in groups of consonant + liquid/nasal
  "assimilation is **sporadic**." Listed under **`fn > mn`**: "W-S `emn`
  even, `hremn` raven (§193.d, footnote 4), and the homonyms `stemn` voice,
  `stemn` period, `stemn` stem (beside `efn`, `hrefn`, `stefn`); nW-S only
  Ru. `stemn` voice (beside `stæfn`)." Direction: **`fn -> mn`**; dialect:
  **West-Saxon** (non-WS retains `fn`); status: **sporadic** assimilation.
- **Luick §75 Anm. 1** (`:5988`): "e vor **jüngerem mn aus fn**: `emn`
  'eben', `stemn` Stimme." Direction **`fn -> mn`**; the `mn` is explicitly
  "**younger**" (jünger).
- **Brunner (Sievers–Brunner) §193.2** (`:8044`): WS, sometimes already
  early-WS, inlaut "**fn ... geht ... oft in mn über**": `emne`, `stemn`
  Stimme, `stemn` Stamm, `hremn` "für `efn`, `stefn`, `stefn`, `hræfn`;"
  later even `mm`/`m`. Direction **`fn -> mn`**; WS.
- **Bülbring §485** (`:9012`): "Im Ws. geht **f vor n + Vokal in m über**":
  `emne`, `hræmn/hremn`, `stemn` 'Stimme', `stemn` 'Steven'. Direction
  **`fn -> mn`**; WS; conditioned by a following vowel (inflected forms).
- **Fulk §6.14** (`:7365`): primary tendency is **`mn -> bn`** ("the first
  consonant tends to lose its nasality by dissimilation"), but "the
  **reverse change (of bn to mn) is well attested in NWGmc**," and "the
  results are **hardly regular**." Footnote 6 (`:7403`): the `stefn ~ stemn`
  etymologies are "**rather insecure**."

**Does the OE grammar derive `stemn` from `stefn`, or `stefn` from `stemn`?**
Within Old English the four grammars agree: **`stefn` (fn) is the base and
`stemn` (mn) is the later, sporadic West-Saxon product** of `fn -> mn`. There
is **no** OE grammarian who derives `stefn` from an OE `stemn`. The one
recorded disagreement (Campbell §193.d n. 4 vs Luick §186, `:5504`) concerns
only the **vowel** (`e`) of `stemn/hremn`, not the consonant direction:
Campbell objects to Luick treating the `e` as an æ-mutation product
conditioned by `mn`, "as the forms `stefn`, `hrefn` are common" (i.e. `mn` is
too late to have conditioned the vowel). Both accept OE `fn -> mn`.

## 6. History of `fn ~ mn` in Old English — judgment

- **ESTABLISHED**: Old English has a real **`fn -> mn`** development. It is
  **West-Saxon**, **sporadic / not exceptionless** (Campbell "sporadic";
  Fulk "hardly regular"), **chronologically late** ("jüngerem", Luick;
  early-WS onward, Brunner), and favoured before a following vowel in
  inflected forms (Bülbring). Non-WS (Ru.¹, Anglian) generally retains `fn`.
- **ESTABLISHED**: It applies across etymologically unrelated words sharing
  the phonological shape (`efn/emn`, `hrefn/hremn`, `stefn/stemn` in all
  three homonyms), i.e. it is a **phonological**, etymology-independent OE
  process.
- **REJECTED (as an OE process)**: a productive OE **`mn -> fn`**. No OE
  grammar posits it; the `f` of `stefn` is pre-OE (Part 7).
- **UNRESOLVED**: whether every OE `mn` in this word is secondary (`< fn`)
  or whether some `mn` directly continues an inherited `-mn-` (see Part 7,
  15).

## 7. Pre-OE origin of the `f`-forms

The OE `fn -> mn` process presupposes that `fn` already existed. Since the
reconstructed stem contains `-mn-` (`*stamn-`), the `f` must come from an
earlier development:

- **Polomé 1967, pp. 818–819** (`:867`): "At an older date, **`-mn-` became
  `*-bn-` in Germanic**, though leveling inside paradigms has often obscured
  the original distribution." The `*-bn-` gives the labial spirant (OE `f`,
  ON `f`). Polomé cites the *parade* case OE `heofon`/OS `heban` 'heaven'
  (spirant leveled through the paradigm) beside ON obliques `hifne`, and
  then, explicitly for our word: **"OE `stefn : stemn` 'prow', as compared
  with ON `stafn` versus OS `stamn`."** He treats `stefn ~ stemn` as an
  inherited **doublet** from the `-m- ~ -b-` alternation, leveled differently.
- **Fulk §6.14** (`:7365`): same primary tendency, `mn -> bn` (m loses
  nasality), citing `heofon`/`heban`; "hardly regular."
- **Kroonen 2011, p. 183** (`:8286`): OE `stefn` (voice), `he(o)fen`
  'heaven', `levene` 'lightning' all continue `*-mn-` with **"vocalization of
  the m"** (giving `f`/`v`), not a diphthong.
- **Kroonen 2013 EDPG p. 480** (`:1738`): for the voice etymon, "Go. `stibna`
  must continue `*stebnō-` or `*stibnō-`, which could have developed out of a
  secondary genitive `*stemnaz` or `*stimnaz` **before the change `*-mn- >
  *-bn-`**." Explicit Germanic `-mn- > -bn-`.

**Answers to the Part III questions:**
1. Is `fn` reconstructible above OE? **PROBABLE-yes** as `*-bn-`: the
   Germanic `-mn- > -bn-` change (Polomé, Fulk, Kroonen) produces it.
2. Does ON `stafn` imply an older `fn`/`bn` variant? **PROBABLE-yes**,
   *unless* ON `stafn` belongs to a different root (next point).
3. Do etym. dictionaries reconstruct more than one stem? **YES / UNRESOLVED**:
   Torp (via Orel p. 371, "**separates `*stabnaz` and `*stamnaz`**"; Polomé
   n. 2, `:927`) links ON `stafn`/OE `stefn` to `*stab-` 'staff, post'
   (ON `stafr`, Skt. `stabhnóti`), which would make the `f` **root-etymological**
   rather than from `-mn-`. Sources are divided.
4. Consonantal dissimilation proposed? **YES**: `-mn- > -bn-` (Polomé, Fulk)
   is the dissimilation.
5. Suffix/stem-class linkage? Orel gives `*stamnaz *stamniz` (masc.
   a-/i-stem); the alternation is not tied to one class here.
6/7. Is `f` secondary by analogy, or is `mn` secondary? **UNRESOLVED at the
   Germanic level**: the two members are old doublets (Polomé), leveled in
   opposite directions across daughters.
8. Contamination between related forms? **POSSIBLE**: with the voice etymon
   and/or with `*stab-` 'staff' and `stofn` `*stub-`.
9. One lexical development or remodeled variants? **PROBABLE**: partly
   remodeled; ‘prow/stern’ is the specialized `stefna` (Part 8).
10. Old enough that no single deterministic PGmc->OE path yields all forms?
    **ESTABLISHED-yes** — this is the central modeling consequence (Part 18).

## 8. `stefna`

- **Clark Hall p. 341** (`:38052`): `stefna` (var. `stafna`) **m., weak
  (n-stem)**, glossed 'prow or stern of a ship'. Distinct entry from `stefn`.
- **Orel p. 371** (`:41239`): under `*stamnaz *stamniz`, OE `stefna` 'prow,
  stern' is listed as the **n-stem** cognate, beside ON `stafn`, OFris
  `stevene` (fem.), OS `stamn`.
- Attestation: Bosworth–Toller ship-compounds `bundenstefna`, `hringedstefna`,
  `forþ-stefna`, `stēor-stefna` (`:42088`, al.) — all nautical.

**Judgment.** `stefna` is **ESTABLISHED** as a separate **weak n-stem**
formation to the same root, **specialized to the nautical 'prow/stern'**
sense (matching ON `stafn` 'stem of a ship', OFris `stevene`). The final `-a`
is **n-stem morphology** (nom.sg. masc. weak), *not* a phonological accretion
on `stefn`. It is therefore a morphological sibling, not a spelling variant.

## 9. `stofn`

- **Clark Hall p. 341** (`:38341`): `stofn` **mf.**, 'trunk, stem, branch,
  shoot; progeny'.
- **Kroonen 2011, p. 286** (`:12975`): reconstructs **`*stubna/ō-`**: ON
  `stofn` n. 'stub', OE `stofn` f. 'tree-stump, shoot' — placed within the
  `*stūfō, *stuppaz` 'stub/stump' family (`*stub- / *stūf- / *stupp-`, with
  Kluge's-law gradation).
- **Luick** (`:11332`): tentatively connects OE `stemn` 'Stamm' with `*stofn`
  ("vielleicht auch `stemn Stamm` aus `*stofn`, vgl. as. `stamn` und me.
  `stam`") — i.e. he found the stem-word's vocalism genuinely unclear.

**Judgment.** `stofn` is **PROBABLE** a **distinct ablaut formation**:
`*stubna/ō-` from the zero/`u`-grade `*stub-` 'stub, stump' (OE `o < u` by
regular lowering), **not** a spelling variant of `stamn/stefn` and **not**
from `*stamn-`. The `o` reflects `*u`, not the `*a` of `*stamn-`. It shares
the general 'stem/stump' semantics and the `-n-` suffixation but belongs to a
neighbouring word-family. Luick's `stemn < *stofn` is a **minority, tentative**
view and is not adopted here.

## 10. Comparative Germanic evidence

| Language | Form | `mn`/`fn`/other | Vowel | Stem/formation | Sense | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PGmc (citation) | `*stamnaz ~ *stamniz` | `mn` | `a` | masc. a-/i-stem | stem, trunk, prow | Orel p. 371 |
| PGmc (alt., Torp) | `*stabnaz` (`*stab-`) | `bn` | `a` | to 'staff/post' | (would explain `f`) | Orel p. 371; Polomé n. 2 |
| Old English | `stefn` III | `fn` | `e` | m. a-stem | stem, trunk, prow | Clark Hall p. 276 |
| Old English | `stemn` | `mn` | `e` | m. (WS variant) | stem, trunk | Campbell §484 |
| Old English | `stefna` | `fn` | `e` | m. n-stem | prow/stern (naut.) | Clark Hall p. 341 |
| Old English | `stofn` | `fn` | `o` (< `*u`) | mf. (`*stubna-`) | trunk, stump, shoot | Kroonen 2011 p. 286 |
| Old Saxon | `stamn` | `mn` | `a` | — | stem | Orel p. 371; Polomé |
| Old Frisian | `stevene` | `v(<f)` | `e` | fem. | stem of a ship | Orel p. 371 |
| Old Norse | `stafn` | `fn` | `a` | — | stem of a ship | Orel p. 371; Polomé |
| MLG | `stam` | `m` | `a` | — | stem | Orel p. 371 |
| OHG / German | `stam` / `Stamm` | `m(m)` | `a` | — | stem, trunk | Orel p. 371 |

Reading of the table: the consonant split (`mn` in OS `stamn`, OE `stemn`;
`fn` in OE `stefn`/`stefna`, ON `stafn`, OFris `stevene`; `m(m)` in
OHG/G/MLG) is **cross-Germanic and inherited**, matching Polomé's picture of
an old `-mn- ~ -bn-(> -fn-)` doublet leveled differently by branch, with a
still-later OHG `-mn- > -mm-`. The vowel `o` of OE `stofn` sets it apart as a
separate `*stub-` formation.

## 11. Textual / dialectal distribution

A targeted (non-exhaustive) check of Bosworth–Toller and Campbell:

- **Voice sense (control, B)**: dat.sg. `stemne` 'with a voice' is pervasive
  in the prose corpus (Ælfric, Blickling, Gregory's Dialogues, Psalter
  glosses; scores of B–T citations). `stefn`/`stemn` 'voice' clearly coexist.
- **Stem/prow sense (A)**: nautical compounds cluster in verse
  (`bundenstefna`, `hringedstefna`, `wundenstefna` in *Beowulf* etc.) with the
  `stefna` n-stem; prose `forþ-stefn(a)` 'prow'.
- **Dialect**: Campbell §484 states `stemn` (mn) is essentially **West-Saxon**;
  non-WS (Ru.¹/Anglian) shows `stefn/stæfn`.

**Judgment.** The consonant distribution is **PROBABLE** dialectal (WS `mn` vs
non-WS `fn`, per Campbell), but a sense-by-consonant split for the stem/prow
lexeme specifically is **UNRESOLVED — no secure distribution established** from
the available evidence (the graphic overlap with the voice homonym and the
verse-bound nautical compounds prevent a clean count).

## 12. Control: the unrelated 'voice, sound' lexeme

- Etymon: **PGmc `*stebnō ~ *stemnō` / `*stimno-`** 'voice' (Orel p. 373;
  Kroonen EDPG p. 480), Go. `stibna`, OE `stefn/stemn`, OFris `stifne/stemme`,
  OS `stemna`, OHG `stimna/stimma`. Etymologically **distinct** from
  `*stamn-` 'stem'.
- **The same OE `fn -> mn`** applies to it: Campbell §484 lists `stemn` voice
  beside `stefn`; Ringe–Taylor p. 346 give `... OE stebn > stefn > stemn`.
- Its `f` has the same deep source: `-mn- > -bn-` before the labial (Polomé;
  Kroonen EDPG p. 480 "before the change `*-mn- > *-bn-`").

**Use as control.** The voice word demonstrates that OE `fn ~ mn` and the
Germanic `-mn- > -bn-` are **etymology-independent phonological processes**
operating identically on both lexemes. This **supports** treating the
stem-word alternation as regular phonology rather than a peculiarity of row
2216 — but precisely because it is shared and homonymous, voice-word
attestations must **never** be counted as evidence for the stem lexeme
(category B, not A).

## 13. Relationship to CAPR's `PNWGmcMnDissimilation`

The live rule (`Germanic/fsts/germanic.txt:2151`):

```
define PNWGmcMnDissimilation [
    {*m} -> {*β} || EnglishStarVocalic _ EnglishStarVocalic EnglishStarConsonant* EnglishStarNasal
];
```

Its structural description requires **intervocalic `*m`** (`V _ V ... N`),
i.e. the `-mVn-` environment of `*xemonų -> heofon` (row 2068; comment at
`germanic.txt:2141-2153`; sources cited there: Fulk §6.14, Kluge–Seebold s.v.
Himmel). In `*stámniz` the `m` is **immediately followed by `n`** (a true
`-mn-` coda cluster), so the left/right contexts are not met and the rule
correctly does **not** fire.

**Is the stemn/stefn alternation a reason to broaden `PNWGmcMnDissimilation`?
No (ESTABLISHED reasoning).**
1. **Different environment.** The rule targets intervocalic `-mVn-`; the
   stem word has a `-mn-` cluster. Polomé and Fulk treat both under one broad
   *tendency*, but the tendency is "hardly regular" (Fulk) and its cluster
   outcome is exactly the disputed `stefn`/`stamn` split — not a clean rule.
2. **Wrong output for our target.** Broadening it to fire on `-mn-` would
   convert `*stámniz -> *stáβniz -> ... -> stefn`, destroying the securely
   attested `stemn` we actually select, and it would also risk perturbing
   other `-mn-` words (e.g. `*táikną -> tācn`, `*wēpną -> wǣpn`) that must
   keep their cluster.
3. **Regularity fails.** Every grammar calls the OE side sporadic/WS and the
   Germanic side irregular; a productive FST rule would over-apply.

Therefore `PNWGmcMnDissimilation` must remain scoped to the intervocalic
`heofon`-type environment and must **not** be broadened for row 2216.

## 14. Chronology

- **Proto-Indo-European**: `*-Cmn- > *-Cn-` after labial roots (Kroonen 2006)
  — feeds Kluge's-law gemination in *other* words (bottom, rime); marginal to
  this lexeme.
- **Common/Northwest Germanic**: `-mn- > -bn-` (Polomé, Fulk) — the source of
  the labial spirant in ON `stafn`, OE `stefn`, OFris `stevene`; leveled
  variably, leaving doublets. **PROBABLE** for this word.
- **Prehistoric OE (CAPR-modeled path)**: retained `-mn-` + regular
  i-mutation (`*a > e`) + high-vowel apocope -> `stemn` (row's selected path).
- **Attested (West-Saxon) OE**: sporadic, late `fn -> mn` (Campbell, Luick
  "jünger", Brunner, Bülbring) -> `stemn` also derivable from `stefn`.
- **OHG**: later dialectal `-mn- > -mm-` (Polomé) -> `Stamm`.

## 15. Competing historical analyses of OE `stemn` (stem)

- **(i) Retained/leveled `-mn-` doublet** (Polomé): `stemn` continues an
  inherited `-mn-` member; `stefn` continues the `-bn-(>fn)` member. — **This
  is the member CAPR models.**
- **(ii) Secondary WS `fn -> mn`** (Campbell, Luick, Brunner, Bülbring):
  `stemn` is a late West-Saxon assimilation of base `stefn`.
- **(iii) Separate root `*stab-`** for the `f`-forms (Torp, via Orel/Polomé
  n. 2): ON `stafn`/OE `stefn` belong to 'staff/post', making the `f`
  root-etymological rather than `< -mn-`.
- **(iv) `*stofn`-linked** vocalic connection (Luick, tentative): links
  `stemn`/stem to the `o`-form — a minority view.

**Overdetermination (ESTABLISHED).** Analyses (i) and (ii) both yield attested
`stemn`. Therefore **a single attested `stemn` token cannot be assigned a
unique history**: it may continue inherited `-mn-` *or* be WS `fn -> mn` from
`stefn`. CAPR's deterministic derivation realizes route (i); the book must not
claim it as the exclusive history of every `stemn`.

## 16. What is established

- **ESTABLISHED**: Row 2216 belongs to the Germanic 'stem/trunk/prow' family
  `*stamnaz ~ *stamniz` (Orel p. 371), distinct from the voice etymon
  `*stebnō/*stimno-` (Orel p. 373; Kroonen EDPG p. 480).
- **ESTABLISHED**: OE has a real **`fn -> mn`** development — West-Saxon,
  sporadic/late, etymology-independent (Campbell §484; Luick §75; Brunner
  §193.2; Bülbring §485).
- **ESTABLISHED**: The `f`-forms' labial ultimately reflects a Germanic
  **`-mn- > -bn-`** tendency (Polomé pp. 818–819; Fulk §6.14; Kroonen).
- **ESTABLISHED**: `stefna` is a **weak n-stem** specialized to nautical
  'prow/stern'; `stofn` is a **distinct `*stubna-`** formation.
- **ESTABLISHED**: CAPR's `*stámniz -> stemn` is one valid route (retained
  `-mn-`); no `mn -> fn` or `fn -> mn` rule is required for it.

## 17. What remains uncertain

- **UNRESOLVED**: For any given OE `stemn` (stem) token, whether it continues
  inherited `-mn-` or is WS `fn -> mn` from `stefn` (overdetermined).
- **UNRESOLVED**: Whether ON `stafn`/OE `stefn` belong to `*stamn-` (via
  `-mn->-bn-`) or to a separate `*stab-` 'staff' (Torp); Orel reports the
  separation as an open alternative.
- **UNRESOLVED / "rather insecure"** (Fulk n. 6): the precise etymology and
  regularity of the whole `stefn ~ stemn` set.
- **UNRESOLVED**: any sense-conditioned (trunk vs prow) consonant distribution
  — **no secure distribution established**.

## 18. CAPR modeling consequences

1. **Keep `PROTO = *stámnaz`?** **Yes** — it is the family's citation
   reconstruction (Orel p. 371); the variation research does not disturb it.
2. **Use `*stámniz` as `PROTOFORM`?** **Yes** — Orel attests the i-stem
   variant `*stamniz`; it is the input that regularly yields an attested OE
   form; nothing in the variation research weakens it.
3. **Select `stemn` as `COUNTERPART`?** **Yes** — `stemn` is attested for the
   stem lexeme (Campbell §484) and is the unique regular CAPR output of
   `*stámniz`; it is a defensible *selected* comparator even though it is
   historically overdetermined.
4. **Add an `mn -> fn` rule?** **No** — no source posits a productive OE
   `mn -> fn`; the `f` is pre-OE and irregular; such a rule would wrongly
   convert `stemn` and other `-mn-` words.
5. **Add an `fn -> mn` rule?** **No** — although OE `fn -> mn` is *real*, it is
   sporadic/WS and unnecessary for the selected `*stámniz -> stemn` path
   (which never produces `fn`); modeling it would only generate an alternative
   comparator we do not need, at the cost of over-application.
6. **Broaden `PNWGmcMnDissimilation`?** **No** — it targets intervocalic
   `-mVn-` (`heofon`); the stem word is a `-mn-` cluster; broadening would
   break both `heofon`-type derivations and other `-mn-` words (Part 13).
7. **Retain `stefn`, `stefna`, `stofn` as comparison forms?** **Yes** — they
   are attested and etymologically relevant but are *not* regular CAPR outputs
   of the selected input (`stefn`/`stefna` need the pre-OE `-mn->-bn-`;
   `stofn` is a different `*stub-` formation), so they belong in the entry as
   comparison forms, not deterministic targets.

## 19. Recommended content for a future row NOTE (do NOT edit the TSV now)

> Stem/trunk/prow lexeme: PGmc `*stámnaz`, i-stem variant `*stámniz` (Orel
> 2003:371). Selected input `*stámniz` regularly yields OE `stemn` via SC020
> z-deletion, SC055 i-umlaut, SC063 high-vowel apocope (retained `-mn-`).
> Attested variants `stefn` (m., stem/prow), `stefna` (weak n-stem, nautical
> 'prow/stern'), `stofn` (mf., `*stubna-`, 'trunk/stump') are comparison forms,
> not modeled outputs. The `f` of `stefn`/ON `stafn` reflects the pre-OE
> Germanic `-mn- > -bn-(> fn)` tendency (Polomé 1967; Fulk §6.14); OE also has
> a sporadic West-Saxon `fn -> mn` (Campbell §484) that independently yields
> `stemn`, so attested `stemn` is historically overdetermined. Distinct from
> the voice homonym `stefn/stemn` < `*stebnō/*stimnō-`. No new sound law added;
> `PNWGmcMnDissimilation` (intervocalic `heofon`-type) is not broadened.

## 20. Recommended content for the final book entry

- **Regular modeled path**: `*stámnaz` (citation) → i-stem input `*stámniz`
  → `stemn`, by regular z-deletion, i-umlaut, and high-vowel apocope, with the
  `-mn-` cluster retained. Italic OE forms; `\emph{*stámniz}` for the
  reconstruction.
- **Attested variation**: present `stefn`, `stefna` (nautical n-stem), `stofn`
  (separate `*stub-` formation) as comparison forms with glosses and one
  attestation each; keep OS `stamn`, ON `stafn`, OFris `stevene`, OHG/G
  `Stamm` in the comparative note.
- **Historically understood processes**: state the Germanic `-mn- > -bn-`
  origin of the `f`, and the sporadic West-Saxon `fn -> mn`, each with page-
  numbered citations (Polomé 1967:818–819; Fulk §6.14; Campbell §484;
  Luick §75; Brunner §193.2; Bülbring §485).
- **Unresolved variation**: note the overdetermination of `stemn` and the
  Torp `*stab-` alternative for the `f`-forms; do not adjudicate them.
- **Explicitly unmodeled**: CAPR does not model `mn ↔ fn` for this word and
  does not broaden `PNWGmcMnDissimilation`; `stefn/stefna/stofn` are not
  generated by the cascade.
- **Control note**: mention that the same OE `fn ~ mn` operates in the
  unrelated 'voice' homonym, kept strictly separate.

## 21. Source table / bibliography (exact locators)

- Orel, V. (2003). *A Handbook of Germanic Etymology*. Leiden: Brill.
  pp. 371 (`*stamnaz *stamniz`), 373 (`*stebnō ~ *stemnō`).
  [`orel_handbook_germanic_etymology.vision.txt:41239, :41519`; page markers
  `:37025`, `:37242`]
- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*. Leiden:
  Brill. p. 480 (`*stimno-`, `*stebnō-`, `*-mn- > *-bn-`).
  [`kroonen_etymological_dictionary_pgmc.vision.txt:24696, :1738`]
- Kroonen, G. (2011). *The Proto-Germanic n-stems*. Amsterdam: Rodopi.
  p. 183 (`stefn`/`heofon`/`levene`, "vocalization of the m"), p. 286
  (`*stubna/ō-` `stofn`). [`kroonen_2011_n_stems.vision.txt:8286, :12975`]
- Kroonen, G. (2006). "Gemination and allomorphy in the Proto-Germanic
  mn-stems: bottom and rime." *ABäG* 61: 17–25.
  [`kroonen_2006_mn_stems_bottom_rime.txt:1`]
- Polomé, E. C. (1967). "Notes on the Reflexes of IE /ms/ in Germanic."
  *RBPh* 45.3. pp. 818–819. [`polome_1967_reflexes_ie_ms.txt:867`]
- Fulk, R. D. (2018). *A Comparative Grammar of the Early Germanic Languages*.
  Amsterdam: Benjamins. §6.14 and n. 6.
  [`fulk_comparative_grammar_early_germanic.vision.txt:7365, :7403`]
- Campbell, A. (1959). *Old English Grammar*. Oxford. §§193.d n. 4, 484, 328.
  [`campbell_old_english_grammar.txt:5504, :12570, :15225`]
- Luick, K. (1914–40). *Historische Grammatik der englischen Sprache*.
  §75 Anm. 1; §186. [`luick_historische_grammatik.txt:5988, :11332, :16996`]
- Brunner, K. (1965). *Altenglische Grammatik* (Sievers–Brunner). §193.2;
  §201. [`brunner_1965_altenglische_grammatik.vision.txt:8044, :4016`]
- Bülbring, K. D. (1902). *Altenglisches Elementarbuch*. §485.
  [`bulbring_altenglisches_elementarbuch.txt:9012`]
- Ringe, D. & Taylor, A. (2014). *The Development of Old English* (A Linguistic
  History of English, vol. 2). Oxford. p. 346.
  [`ringe_taylor_linguistic_history_vol2.txt:18934`]
- Clark Hall, J. R. (1960). *A Concise Anglo-Saxon Dictionary*. 4th ed.
  pp. 276, 341. [`clark_hall_concise_anglo_saxon_dictionary.vision.txt:38045,
  :38341`]
- Bosworth, J. & Toller, T. N. *An Anglo-Saxon Dictionary* (+ Supplement).
  s.vv. `stefn`, `stefna`, prow compounds.
  [`bosworth_toller_anglo_saxon_dictionary.vision.txt` passim]

Cross-reference: `Germanic/docs/dossier-stem-2026.md` (i-stem input
hypothesis); `Germanic/docs/audits/2216-stem-before-state.md`;
`Germanic/docs/audits/2216-stem-candidate-probe.md`.

# SC053-SC054 Pre-umlaut Bridge and W-loss — literature dossier

## Rule metadata

- **change_ids:** SC053; SC054
- **display_names:** OE Post Velar W Loss; OE W Loss Before I
- **FOMA rule names:** `OEPostVelarWLoss`; `OEWLossBeforeI`
- **current_orders:** SC053 immediately precedes SC054 between the promoted SC052 hinge report and the promoted SC055-SC056 umlaut-core report
- **chronology card paths:**
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC053-oe-post-velar-w-loss.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC054-oe-w-loss-before-i.md`
- **representative failures / witnesses:**
  - SC053: none; the card found no positive first-break boundary in either direction
  - SC054: `sea`
- **local chronology summary:**
  - SC053 has no positive earlier boundary: the earlier search stops at bundled `PWGmcChanges`.
  - SC053 has no positive later boundary: the later search finds no real break before the current search boundary at SC087.
  - SC054 must follow SC020, with `sea`.
  - SC054 must precede SC063, with `sea`.
  - The pair is adjacent and book-useful as bridge material, but the live positive chronology resides almost entirely in SC054.

## Historical problem

SC053-SC054 now sits in a narrow but awkward chronological slot. On the left is the promoted SC052 velar-palatalization hinge report. On the right is the promoted SC055-SC056 umlaut-core report. The assembled book therefore needs explicit prose for both ordinary FST changes here without pretending that they form a large textbook chapter.

SC053 is the weaker member. CAPR implements it as the narrow simplification of `*ngw` to `*ng`, matching derivations such as `*singwan > singan`, but the chronology card finds no positive first-break boundary in either direction. That makes SC053 hard to narrate as a genuine chronology anchor. SC054 is stronger: the rule deleting `w` before unstressed `i` is a real handbook phenomenon, and the `sea` derivation gives it a narrow but historically intelligible two-sided chronology profile. The chapter-shape problem is therefore whether the eventual prose should remain a short adjacent SC053-SC054 bridge report or become an even shorter SC054-centered note that still keeps SC053 visible as residual bridge material.

## Source dossier

### Ringe and Taylor 2014

- **source_key:** `RingeTaylor2014`
- **locator:** §6.4.2; §6.7.1
- **terminology:** early changes of front vowels and loss of `*w` before `*i`; narrow `*ngw > *ng` simplification
- **short quotation:** "`loss of *w before *i`"; "`PGmc *singwan ... > OE singan`"
- **paraphrase:** Ringe and Taylor provide the cleanest source framing for both members of the pair. In their Old English sound-change sequence they explicitly discuss loss of `*w` before `*i`, deriving `PGmc *saiwiz` 'sea' through `*sawi > *sei > OE sǣ` [@RingeTaylor2014, §6.7.1]. Elsewhere they also derive `PGmc *singwan` to OE `singan`, which gives a narrow comparative anchor for SC053's `*ngw > *ng` simplification [@RingeTaylor2014, §6.4.2].
- **conditioning:** for SC054, non-word-initial `w` before unstressed `i`; for SC053, `w` after non-initial velars in `*ngw` clusters
- **chronology:** Ringe and Taylor make SC054 historically legible as an early pre-umlaut development. Their `sea` derivation fits CAPR's need to place SC054 before later umlaut material. SC053 receives only thin comparative support: it looks like a narrow cleanup inside a larger velar/glide zone rather than a separately narrated chapter.
- **examples:** `*saiwiz > *sawi > *sei > sǣ`; `*singwan > singan`
- **cautions:** This source strongly supports SC054, but it does not turn SC053-SC054 into a natural pair. SC053 remains implicit and narrow even here.

### Campbell 1959

- **source_key:** `Campbell1959`
- **locator:** §406; discussion of `sǣ` / `ē` paradigms
- **terminology:** loss of `w` before `i`; analogical restoration of `w`
- **short quotation:** "`OE forms often show loss of [w] before i`"
- **paraphrase:** Campbell gives the classical handbook statement that Old English often loses `w` before `i`, while also warning that analogy frequently restores the glide in many paradigms [@Campbell1959, §406]. He treats `sǣ` 'sea' as a standard example developed from `*saiwi-`, and he notes abnormal forms such as `sǣwe` that preserve or restore the glide [@Campbell1959, §406].
- **conditioning:** `w` before `i` in weak verbs and noun paradigms; analogical restoration obscures the bare phonological development
- **chronology:** Campbell supports a genuinely historical SC054, but one whose surface reflexes are often reshaped by analogy. That matters for the eventual report: the rule belongs before the umlaut core, yet it should still be narrated as a narrow bridge process rather than a broad central chapter.
- **examples:** `sǣ`; `ē`; restored or exceptional `sǣwe`
- **cautions:** Campbell is excellent for SC054's source basis and for the warning about analogical noise. He does not provide an equally strong separate chapter rationale for SC053.

### Luick 1914

- **source_key:** `Luick1914`
- **locator:** §187
- **terminology:** umlauted `ā/ă` after earlier loss of the glide
- **short quotation:** "`sa 'See' (aus *sāwi- < wg. *saiwi-)`"
- **paraphrase:** Luick cites `sa` 'sea' from `*sāwi- < *saiwi-` as a clear example in the discussion of early Old English umlaut outcomes [@Luick1914, §187]. That makes him useful for the sequencing point: the glide must already be gone for the later fronted vowel result to emerge in the way the handbook tradition describes it.
- **conditioning:** inherited `*aiw` / `*āwi` material before later umlaut effects
- **chronology:** Luick reinforces the same chronology as Campbell and Ringe and Taylor: the glide-loss process belongs on the pre-umlaut side of the vowel changes.
- **examples:** `sa` / `sǣ` 'sea'
- **cautions:** Luick supports SC054's chronology, but he says nothing about an SC053-SC054 pair and nothing substantial about SC053 itself.

## CAPR formulation versus literature

CAPR's `OEPostVelarWLoss` is much narrower than most handbook sound-change chapters. The live rule is simply:

```text
*w -> 0 || *n *g _
```

That maps well enough onto the comparative derivation `*singwan > singan`, and the internal rule comment is careful to restrict the process to `*ngw > *ng` while excluding post-vocalic `*gw` cases such as `snow` and `swallow`. But the literature support is correspondingly thin. SC053 looks more like residual implementation bridge material than like a chapter center, and the chronology card confirms that by providing no positive first-break boundary in either direction.

`OEWLossBeforeI`, by contrast, aligns directly with a real source tradition:

```text
*w -> 0 || EnglishStarVocalic _ *i .#.
```

Campbell, Ringe and Taylor, and Luick all support the `sea` derivation and the underlying historical point that loss of `w` before unstressed `i` belongs before later umlaut outcomes [@Campbell1959, §406; @RingeTaylor2014, §6.7.1; @Luick1914, §187]. That makes SC054 historically legible, though still narrow. The rule is not a major textbook headline on the scale of SC055 i-umlaut, but it is more than a purely internal CAPR convenience.

The pairing itself is therefore practical and chronological rather than traditional. SC053 and SC054 are adjacent ordinary FST changes that both need explicit prose. Yet only SC054 has strong source-backed chronology, and even that evidence is narrow because both positive boundaries currently depend on the same `sea` derivation. The eventual report should present the unit as a modest bridge, not as a strong historical chapter.

## Chronology implications

- SC053 has no positive earlier boundary; the earlier search stops at bundled `PWGmcChanges`.
- SC053 has no positive later boundary; the later search records only a no-break-before-search-boundary result at SC087.
- SC054 must follow SC020, with `sea`.
- SC054 must precede SC063, with `sea`.
- SC053 and SC054 do not form an internal reciprocal pair.
- The evidence therefore supports a bridge treatment in which SC053 stays explicit as residual material and SC054 carries the real positive chronology.
- Any eventual production report should keep SC054 in strict chronological position between SC052 and SC055-SC056, while treating the later SC063 relation as a cross-reference rather than as a reason to build a non-contiguous chapter.

## Open questions

- Should SC053-SC054 eventually become a short adjacent bridge report?
- Should the final prose instead become an SC054-centered note with SC053 kept visible as boundary-limited residual material?
- How much space does SC053 deserve, given its thin source tradition and card-negative profile?
- How much of the `sea` derivation should the book spell out for SC054?
- How should SC054 point rightward to later chronology such as SC063 without turning that relation into a non-contiguous chapter?
- How can the final prose keep the "every ordinary FST change gets explicit prose" rule visible without overpromoting this narrow bridge?

## Dossier status

draft_complete

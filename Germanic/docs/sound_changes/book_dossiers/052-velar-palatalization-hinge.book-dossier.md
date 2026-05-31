# SC052: Velar Palatalization Hinge

## 1. Role in the book

`SC052` is the next mature unresolved palatalization-side candidate after the
promotion of `SC051`. It now sits between a left-edge feeder (`SC050`) and the
already promoted `SC055-SC056` umlaut core, making it one of the clearest
remaining hinge units in the sound-change half.

That does not mean the chapter shape is settled. The real question is whether
the book eventually wants:

1. a standalone `SC052` hinge report; or
2. a narrower `SC050-SC052` paired report.

## 2. Name and basic formulation

- **main change_id:** `SC052`
- **display_name:** `OE Velar Palatalization`
- **rule_name:** `OEVelarPalatalization`
- **current_order:** `52`
- **contextual left change:** `SC050` **Sievers Law Syncope** (`SieversLawSyncope`, order `50`)
- **contextual right change:** `SC055` **OE I Umlaut** (`OEIUmlaut`, order `55`)
- **related later question:** `SC057` **OE J Cluster Coalescence** (`OEJClusterCoalescence`, order `57`)
- **cards:**
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC050-sievers-law-syncope.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC052-oe-velar-palatalization.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC055-oe-i-umlaut.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC057-oe-j-cluster-coalescence.md`

Working formulation: `SC052` isolates the Old English palatalization of plain
velars `k/g` in the front-vocalic and `j`-adjacent environments that CAPR tests
locally. It is close to, but not the same as, the already promoted `SC051`
`sk`-palatalization rule.

## 3. Traditional description and literature

The literature dossier supports a stable middle position.

The standard grammars all support plain velar palatalization as a real Old
English development. They also keep it close to the wider palatalization zone
that includes `sk`-palatalization, while treating i-umlaut as a later and
larger vowel chapter. That is the strongest argument for `SC052` as a hinge:
the process is historically real and chapter-capable, but it lives between two
already promoted neighbors rather than replacing either of them.

The weakest source support concerns `SC050`. Specialist Sievers-law work shows
why the left-edge feeder is real, but it does not naturally turn Sievers-law
syncope into the same historical chapter as velar palatalization. So the live
question is mainly chapter architecture, not process reality.

## 4. Formal implementation

In CAPR, `OEVelarPalatalization` is a targeted consonant rule.

1. `*k` becomes palatal before front vowels, before `*j`, and in a few
   front-vowel-adjacent positions that preserve the modeled contrast.
2. `*g` likewise becomes palatal before front vowels, after front vowels at
   certain edges, and before `*j`.

`SC050` matters here only as feeder/context unless the chapter is later paired:
`SieversLawSyncope` deletes `*i` before `*j` after a consonantal environment,
which is exactly why the `stretch` relation is visible at all.

## 5. Place in the cascade

`SC052` sits in a structurally rich position.

1. It follows `SC050` **Sievers Law Syncope**.
2. It also follows the already promoted `SC051` **OE Sk Palatalization** in the assembled order.
3. It precedes the `SC053-SC054` pre-umlaut bridge.
4. It precedes the already promoted `SC055-SC056` **umlaut-core** report.
5. `SC057` remains a later unresolved palatalization-side question downstream.

This makes `SC052` more naturally a hinge chapter than a residual placeholder.

## 6. Order-testing evidence

The local network is stronger than ordinary scaffold material.

1. `SC050`'s later boundary is across `SC052`, with `stretch`.
2. `SC052`'s earlier boundary is across `SC050`, also with `stretch`.
3. `SC052`'s later boundary is across `SC055`, with `cow` and `lung`.
4. `SC050`'s earlier side is runner-limited and not a positive historical boundary.

So the real evidence is asymmetric but meaningful: `SC052` itself is anchored on
both sides, while `SC050` is only locally strong on the right.

## 7. Interpretation for the book

`SC052` is probably stronger than a residual scaffold.

The main uncertainty is not whether plain velar palatalization is real. It is
whether the book should present that reality as a standalone hinge chapter or as
part of a narrower `SC050-SC052` pair.

Whatever shape is chosen later, the report should avoid duplication in both
directions:

1. it should not repeat the already promoted `SC051` singleton as if all
   palatalization were one chapter;
2. it should not rewrite the already promoted `SC055-SC056` report as if the
   umlaut core were merely a continuation of `SC052`.

## 8. Relation to neighbouring changes

1. **SC050 Sievers Law Syncope** is the possible left feeder and the only serious candidate for a paired left edge.
2. **SC051 OE Sk Palatalization** is the already promoted neighboring palatalization singleton.
3. **SC055-SC056 Umlaut core** is the already promoted right context.
4. **SC057 OE J Cluster Coalescence** remains later unresolved palatalization-side material.

## 9. Remaining uncertainty

1. Standalone `SC052` versus a later `SC050-SC052` pair.
2. The role of `SC057` in any future palatalization-side architecture.
3. How much narrative weight the single `stretch` feeder witness should bear.
4. The risk of duplicating the promoted `SC051` report.
5. The risk of duplicating the promoted umlaut-core report.

## 10. Proposed book-section outline

1. **If promoted later as standalone `SC052`**
   1. Why plain velar palatalization deserves its own hinge chapter
   2. How it relates to but differs from `SC051`
   3. `SC050 < SC052 < SC055`
   4. Why the right edge matters for the umlaut core
   5. What remains unresolved with `SC057`
2. **If promoted later as `SC050-SC052`**
   1. A left-edge feeder and a palatalization hinge
   2. What `stretch` actually proves
   3. Why the pair still centers on `SC052`
   4. How the pair leads into the promoted umlaut core
   5. Why the chapter must still avoid duplicating `SC051`

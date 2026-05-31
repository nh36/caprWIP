# SC066-SC068: Syncope and Degemination Corridor

## 1. Role in the book

SC066-SC068 is now the clearest remaining corridor-scale candidate after the
promotion of SC026-SC027. It tests a different kind of chapter shape from the
nasal-spirant report: not a bundled early Germanic law, but a late weak-tail
sequence in which vowel reduction creates new consonant clusters and the model
then cleans them up.

That makes it a useful next candidate for the production layer. The corridor
already has visible local order evidence, especially around `spindle`, but it
still needs human review because the chapter shape is not fully settled. The
sources support syncope strongly, cluster simplification moderately, and the
three-rule segmentation only unevenly.

## 2. Name and basic formulation

- **change_ids:** `SC066`; `SC067`; `SC068`
- **display_names:** `OE L Adjacent Syncope`; `OE Dental Assimilation`; `OE Preconsonantal Degemination`
- **rule_names:** `OELAdjacentSyncope`; `OEDentalAssimilation`; `OEPreconsonantalDegemination`
- **current_orders:** `66`; `67`; `68`
- **cards:**
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC066-oe-l-adjacent-syncope.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC067-oe-dental-assimilation.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC068-oe-preconsonantal-degemination.md`

Working formulation: CAPR currently treats the corridor as a late Old English
sequence in which a medial vowel is lost next to `l`, new clusters are locally
assimilated where necessary, and preconsonantal geminates are simplified before
sonorants. The historical core is strongest for the syncope plus downstream
cluster-cleanup logic, weaker for the exact three-part segmentation.

## 3. Traditional description and literature

The new literature dossier points in a fairly consistent direction.

Campbell, Hogg, Luick, Brunner, and Ringe and Taylor all distinguish final
high-vowel loss from medial syncope rather than collapsing them into one rule.
That matters because the corridor sits in the late weak-tail zone after the
apocope material represented earlier in the book by SC063.

The same sources also support the idea that syncope can create awkward
consonant groups that then undergo secondary cleanup. Hogg says this in the
broadest way, Ringe and Taylor most explicitly, and Brunner gives especially
useful support for the `nettle` type. The historical tradition, however, does
not naturally present all three CAPR rules as coequal named laws. `SC066` is
clearly handbook-facing; `SC068` is intelligible as a consequence of cluster
formation; `SC067` is the most likely bridge member rather than the core of the
chapter.

## 4. Formal implementation

The three CAPR rules are simple in prose even if the historical mapping is not.

1. `OELAdjacentSyncope` deletes medial `*i` before `l` after a stressed syllable.
2. `OEDentalAssimilation` deletes `*θ` after `*t`, treating a post-syncope dental cluster as unstable.
3. `OEPreconsonantalDegemination` simplifies `tt` and `nn` before a following sonorant.

This is useful book material because it shows how CAPR makes cleanup logic
explicit. The literature often describes syncope and the resulting consonant
adjustments more holistically. CAPR instead keeps them as adjacent operations so
the derivational order can be tested.

## 5. Place in the cascade

In the assembled sound-change half, this corridor belongs after SC063 and the
immediate post-apocope tail, but before the larger late unstressed-tail cluster.

1. On the left, SC063 provides the earlier weak-tail context.
2. SC064-SC065 form the immediate post-apocope tail that leads into the present corridor.
3. SC066-SC068 then makes one narrow syncope-and-cleanup sequence explicit.
4. On the right, SC069-SC078 continues the broader late unstressed-tail cluster.

That placement gives the corridor a good narrative role: it can show what
happens once earlier weak-tail reductions have opened the door to later medial
loss and local consonant repair.

## 6. Order-testing evidence

The chronology cards are strong at the edges and weaker in the middle.

1. `SC066` must follow `SC055` OE I Umlaut. The key witnesses are `nettle` and `spindle`.
2. `SC066` must precede `SC068` OE Preconsonantal Degemination. The key witness is `spindle`, where delaying syncope leaves `spinnl`.
3. `SC067` currently has no positive earlier or later first-break boundary; both sides are limited by the present search space rather than by a detected historical break.

So the clearest positive local claim is not "all three rules form a perfect
reciprocal chain." It is narrower: the present model strongly requires
`SC066 < SC068`, while `SC067` sits between them as a plausible but presently
less decisive bridge rule.

## 7. Interpretation for the book

If promoted later, this corridor would show that late weak-tail reduction is not
just about vowel loss in isolation. Once syncope removes a medial vowel, the
language has to live with the cluster that remains, and CAPR makes that cleanup
logic visible.

That is the positive book value of the chapter. The caution is that the book
should distinguish clearly between:

1. literature-backed phonological processes such as late medial syncope and downstream simplification;
2. CAPR-specific segmentation choices such as giving the dental cleanup its own named step.

In other words, the chapter could be very good production prose, but only if it
admits that the three-rule corridor is partly historical description and partly
formal articulation.

## 8. Relation to neighbouring changes

1. **SC063 OE High Vowel Apocope** is the main earlier weak-tail context and should remain explicitly visible in any future chapter introduction.
2. **SC064-SC065** form the immediate post-apocope tail and help explain why SC066-SC068 belongs in the late reduction zone rather than in an isolated consonant chapter.
3. **SC069-SC078** is the broader late unstressed-tail cluster that follows after this narrower corridor and should remain separate unless future splitting changes the architecture.

The corridor therefore looks chapter-sized precisely because it sits between an
already-promoted weak-tail chapter and a still-broad late-tail scaffold.

## 9. Remaining uncertainty

1. It is still unclear whether all three rules should remain equal members of one promoted chapter.
2. `SC067` may prove to be a bridge note rather than a core corridor anchor.
3. The final chapter label is unsettled: **Syncope and Degemination Corridor** is serviceable, but a more explicitly late weak-tail label may read better in book prose.
4. `SC068` may need to be narratively subordinate to syncope rather than presented as a coequal headline process.
5. `spindle` is extremely useful, but it may end up carrying too much of the local order argument if no broader witness set is foregrounded.

## 10. Proposed book-section outline

1. **Late weak-tail syncope and cluster cleanup**
2. **Why this corridor follows the apocope zone**
3. **SC066 as the main handbook-facing syncope rule**
4. **Why syncope creates a cleanup problem**
5. **SC067 as dental assimilation inside the cleanup sequence**
6. **SC068 and the `spindle` problem**
7. **What the chronology cards really prove**
8. **Which parts come from the literature, and which from CAPR's segmentation**
9. **Why this chapter probably stays narrow rather than expanding into the whole late-tail cluster**

# Pilot book dossier report

## 1. Dossiers created

This pass created two prose-ready pilot dossiers:

1. `Germanic/docs/sound_changes/book_dossiers/043-anglo-frisian-brightening.book-dossier.md`
2. `Germanic/docs/sound_changes/book_dossiers/063-oe-high-vowel-apocope.book-dossier.md`

These are the two sound changes that the inventory had already identified as the only current cases with substantial literature material and first-draft readiness.

## 2. Existing files used

The dossiers were built from existing repository material only. The main inputs were:

1. `Germanic/docs/sound_changes/book_dossiers/sound_change_book_dossier_inventory.tsv`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC043-anglo-frisian-brightening.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC063-oe-high-vowel-apocope.md`
4. `Germanic/docs/sound_changes/literature_dossiers/043-anglo-frisian-brightening.dossier.md`
5. `Germanic/docs/sound_changes/literature_dossiers/063-oe-high-vowel-apocope.dossier.md`
6. `Germanic/docs/sound_changes/change_entries/043-anglo-frisian-brightening.change.md`
7. `Germanic/docs/sound_changes/change_entries/063-oe-high-vowel-apocope.change.md`
8. `Germanic/fsts/germanic.txt`
9. the existing chronology export layer, especially `chronology_graph_edges_core.tsv` and `chronology_graph_edges_contextual.tsv`
10. the repository reference witnesses already harvested into the literature dossiers

## 3. Did the mini-chapter template work?

Yes. The ten-part template is workable for prose-ready dossier writing when the following layers are all present:

1. a stable chronology card;
2. a substantial literature dossier;
3. a known FOMA definition;
4. at least one existing change-entry or chapter scaffold.

It worked especially well for distinguishing:

1. the historical rule as presented in the literature;
2. the internal CAPR formalization;
3. the narrow order-testing evidence;
4. the near-book prose synthesis.

## 4. What should change before scaling further?

Before scaling beyond the two pilots, the workflow would benefit from a few refinements:

1. **Keep literature and implementation visibly separate.** The dossier format works best when the historical rule is stated first and the FOMA material is then framed as an implementation of it, not as a replacement for it.
2. **Expect one technical note per chapter.** Both pilots needed a short explanation of which parts of the implementation are model-specific approximations rather than headline historical claims.
3. **Treat chronology exports as supporting metadata, not chapter structure.** The graph/export layer helped identify neighbors, but the best prose still came from the literature dossiers and chronology cards rather than from edge TSVs.
4. **Add a short source-provenance header if this scales.** The current pilot structure works, but later dossiers would benefit from a compact block listing the exact literature dossier, change entry, chronology card, and FOMA rule location up front.
5. **Decide how much exact FOMA to quote.** The short SC043 rule quotes cleanly; the longer SC063 rule is still usable, but later dossiers may need a house style distinguishing full rule quotation from excerpt-plus-appendix treatment.

## 5. What should be done next?

The next step should **not** be graph visualization.

Of the two strategic paths:

1. **Path A:** continue drafting only where substantial literature dossiers already exist;
2. **Path B:** create literature dossiers for the next high-priority reciprocal/local pairs before attempting more prose-ready book dossiers;

the present pilots support **Path B**.

Path A is effectively exhausted for now, because these two pilots are the only current cases with substantial literature-backed dossier material. The practical next move is therefore to create literature dossiers for the next high-priority reciprocal/local pairs and only then promote them into book dossiers.

Recommended next literature-dossier targets:

1. `SC016 / SC017`
2. `SC019 / SC020`
3. `SC052 / SC055`
4. `SC054 / SC055`, if later review confirms that this is the most useful late-cluster pairing for prose rather than merely a narrow local dependency

Once at least one of those pairs has a substantial literature dossier, the next agent task should build the corresponding prose-ready book dossiers in the same format used here.

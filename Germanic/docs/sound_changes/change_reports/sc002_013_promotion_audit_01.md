# SC002-SC013 backend promotion audit 01

## Baseline findings

1. `SC001` is excluded from backend promotion because `sound_change_inventory.tsv` marks it as a `support_stage` and explicitly notes that it is an input handoff stage rather than a historical sound-change entry.
2. `SC002-SC013` are all marked `historical_sound_change` with `include_in_volume=yes` in `Germanic/docs/sound_changes/sound_change_inventory.tsv`.
3. `SC002-SC013` are not yet present in `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`.
4. Existing order-test infrastructure for `SC002-SC013` is limited. `order_sensitivity_first_break_batch_04_manifest.tsv` marks `SC002-SC013` as `skipped` because the current runner does not yet reorder inside bundles or non-explicit chain positions.

## Existing evidence by SC number

| SC | Display name | FOMA rule | Historical stage | Compact-trace count | Example lexemes | `needs_human_review` | Likely report shape | Source/dossier material now present | Chronology/order-test status | What is still missing before reader-facing use |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- |
| `SC002` | Gm Simplification | `PGmcGmSimplification` | Proto-Germanic | 2 | `dream`, `team` | no | singleton | **Created in this pass:** full report, literature dossier, book dossier | No validated card before this pass; draft card created from batch-04 skip status | Validated order evidence; broader phonological source discussion beyond lexical dictionaries; stronger confirmation of the `team` family in prose use |
| `SC003` | Rhotacism | `PGmcRhotacism` | Proto-Germanic in inventory; stage label needs review | 7 | `deer`, `hoard`, `learn`, `berry`, `learn (3sg)` | no | singleton | **Created in this pass:** full report, literature dossier, book dossier | No validated card before this pass; draft card created from batch-04 skip status | Validated order evidence; explicit stage-label review against WGmc/NWGmc framing in the literature |
| `SC004` | PWGmc Ai Monophthongization | `PWGmcAiMonophthongization` | Proto-West Germanic | 25 | `bone`, `deal`, `dough`, `flesh`, `ghost` | no | singleton opener | No dedicated report or dossier yet | No card; only skipped batch-04 status | Full report, dossiers, draft/validated chronology support, source consolidation |
| `SC005` | NWGmc A To U Before M | `NWGmcAToUBeforeM` | Northwest Germanic label inside PWGmc bundle | 1 | `shoulder` | yes | cautious singleton | No dedicated report or dossier yet | No card; only skipped batch-04 status | Full report, dossiers, chronology support, and human review of stage labeling inside the PWGmc bundle |
| `SC006` | PWGmc Early I Apocope | `PWGmcEarlyIApocope` | Proto-West Germanic | 9 | `thousand`, `bore (3sg)`, `have`, `learn (3sg)`, `lick (3sg)` | no | singleton | No dedicated report or dossier yet | No card; only skipped batch-04 status | Full report, dossiers, chronology support |
| `SC007` | PWGmc Final Or Lowering | `PWGmcFinalOrLowering` | Proto-West Germanic | 2 | `four`, `water` | no | possible pair with SC008 | No dedicated report or dossier yet | No card; only skipped batch-04 status | Source check on relation to SC008; reports/dossiers/cards |
| `SC008` | PWGmc Coronal W Assimilation | `PWGmcCoronalWAssimilation` | Proto-West Germanic | 1 | `four` | no | possible pair with SC007 | No dedicated report or dossier yet | No card; only skipped batch-04 status | Source check on relation to SC007; reports/dossiers/cards |
| `SC009` | PWGmc Ij Contraction | `PWGmcIjContraction` | Proto-West Germanic | 1 | `friend` | no | likely singleton unless grouped later | No dedicated report or dossier yet | No card; only skipped batch-04 status | Source support and chronology support; grouping still uncertain |
| `SC010` | PWGmc J Gemination | `PWGmcJGemination` | Proto-West Germanic | 8 | `hedge`, `net`, `set`, `sit`, `will` | no | likely singleton or narrow j-development set | No dedicated report or dossier yet | No card; only skipped batch-04 status | Source support and chronology support; grouping still uncertain |
| `SC011` | PWGmc Syllabic J | `PWGmcSyllabicJ` | Proto-West Germanic | 0 | — | no | likely separate note unless evidence grows | No dedicated report or dossier yet | No card; only skipped batch-04 status | Example set, source support, chronology support; especially weak backend evidence at present |
| `SC012` | PWGmc L Th Voicing | `PWGmcLThVoicing` | Proto-West Germanic | 4 | `field`, `fold`, `gold`, `wold` | no | possible pair with SC013 | No dedicated report or dossier yet | No card; only skipped batch-04 status | Source check on relation to SC013; reports/dossiers/cards |
| `SC013` | PWGmc Dental Hardening | `PWGmcDentalHardening` | Proto-West Germanic | 4 | `lade`, `needle`, `find`, `cud` | no | possible pair with SC012 | No dedicated report or dossier yet | No card; only skipped batch-04 status | Source check on relation to SC012; reports/dossiers/cards |

## Proposed grouping plan after review

1. **SC002** — keep as a singleton. The lexical support is narrow and there is no evidence for a broader grouped treatment.
2. **SC003** — keep as a singleton. The historical phenomenon is clear, but the stage label needs review before any grouping question matters.
3. **SC004** — likely singleton opener. It has enough trace weight to stand alone if backend resources are prepared.
4. **SC005** — cautious singleton. The `needs_human_review=yes` flag and its NWGmc label inside the PWGmc bundle make it a poor grouping candidate until the stage-label issue is settled.
5. **SC006** — likely singleton. It has its own morphophonological identity and a usable trace set.
6. **SC007-SC008** — plausible later pair. Both touch the `four` family, so a paired backend batch is worth evaluating once source support is assembled.
7. **SC009-SC011** — do not pre-group yet. The shared j-development theme is real, but `SC011` currently has no compact-trace occurrence count and would need separate evidence before a grouped plan is persuasive.
8. **SC012-SC013** — possible later pair. The consonant-focused shape is suggestive, but no source or chronology layer yet supports the grouping strongly enough to commit to it.

## SC002-SC003 manifest decision

1. `report_manifest.tsv` should remain unchanged in this pass.
2. SC002 and SC003 now have production-style reports and dossier stubs, but their chronology layer is still only draft-level because the current order-test infrastructure skips them.
3. SC002 also still needs broader phonological source support beyond the lexical dictionary evidence now in hand.
4. SC003 additionally needs a stage-label review because the strongest literature frames rhotacism later than the current inventory label suggests.

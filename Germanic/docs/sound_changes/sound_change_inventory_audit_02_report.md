# Sound-change inventory audit 02 report

## Summary

- Total sandbox stages inspected: **95**.
- Historical sound changes: **84**.
- Support stages: **2**.
- Orthography/surface stages: **5**.
- Duplicate applications: **1**.
- Technical markers: **3**.
- Left uncertain: **0**.
- Proposed main book entries: **84**.
- Proposed appendix entries: **8**.

## What changed

- Updated `Germanic/docs/sound_changes/sound_change_inventory.tsv` with classification columns: `entry_type`, `include_in_volume`, `historical_stage`, `pipeline_stage`, `canonical_change_id`, `duplicate_group`, `is_reader_facing`, `needs_human_review`, and `review_note`.
- Rebuilt `Germanic/docs/sound_changes/sound_change_aliases.tsv` with explicit trace, sandbox, FOMA, normalized, book-display, and literature-search aliases.
- Added `Germanic/docs/sound_changes/sound_change_book_entry_plan.tsv` as the first draft table of contents for the sound-change volume.
- Updated the two pilot change-entry stubs to carry the new classification metadata.
- Added this report at `Germanic/docs/sound_changes/sound_change_inventory_audit_02_report.md`.

## Classification principles

- `historical_sound_change`: a reader-facing rule likely to become a main volume entry.
- `support_stage`: a pipeline handoff or validator needed by the transducer, but not a book entry.
- `orthography_surface`: a post-phonological spelling/surface conversion rule worth appendix treatment at most.
- `duplicate_application`: a second sandbox checkpoint for a rule already represented by a canonical entry.
- `technical_marker`: an internal marker or cleanup rule used to manage conditioning rather than to assert a standalone historical change.

## Historical stage vs pipeline stage

| change_id | display_name | historical_stage | pipeline_stage | review_note |
| --- | --- | --- | --- | --- |
| SC001 | Proto Input | Technical | Proto-Germanic consonant inheritance | Input handoff stage feeding the cascade, not a historical sound change entry. |
| SC005 | NWGmc A To U Before M | Northwest Germanic | Proto-West Germanic developments | NWGmc-labeled rule remains inside the PWGmcChanges pipeline bundle; preserve bundle order but flag the historical label split. |
| SC016 | OE Ws Palatal Glide | Old English | Northwest Germanic developments | The rule is labeled OE/West Saxon but is checkpointed before the main Old English section break in the sandbox. |
| SC020 | PGmc Final Z Deletion | Proto-Germanic | Northwest Germanic developments | The cascade applies this PGmc-labeled rule in the NWGmc section; keep pipeline order but flag the earlier historical label. |
| SC038 | OE Strip Secondary Stress | Technical | Old English | Marker-stripping cleanup for secondary-stress graves; keep only as methodological appendix material. |
| SC041 | PWGmc Final Bare A Loss | Proto-West Germanic | Old English | PWGmc-labeled loss is implemented late in the OE pipeline; dossier work should explain the historical vs computational placement. |
| SC042 | PWGmc Surviving Bimoric O Unrounding | Proto-West Germanic | Old English | PWGmc-labeled unrounding is implemented late in the OE pipeline; keep the sandbox order but flag the chronology mismatch. |
| SC049 | PGmc B Allophony | Proto-Germanic | Old English | PGmc B Allophony is intentionally delayed in the live cascade, so the historical label and pipeline placement diverge. |
| SC050 | Sievers Law Syncope | Proto-West Germanic | Old English | Sievers Law Syncope is provisionally grouped with Proto-West Germanic developments even though the sandbox checkpoints it in the Old English section. |
| SC062 | OE Weight Markers | Technical | Old English | Identity marker stage used for weight-sensitive conditioning before apocope; appendix only. |
| SC064 | NWGmc In Stem N Loss | Northwest Germanic | Old English | NWGmc In Stem N Loss is applied after OEHighVowelApocope in the current cascade, so the historical label needs an explanatory note. |
| SC084 | OE Weight Cleanup | Technical | Old English | Identity cleanup checkpoint after weight-sensitive rules; methodological appendix only. |
| SC090 | OE Cj Cleanup | Orthography & surface | Old English | Post-cascade palatal-cluster cleanup before orthography; treat as appendix machinery, not a main sound change. |
| SC091 | OE Xs Merge | Orthography & surface | Old English | Post-cascade surface merge feeding orthographic x; keep as appendix material rather than a reader-facing historical entry. |
| SC095 | Old English Surface | Technical | Orthography & surface | Final surface acceptor/filter, not a historical sound change rule. |

Do not read these rows as requests to change the cascade. They separate the historical classification from the current computational checkpoint order only.

## Duplicate and canonical mapping

- `OEPrefixAReduction`: SC035 (OE Prefix A Reduction Early, order 35, canonical SC035), SC077 (OE Prefix A Reduction Late, order 77, canonical SC035)

## Book-entry plan

- `sound_change_book_entry_plan.tsv` currently proposes **84** main entries and **8** appendix entries.
- High-priority literature dossier candidates: PWGmc J Gemination, PGmc Final Z Deletion, NWGmc Nasal Spirant Lengthening, NWGmc Nasal Spirant Loss, PWGmc Final Bare A Loss, Anglo Frisian Brightening, OE Breaking, OE Heavy Syllable Nasal Apocope, OE Secondary Nasalization, Sievers Law Syncope, OE I Umlaut, OE Back Mutation.
- High-priority order-sensitivity candidates: NWGmc A To U Before M, OE Ws Palatal Glide, PGmc Final Z Deletion, PWGmc Final Bare A Loss, PWGmc Surviving Bimoric O Unrounding, Anglo Frisian Brightening, OE Breaking, OE Heavy Syllable Nasal Apocope, OE Secondary Nasalization, PGmc B Allophony, Sievers Law Syncope, OE I Umlaut.

## Alias mapping

- Alias rows now cover `trace_label`, `sandbox_stage_name`, `foma_rule_name`, `normalized_stage_name`, `book_display_candidate`, and `literature_search_alias` categories (495 total rows).
- Added obvious search aliases for major rules such as `OE I Umlaut` (`i-umlaut`, `i-mutation`), `Anglo Frisian Brightening` (`Anglo-Frisian brightening`, `first fronting`), `OE Breaking` (`breaking`), and the nasal-spirant rules (`nasal spirant law`).
- Uncertain or taxonomy-forced cases are flagged in the inventory `review_note` column rather than hidden inside the alias table.

## Remaining human-review items

| change_id | display_name | historical_stage | pipeline_stage | review_note |
| --- | --- | --- | --- | --- |
| SC005 | NWGmc A To U Before M | Northwest Germanic | Proto-West Germanic developments | NWGmc-labeled rule remains inside the PWGmcChanges pipeline bundle; preserve bundle order but flag the historical label split. |
| SC016 | OE Ws Palatal Glide | Old English | Northwest Germanic developments | The rule is labeled OE/West Saxon but is checkpointed before the main Old English section break in the sandbox. |
| SC020 | PGmc Final Z Deletion | Proto-Germanic | Northwest Germanic developments | The cascade applies this PGmc-labeled rule in the NWGmc section; keep pipeline order but flag the earlier historical label. |
| SC041 | PWGmc Final Bare A Loss | Proto-West Germanic | Old English | PWGmc-labeled loss is implemented late in the OE pipeline; dossier work should explain the historical vs computational placement. |
| SC042 | PWGmc Surviving Bimoric O Unrounding | Proto-West Germanic | Old English | PWGmc-labeled unrounding is implemented late in the OE pipeline; keep the sandbox order but flag the chronology mismatch. |
| SC043 | Anglo Frisian Brightening | Old English | Old English | The current taxonomy has no separate Anglo-Frisian bucket, so this rule is provisionally filed under Old English for book planning. |
| SC049 | PGmc B Allophony | Proto-Germanic | Old English | PGmc B Allophony is intentionally delayed in the live cascade, so the historical label and pipeline placement diverge. |
| SC050 | Sievers Law Syncope | Proto-West Germanic | Old English | Sievers Law Syncope is provisionally grouped with Proto-West Germanic developments even though the sandbox checkpoints it in the Old English section. |
| SC064 | NWGmc In Stem N Loss | Northwest Germanic | Old English | NWGmc In Stem N Loss is applied after OEHighVowelApocope in the current cascade, so the historical label needs an explanatory note. |

## Recommended next task

**B. Build first literature dossier pilot.**

The book-entry list is now stable enough to start one pilot dossier (preferably `SC043` or `SC063`), with the order-sensitivity runner skeleton as the next computational task after that.

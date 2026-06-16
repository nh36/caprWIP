# Reader-facing remaining gap audit 01

> Superseded editorially by `reader_facing_sc005_009_012_inclusion_01_report.md`, which records the later decision to include `SC005`, `SC009`, and `SC012` in the reader-facing sequence while keeping their cautions visible.

## Latest commit inspected

1. `a50972de docs: add reader-facing SC010 SC011 and SC013`

## Baseline confirmations

1. Local section 18 exists:
   - `Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_18_docker.sh`
   - `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_18.md`
   - `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_18.pdf`
2. Local section 18 is the current target:
   - `reader_facing_check_utils.py` sets `DEFAULT_BUILD_SCRIPT` to `build_reader_facing_local_section_18_docker.sh`
   - `README.md` now points the active local build command at section 18
3. `SC010` is reader-facing.
4. `SC011` is reader-facing.
5. `SC013` is reader-facing.
6. `SC012` is not reader-facing.
7. No `012-*.md` reader-facing file exists.
8. Local section 17 was not overwritten.
9. No FST rules or lexical TSV data were changed in the local-section-18 pass.

## Current reader-facing chapter order from `SC003` through `SC087`

1. `003-west-germanic-rhotacism.md`
2. `004-pwgmc-ai-monophthongization.md`
3. `006-early-i-apocope.md`
4. `007-final-o-lowering-before-r.md`
5. `008-coronal-w-assimilation.md`
6. `010-west-germanic-j-gemination.md`
7. `011-syllabic-j-after-final-vowel-loss.md`
8. `013-dental-hardening.md`
9. `014-015-opening-vowel-prelude.md`
10. `016-017-west-saxon-palatal-glide-and-u-lowering.md`
11. `018-stressed-monosyllable-o-raising.md`
12. `019-020-final-long-o-raising-and-final-z-deletion.md`
13. `021-unstressed-o-raising.md`
14. `022-mn-dissimilation.md`
15. `023-n-stem-n-loss.md`
16. `024-long-e-lowering.md`
17. `025-long-e-nasal-rounding.md`
18. `026-027-nasal-spirant-changes.md`
19. `028-preconsonantal-x-loss.md`
20. `029-030-awj-glide-and-au-fronting.md`
21. `031-034-west-saxon-diphthong-chain.md`
22. `035-037-prefix-and-compound-adjustments.md`
23. `039-040-medial-unstressed-vowel-changes.md`
24. `041-final-bare-a-loss.md`
25. `042-surviving-bimoric-o-unrounding.md`
26. `043-anglo-frisian-brightening.md`
27. `044-045-breaking-and-velar-fricative-palatalization.md`
28. `046-048-restoration-and-nasal-tail-changes.md`
29. `049-050-b-allophony-and-sievers-law-syncope.md`
30. `051-sk-palatalization.md`
31. `052-velar-palatalization.md`
32. `053-054-pre-umlaut-bridge-and-w-loss.md`
33. `055-056-i-umlaut-core.md`
34. `057-j-cluster-coalescence.md`
35. `058-nasal-dissimilation.md`
36. `059-oe-back-mutation.md`
37. `060-ws-palatal-umlaut-note.md`
38. `061-weak-tail-nasal-loss-note.md`
39. `063-high-vowel-apocope.md`
40. `064-065-post-apocope-tail.md`
41. `066-068-syncope-and-degemination-corridor.md`
42. `069-early-o-shortening-context-note.md`
43. `070-071-early-unstressed-fronting-shortening-bridge.md`
44. `072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md`
45. `074-075-medial-unstressed-i-lowering.md`
46. `076-prefix-i-reduction.md`
47. `078-weak-tail-reduction.md`
48. `079-080-final-j-loss-and-final-geminate-simplification.md`
49. `081-083-j-strengthening-vocalization-and-ei-contraction.md`
50. `085-086-h-loss-and-contraction.md`
51. `087-r-metathesis.md`

## Current manifest-backed SC coverage

1. `reader_facing_manifest_coverage_06.md` reports that every manifest row in `report_manifest.tsv` is covered by the current reader-facing chapter set.
2. The reader-facing SC-numbered set now includes:
   - `SC003`, `SC004`, `SC006`, `SC007`, `SC008`, `SC010`, `SC011`, `SC013`
   - `SC014`, `SC015`, `SC016`, `SC017`, `SC018`, `SC019`, `SC020`, `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC027`, `SC028`, `SC029`, `SC030`, `SC031`, `SC032`, `SC033`, `SC034`, `SC035`, `SC036`, `SC037`, `SC039`, `SC040`, `SC041`, `SC042`, `SC043`, `SC044`, `SC045`, `SC046`, `SC047`, `SC048`, `SC049`, `SC050`, `SC051`, `SC052`, `SC053`, `SC054`, `SC055`, `SC056`, `SC057`, `SC058`, `SC059`, `SC060`, `SC061`, `SC063`, `SC064`, `SC065`, `SC066`, `SC067`, `SC068`, `SC069`, `SC070`, `SC071`, `SC072`, `SC073`, `SC074`, `SC075`, `SC076`, `SC078`, `SC079`, `SC080`, `SC081`, `SC082`, `SC083`, `SC085`, `SC086`, `SC087`
3. No manifest SC numbers are missing from reader-facing rule headings.
4. No reader-facing SC numbers appear outside the manifest-backed set.

## Complete list of expected gaps

1. `SC005`
2. `SC009`
3. `SC012`
4. `SC038`
5. `SC062`
6. `SC077`
7. `SC084`

## Early-gap classifications

### `SC005`

1. Classification: deliberately excluded early rule.
2. Reason: the stage-label / human-review issue remains unresolved.
3. Reader-facing status: correctly absent.
4. Recommendation: do not reopen in a reader-facing pass.

### `SC009`

1. Classification: deliberately excluded early rule.
2. Reason: the evidence remains too lexically unique.
3. Reader-facing status: correctly absent.
4. Recommendation: do not reopen in a reader-facing pass.

### `SC012`

1. Classification: deliberately excluded early rule.
2. Reason: the chronology is negative on both sides and the stage-label issue remains unresolved.
3. Reader-facing status: correctly absent.
4. Recommendation: do not reopen in a reader-facing pass.

## Later-gap classifications

### `SC038`

1. Classification: not manifest-backed and correctly absent.
2. Direct evidence:
   - `sound_change_inventory.tsv` marks `SC038` `OE Strip Secondary Stress` as a `technical_marker`, `appendix`, and “methodological appendix material”.
   - `chronology_card_index.tsv` records `SC037`'s later break across `SC038` as `technical_marker`, not an ordinary historical boundary.
   - `sound_change_half_scaffold.tsv` keeps `SC037` inside `035-037` and describes `SC038` only as a technical marker.
3. Indirect coverage: **yes**.
   - `035-037-prefix-and-compound-adjustments.md` explicitly explains that `SC037`'s `rainbow` boundary crosses `SC038 OEStripSecondaryStress`, but that this is technical rather than ordinary-historical.
4. Genuine missing prose: **no**.
5. Recommended next action: none for reader-facing drafting; keep it excluded.

### `SC062`

1. Classification: not manifest-backed and correctly absent.
2. Direct evidence:
   - `sound_change_inventory.tsv` marks `SC062` `OE Weight Markers` as a `technical_marker`, `appendix`, “Technical”, and “appendix only”.
   - `reader_facing_local_section_03_report.md` states that no reader-facing `SC062` unit was added and that the manifest sequence moves directly from `SC061` to `SC063`.
   - `SC063`'s backend chronology notes say the rule moves safely across `SC062`; it is not itself the historical breakpoint.
3. Indirect coverage: **no meaningful reader-facing prose coverage**.
   - The current reader-facing `063-high-vowel-apocope.md` chapter does not promote `SC062` as a prose unit.
4. Genuine missing prose: **no**.
5. Recommended next action: none for reader-facing drafting; keep it excluded as technical marker material.

### `SC077`

1. Classification: not manifest-backed and correctly absent.
2. Direct evidence:
   - `reader_facing_local_section_05_report.md` states that no `SC077` unit was added and that the sequence continues from `SC076` to `SC078`.
   - `sound_change_inventory.tsv` contains `SC076`, then `SC078` with `current_order` `77`; there is no distinct `SC077` change row.
   - `report_manifest.tsv` and `sound_change_half_scaffold.tsv` likewise contain `SC078` as the next promoted late-tail note and no separate `SC077` row.
3. Indirect coverage: **no**, because there is no separate `SC077` change to cover.
4. Genuine missing prose: **no**.
5. Recommended next action: none for reader-facing drafting; this is a numbering gap, not a missing prose unit.

### `SC084`

1. Classification: not manifest-backed and correctly absent.
2. Direct evidence:
   - `sound_change_inventory.tsv` marks `SC084` `OE Weight Cleanup` as a `technical_marker`, `appendix`, “Technical”, and “methodological appendix only”.
   - `reader_facing_local_section_06_report.md` states that no `SC084` unit was added and that the sequence moves directly from `SC083` to `SC085`.
   - `085-086-h-loss-and-contraction.md` begins at `SC085`; `SC084` is not treated as a prose-bearing sound change.
3. Indirect coverage: **no meaningful reader-facing prose coverage**.
4. Genuine missing prose: **no**.
5. Recommended next action: none for reader-facing drafting; keep it excluded as technical marker material.

## Which later gaps should be handled next

1. None of `SC038`, `SC062`, `SC077`, or `SC084` is a genuine next reader-facing prose task.
2. `SC038`, `SC062`, and `SC084` are technical-marker / appendix-only stages.
3. `SC077` is a numbering gap rather than a missing change unit.

## Recommended next pass

1. **Whole-volume coverage/readability review**, not a new gap-filling prose pass.
2. Rationale:
   - the three early exclusions (`SC005`, `SC009`, `SC012`) remain deliberately out for documented backend reasons;
   - the four later “gaps” are not real missing reader-facing chapters;
   - `SC038` is already covered indirectly in context, while `SC062`, `SC077`, and `SC084` are correctly absent for technical or numbering reasons.

## Checks run

1. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py`
   - passed
2. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py`
   - passed
   - files checked: 51
   - citation issues: 0
3. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_18_docker.sh`
   - passed
4. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_18_docker.sh`
   - passed
   - files checked: 51
   - links checked: 460
   - issues: 0
5. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py`
   - passed
   - sections checked: 82
   - warnings: 0
6. PDF rebuild:
   - not run
   - no check indicated that the section-18 outputs were stale or inconsistent

## Scope confirmations

1. No reader-facing chapters were created in this pass.
2. No local section 19 was created in this pass.
3. No FST rules were changed.
4. No lexical TSV data were changed.

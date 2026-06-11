# Reader-facing local section 04 report

## Local-section-03 introduction cleanup

The generated introduction in `build_reader_facing_local_section_03_docker.sh`
was rewritten so that the assembled PDF now opens with book prose instead of
process language. The removed sentence about “no new earlier material” and a
“late-tail rollout” is gone from the generated Markdown and PDF.

The new local-section-03 introduction now reads in substance:

1. the section follows an ordered stretch of Old English sound changes from
   labial allophony through later syncope and degemination;
2. the chapters vary in scale;
3. narrower chapters matter because they fix lexical breakpoints in the
   finite-state cascade.

## Generated-prose checker

This pass adds:

1. `Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py`

The checker parses the introduction prose embedded in the active build script's
Python `parts` list and fails if that prose contains project/process language
such as:

1. `extension`
2. `rollout`
3. `inserted`
4. `batch`
5. `current section`
6. `local-section`
7. `reader-facing`
8. `workflow`
9. `project`
10. `build target`
11. `generated`
12. `pilot`
13. `scaffold`
14. `manifest`

The checker now runs in the pre-build gate list for both:

1. `build_reader_facing_local_section_03_docker.sh`
2. `build_reader_facing_local_section_04_docker.sh`

## New chapters added

1. `069-early-o-shortening-context-note.md`
2. `070-071-early-unstressed-fronting-shortening-bridge.md`
3. `072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md`

## Source reports and dossiers consulted

### Source reports

1. `Germanic/docs/sound_changes/change_reports/full/069-early-o-shortening-context-note.md`
2. `Germanic/docs/sound_changes/change_reports/full/070-071-early-unstressed-fronting-shortening-bridge.md`
3. `Germanic/docs/sound_changes/change_reports/full/072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md`

### Shared dossiers

1. `Germanic/docs/sound_changes/literature_dossiers/069-078-late-unstressed-tail-cluster.dossier.md`
2. `Germanic/docs/sound_changes/book_dossiers/069-078-late-unstressed-tail-cluster.book-dossier.md`

### Chronology cards

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC069-oe-early-o-shortening.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC070-oe-unstressed-fronting-early.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC071-oe-late-o-shortening.md`
4. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC072-oe-unstressed-long-vowel-shortening.md`
5. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC073-oe-unstressed-ae-merger.md`

## Exact chapter order

1. `049-050-b-allophony-and-sievers-law-syncope.md`
2. `051-sk-palatalization.md`
3. `052-velar-palatalization.md`
4. `053-054-pre-umlaut-bridge-and-w-loss.md`
5. `055-056-i-umlaut-core.md`
6. `057-j-cluster-coalescence.md`
7. `058-nasal-dissimilation.md`
8. `059-oe-back-mutation.md`
9. `060-ws-palatal-umlaut-note.md`
10. `061-weak-tail-nasal-loss-note.md`
11. `063-high-vowel-apocope.md`
12. `064-065-post-apocope-tail.md`
13. `066-068-syncope-and-degemination-corridor.md`
14. `069-early-o-shortening-context-note.md`
15. `070-071-early-unstressed-fronting-shortening-bridge.md`
16. `072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md`

## Chronology evidence for SC069-SC073

1. `SC069` is intentionally modest. Its positive evidence is a broad/far earlier
   relation to `SC023 NWGmcNStemNLoss`, and its later side remains open within
   the tested range.
2. `SC070` is the stronger hinge of the new bridge. It must follow
   [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and come before
   [SC071 OELateOShortening](#rule-OELateOShortening).
3. `SC071` is the follower on the right side of that seam. Its earlier boundary
   is reciprocal with `SC070`, while its later side remains boundary-limited.
4. `SC072` is the strongest new center. It must follow
   [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) and precede
   [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).
5. `SC073` directly reciprocates `SC072` on the left and points forward to
   `SC085 OEHLoss` on the right.

## Exact wrong-output diagnostics added

1. `SC069`: \emph{*nḗdrōn} -> *nǣdran* instead of expected OE *nǣdre* ‘adder’;
   \emph{*érθōn} -> *eorþan* instead of expected *eorþe* ‘earth’;
   \emph{*fláskōn} -> *flascan* instead of expected *flasce* ‘flask’.
2. `SC070` earlier: \emph{*lúnganjō} -> *lunġen* instead of expected OE
   *lungen* ‘lungs’.
3. `SC070` later: \emph{*búrōθi} -> *boreþ* instead of expected OE *boraþ*
   ‘bears’; \emph{*mḗnōθz} -> *mōneþ* instead of expected *mōnaþ* ‘month’.
4. `SC071` earlier: \emph{*búrōθi} -> *boreþ* instead of expected OE *boraþ*;
   \emph{*líznōθi} -> *liorneþ* instead of expected *liornaþ*.
5. `SC072` earlier: \emph{*fúrxtīnaz} -> *fyrhten* instead of expected OE
   *fyrhte* ‘fright’.
6. `SC072` later: \emph{*nḗdrōn} -> *nǣdræ* instead of expected OE *nǣdre*;
   \emph{*fádēr} -> *fædær* instead of expected *fæder*.
7. `SC073` earlier: \emph{*nḗdrōn} -> *nǣdræ* instead of expected OE *nǣdre*;
   \emph{*fádēr} -> *fædær* instead of expected *fæder*.
8. `SC073` later: \emph{*táixōn} -> *tāæ* instead of expected OE *tā* ‘toe’.

## One-sided or boundary-limited cases

1. `SC069` remains one-sided: the earlier relation is broad and far, while the
   later side shows no real break within the tested range.
2. `SC070` is two-sided, but its earlier side is narrow and concentrated in
   `lungen`.
3. `SC071` remains one-sided: its earlier relation to `SC070` is clear, but no
   later real break is identified within the tested range.
4. `SC073` is two-sided, but its later side is much narrower than its broad
   reciprocal earlier relation to `SC072`.

## Checker results

### Cross-reference checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_04_docker.sh
```

Result:

1. chapter files checked: 16
2. sound-change links checked: 115
3. issues: 0

### Chronology-evidence checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

Result:

1. sections checked: 28
2. warnings: 0

### Citation checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py
```

Result:

1. files checked: 16
2. citation issues: 0

### FOMA-width checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
```

Result:

1. `foma` blocks checked: 28
2. blocks over the conservative old-rendering threshold: 6
3. flagged source blocks:
   - `SC056` `OEWsPalatalDiphthongization`
   - `SC058` `OENasalDissimilation`
   - `SC063` `OEHighVowelApocope`
   - `SC065` `OEMedialSyncope`
   - `SC069` `OEEarlyOShortening`
   - `SC071` `OELateOShortening`

### Style checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Result:

1. no warnings

### Generated-prose checker

Commands:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_03_docker.sh
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_04_docker.sh
```

Result:

1. local-section-03 introduction paragraphs checked: 2; issues: 0
2. local-section-04 introduction paragraphs checked: 2; issues: 0

### Section-order checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_04_docker.sh
```

Result:

1. passes
2. confirms the ordered unique SC sequence
   `SC049, SC050, SC051, SC052, SC053, SC054, SC055, SC056, SC057, SC058, SC059, SC060, SC061, SC063, SC064, SC065, SC066, SC067, SC068, SC069, SC070, SC071, SC072, SC073`

## PDF build result

Commands:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_03_docker.sh
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_04_docker.sh
```

Result:

1. `reader_facing_local_section_03.md` and `.pdf` regenerated successfully with
   the cleaned introduction.
2. `reader_facing_local_section_04.md` and `.pdf` generated successfully.
3. SC069 through SC073 appear in the correct order in local section 04.
4. no `SC### < SC###` notation remains in the assembled reader-facing prose.
5. current-section cross-references show both SC number and FST rule name and
   remain linked in local section 04.
6. outside-section references show both SC number and FST rule name and remain
   plain text in the assembled output.
7. FOMA code still builds under the width-safe `ReaderFacingFoma` route.
8. citations remain page-bearing.
9. the `# References` heading remains present.
10. generated introductions no longer contain project/process language.

## Remaining PDF issues for human review

No automated blocker remains. The routine visual follow-up is still the same set
of width-wrapped code boxes flagged by the FOMA-width checker:

1. `SC056`
2. `SC058`
3. `SC063`
4. `SC065`
5. `SC069`
6. `SC071`

The local-section-04 cross-reference behavior is otherwise clean in the
assembled Markdown: SC072 remains plain text in local section 03 and becomes a
working link in local section 04 because the build script now resolves rule
links against the active chapter set.

## Scope confirmation

1. No new chapter beyond SC073 was added.
2. No FST rules were substantively changed.
3. No TSV files were substantively changed.
4. No chronology cards were substantively changed.
5. No standardized source reports were substantively changed.
6. No source dossiers were substantively changed.
7. No book dossiers were substantively changed.

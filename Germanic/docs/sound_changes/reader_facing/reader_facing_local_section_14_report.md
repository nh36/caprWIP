# Reader-facing local section 14 report

## New chapter added

1. `014-015-opening-vowel-prelude.md`

## Source report, dossier, book dossier, and chronology cards consulted

### Source report

1. `Germanic/docs/sound_changes/change_reports/full/014-015-opening-vowel-prelude.md`

### Dossier

1. `Germanic/docs/sound_changes/literature_dossiers/014-015-opening-vowel-prelude.dossier.md`

### Book dossier

1. `Germanic/docs/sound_changes/book_dossiers/014-015-opening-vowel-prelude.book-dossier.md`

### Chronology cards

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC014-nwgmc-unstressed-ai-monophthongization.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC015-nwgmc-i-lowering.md`

## Exact chapter order

1. `014-015-opening-vowel-prelude.md`
2. `016-017-west-saxon-palatal-glide-and-u-lowering.md`
3. `018-stressed-monosyllable-o-raising.md`
4. `019-020-final-long-o-raising-and-final-z-deletion.md`
5. `021-unstressed-o-raising.md`
6. `022-mn-dissimilation.md`
7. `023-n-stem-n-loss.md`
8. `024-long-e-lowering.md`
9. `025-long-e-nasal-rounding.md`
10. `026-027-nasal-spirant-changes.md`
11. `028-preconsonantal-x-loss.md`
12. `029-030-awj-glide-and-au-fronting.md`
13. `031-034-west-saxon-diphthong-chain.md`
14. `035-037-prefix-and-compound-adjustments.md`
15. `039-040-medial-unstressed-vowel-changes.md`
16. `041-final-bare-a-loss.md`
17. `042-surviving-bimoric-o-unrounding.md`
18. `043-anglo-frisian-brightening.md`
19. `044-045-breaking-and-velar-fricative-palatalization.md`
20. `046-048-restoration-and-nasal-tail-changes.md`
21. `049-050-b-allophony-and-sievers-law-syncope.md`
22. `051-sk-palatalization.md`
23. `052-velar-palatalization.md`
24. `053-054-pre-umlaut-bridge-and-w-loss.md`
25. `055-056-i-umlaut-core.md`
26. `057-j-cluster-coalescence.md`
27. `058-nasal-dissimilation.md`
28. `059-oe-back-mutation.md`
29. `060-ws-palatal-umlaut-note.md`
30. `061-weak-tail-nasal-loss-note.md`
31. `063-high-vowel-apocope.md`
32. `064-065-post-apocope-tail.md`
33. `066-068-syncope-and-degemination-corridor.md`
34. `069-early-o-shortening-context-note.md`
35. `070-071-early-unstressed-fronting-shortening-bridge.md`
36. `072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md`
37. `074-075-medial-unstressed-i-lowering.md`
38. `076-prefix-i-reduction.md`
39. `078-weak-tail-reduction.md`
40. `079-080-final-j-loss-and-final-geminate-simplification.md`
41. `081-083-j-strengthening-vocalization-and-ei-contraction.md`
42. `085-086-h-loss-and-contraction.md`
43. `087-r-metathesis.md`

## Chronology evidence for SC014 and SC015

1. `SC014` has no positive historical first-break boundary in either tested direction. The earlier search reaches bundled earlier material with no real break, and the later search reaches the present search limit with no real break.
2. `SC015` uses *weorold* ‘world’ and places [SC015 NWGmcILowering](#rule-NWGmcILowering) before [SC036 OEInterStressRaising](#rule-OEInterStressRaising). No earlier positive boundary is currently available.

## Wrong-output diagnostics included, where available

1. `SC014`: no exact wrong output is available, because neither direction yields a historical first-break witness.
2. `SC015`: PGmc \emph{*wír-àldu} -> *wuruld* instead of expected OE *weorold* ‘world’ if moved too late.

## Chronology-negative, one-sided, broad/far, or boundary-limited cases

1. `SC014` is chronology-negative in current testing: both sides are bounded by the search space rather than by a detected historical break.
2. `SC015` is one-sided: the later boundary against [SC036 OEInterStressRaising](#rule-OEInterStressRaising) is real, but the earlier search reaches bundled earlier material without a real break.

## Grouped-chapter justification for SC014-SC015

1. The chapter stays grouped only as a short asymmetric opening pair.
2. Its internal discussion is split into a brief shared orientation and then separate historical discussions and separate SC-numbered rule sections for `SC014` and `SC015`.
3. `SC014` remains brief because it is source-backed but chronology-negative.
4. `SC015` carries the stronger `world`-based chronology and therefore carries most of the historical weight.

## Checker results

### Style checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Result:

1. no warnings

### Citation checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py
```

Result:

1. files checked: 43
2. citation issues: 0

### FOMA-width checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
```

Result:

1. `foma` blocks checked: 74
2. blocks over the conservative old-rendering threshold: 10
3. the new `SC014-SC015` chapter adds two new `foma` blocks and none exceed the threshold
4. the flagged source blocks remain the pre-existing wrapped cases in `SC042`, `SC056`, `SC058`, `SC063`, `SC065`, `SC069`, `SC071`, `SC076`, `SC079`, and `SC083`

### Section-order checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_14_docker.sh
```

Result:

1. passes
2. confirms the ordered unique SC sequence
   `SC014, SC015, SC016, SC017, SC018, SC019, SC020, SC021, SC022, SC023, SC024, SC025, SC026, SC027, SC028, SC029, SC030, SC031, SC032, SC033, SC034, SC035, SC036, SC037, SC039, SC040, SC041, SC042, SC043, SC044, SC045, SC046, SC047, SC048, SC049, SC050, SC051, SC052, SC053, SC054, SC055, SC056, SC057, SC058, SC059, SC060, SC061, SC063, SC064, SC065, SC066, SC067, SC068, SC069, SC070, SC071, SC072, SC073, SC074, SC075, SC076, SC078, SC079, SC080, SC081, SC082, SC083, SC085, SC086, SC087`

### Cross-reference checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_14_docker.sh
```

Result:

1. files checked: 43
2. links checked: 408
3. issues: 0

### Chronology-evidence checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

Result:

1. sections checked: 74
2. warnings: 0

### Generated-prose checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_14_docker.sh
```

Result:

1. introduction paragraphs checked: 2
2. issues: 0

### Grouped-chapter checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Result:

1. passes inside the style checker with no grouped-chapter warnings

## Manifest-coverage audit result

Source:

```bash
Germanic/docs/sound_changes/reader_facing/reader_facing_manifest_coverage_01.md
```

Result:

1. all manifest rows in `Germanic/docs/sound_changes/change_reports/report_manifest.tsv` are covered by the local-section-14 reader-facing chapter set
2. no manifest SC numbers are missing from reader-facing rule headings
3. no reader-facing SC numbers fall outside the manifest
4. expected gaps inside the manifest-backed span are `SC038`, `SC062`, `SC077`, and `SC084`
5. `SC001-SC013` are outside the current manifest-backed reader-facing programme because the manifest begins at `SC014-SC015`

## PDF build result

Command:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_14_docker.sh
```

Result:

1. generated `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_14.md`
2. generated `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_14.pdf`
3. generated `Germanic/docs/sound_changes/reader_facing/reader_facing_manifest_coverage_01.md`
4. the Docker/Pandoc build exited successfully; Pandoc emitted the usual `Ticker: poll failed: Interrupted system call` warnings without preventing output

## Remaining PDF issues for human review

1. Usual visual review of page turns and wrapped `foma` blocks is still worthwhile, especially in the already-known long-line chapters `SC042`, `SC056`, `SC058`, `SC063`, `SC065`, `SC069`, `SC071`, `SC076`, `SC079`, and `SC083`.
2. The new `SC014-SC015` chapter openings and chronology paragraphs should still be read once in the PDF for ordinary layout smoothness, even though no automated gate failure remains.

## Unchanged upstream materials

1. No FST rules were substantively changed.
2. No TSV files were substantively changed.
3. No chronology cards were substantively changed.
4. No standardized source reports were substantively changed.
5. No source dossiers were substantively changed.
6. No book dossiers were substantively changed.

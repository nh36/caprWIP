# Reader-facing local section 15 report

## SC003 chapter created

1. `003-west-germanic-rhotacism.md`

## Backend sources consulted

1. `Germanic/docs/sound_changes/change_reports/full/003-pgmc-rhotacism.md`
2. `Germanic/docs/sound_changes/literature_dossiers/003-pgmc-rhotacism.dossier.md`
3. `Germanic/docs/sound_changes/book_dossiers/003-pgmc-rhotacism.book-dossier.md`
4. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC003-pgmc-rhotacism.md`

## CAPR rule-name and historical-label distinction

1. The chapter title is `West Germanic rhotacism`.
2. The rule heading keeps the implementation label in place as `SC003. West Germanic rhotacism (`PGmcRhotacism`)`.
3. The historical discussion states that `PGmcRhotacism` is the CAPR implementation name, while the historical change is a later West Germanic rhotacism after the Proto-West-Germanic stage.
4. The chapter also keeps [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) separate, rather than collapsing final `*z` deletion into SC003.

## Chronology evidence summary

1. The earlier side is boundary-only: SC003 moves safely across plain-text `SC002 PGmcGmSimplification` to order `2` and no earlier positive boundary appears within the tested range.
2. The later side gives a real one-sided historical boundary at [SC044 OEBreaking](#rule-OEBreaking).
3. That later boundary is broad and distant rather than local.
4. The chapter keeps the exact validated diagnostics:
   - PGmc \emph{*líznōjaną} -> *lirnian* instead of expected OE *liornian* ‘learn’
   - PGmc \emph{*líznōθi} -> *lirnaþ* instead of expected *liornaþ*
   - PGmc \emph{*líznô} -> *lirna* instead of expected *liorna*
   - PGmc \emph{*mízdai} -> *merde* instead of expected OE *meorde* ‘meed’
5. The prose states the usable ordering conclusion in words: SC003 must come before [SC044 OEBreaking](#rule-OEBreaking) in the modeled sequence.

## Cross-reference handling for SC044

1. All SC044 references in the new chapter use both the SC number and the FST rule name: [SC044 OEBreaking](#rule-OEBreaking).
2. Because SC044 is in the current local-section-15 build, those references remain live internal links.
3. The cross-reference checker reports `issues: 0`.

## Confirmation that SC002 was not added

1. No SC002 reader-facing chapter was created.
2. No local-section-15 chapter file for SC002 exists.
3. `reader_facing_manifest_coverage_03.md` confirms that `SC002` is absent because `report_manifest.tsv` does not include it.

## Exact chapter order

1. `003-west-germanic-rhotacism.md`
2. `014-015-opening-vowel-prelude.md`
3. `016-017-west-saxon-palatal-glide-and-u-lowering.md`
4. `018-stressed-monosyllable-o-raising.md`
5. `019-020-final-long-o-raising-and-final-z-deletion.md`
6. `021-unstressed-o-raising.md`
7. `022-mn-dissimilation.md`
8. `023-n-stem-n-loss.md`
9. `024-long-e-lowering.md`
10. `025-long-e-nasal-rounding.md`
11. `026-027-nasal-spirant-changes.md`
12. `028-preconsonantal-x-loss.md`
13. `029-030-awj-glide-and-au-fronting.md`
14. `031-034-west-saxon-diphthong-chain.md`
15. `035-037-prefix-and-compound-adjustments.md`
16. `039-040-medial-unstressed-vowel-changes.md`
17. `041-final-bare-a-loss.md`
18. `042-surviving-bimoric-o-unrounding.md`
19. `043-anglo-frisian-brightening.md`
20. `044-045-breaking-and-velar-fricative-palatalization.md`
21. `046-048-restoration-and-nasal-tail-changes.md`
22. `049-050-b-allophony-and-sievers-law-syncope.md`
23. `051-sk-palatalization.md`
24. `052-velar-palatalization.md`
25. `053-054-pre-umlaut-bridge-and-w-loss.md`
26. `055-056-i-umlaut-core.md`
27. `057-j-cluster-coalescence.md`
28. `058-nasal-dissimilation.md`
29. `059-oe-back-mutation.md`
30. `060-ws-palatal-umlaut-note.md`
31. `061-weak-tail-nasal-loss-note.md`
32. `063-high-vowel-apocope.md`
33. `064-065-post-apocope-tail.md`
34. `066-068-syncope-and-degemination-corridor.md`
35. `069-early-o-shortening-context-note.md`
36. `070-071-early-unstressed-fronting-shortening-bridge.md`
37. `072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md`
38. `074-075-medial-unstressed-i-lowering.md`
39. `076-prefix-i-reduction.md`
40. `078-weak-tail-reduction.md`
41. `079-080-final-j-loss-and-final-geminate-simplification.md`
42. `081-083-j-strengthening-vocalization-and-ei-contraction.md`
43. `085-086-h-loss-and-contraction.md`
44. `087-r-metathesis.md`

## Manifest coverage result

1. Source: `Germanic/docs/sound_changes/reader_facing/reader_facing_manifest_coverage_03.md`
2. All manifest rows in `Germanic/docs/sound_changes/change_reports/report_manifest.tsv` are covered by the local-section-15 reader-facing chapter set.
3. `SC003` is now covered by `003-west-germanic-rhotacism.md`.
4. `SC002` remains absent because it is not in `report_manifest.tsv`.
5. `SC014-SC087` coverage remains intact.
6. No manifest SC numbers are missing from reader-facing rule headings.
7. No reader-facing SC numbers fall outside the manifest.
8. Expected gaps after `SC014` remain `SC038`, `SC062`, `SC077`, and `SC084`.
9. The manifest-backed sequence now opens with `SC003` and then resumes at `SC014-SC015`.
10. No separate manifest-coverage checker exists; the local-section-15 build regenerated this coverage audit directly.

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

1. files checked: 44
2. citation issues: 0

### FOMA-width checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
```

Result:

1. `foma` blocks checked: 75
2. blocks over the conservative old-rendering threshold: 10
3. the new `SC003` chapter adds one `foma` block and it does not exceed the threshold
4. the flagged blocks remain the same pre-existing wrapped cases in `SC042`, `SC056`, `SC058`, `SC063`, `SC065`, `SC069`, `SC071`, `SC076`, `SC079`, and `SC083`

### Section-order checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_15_docker.sh
```

Result:

1. passes
2. confirms the ordered unique SC sequence beginning with `SC003` and continuing through `SC087`

### Cross-reference checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_15_docker.sh
```

Result:

1. files checked: 44
2. links checked: 415
3. issues: 0

### Chronology-evidence checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

Result:

1. sections checked: 75
2. warnings: 0

### Generated-prose checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_15_docker.sh
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

## PDF build result

Command:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_15_docker.sh
```

Result:

1. generated `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_15.md`
2. generated `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_15.pdf`
3. generated `Germanic/docs/sound_changes/reader_facing/reader_facing_manifest_coverage_03.md`
4. the Docker/Pandoc build exited successfully
5. Pandoc emitted the usual `Ticker: poll failed: Interrupted system call` warnings without preventing output

## Remaining PDF issues for human review

1. The new SC003 opening chapter should be read once in the PDF to confirm that the distinction between West Germanic history and the CAPR rule label remains clear on the page.
2. The live links from SC003 to SC020 and SC044 should be checked visually once in the PDF.
3. The already-known long-line chapters `SC042`, `SC056`, `SC058`, `SC063`, `SC065`, `SC069`, `SC071`, `SC076`, `SC079`, and `SC083` remain worth a quick visual review for wrapped `foma` lines.

## Unchanged upstream materials

1. No FST rules were substantively changed.
2. No TSV lexical data were substantively changed.
3. No production source reports were substantively changed.

# Reader-facing local section 10 report

## New chapters added

1. `028-preconsonantal-x-loss.md`
2. `029-030-awj-glide-and-au-fronting.md`

## No SC026-SC027 unit added

1. Local section 10 adds only the new `SC028` and `SC029-SC030` chapters.
2. No standalone reader-facing `SC026` or `SC027` file or chapter was created in this pass.

## Source reports, dossier, book dossier, and chronology cards consulted

### Source reports

1. `Germanic/docs/sound_changes/change_reports/full/028-preconsonantal-x-loss-note.md`
2. `Germanic/docs/sound_changes/change_reports/full/029-030-awj-glide-and-au-fronting-core.md`

### Dossier

1. `Germanic/docs/sound_changes/literature_dossiers/028-030-glide-and-fronting-entry.dossier.md`

### Book dossier

1. `Germanic/docs/sound_changes/book_dossiers/028-030-glide-and-fronting-entry.book-dossier.md`

### Chronology cards

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC028-nwgmc-preconsonantal-x-loss.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC029-oe-awj-glide-formation.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC030-oe-au-fronting.md`

## Exact chapter order

1. `028-preconsonantal-x-loss.md`
2. `029-030-awj-glide-and-au-fronting.md`
3. `031-034-west-saxon-diphthong-chain.md`
4. `035-037-prefix-and-compound-adjustments.md`
5. `039-040-medial-unstressed-vowel-changes.md`
6. `041-final-bare-a-loss.md`
7. `042-surviving-bimoric-o-unrounding.md`
8. `043-anglo-frisian-brightening.md`
9. `044-045-breaking-and-velar-fricative-palatalization.md`
10. `046-048-restoration-and-nasal-tail-changes.md`
11. `049-050-b-allophony-and-sievers-law-syncope.md`
12. `051-sk-palatalization.md`
13. `052-velar-palatalization.md`
14. `053-054-pre-umlaut-bridge-and-w-loss.md`
15. `055-056-i-umlaut-core.md`
16. `057-j-cluster-coalescence.md`
17. `058-nasal-dissimilation.md`
18. `059-oe-back-mutation.md`
19. `060-ws-palatal-umlaut-note.md`
20. `061-weak-tail-nasal-loss-note.md`
21. `063-high-vowel-apocope.md`
22. `064-065-post-apocope-tail.md`
23. `066-068-syncope-and-degemination-corridor.md`
24. `069-early-o-shortening-context-note.md`
25. `070-071-early-unstressed-fronting-shortening-bridge.md`
26. `072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md`
27. `074-075-medial-unstressed-i-lowering.md`
28. `076-prefix-i-reduction.md`
29. `078-weak-tail-reduction.md`
30. `079-080-final-j-loss-and-final-geminate-simplification.md`
31. `081-083-j-strengthening-vocalization-and-ei-contraction.md`
32. `085-086-h-loss-and-contraction.md`
33. `087-r-metathesis.md`

## Chronology evidence for SC028, SC029, and SC030

1. `SC028` has no positive historical first-break boundary in either tested direction. The earlier search reaches bundled earlier material with no real break, and the later search reaches the present search limit with no real break.
2. `SC029` uses *hīeġ* ‘hay’ and *strīeġan* ‘strew’ and places [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) before [SC030 OEAuFronting](#rule-OEAuFronting). Its earlier side remains boundary-limited.
3. `SC030` uses the same *hay* / *strew* 'strew' pair on the earlier side and a broader no-output later set including *ġelīefan* ‘believe’, *brēad* ‘bread’, and *drēam* ‘dream’. It places [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) before [SC030 OEAuFronting](#rule-OEAuFronting) and [SC030 OEAuFronting](#rule-OEAuFronting) before [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).

## Wrong-output diagnostics included, where available

1. `SC028`: no exact wrong output is available, because neither direction yields a historical first-break witness.
2. `SC029`: \emph{*xáwwją} -> *hauġ* instead of expected OE *hīeġ* ‘hay’ and \emph{*stráwjaną} -> *strauian* instead of *strīeġan* ‘strew’ if moved too late.
3. `SC030`: \emph{*xáwwją} -> *hauġ* instead of *hīeġ* and \emph{*stráwjaną} -> *strauian* instead of *strīeġan* if moved too early; \emph{*galáubijaną}, \emph{*bráudą}, \emph{*dráugmaz}, and sixteen other derivations fail to produce output at all (\emph{+?}) instead of yielding expected Old English forms if moved too late.

## Chronology-negative, one-sided, broad/far, or boundary-limited cases

1. `SC028` is chronology-negative in current testing: both sides are bounded by the search space rather than by a detected historical break.
2. `SC029` is one-sided: the later `hay` / `strew` boundary is real, but the earlier search reaches bundled earlier material without a real break.
3. `SC030` is two-sided, but its later side is broad and no-output-heavy because it hands forward into [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) through failed derivations rather than competing surface reflexes.

## Grouped-chapter justification for SC029-SC030

1. The paired chapter is justified because the same *hay* / *strew* 'strew' material passes through both rules.
2. [SC029 OEAwjGlideFormation](#rule-OEAwjGlideFormation) reshapes the older \emph{awj} sequence, and [SC030 OEAuFronting](#rule-OEAuFronting) then fronts the resulting \emph{au}.
3. The internal discussion is still split: one short orientation section introduces the pair, followed by separate historical discussions and separate SC-numbered rule sections for `SC029` and `SC030`.
4. `SC028` remains separate because its history is legible but its current chronology is negative.

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

1. files checked: 33
2. citation issues: 0

### FOMA-width checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
```

Result:

1. `foma` blocks checked: 60
2. blocks over the conservative old-rendering threshold: 10
3. the new `SC028-SC030` chapters add three new `foma` blocks and none exceed the threshold
4. the flagged source blocks remain the pre-existing wrapped cases in `SC042`, `SC056`, `SC058`, `SC063`, `SC065`, `SC069`, `SC071`, `SC076`, `SC079`, and `SC083`

### Section-order checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_10_docker.sh
```

Result:

1. passes
2. confirms the ordered unique SC sequence
   `SC028, SC029, SC030, SC031, SC032, SC033, SC034, SC035, SC036, SC037, SC039, SC040, SC041, SC042, SC043, SC044, SC045, SC046, SC047, SC048, SC049, SC050, SC051, SC052, SC053, SC054, SC055, SC056, SC057, SC058, SC059, SC060, SC061, SC063, SC064, SC065, SC066, SC067, SC068, SC069, SC070, SC071, SC072, SC073, SC074, SC075, SC076, SC078, SC079, SC080, SC081, SC082, SC083, SC085, SC086, SC087`

### Cross-reference checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_10_docker.sh
```

Result:

1. files checked: 33
2. links checked: 346
3. issues: 0

### Chronology-evidence checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

Result:

1. sections checked: 60
2. warnings: 0

### Generated-prose checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_10_docker.sh
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
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_10_docker.sh
```

Result:

1. generated `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_10.md`
2. generated `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_10.pdf`
3. the Docker/Pandoc build exited successfully; Pandoc emitted the usual `Ticker: poll failed: Interrupted system call` warnings without preventing output

## Remaining PDF issues for human review

1. Usual visual review of page turns and wrapped `foma` blocks is still worthwhile, especially in the already-known long-line chapters `SC042`, `SC056`, `SC058`, `SC063`, `SC065`, `SC069`, `SC071`, `SC076`, `SC079`, and `SC083`.
2. The new `SC028-SC030` chapter openings and chronology paragraphs should still be read once in the PDF for ordinary layout smoothness, even though no automated gate failure remains.

## Unchanged upstream materials

1. No FST rules were substantively changed.
2. No TSV files were substantively changed.
3. No chronology cards were substantively changed.
4. No standardized source reports were substantively changed.
5. No source dossiers were substantively changed.
6. No book dossiers were substantively changed.

# Reader-facing local section 11 report

## New chapter added

1. `026-027-nasal-spirant-changes.md`

## No SC021-SC025 unit added

1. Local section 11 adds only the new `SC026-SC027` chapter.
2. No standalone reader-facing `SC021`, `SC022`, `SC023`, `SC024`, or `SC025` file or chapter was created in this pass.

## Source report, dossier, book dossier, and chronology cards consulted

### Source report

1. `Germanic/docs/sound_changes/change_reports/full/026-027-nasal-spirant-corridor.md`

### Dossier

1. `Germanic/docs/sound_changes/literature_dossiers/026-027-nasal-spirant-corridor.dossier.md`

### Book dossier

1. `Germanic/docs/sound_changes/book_dossiers/026-027-nasal-spirant-corridor.book-dossier.md`

### Chronology cards

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC026-nwgmc-nasal-spirant-lengthening.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC027-nwgmc-nasal-spirant-loss.md`

## Exact chapter order

1. `026-027-nasal-spirant-changes.md`
2. `028-preconsonantal-x-loss.md`
3. `029-030-awj-glide-and-au-fronting.md`
4. `031-034-west-saxon-diphthong-chain.md`
5. `035-037-prefix-and-compound-adjustments.md`
6. `039-040-medial-unstressed-vowel-changes.md`
7. `041-final-bare-a-loss.md`
8. `042-surviving-bimoric-o-unrounding.md`
9. `043-anglo-frisian-brightening.md`
10. `044-045-breaking-and-velar-fricative-palatalization.md`
11. `046-048-restoration-and-nasal-tail-changes.md`
12. `049-050-b-allophony-and-sievers-law-syncope.md`
13. `051-sk-palatalization.md`
14. `052-velar-palatalization.md`
15. `053-054-pre-umlaut-bridge-and-w-loss.md`
16. `055-056-i-umlaut-core.md`
17. `057-j-cluster-coalescence.md`
18. `058-nasal-dissimilation.md`
19. `059-oe-back-mutation.md`
20. `060-ws-palatal-umlaut-note.md`
21. `061-weak-tail-nasal-loss-note.md`
22. `063-high-vowel-apocope.md`
23. `064-065-post-apocope-tail.md`
24. `066-068-syncope-and-degemination-corridor.md`
25. `069-early-o-shortening-context-note.md`
26. `070-071-early-unstressed-fronting-shortening-bridge.md`
27. `072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md`
28. `074-075-medial-unstressed-i-lowering.md`
29. `076-prefix-i-reduction.md`
30. `078-weak-tail-reduction.md`
31. `079-080-final-j-loss-and-final-geminate-simplification.md`
32. `081-083-j-strengthening-vocalization-and-ei-contraction.md`
33. `085-086-h-loss-and-contraction.md`
34. `087-r-metathesis.md`

## Chronology evidence for SC026 and SC027

1. `SC026` uses *fȳst* ‘fist’, *gōs* ‘goose’, and *ġeoguþ* ‘youth’ and places [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) before [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss). No earlier positive boundary is currently available.
2. `SC027` uses the same *fȳst* / *gōs* / *ġeoguþ* witness set and places [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) before [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss). No later positive boundary is currently available.

## Wrong-output diagnostics included, where available

1. `SC026`: \emph{*fúnxstiz} -> *fyst* instead of expected OE *fȳst* ‘fist’, \emph{*gánsz} -> *ġeas* instead of *gōs* ‘goose’, and \emph{*júgunθ} -> *ġeogoþ* instead of *ġeoguþ* ‘youth’ if moved too late.
2. `SC027`: the same three wrong outputs appear if the rule is moved too early.

## Chronology-negative, one-sided, broad/far, or boundary-limited cases

1. `SC026` is one-sided: the later boundary against [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) is real, but the earlier search reaches bundled earlier material without a real break.
2. `SC027` is one-sided in the opposite direction: the earlier boundary against [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) is real, but the later search reaches the present search limit with no real break.

## Grouped-chapter justification for SC026-SC027

1. A paired chapter is justified because the handbook tradition describes one bundled historical development in which nasal loss before voiceless spirants is accompanied by compensatory lengthening.
2. The internal relation is also derivationally explicit: [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) adjusts the vowel while the conditioning sequence is still present, and [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) then removes the nasal.
3. The chapter therefore keeps one shared historical discussion and two separate SC-numbered rule sections, because the interaction is real rather than merely adjacent.

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

1. files checked: 34
2. citation issues: 0

### FOMA-width checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
```

Result:

1. `foma` blocks checked: 62
2. blocks over the conservative old-rendering threshold: 10
3. the new `SC026-SC027` chapter adds two new `foma` blocks and none exceed the threshold
4. the flagged source blocks remain the pre-existing wrapped cases in `SC042`, `SC056`, `SC058`, `SC063`, `SC065`, `SC069`, `SC071`, `SC076`, `SC079`, and `SC083`

### Section-order checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_11_docker.sh
```

Result:

1. passes
2. confirms the ordered unique SC sequence
   `SC026, SC027, SC028, SC029, SC030, SC031, SC032, SC033, SC034, SC035, SC036, SC037, SC039, SC040, SC041, SC042, SC043, SC044, SC045, SC046, SC047, SC048, SC049, SC050, SC051, SC052, SC053, SC054, SC055, SC056, SC057, SC058, SC059, SC060, SC061, SC063, SC064, SC065, SC066, SC067, SC068, SC069, SC070, SC071, SC072, SC073, SC074, SC075, SC076, SC078, SC079, SC080, SC081, SC082, SC083, SC085, SC086, SC087`

### Cross-reference checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_11_docker.sh
```

Result:

1. files checked: 34
2. links checked: 354
3. issues: 0

### Chronology-evidence checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

Result:

1. sections checked: 62
2. warnings: 0

### Generated-prose checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_11_docker.sh
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
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_11_docker.sh
```

Result:

1. generated `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_11.md`
2. generated `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_11.pdf`
3. the Docker/Pandoc build exited successfully; Pandoc emitted the usual `Ticker: poll failed: Interrupted system call` warnings without preventing output

## Remaining PDF issues for human review

1. Usual visual review of page turns and wrapped `foma` blocks is still worthwhile, especially in the already-known long-line chapters `SC042`, `SC056`, `SC058`, `SC063`, `SC065`, `SC069`, `SC071`, `SC076`, `SC079`, and `SC083`.
2. The new `SC026-SC027` discussion and chronology paragraphs should still be read once in the PDF for ordinary layout smoothness, even though no automated gate failure remains.

## Unchanged upstream materials

1. No FST rules were substantively changed.
2. No TSV files were substantively changed.
3. No chronology cards were substantively changed.
4. No standardized source reports were substantively changed.
5. No source dossiers were substantively changed.
6. No book dossiers were substantively changed.

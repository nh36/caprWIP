# Reader-facing local section 05 report

## New chapters added

1. `074-075-medial-unstressed-i-lowering.md`
2. `076-prefix-i-reduction.md`
3. `078-weak-tail-reduction.md`

No reader-facing `SC077` unit was added. The ordinary manifest sequence for the
current stretch continues from `SC076` to `SC078`, and the local-section-05
build preserves that gap instead of inventing an extra chapter.

## Source reports and dossiers consulted

### Source reports

1. `Germanic/docs/sound_changes/change_reports/full/074-075-medial-unstressed-i-lowering-bridge.md`
2. `Germanic/docs/sound_changes/change_reports/full/076-prefix-i-reduction-note.md`
3. `Germanic/docs/sound_changes/change_reports/full/078-weak-tail-reduction-right-edge-note.md`

### Shared dossiers

1. `Germanic/docs/sound_changes/literature_dossiers/069-078-late-unstressed-tail-cluster.dossier.md`
2. `Germanic/docs/sound_changes/book_dossiers/069-078-late-unstressed-tail-cluster.book-dossier.md`

### Chronology cards

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC074-oe-med-unstressed-i-lowering1.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC075-oe-med-unstressed-i-lowering.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC076-oe-prefix-i-reduction.md`
4. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC078-oe-weak-tail-reduction.md`

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
17. `074-075-medial-unstressed-i-lowering.md`
18. `076-prefix-i-reduction.md`
19. `078-weak-tail-reduction.md`

## Chronology evidence for SC074, SC075, SC076, and SC078

1. `SC074` now states a two-sided relation: it must follow
   [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
   and must come before [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering).
2. `SC075` is explicitly one-sided: it must follow
   [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1), but no
   later real break is identified within the tested range.
3. `SC076` remains fully boundary-limited. The chapter says plainly that no
   positive earlier or later first-break boundary is currently available.
4. `SC078` is two-sided and more substantial: it must follow
   [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) and must
   come before SC086 OEContraction, with the later SC086 relation kept as a
   cross-reference rather than an annexation of the next cluster.

## Wrong-output diagnostics included

1. `SC074` earlier: \emph{*fúrxtīnaz} -> *fyrhti* instead of expected OE
   *fyrhte* ‘fright’.
2. `SC074` later: \emph{*skíllingaz} -> *sċilleng* instead of expected OE
   *sċilling* ‘shilling’.
3. `SC075` earlier: \emph{*skíllingaz} -> *sċilleng* instead of expected OE
   *sċilling*.
4. `SC078` earlier: \emph{*bákaną} -> *bacen* instead of expected OE *bacan*
   ‘bake’; \emph{*bíndaną} -> *binden* instead of expected *bindan* ‘bind’.
5. `SC078` later: \emph{*fléuxaną} -> *flēoan* instead of expected OE *flēon*
   ‘flee’; \emph{*sláxaną} -> *sleaan* instead of expected *slēan* ‘slay’.

No exact wrong-output diagnostic is available for `SC076`, and the chapter says
so directly.

## One-sided or boundary-limited cases

1. `SC075` remains one-sided: earlier boundary real, later side runner-bounded.
2. `SC076` remains boundary-limited on both sides.
3. `SC078` is two-sided, but its earlier boundary is broad and computationally
   heavy, while the later SC086 relation is much narrower and more directly
   interpretable.

## Grouped-chapter justification for `074-075`

`074-075-medial-unstressed-i-lowering.md` remains a grouped chapter with one
explicit shared historical discussion because the prose explains a close
derivational interaction between the two rules:

1. `SC074` spreads the broader unstressed-\emph{i} lowering.
2. `SC075` immediately narrows that outcome by restoring \emph{i} before
   \emph{*ng}.

This is not mere adjacency in the cascade. The second rule directly repairs the
overbroad result of the first in the `sċilling` witness family, so the grouped
chapter is justified under the current style rule.

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

1. files checked: 19
2. citation issues: 0

### FOMA-width checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
```

Result:

1. `foma` blocks checked: 32
2. blocks over the conservative old-rendering threshold: 7
3. flagged source blocks:
   - `SC056` `OEWsPalatalDiphthongization`
   - `SC058` `OENasalDissimilation`
   - `SC063` `OEHighVowelApocope`
   - `SC065` `OEMedialSyncope`
   - `SC069` `OEEarlyOShortening`
   - `SC071` `OELateOShortening`
   - `SC076` `OEPrefixIReduction`

### Section-order checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_05_docker.sh
```

Result:

1. passes
2. confirms the ordered unique SC sequence
   `SC049, SC050, SC051, SC052, SC053, SC054, SC055, SC056, SC057, SC058, SC059, SC060, SC061, SC063, SC064, SC065, SC066, SC067, SC068, SC069, SC070, SC071, SC072, SC073, SC074, SC075, SC076, SC078`

### Cross-reference checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_05_docker.sh
```

Result:

1. files checked: 19
2. links checked: 135
3. issues: 0

### Chronology-evidence checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

Result:

1. sections checked: 32
2. warnings: 0

### Generated-prose checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_05_docker.sh
```

Result:

1. introduction paragraphs checked: 2
2. issues: 0

## PDF build result

Build command:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_05_docker.sh
```

Result:

1. `reader_facing_local_section_05.md` generated successfully.
2. `reader_facing_local_section_05.pdf` generated successfully.
3. SC074, SC075, SC076, and SC078 appear in the expected order.
4. no `SC### < SC###` notation remains in the assembled prose.
5. current-section sound-change references show both SC number and FST rule
   name and remain linked.
6. outside-section references show both SC number and FST rule name and remain
   plain text, for example `SC086 OEContraction` and `SC087 OERMetathesis`.
7. FOMA code continues to build through the width-safe `ReaderFacingFoma`
   route.
8. citations remain page-bearing.
9. the `# References` heading remains present.
10. the generated introduction remains book prose and does not describe the
    expansion process.

## Remaining PDF issues for human review

No automated blocker remains. The routine visual follow-up is the same set of
width-wrapped code boxes flagged by the FOMA-width checker, especially the new
`SC076 OEPrefixIReduction` block alongside the previously known longer rules.

## Scope confirmation

1. No `SC077` chapter was added.
2. No FST rules were substantively changed.
3. No TSV files were substantively changed.
4. No chronology cards were substantively changed.
5. No standardized source reports were substantively changed.
6. No source dossiers were substantively changed.
7. No book dossiers were substantively changed.

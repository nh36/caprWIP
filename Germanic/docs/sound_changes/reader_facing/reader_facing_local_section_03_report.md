# Reader-facing local section 03 report

## New chapters added

1. `063-high-vowel-apocope.md`
2. `064-065-post-apocope-tail.md`
3. `066-068-syncope-and-degemination-corridor.md`

No reader-facing `SC062` unit was added. The ordinary manifest sequence for this stretch moves from `SC061` to `SC063`, so the new local batch preserves that gap instead of inventing an extra chapter.

## Source reports and dossiers consulted

### Source reports

1. `Germanic/docs/sound_changes/change_reports/full/063-oe-high-vowel-apocope.md`
2. `Germanic/docs/sound_changes/change_reports/full/064-065-post-apocope-tail.md`
3. `Germanic/docs/sound_changes/change_reports/full/066-068-syncope-and-degemination-corridor.md`

### Literature dossiers

1. `Germanic/docs/sound_changes/literature_dossiers/063-oe-high-vowel-apocope.dossier.md`
2. `Germanic/docs/sound_changes/literature_dossiers/064-065-post-apocope-tail.dossier.md`
3. `Germanic/docs/sound_changes/literature_dossiers/066-068-syncope-and-degemination-corridor.dossier.md`

### Book dossiers

1. `Germanic/docs/sound_changes/book_dossiers/063-oe-high-vowel-apocope.book-dossier.md`
2. `Germanic/docs/sound_changes/book_dossiers/064-065-post-apocope-tail.book-dossier.md`
3. `Germanic/docs/sound_changes/book_dossiers/066-068-syncope-and-degemination-corridor.book-dossier.md`

### Chronology cards

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC063-oe-high-vowel-apocope.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC064-nwgmc-in-stem-n-loss.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC065-oe-medial-syncope.md`
4. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC066-oe-l-adjacent-syncope.md`
5. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC067-oe-dental-assimilation.md`
6. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC068-oe-preconsonantal-degemination.md`

## Exact chapter order used

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

## Chronology evidence added for SC063-SC068

1. `SC063` now states a two-sided weak-tail chronology: earlier than `SC072` because delayed apocope yields *fyrht* instead of expected OE *fyrhte* ‘fright’, and later than `SC055` because early apocope yields *cū* and *brūd* instead of expected *cȳ* ‘cow’ and *brȳd* ‘bride’.
2. `SC064` now states a two-sided but narrow chronology: PGmc \emph{*fúrxtīnaz} yields *fyrhten* instead of expected OE *fyrhte* ‘fright’ if the rule is moved before `SC041` or delayed until after `SC072`.
3. `SC065` is stated honestly as boundary-limited. The chapter explains the historical setting of late medial syncope but says plainly that the current first-break tests do not provide a positive earlier boundary, a positive later boundary, or an exact wrong output for this specific rule.
4. `SC066` now gives the clearest local chain in the new batch: \emph{*nátilōn} yields *nætle* instead of expected OE *netle* ‘nettle’, and \emph{*spénnilō} yields *spenl* instead of *spinl* ‘spindle’ if the rule is moved before `SC055`; the same \emph{*spénnilō} yields *spinnl* if the rule is delayed until after `SC068`.
5. `SC067` is also stated as boundary-limited. The prose makes clear that the dental cleanup is historically plausible inside the sequence but presently lacks a positive first-break diagnostic of its own.
6. `SC068` now has an explicit earlier boundary: if the rule is moved before `SC066`, \emph{*spénnilō} yields *spinnl* instead of expected OE *spinl* ‘spindle’. The later side remains one-sided, and the chapter says so directly.

## Exact wrong-output diagnostics included

1. `SC063` earlier: \emph{*kūi} -> *cū* instead of expected OE *cȳ* ‘cow’; \emph{*brūdiz} -> *brūd* instead of expected OE *brȳd* ‘bride’.
2. `SC063` later: \emph{*fúrxtīnaz} -> *fyrht* instead of expected OE *fyrhte* ‘fright’.
3. `SC064` earlier and later: \emph{*fúrxtīnaz} -> *fyrhten* instead of expected OE *fyrhte* ‘fright’.
4. `SC066` earlier: \emph{*nátilōn} -> *nætle* instead of expected OE *netle* ‘nettle’; \emph{*spénnilō} -> *spenl* instead of expected OE *spinl* ‘spindle’.
5. `SC066` later: \emph{*spénnilō} -> *spinnl* instead of expected OE *spinl* ‘spindle’.
6. `SC068` earlier: \emph{*spénnilō} -> *spinnl* instead of expected OE *spinl* ‘spindle’.

## One-sided or boundary-limited diagnostics

1. `SC065` remains boundary-limited on both sides. No exact wrong early or late output is currently available.
2. `SC067` remains boundary-limited on both sides. No exact wrong early or late output is currently available.
3. `SC068` has an exact earlier boundary but no later real break before the current search boundary.
4. `SC064` is two-sided, but both sides are still concentrated in the same `fright` witness family and are described that way in the prose.

## Checker results

### Citation checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py
```

Result:

- files checked: 13
- citation issues: 0

### FOMA-width checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
```

Result:

- `foma` blocks checked: 23
- blocks over the conservative old-rendering threshold: 4
- over-threshold source blocks: `SC056`, `SC058`, `SC063`, `SC065`
- build-side `ReaderFacingFoma` wrapping remains active for all of them

### Style checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Result:

- no warnings

### Section-order checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_03_docker.sh
```

Result:

- passes
- confirms the ordered unique SC sequence `SC049, SC050, SC051, SC052, SC053, SC054, SC055, SC056, SC057, SC058, SC059, SC060, SC061, SC063, SC064, SC065, SC066, SC067, SC068`

### Chronology-evidence checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

Result:

- sections checked: 23
- warnings: 0

## PDF build result

Build command:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_03_docker.sh
```

Result:

1. `reader_facing_local_section_03.md` generated successfully.
2. `reader_facing_local_section_03.pdf` generated successfully.
3. The assembled Markdown preserves the intended chapter order and includes the new chapter titles for `063`, `064-065`, and `066-068`.
4. The assembled Markdown still ends with an explicit `# References` heading.
5. The same hardened PDF route remains in use: page-bearing citations, width-safe `ReaderFacingFoma` blocks, SC-numbered rule headings, section-order checking, and chronology-evidence checking.

## Remaining PDF issues for human review

No automated blocker remains. The only routine visual follow-up still worth a human glance is the four wrapped code boxes that exceed the old source-width threshold:

1. `SC056` West Saxon palatal diphthongization
2. `SC058` Nasal dissimilation
3. `SC063` High-vowel apocope
4. `SC065` Medial syncope before dentals

Those blocks now build inside the width-safe `ReaderFacingFoma` environment, but they remain the most natural places for final visual spot-checking in the PDF.

## Scope confirmation

1. No new chapter was added for `SC062`.
2. No FST rules were changed.
3. No TSV files were changed.
4. No chronology cards were changed.
5. No standardized source reports were substantively changed.
6. No source dossiers were substantively changed.
7. No book dossiers were substantively changed.

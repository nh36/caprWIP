# Reader-facing local section 02 report

## New chapters added

This pass added exactly three new reader-facing chapters:

1. `059-oe-back-mutation.md`
2. `060-ws-palatal-umlaut-note.md`
3. `061-weak-tail-nasal-loss-note.md`

No larger chapter batch was added.

## Source reports and dossiers used

The new chapters were derived from:

- `Germanic/docs/sound_changes/change_reports/full/059-oe-back-mutation.md`
- `Germanic/docs/sound_changes/change_reports/full/060-ws-palatal-umlaut-note.md`
- `Germanic/docs/sound_changes/change_reports/full/061-weak-tail-nasal-loss-note.md`

The shared dossier context used for the batch was:

- `Germanic/docs/sound_changes/literature_dossiers/059-061-back-mutation-and-weak-tail-bridge.dossier.md`
- `Germanic/docs/sound_changes/book_dossiers/059-061-back-mutation-and-weak-tail-bridge.book-dossier.md`

## Preserved outputs

The following existing outputs were preserved:

- `reader_facing_pilot_01.md`
- `reader_facing_pilot_01.pdf`
- `reader_facing_pilot_02.md`
- `reader_facing_pilot_02.pdf`
- `reader_facing_local_section_01.md`
- `reader_facing_local_section_01.pdf`
- `build_reader_facing_pilot_docker.sh`
- `build_reader_facing_pilot_02_docker.sh`
- `build_reader_facing_local_section_01_docker.sh`

## Ten-chapter order used

The local-section-02 build assembles chapters in this order:

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

## Small changes made to existing chapter files

Only one existing chapter file received tiny mechanical prose changes:

- `049-050-b-allophony-and-sievers-law-syncope.md`
  - retained “two changes together” wording;
  - smoothed the `streċċan` / `strecċan` sentence once more for cleaner PDF
    reading;
  - adjusted the phrase around Germanic `*b` so the reconstructed form reads more
    naturally in prose.

No other existing reader-facing chapter files were substantively revised.

## New build and outputs

This pass added:

- `build_reader_facing_local_section_02_docker.sh`
- `reader_facing_local_section_02.md`
- `reader_facing_local_section_02.pdf`

The new section introduction now frames the stretch from labial allophony and
Sievers-law syncope through palatalization, pre-umlaut glide loss, i-umlaut,
nasal dissimilation, back mutation, and the two short weak-tail notes, without
presenting the whole section as one single historical law.

## Checker result

Command run:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Result:

- passes with no warnings

The checker skip list was extended deliberately to exclude
`reader_facing_local_section_02.md` and
`reader_facing_local_section_02_report.md` so generated assembly output and the
report do not create false positives. The chapter files remain under check.

## PDF build result

Command run:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_02_docker.sh
```

Result:

- `reader_facing_local_section_02.md` generated successfully
- `reader_facing_local_section_02.pdf` generated successfully

## Points for human PDF review

- `059-oe-back-mutation.md` is the center of the new batch and should be checked
  visually against the shorter notes on either side to confirm the intended
  asymmetry.
- `060-ws-palatal-umlaut-note.md` and `061-weak-tail-nasal-loss-note.md` should
  be checked to make sure they remain brief and do not visually compete with the
  back-mutation chapter.
- The section introduction should be checked in the PDF for pacing at the point
  where the earlier palatalization/umlaut material gives way to back mutation
  and the two weak-tail notes.

## Scope confirmation

- No FST rules were changed.
- No TSV files were changed.
- No chronology-card files were changed.
- No standardized source reports were substantively changed.
- No source dossiers or book dossiers were substantively changed.
- Outside the new chapter files and local-section-02 build/report files, the
  only support changes were:
  - `reader_facing/README.md`
  - `reader_facing/check_reader_facing_style.py`
  - the tiny mechanical polish in `049-050-b-allophony-and-sievers-law-syncope.md`

# Reader-facing local section 01 report

## Chapters included

The ordered local section includes exactly these seven existing chapter files:

1. `049-050-b-allophony-and-sievers-law-syncope.md`
2. `051-sk-palatalization.md`
3. `052-velar-palatalization.md`
4. `053-054-pre-umlaut-bridge-and-w-loss.md`
5. `055-056-i-umlaut-core.md`
6. `057-j-cluster-coalescence.md`
7. `058-nasal-dissimilation.md`

No new sound-change chapters were added in this pass.

## Preserved pilot files

These files were preserved and not overwritten or deleted:

- `reader_facing_pilot_01.md`
- `reader_facing_pilot_01.pdf`
- `build_reader_facing_pilot_docker.sh`
- `reader_facing_pilot_02.md`
- `reader_facing_pilot_02.pdf`
- `build_reader_facing_pilot_02_docker.sh`
- `reader_facing_pilot_02_report.md`

## Chapter order used

The local-section build assembles the seven chapters in this chronological order:

1. `049-050-b-allophony-and-sievers-law-syncope.md`
2. `051-sk-palatalization.md`
3. `052-velar-palatalization.md`
4. `053-054-pre-umlaut-bridge-and-w-loss.md`
5. `055-056-i-umlaut-core.md`
6. `057-j-cluster-coalescence.md`
7. `058-nasal-dissimilation.md`

## Small prose fixes made

Only very small prose fixes were made:

- in `049-050-b-allophony-and-sievers-law-syncope.md`, “keeping the two
  chapters together” was changed to “keeping the two changes together”;
- in the same file, the `streċċan` / `strecċan` sentence was smoothed slightly
  so the derivational consequence reads more cleanly.

No broad rewriting was done to the seven chapter files.

## New build and outputs

This pass added:

- `build_reader_facing_local_section_01_docker.sh`
- `reader_facing_local_section_01.md`
- `reader_facing_local_section_01.pdf`

The assembled local section also begins with a short reader-facing introduction
that frames the stretch from labial allophony and Sievers-law syncope through
palatalization, pre-umlaut glide loss, i-umlaut, later j-cluster coalescence,
and nasal dissimilation.

## Checker result

Command run:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Result:

- passes with no warnings

The checker skip list was extended deliberately to exclude
`reader_facing_local_section_01.md` and `reader_facing_local_section_01_report.md`
so generated assembly output and the report file do not create false positives.
The chapter files themselves remain under check.

## PDF build result

Command run:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_01_docker.sh
```

Result:

- `reader_facing_local_section_01.md` generated successfully
- `reader_facing_local_section_01.pdf` generated successfully

## Points for human PDF review

- The section introduction should be reviewed in the rendered PDF for tone and
  pacing against the first chapter opening.
- The `049-050` chapter remains intentionally asymmetric, so its scale should be
  reviewed visually against the stronger palatalization and umlaut chapters that
  follow it.
- The `057` chapter remains intentionally brief and one-sided, so its shortness
  should be reviewed in context rather than expanded automatically.

## Scope confirmation

- No new sound-change chapters were added beyond the current seven.
- No FST rules were changed.
- No TSV files were changed.
- No chronology-card files were changed.
- No standardized source reports were substantively changed.
- No source dossiers or book dossiers were substantively changed.
- Outside the local-section build/report files, only these support files changed:
  - `reader_facing/README.md`
  - `reader_facing/check_reader_facing_style.py`

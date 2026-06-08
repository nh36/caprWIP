# Reader-facing pilot 02 report

## Existing pilot files preserved unchanged

The following files were kept as the baseline model and were not substantively
rewritten in this pass:

- `Germanic/docs/sound_changes/reader_facing/052-velar-palatalization.md`
- `Germanic/docs/sound_changes/reader_facing/055-056-i-umlaut-core.md`
- `Germanic/docs/sound_changes/reader_facing/058-nasal-dissimilation.md`
- `Germanic/docs/sound_changes/reader_facing/reader_facing_pilot_01.md`
- `Germanic/docs/sound_changes/reader_facing/reader_facing_pilot_01.pdf`
- `Germanic/docs/sound_changes/reader_facing/build_reader_facing_pilot_docker.sh`

## New chapters added

| New chapter | Derived from source report |
| --- | --- |
| `049-050-b-allophony-and-sievers-law-syncope.md` | `Germanic/docs/sound_changes/change_reports/full/049-050-onset-allophony-and-sievers-law-bridge.md` |
| `051-sk-palatalization.md` | `Germanic/docs/sound_changes/change_reports/full/051-oe-sk-palatalization.md` |
| `053-054-pre-umlaut-bridge-and-w-loss.md` | `Germanic/docs/sound_changes/change_reports/full/053-054-pre-umlaut-bridge-and-w-loss.md` |
| `057-j-cluster-coalescence.md` | `Germanic/docs/sound_changes/change_reports/full/057-oe-j-cluster-coalescence-note.md` |

## Reader-facing transformations

Moving from the standardized source reports to the new reader-facing chapters
required the same changes already visible in the original three pilot chapters:

- the seven-part source-report scaffold was rewritten as book prose with one
  `## Historical discussion` section and rule-level subsections below it;
- source tradition and CAPR implementation were kept distinct, but the
  distinction now lives inside chapter prose instead of source-report headings;
- chronology was restated through lexical consequences and chapter sequencing,
  without source-report lifecycle language;
- FOMA material was kept only as one-`define` reader-useful code blocks;
- weak or asymmetrical evidence was kept explicitly modest, especially for the
  allophony, post-velar `w`-loss, and j-cluster chapters.

## New pilot-02 assembly files

This pass added:

- `Germanic/docs/sound_changes/reader_facing/source_note_pilot_02.md`
- `Germanic/docs/sound_changes/reader_facing/build_reader_facing_pilot_02_docker.sh`
- `Germanic/docs/sound_changes/reader_facing/reader_facing_pilot_02.md`
- `Germanic/docs/sound_changes/reader_facing/reader_facing_pilot_02.pdf`

Pilot 02 preserves the original three chapter files unchanged and appends the
new four-chapter batch afterward in the expanded assembled pilot.

## Checker and build status

- Style checker command run:
  - `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py`
- Result:
  - passes with no warnings after the new chapters and skip-list updates
- Expanded build command run:
  - `bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_pilot_02_docker.sh`
- Result:
  - `reader_facing_pilot_02.md` generated successfully
  - `reader_facing_pilot_02.pdf` generated successfully

## Remaining awkward passages for human review

No checker-blocking issues remain. The passages most worth later human review
are the ones already expected from the source material:

- `049-050` remains an intentionally asymmetric pairing, since the allophony rule
  is much thinner historically than Sievers-law syncope.
- `053-054` also remains structurally uneven, with the `*ngw > *ng` rule far
  slighter than the `sea`-type loss of `w` before `i`.
- `057` is necessarily short because its earlier relation is clearer than any
  later lexical breakpoint.

## Scope confirmation

- No FST rules were changed.
- No TSV files were changed.
- No chronology-card files were changed.
- No source reports were substantively changed.
- No source dossiers or book dossiers were substantively changed.
- The only code/doc support changes outside the new chapters themselves were:
  - the pilot-02 build/source-note files;
  - a small `README.md` update in `reader_facing/`;
  - a small skip-list update in `check_reader_facing_style.py` so generated
    pilot-02/report files do not pollute the chapter-level style audit.

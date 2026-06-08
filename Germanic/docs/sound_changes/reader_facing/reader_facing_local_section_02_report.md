# Reader-facing local section 02 report

## Scope

This pass did **not** add another large batch of reader-facing sound-change
chapters. The section still runs through the same ten chapters, ending at
`061-weak-tail-nasal-loss-note.md`.

The rightward extension chapters already in place remain:

1. `059-oe-back-mutation.md`
2. `060-ws-palatal-umlaut-note.md`
3. `061-weak-tail-nasal-loss-note.md`

No additional sound-change chapters were added beyond those ten.

## Source reports and dossiers used

The rightward extension still derives from:

- `Germanic/docs/sound_changes/change_reports/full/059-oe-back-mutation.md`
- `Germanic/docs/sound_changes/change_reports/full/060-ws-palatal-umlaut-note.md`
- `Germanic/docs/sound_changes/change_reports/full/061-weak-tail-nasal-loss-note.md`

and from the shared dossier context:

- `Germanic/docs/sound_changes/literature_dossiers/059-061-back-mutation-and-weak-tail-bridge.dossier.md`
- `Germanic/docs/sound_changes/book_dossiers/059-061-back-mutation-and-weak-tail-bridge.book-dossier.md`

## Preserved outputs

These outputs were preserved:

- `reader_facing_pilot_01.md`
- `reader_facing_pilot_01.pdf`
- `reader_facing_pilot_02.md`
- `reader_facing_pilot_02.pdf`
- `reader_facing_local_section_01.md`
- `reader_facing_local_section_01.pdf`
- `build_reader_facing_pilot_docker.sh`
- `build_reader_facing_pilot_02_docker.sh`
- `build_reader_facing_local_section_01_docker.sh`

`reader_facing_local_section_02.md` and `reader_facing_local_section_02.pdf`
were the target outputs for this pass and were regenerated in place.

## Ten-chapter order used

The local-section-02 build now assembles chapters in this order:

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

## Typographic and prose fixes made

This pass fixed the typography and reader-facing prose of the existing ten
chapters rather than adding new content.

### Typography

- bare starred linguistic forms in prose and headings were converted to safe
  forms, using raw LaTeX `\emph{*form}` where visible reconstructed forms were
  intended;
- all rule-level section headings now include visible SC numbers;
- `reader_facing_local_section_02.md` now ends with an explicit `# References`
  heading and `#refs` placeholder so the bibliography appears under a visible
  heading in the PDF.

### Small chapter-level prose changes

- `049-050-b-allophony-and-sievers-law-syncope.md`
  - repaired bare-star forms around Germanic `*b`, Sievers-law `*i` / `*j`, and
    the `*-CijV-*` / `*-CjV-*` patterns;
  - smoothed the `streċċan` / `strecċan` sentence.
- `057-j-cluster-coalescence.md`
  - kept the chapter short while removing a small amount of chapter-management
    phrasing.
- `058-nasal-dissimilation.md`
  - repaired the quoted `*n` form and one small phrase about what the rule keeps
    visible.
- `059-oe-back-mutation.md`
  - kept SC059 as the center of the group while reducing local-section/extension
    phrasing.
- `060-ws-palatal-umlaut-note.md`
  - kept the note short and one-sided while reducing chapter-planning language;
  - repaired the `*h`-cluster heading and `*i` / `*h` prose forms.
- `061-weak-tail-nasal-loss-note.md`
  - rewrote the ending so it reads as historical discussion rather than chapter
    self-commentary;
  - repaired the final weak-tail `*-ną`, `*-mą`, `*-n`, and `*-m` forms.

No broad restructuring of the ten chapters was undertaken.

## Checker result

Command run:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Result:

- passes with no warnings

The strengthened checker now:

- flags bare starred forms outside fenced code blocks;
- checks that rule-level headings carry SC numbers;
- scans for a stronger set of project-facing prose markers;
- continues to skip generated assembly files and report files rather than chapter
  files.

The checker failed before the chapter fixes and passed after them.

## Cascade-order verification

Command run:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_02_docker.sh
```

Result:

- passed successfully
- confirmed chapter order from `SC049` through `SC061`
- confirmed internal multi-rule order:
  - `SC049` before `SC050`
  - `SC053` before `SC054`
  - `SC055` before `SC056`

## PDF build result

Command run:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_02_docker.sh
```

Result:

- `reader_facing_local_section_02.md` generated successfully
- `reader_facing_local_section_02.pdf` generated successfully

## Points for human PDF review

- Confirm that the long unintended italic stretches caused by bare starred forms
  are gone everywhere, especially in the `049-050`, `051`, `053-054`, and
  `060` chapters.
- Check the rule headings with SC numbers for visual balance, especially the
  longer `SC060` heading with the `*h`-cluster phrase.
- Check the final bibliography page to confirm that the visible `References`
  heading and spacing are satisfactory.
- Check that `059` still reads as the clear center of the rightward extension,
  with `060` and `061` remaining visibly shorter.

## Scope confirmation

- No FST rules were changed.
- No TSV files were changed.
- No chronology-card files were changed.
- No standardized source reports were substantively changed.
- No source dossiers or book dossiers were substantively changed.
- Outside the ten chapter files, the only support changes in this pass were:
  - `reader_facing/check_reader_facing_style.py`
  - `reader_facing/check_reader_facing_section_order.py`
  - `reader_facing/build_reader_facing_local_section_02_docker.sh`

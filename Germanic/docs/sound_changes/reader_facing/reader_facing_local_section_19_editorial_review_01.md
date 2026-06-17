# Reader-facing local section 19 editorial review 01

## Latest commit inspected

1. `16e024f9 docs: include SC005 SC009 and SC012 reader-facing`

## Files edited

1. `Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
2. `Germanic/docs/sound_changes/reader_facing/005-unstressed-a-raising-before-final-m.md`
3. `Germanic/docs/sound_changes/reader_facing/009-ij-contraction-in-friend.md`
4. `Germanic/docs/sound_changes/reader_facing/012-lth-voicing.md`
5. `Germanic/docs/sound_changes/reader_facing/013-dental-hardening.md`

## Introduction changes

1. The opening was shortened from a long catalogue sentence to two shorter framing paragraphs.
2. The revised introduction now:
   - states the scope of the section as a continuous sequence from early West Germanic changes to Old English r-metathesis;
   - distinguishes larger familiar changes from smaller witness-driven notes; and
   - explains that the numbered sections do not all carry the same historical weight.

## Numbering-note changes

1. The numbering note was kept, but tightened.
2. It now says only that:
   - the numbering remains traceable to the CAPR inventory and chronology tests; and
   - `SC038`, `SC062`, and `SC084` are technical or weight-marking stages, while `SC077` is a numbering gap.
3. It does not describe `SC005`, `SC009`, or `SC012` as omissions.

## SC005 integration changes

1. The opening of `005-unstressed-a-raising-before-final-m.md` now presents the rule as a short morphophonological note grounded in inflectional material, rather than as an awkward exception.
2. The closing chronology language now keeps the broad/far later boundary while reducing the sense of apology.

## SC009 integration changes

1. The opening of `009-ij-contraction-in-friend.md` now treats lexical narrowness as part of the historical interpretation, not as an objection to inclusion.
2. The closing lines now hand the sequence forward more naturally into the tighter SC010/SC011 seam.

## SC012 integration changes

1. `012-lth-voicing.md` now reads more clearly as a cautious but genuine chapter on the `lþ > ld` development.
2. The scope caution remains explicit, but the tone is less defensive.
3. The chapter now links forward more naturally to `SC013` and states plainly that no exact wrong-output witness exists because the chronology is boundary-only on both sides.

## Chronology-phrasing changes

1. The revised prose keeps all core distinctions:
   - tight local seam for `SC010` / `SC011`
   - broad/far later boundaries for `SC005` and `SC009`
   - boundary-only / negative chronology for `SC012` and `SC013`
2. Repetition was reduced selectively by varying how boundary-only and broad/far results are described.
3. No chronology facts were removed.

## FOMA-width inspection result

1. The FOMA-width checker still reports `11` over-threshold blocks overall.
2. The newly added or newly reviewed early chapters do **not** add to that set:
   - `005-unstressed-a-raising-before-final-m.md` — longest line `87`, over-threshold: `no`
   - `009-ij-contraction-in-friend.md` — longest line `54`, over-threshold: `no`
   - `012-lth-voicing.md` — longest line `26`, over-threshold: `no`
3. No front-matter width problem was introduced by the revised introduction or numbering note.

## Checks run and results

1. `bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - passed
   - regenerated `reader_facing_local_section_19.md`
   - regenerated `reader_facing_local_section_19.pdf`
   - regenerated `reader_facing_manifest_coverage_07.md`
2. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py`
   - no warnings
3. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py`
   - files checked: `54`
   - citation issues: `0`
4. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py`
   - `foma` blocks checked: `85`
   - blocks over threshold: `11`
5. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - passed
6. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - files checked: `54`
   - links checked: `496`
   - issues: `0`
7. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py`
   - sections checked: `85`
   - warnings: `0`
8. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - introduction paragraphs checked: `5`
   - issues: `0`
9. `git diff --check`
   - passed

## PDF build result

1. `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.pdf` regenerated successfully.
2. Pandoc emitted the usual `Ticker: poll failed: Interrupted system call` warnings without preventing output.

## Scope confirmations

1. No new sound-change chapters were created.
2. No local section 20 was created.
3. No manifest files were changed in this editorial review pass.
4. No FST rules were changed.
5. No lexical TSV data were changed.

## Remaining editorial issues for human review

1. The new introduction and numbering note should be checked visually in the PDF to make sure they sit comfortably on the page and do not feel too abrupt before `SC003`.
2. The transitions across `SC009 -> SC010`, `SC012 -> SC013`, and `SC013 -> SC014-015` are now smoother, but they are still the likeliest places for a human reader to notice tonal shifts.
3. The pre-existing over-threshold `foma` blocks elsewhere in the section remain worth a quick PDF spot-check even though they are not new.

## Handoff for the next task

1. Local section 19 now includes a continuous early sequence from SC003 through SC013, with SC005, SC009, and SC012 integrated as cautious but genuine reader-facing sound-change sections. The only remaining non-chapter numbers are SC038, SC062, SC077, and SC084. The next pass should review the generated PDF visually and then decide whether to proceed to a whole-volume copy-edit or to address any remaining PDF-specific formatting issues.

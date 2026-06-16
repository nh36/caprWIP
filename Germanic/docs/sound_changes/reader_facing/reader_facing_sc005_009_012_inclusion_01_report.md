# SC005-SC009-SC012 reader-facing inclusion 01 report

## Latest commit inspected

1. `42f2e0f6 docs: audit remaining reader-facing sound-change gaps`

## Why SC005 is now included

1. The pre-\emph{m} raising has linguistic content and should not remain invisible between `SC004` and `SC006`.
2. The source base supports a real unstressed-vowel development in inflectional material.
3. The section makes the caution visible by keeping the inflectional setting central and by not letting the compact trace witness `shoulder` carry the whole case.

## Why SC009 is now included

1. The `friend` development is linguistically meaningful and should not disappear between `SC008` and `SC010`.
2. The section keeps the lexical narrowness explicit instead of treating it as a reason for omission.
3. The prose explains that this is a short lexical sound-change note, not a broadly productive law.

## Why SC012 is now included

1. The `lþ > ld` development is source-supported and should not remain invisible between `SC011` and `SC013`.
2. The section keeps the northern-West-Germanic scope caution visible.
3. The prose states plainly that the order test does not provide a positive local boundary.

## How each one is cautioned

1. `SC005` is framed as a cautious inflectional or morphophonological note with a broad/far later boundary and a stage label that remains more technical than the chapter title.
2. `SC009` is framed as a narrow lexical note whose historical case remains effectively the `friend` family alone.
3. `SC012` is framed as a cautious scope-limited note whose chronology is boundary-only on both sides.

## Backend reports updated

1. `Germanic/docs/sound_changes/change_reports/full/005-nwgmc-a-to-u-before-m.md`
2. `Germanic/docs/sound_changes/literature_dossiers/005-nwgmc-a-to-u-before-m.dossier.md`
3. `Germanic/docs/sound_changes/book_dossiers/005-nwgmc-a-to-u-before-m.book-dossier.md`
4. `Germanic/docs/sound_changes/change_reports/full/009-pwgmc-ij-contraction.md`
5. `Germanic/docs/sound_changes/literature_dossiers/009-pwgmc-ij-contraction.dossier.md`
6. `Germanic/docs/sound_changes/book_dossiers/009-pwgmc-ij-contraction.book-dossier.md`
7. `Germanic/docs/sound_changes/change_reports/full/012-pwgmc-l-th-voicing.md`
8. `Germanic/docs/sound_changes/literature_dossiers/012-pwgmc-l-th-voicing.dossier.md`
9. `Germanic/docs/sound_changes/book_dossiers/012-pwgmc-l-th-voicing.book-dossier.md`

## Manifest files updated

1. `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`
2. `Germanic/docs/sound_changes/change_reports/sound_change_half_scaffold.tsv`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
4. `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
5. `Germanic/docs/sound_changes/book_dossiers/sound_change_book_dossier_inventory.tsv`

## Reader-facing chapters created

1. `Germanic/docs/sound_changes/reader_facing/005-unstressed-a-raising-before-final-m.md`
2. `Germanic/docs/sound_changes/reader_facing/009-ij-contraction-in-friend.md`
3. `Germanic/docs/sound_changes/reader_facing/012-lth-voicing.md`

## Local-section-19 chapter order

1. `003-west-germanic-rhotacism.md`
2. `004-pwgmc-ai-monophthongization.md`
3. `005-unstressed-a-raising-before-final-m.md`
4. `006-early-i-apocope.md`
5. `007-final-o-lowering-before-r.md`
6. `008-coronal-w-assimilation.md`
7. `009-ij-contraction-in-friend.md`
8. `010-west-germanic-j-gemination.md`
9. `011-syllabic-j-after-final-vowel-loss.md`
10. `012-lth-voicing.md`
11. `013-dental-hardening.md`
12. `014-015-opening-vowel-prelude.md`
13. then the existing `SC014` onward local-section-18 sequence continues unchanged through `087-r-metathesis.md`

## Coverage report created

1. `Germanic/docs/sound_changes/reader_facing/reader_facing_manifest_coverage_07.md`
2. It confirms `SC003-SC013` are now all covered in the reader-facing sequence.
3. The only remaining expected non-chapter numbers are `SC038`, `SC062`, `SC077`, and `SC084`.

## Numbering note updated

1. The assembled `reader_facing_local_section_19.md` now carries a short numbering note near the beginning.
2. That note no longer lists `SC005`, `SC009`, or `SC012` as omitted.
3. It lists only `SC038`, `SC062`, `SC077`, and `SC084` as non-chapter technical or numbering-only cases.

## Checks run and results

1. `python3 Germanic/tools/audit_sound_change_report_style.py`
   - passed
2. `SOUND_CHANGE_VOLUME_OUTPUT_MD=/tmp/sc005_009_012_inclusion_volume.md SOUND_CHANGE_COVERAGE_REPORT_MD=/tmp/sc005_009_012_inclusion_coverage.md python3 Germanic/docs/assembly/build_sound_change_volume.py`
   - passed
   - wrote a temporary assembled half with `53` sound-change unit(s)
3. `bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - passed after one cleanup rerun to clear the initial SC012 chronology-note warning
4. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py`
   - no warnings
5. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py`
   - files checked: `54`
   - citation issues: `0`
6. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py`
   - `foma` blocks checked: `85`
   - blocks over the conservative old-rendering threshold: `11`
7. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - passed
8. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - files checked: `54`
   - links checked: `491`
   - issues: `0`
9. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py`
   - sections checked: `85`
   - warnings: `0`
10. `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh`
   - introduction paragraphs checked: `4`
   - issues: `0`
11. `git diff --check`
   - passed

## PDF build result

1. `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md` generated successfully.
2. `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.pdf` generated successfully.
3. Pandoc emitted the usual `Ticker: poll failed: Interrupted system call` warnings without preventing output.

## Remaining non-chapter technical numbers

1. `SC038`
2. `SC062`
3. `SC077`
4. `SC084`

## Scope confirmations

1. No chapters were created for `SC038`, `SC062`, `SC077`, or `SC084`.
2. No FST rules were changed.
3. No lexical TSV data were changed.

## Handoff for the next task

1. SC005, SC009, and SC012 are now included as reader-facing sound-change sections. Their cautions are visible in the prose rather than used as grounds for omission. The only remaining non-chapter numbers are technical or numbering-only cases: SC038, SC062, SC077, and SC084. The next pass should be a whole-volume readability and consistency review of local section 19, with attention to transitions, repeated chronology phrasing, the technical-numbering note, and whether the early SC003-SC013 sequence now reads as a continuous account.

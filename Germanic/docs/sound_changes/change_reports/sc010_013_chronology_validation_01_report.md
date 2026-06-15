# SC010-SC013 chronology validation 01 report

## Latest commit inspected

1. `c3e5b5b8 docs: prepare SC010-SC013 backend promotion`

## TSV files inspected

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_failures.tsv`

## SC010 earlier result

1. Result: `no_break_before_boundary`
2. Safe computational window on that side extends down to order `4`.
3. The last crossed historical stage is `SC004` `PWGmcAiMonophthongization`.
4. This is boundary-only rather than a positive earlier chronology constraint.

## SC010 later result

1. Result: `first_break_found`
2. First later break: `SC010_later_order_11`
3. Named crossed rule: `SC011` `PWGmcSyllabicJ`
4. Exact diagnostic: PGmc `*nátją` yields expected OE `nett`, but the later-shifted variant yields `nete`.
5. This is a tight local reciprocal boundary rather than a broad/far rightward limit.

## SC011 earlier result

1. Result: `first_break_found`
2. First earlier break: `SC011_earlier_order_10`
3. Named crossed rule: `SC010` `PWGmcJGemination`
4. Exact diagnostic: PGmc `*nátją` yields expected OE `nett`, but the earlier-shifted variant yields `nete`.
5. This is the reciprocal side of the SC010/SC011 local seam.

## SC011 later result

1. Result: `no_break_before_boundary`
2. Safe computational window on that side extends through order `86`.
3. The search reaches `SC087` `OERMetathesis` with no real break.
4. This is boundary-only rather than a positive later chronology constraint.

## SC012 earlier result

1. Result: `no_break_before_boundary`
2. Safe computational window on that side extends down to order `4`.
3. The last crossed historical stage is `SC004` `PWGmcAiMonophthongization`.
4. This is boundary-only and chronology-negative.

## SC012 later result

1. Result: `no_break_before_boundary`
2. Safe computational window on that side extends through order `86`.
3. The search reaches `SC087` `OERMetathesis` with no real break.
4. This is boundary-only and chronology-negative.

## SC013 earlier result

1. Result: `no_break_before_boundary`
2. Safe computational window on that side extends down to order `4`.
3. The last crossed historical stage is `SC004` `PWGmcAiMonophthongization`.
4. This is boundary-only and chronology-negative.

## SC013 later result

1. Result: `no_break_before_boundary`
2. Safe computational window on that side extends through order `86`.
3. The search reaches `SC087` `OERMetathesis` with no real break.
4. This is boundary-only and chronology-negative.

## Chronology cards created

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC010-pwgmc-j-gemination.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC011-pwgmc-syllabic-j.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC012-pwgmc-l-th-voicing.md`
4. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC013-pwgmc-dental-hardening.md`

## Backend reports, dossiers, and book dossiers updated

1. Reports updated:
   - `Germanic/docs/sound_changes/change_reports/full/010-pwgmc-j-gemination.md`
   - `Germanic/docs/sound_changes/change_reports/full/011-pwgmc-syllabic-j.md`
   - `Germanic/docs/sound_changes/change_reports/full/012-pwgmc-l-th-voicing.md`
   - `Germanic/docs/sound_changes/change_reports/full/013-pwgmc-dental-hardening.md`
2. Literature dossiers updated:
   - `Germanic/docs/sound_changes/literature_dossiers/010-pwgmc-j-gemination.dossier.md`
   - `Germanic/docs/sound_changes/literature_dossiers/011-pwgmc-syllabic-j.dossier.md`
   - `Germanic/docs/sound_changes/literature_dossiers/012-pwgmc-l-th-voicing.dossier.md`
   - `Germanic/docs/sound_changes/literature_dossiers/013-pwgmc-dental-hardening.dossier.md`
3. Book dossiers updated:
   - `Germanic/docs/sound_changes/book_dossiers/010-pwgmc-j-gemination.book-dossier.md`
   - `Germanic/docs/sound_changes/book_dossiers/011-pwgmc-syllabic-j.book-dossier.md`
   - `Germanic/docs/sound_changes/book_dossiers/012-pwgmc-l-th-voicing.book-dossier.md`
   - `Germanic/docs/sound_changes/book_dossiers/013-pwgmc-dental-hardening.book-dossier.md`

## Manifest promotion decision for SC010

1. `SC010` is promoted.
2. Reason: source support is adequate, the chronology card is validated from real TSV output, and the later side supplies a tight local reciprocal boundary with `SC011` via `net`.

## Manifest promotion decision for SC011

1. `SC011` is promoted.
2. Reason: source support is adequate, the chronology card is validated from real TSV output, and the earlier side supplies the reciprocal local boundary with `SC010` via `net`.
3. Caution retained: the current compact trace remains direct-hit-light, so later prose must keep that visible.

## Manifest promotion decision for SC012

1. `SC012` is **not** promoted.
2. Exact blockers:
   - the best source-stage wording remains narrower than the inventory's plain PWGmc label; and
   - the validated chronology card is negative on both sides, so it supplies no positive historical boundary.

## Manifest promotion decision for SC013

1. `SC013` is promoted.
2. Reason: the source support for the historical hardening itself is strong enough to justify a short singleton note, even though the chronology card is negative on both sides.
3. Caution retained: later prose must treat both boundaries as methodological limits rather than positive local ordering claims.

## Whether `report_manifest.tsv` was updated

1. Yes.
2. The manifest/index/inventory layer was updated consistently for `SC010`, `SC011`, and `SC013` only:
   - `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`
   - `Germanic/docs/sound_changes/change_reports/sound_change_half_scaffold.tsv`
   - `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
   - `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
   - `Germanic/docs/sound_changes/book_dossiers/sound_change_book_dossier_inventory.tsv`

## Checks run and results

1. `python3 Germanic/tools/audit_sound_change_report_style.py`
   - passed
2. `SOUND_CHANGE_VOLUME_OUTPUT_MD=/tmp/sc010_013_validation_volume.md SOUND_CHANGE_COVERAGE_REPORT_MD=/tmp/sc010_013_validation_coverage.md python3 Germanic/docs/assembly/build_sound_change_volume.py`
   - passed
   - wrote a temporary assembled half with `50` sound-change unit(s)
   - temporary files were removed afterward
3. Manual heading check on the four SC010-SC013 full reports
   - passed
4. Manual style-tripwire grep on the four SC010-SC013 full reports
   - no matches
5. `git --no-pager diff --check`
   - passed

## Scope confirmations

1. No reader-facing chapters were created.
2. No local section 18 was created.
3. No production FST rules were changed.
4. No lexical TSV data were changed.

## Handoff for the next task

1. The next task should add reader-facing prose only for the promoted rules `SC010`, `SC011`, and `SC013`, create local section `18`, and continue to leave `SC012` out in this pass unless later source/stage work changes its status.

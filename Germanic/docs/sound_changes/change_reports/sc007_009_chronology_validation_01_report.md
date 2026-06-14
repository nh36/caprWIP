# SC007-SC009 chronology validation 01 report

## Latest commit inspected

1. `811e5c31 docs: prepare SC007-SC009 backend promotion`

## TSV files inspected

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv`

## SC007 results

### Earlier

1. Result: `no_break_before_boundary`
2. Last safe order: `4`
3. Crossed stage before boundary: `SC004` PWGmc Ai Monophthongization
4. Historical status: boundary-only / non-positive

### Later

1. Result: `first_break_found`
2. First break order: `43`
3. Named boundary rule: `SC043` Anglo Frisian Brightening / `AngloFrisianBrightening`
4. Historical status: real one-sided historical boundary, broad/far rather than tightly local
5. Exact wrong-output diagnostic:
   - `*wátōr` -> expected `wæter`, variant `water`

## SC008 results

### Earlier

1. Result: `no_break_before_boundary`
2. Last safe order: `4`
3. Crossed stage before boundary: `SC004` PWGmc Ai Monophthongization
4. Historical status: boundary-only / non-positive

### Later

1. Result: `first_break_found`
2. First break order: `31`
3. Named boundary rule: `SC031` OE WW Simplification / `OEWWSimplification`
4. Historical status: real one-sided historical boundary, broad/far rather than tightly local
5. Exact wrong-output diagnostic:
   - `*fédwōr` -> expected `fēower`, variant `fēowwer`

## SC009 results

### Earlier

1. Result: `no_break_before_boundary`
2. Last safe order: `4`
3. Crossed stage before boundary: `SC004` PWGmc Ai Monophthongization
4. Historical status: boundary-only / non-positive

### Later

1. Result: `first_break_found`
2. First break order: `32`
3. Named boundary rule: `SC032` OE Diphthong Leveling / `OEDiphthongLeveling`
4. Historical status: real one-sided historical boundary, broad/far rather than tightly local
5. Exact wrong-output diagnostic:
   - `*fríjōndz` -> expected `frēond`, variant `friund`

## Chronology cards created

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC007-pwgmc-final-or-lowering.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC008-pwgmc-coronal-w-assimilation.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC009-pwgmc-ij-contraction.md`

## Backend reports, literature dossiers, and book dossiers updated

Updated:

1. `Germanic/docs/sound_changes/change_reports/full/007-pwgmc-final-or-lowering.md`
2. `Germanic/docs/sound_changes/change_reports/full/008-pwgmc-coronal-w-assimilation.md`
3. `Germanic/docs/sound_changes/change_reports/full/009-pwgmc-ij-contraction.md`
4. `Germanic/docs/sound_changes/literature_dossiers/007-pwgmc-final-or-lowering.dossier.md`
5. `Germanic/docs/sound_changes/literature_dossiers/008-pwgmc-coronal-w-assimilation.dossier.md`
6. `Germanic/docs/sound_changes/literature_dossiers/009-pwgmc-ij-contraction.dossier.md`
7. `Germanic/docs/sound_changes/book_dossiers/007-pwgmc-final-or-lowering.book-dossier.md`
8. `Germanic/docs/sound_changes/book_dossiers/008-pwgmc-coronal-w-assimilation.book-dossier.md`
9. `Germanic/docs/sound_changes/book_dossiers/009-pwgmc-ij-contraction.book-dossier.md`

The old “no validated chronology card exists yet” wording was replaced with the actual SC007-SC009 results.

## Manifest promotion decision for SC007

**Promoted.**

Reason:

1. The chronology card is validated and gives a real one-sided later boundary at `SC043`.
2. The source support is narrow but explicit and acceptable for a short singleton note centered on `four` and `water`.
3. The report keeps the narrow environment and witness-set caution visible.

## Manifest promotion decision for SC008

**Promoted.**

Reason:

1. The chronology card is validated and gives a real one-sided later boundary at `SC031`.
2. The source support is narrow but historically solid, with both lexical and plural-pronominal support.
3. The report keeps the small witness set and the broad/far boundary caution explicit.

## Manifest promotion decision for SC009

**Not promoted.**

Exact blockers:

1. The chronology card is validated, but the rule remains lexically unique.
2. The source tradition itself warns against broader generalization from the `friend` sequence.
3. Even with real chronology, the evidence remains too narrow for a manifest-backed singleton note at this stage.

## Manifest/scaffold/index updates

Updated:

1. `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`
2. `Germanic/docs/sound_changes/change_reports/sound_change_half_scaffold.tsv`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
4. `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
5. `Germanic/docs/sound_changes/book_dossiers/sound_change_book_dossier_inventory.tsv`

Result:

1. `SC007` and `SC008` were added to the manifest-backed backend layer.
2. `SC009` was intentionally left out.

## Checks run and results

### Report style audit

Command:

```bash
python3 Germanic/tools/audit_sound_change_report_style.py
```

Result:

1. Passed.
2. Because `SC007` and `SC008` are now manifest-listed, the automated audit covers them directly.

### Manifest/scaffold consistency check

Command:

```bash
SOUND_CHANGE_VOLUME_OUTPUT_MD=/tmp/sc007_009_validation_volume.md \
SOUND_CHANGE_COVERAGE_REPORT_MD=/tmp/sc007_009_validation_coverage.md \
python3 Germanic/docs/assembly/build_sound_change_volume.py

rm -f /tmp/sc007_009_validation_volume.md /tmp/sc007_009_validation_coverage.md
```

Result:

1. Passed.
2. The temporary build wrote a consistent assembled sound-change register after the SC007 and SC008 manifest/scaffold additions.

### Manual style check for unmanifested SC009

Commands:

```bash
grep -n "^#### " \
  Germanic/docs/sound_changes/change_reports/full/007-pwgmc-final-or-lowering.md \
  Germanic/docs/sound_changes/change_reports/full/008-pwgmc-coronal-w-assimilation.md \
  Germanic/docs/sound_changes/change_reports/full/009-pwgmc-ij-contraction.md

grep -n "reader-facing\|promot\|workflow\|project\|scaffold\|assembled\|book-facing" \
  Germanic/docs/sound_changes/change_reports/full/007-pwgmc-final-or-lowering.md \
  Germanic/docs/sound_changes/change_reports/full/008-pwgmc-coronal-w-assimilation.md \
  Germanic/docs/sound_changes/change_reports/full/009-pwgmc-ij-contraction.md
```

Result:

1. All three reports keep the required section order.
2. The style-tripwire grep is now clean.

## Scope confirmations

1. No reader-facing chapters were created.
2. No local section 17 was created.
3. No FST rules were changed.
4. No lexical TSV data were changed.

## Handoff for the next task

Because `SC007` and `SC008` are now promoted while `SC009` is not, the next task should be to add only the promoted rules to reader-facing prose and create **local section 17** around `SC007` and `SC008`, while continuing to leave `SC009` out.

# SC002-SC003 chronology validation 01 report

## Heavy TSV files inspected

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_failures.tsv`

## First-break results

### SC002 earlier

1. Result: `no_break_before_boundary`
2. Current order: `2`
3. Boundary reached: start of the tested historical chain at order `2`
4. Historical status: boundary-only / non-positive
5. Notes: no earlier swap exists inside the temporary early-rule harness beyond the excluded support/input stage `SC001 EnglishProtoInput`

### SC002 later

1. Result: `first_break_found`
2. First break order: `93`
3. Crossed stage: `SC094` Old English Remove Stars
4. Crossed stage type: `orthography_surface`
5. Historical status: non-historical computational break
6. Representative failures: `dream`, `team`
7. Exact wrong outputs captured:
   - `*dráugmaz` -> expected `drēam`, variant `drēagm`
   - `*táugmaz` -> expected `tēam`, variant `tēagm`

### SC003 earlier

1. Result: `no_break_before_boundary`
2. Last safe order: `2`
3. Crossed stage before boundary: `SC002` Gm Simplification
4. Historical status: boundary-only / non-positive
5. Notes: SC003 moves earlier safely across SC002, then reaches the left edge of the tested historical chain with no real break

### SC003 later

1. Result: `first_break_found`
2. First break order: `44`
3. Crossed stage: `SC044` OE Breaking
4. Crossed stage type: `historical_sound_change`
5. Historical status: real one-sided historical boundary, broad/far rather than tightly local
6. Representative failures: `learn`, `learn (3sg)`, `learn (iptv.2sg)`, `meed`
7. Exact wrong outputs captured:
   - `*líznōjaną` -> expected `liornian`, variant `lirnian`
   - `*líznōθi` -> expected `liornaþ`, variant `lirnaþ`
   - `*líznô` -> expected `liorna`, variant `lirna`
   - `*mízdai` -> expected `meorde`, variant `merde`

## Validated chronology cards

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC002-pgmc-gm-simplification.md` was rewritten from draft status to validated `first_break_complete`.
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC003-pgmc-rhotacism.md` was rewritten from draft status to validated `first_break_complete`.
3. Both cards now cite the real early-rule summary, changes, and failures TSVs.

## Reports and dossiers updated

Updated:

1. `Germanic/docs/sound_changes/change_reports/full/002-pgmc-gm-simplification.md`
2. `Germanic/docs/sound_changes/change_reports/full/003-pgmc-rhotacism.md`
3. `Germanic/docs/sound_changes/literature_dossiers/002-pgmc-gm-simplification.dossier.md`
4. `Germanic/docs/sound_changes/literature_dossiers/003-pgmc-rhotacism.dossier.md`
5. `Germanic/docs/sound_changes/book_dossiers/002-pgmc-gm-simplification.book-dossier.md`
6. `Germanic/docs/sound_changes/book_dossiers/003-pgmc-rhotacism.book-dossier.md`

The draft-only chronology language was replaced with the actual validated results. Remaining source-support and stage-label cautions were preserved.

## Manifest update

1. `Germanic/docs/sound_changes/change_reports/report_manifest.tsv` was **not** updated.

### Remaining blockers

#### SC002

1. The validated chronology card still yields no ordinary historical boundary: the earlier side is only the start boundary of the tested chain, and the later side breaks only at non-historical `SC094` Old English Remove Stars.
2. The source base remains narrow and mainly etymological rather than a broader phonological discussion.
3. SC002 is therefore still not strong enough for manifest promotion.

#### SC003

1. The chronology layer is now good enough for backend use, but the stage-label review remains unresolved: the strongest literature still pushes toward a later West Germanic / Northwest Germanic framing than the inventory's simple `Proto-Germanic` label.
2. Because that historical placement question is still open, SC003 was left out of the manifest in this pass.

## Checks run

### Report style audit

Command:

```bash
python3 Germanic/tools/audit_sound_change_report_style.py
```

Result:

1. Passed for the current manifest-backed report set.
2. As expected, this automated audit still scopes itself to the manifest-backed rows and therefore does not automatically include the still-unmanifested SC002/SC003 reports.

### Manifest/scaffold consistency check

Command:

```bash
SOUND_CHANGE_VOLUME_OUTPUT_MD=/tmp/sc002_003_validation_volume.md SOUND_CHANGE_COVERAGE_REPORT_MD=/tmp/sc002_003_validation_coverage.md python3 Germanic/docs/assembly/build_sound_change_volume.py
```

Result:

1. Passed.
2. This confirms that the unchanged manifest/scaffold/index layer remains internally consistent after the SC002/SC003 chronology-card rewrite.

## Scope confirmations

1. No reader-facing chapters were created.
2. Production FST files were not changed.
3. The heavy SC002-SC003 first-break computation was not rerun.

## Next recommended backend step

1. Resolve the SC003 stage-label review so the report can either remain cautiously `Proto-Germanic` or be relabeled more explicitly.
2. Broaden SC002's source base beyond the current lexical-etymological evidence.
3. After that, make a small coordinated left-edge promotion pass for whichever of SC002 and SC003 is then genuinely ready, including any necessary manifest/scaffold updates.

# SC004-SC006 chronology validation 01 report

## Heavy TSV files inspected

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv`

## First-break results

### SC004 earlier

1. Result: `no_break_before_boundary`
2. Current order: `4`
3. Boundary reached: left edge of the tested expanded-PWGmc chain at order `4`
4. Historical status: boundary-only / non-positive
5. Notes: SC004 is already the first rule in the expanded-PWGmc profile, so no earlier move exists within that tested chain

### SC004 later

1. Result: `first_break_found`
2. First break order: `36`
3. Crossed stage: `SC036` OE Inter Stress Raising
4. Crossed stage type: `historical_sound_change`
5. Historical status: real one-sided historical boundary, broad/far rather than tightly local
6. Representative failures: `soul`
7. Exact wrong-output diagnostics:
   - `*sáiwalō` -> expected `sāwol`, variant `sāwel`

### SC005 earlier

1. Result: `no_break_before_boundary`
2. Last safe order: `4`
3. Crossed stage before boundary: `SC004` PWGmc Ai Monophthongization
4. Historical status: boundary-only / non-positive
5. Notes: SC005 moves earlier safely across SC004, then reaches the left edge of the tested expanded-PWGmc chain with no real break

### SC005 later

1. Result: `first_break_found`
2. First break order: `17`
3. Crossed stage: `SC017` NWGmc U Lowering
4. Crossed stage type: `historical_sound_change`
5. Historical status: real one-sided historical boundary, broad/far rather than tightly local
6. Representative failures: `shoulder`
7. Exact wrong-output diagnostics:
   - `*skúldramiz` -> expected `sċuldrum`, variant `sċoldrum`

### SC006 earlier

1. Result: `no_break_before_boundary`
2. Last safe order: `4`
3. Crossed stage before boundary: `SC004` PWGmc Ai Monophthongization
4. Historical status: boundary-only / non-positive
5. Notes: SC006 moves earlier safely across SC005 and SC004, then reaches the left edge of the tested expanded-PWGmc chain with no real break

### SC006 later

1. Result: `first_break_found`
2. First break order: `34`
3. Crossed stage: `SC034` OE Aw Long Diphthong
4. Crossed stage type: `historical_sound_change`
5. Historical status: real one-sided historical boundary, broad/far rather than tightly local
6. Representative failures: `show (3sg)`
7. Exact wrong-output diagnostics:
   - `*skáwōθi` -> expected `sċēawaþ`, variant `sċēaweþ`

## Chronology cards created

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC004-pwgmc-ai-monophthongization.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC005-nwgmc-a-to-u-before-m.md`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC006-pwgmc-early-i-apocope.md`

All three now use validated `first_break_complete` status and cite the real expanded-PWGmc TSV family.

## Backend reports, literature dossiers, and book dossiers updated

Updated:

1. `Germanic/docs/sound_changes/change_reports/full/004-pwgmc-ai-monophthongization.md`
2. `Germanic/docs/sound_changes/change_reports/full/005-nwgmc-a-to-u-before-m.md`
3. `Germanic/docs/sound_changes/change_reports/full/006-pwgmc-early-i-apocope.md`
4. `Germanic/docs/sound_changes/literature_dossiers/004-pwgmc-ai-monophthongization.dossier.md`
5. `Germanic/docs/sound_changes/literature_dossiers/005-nwgmc-a-to-u-before-m.dossier.md`
6. `Germanic/docs/sound_changes/literature_dossiers/006-pwgmc-early-i-apocope.dossier.md`
7. `Germanic/docs/sound_changes/book_dossiers/004-pwgmc-ai-monophthongization.book-dossier.md`
8. `Germanic/docs/sound_changes/book_dossiers/005-nwgmc-a-to-u-before-m.book-dossier.md`
9. `Germanic/docs/sound_changes/book_dossiers/006-pwgmc-early-i-apocope.book-dossier.md`

The old “no validated chronology card exists yet” wording was replaced with the actual SC004-SC006 results.

## Manifest promotion decisions

### SC004

**Promoted.**

Reason:

1. The chronology card is validated and now gives a real one-sided historical boundary at `SC036` via `soul`.
2. The source layer is not perfect for the full CAPR packaging, but the report now states that caution explicitly and keeps the stronger support on the unstressed and word-final side visible.
3. That scope caution is acceptable for a short singleton note.

### SC005

**Not promoted.**

Exact blockers:

1. The chronology card is validated, but the stage-label / `needs_human_review` issue remains unresolved.
2. The source layer still fits a wider North/West-Germanic inflectional development at least as well as a narrowly Northwest-Germanic singleton.
3. The current support is heavily morphological and only lightly lexical, with `shoulder` as the sole compact-trace witness.
4. Those cautions were preserved explicitly rather than smoothed away.

### SC006

**Promoted.**

Reason:

1. The chronology card is validated and now gives a real one-sided historical boundary at `SC034` via `show (3sg)`.
2. The source support remains solid, especially for the suffixal anti-umlaut logic and the `geoguþ` family.
3. The remaining caution is one of scale and witness distribution, not of historical existence, so a short singleton note is acceptable.

## Manifest, scaffold, and indexed-summary updates

Updated:

1. `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`
2. `Germanic/docs/sound_changes/change_reports/sound_change_half_scaffold.tsv`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
4. `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
5. `Germanic/docs/sound_changes/book_dossiers/sound_change_book_dossier_inventory.tsv`

Result:

1. `SC004` and `SC006` were added to the manifest-backed backend layer.
2. `SC005` was intentionally left out.

## Checks run and results

### Report style audit

Command:

```bash
python3 Germanic/tools/audit_sound_change_report_style.py
```

Result:

1. Passed.
2. Because `SC004` and `SC006` are now manifest-listed, the automated audit covers them directly.

### Manifest/scaffold consistency check

Command:

```bash
SOUND_CHANGE_VOLUME_OUTPUT_MD=/tmp/sc004_006_validation_volume.md SOUND_CHANGE_COVERAGE_REPORT_MD=/tmp/sc004_006_validation_coverage.md python3 Germanic/docs/assembly/build_sound_change_volume.py
```

Result:

1. Passed.
2. The temporary build wrote `45` assembled sound-change units, confirming that the new manifest rows, scaffold rows, chronology index rows, and book-dossier inventory rows are internally consistent.

### Manual style check for still-unmanifested SC005

Because SC005 remains outside the manifest, it is not covered automatically by the report-style audit. A manual heading check confirmed that `Germanic/docs/sound_changes/change_reports/full/005-nwgmc-a-to-u-before-m.md` still follows the required section skeleton from `STYLE_STANDARD.md`:

1. `Historical formulation`
2. `Source tradition`
3. `CAPR implementation`
4. `Place in the cascade`
5. `Order evidence`
6. `Interpretation`
7. `Remaining cautions`

## Scope confirmations

1. No reader-facing chapters were created.
2. Production FST files were not changed.
3. TSV lexical data were not changed.
4. The heavy first-break computation was not rerun.

## Next recommended step

1. Revisit SC005 only after a focused stage-label review strong enough either to settle the `NWGmc` label or to justify a still more cautious replacement.
2. Once that is done, decide whether the early manifest-backed reader-facing programme should add `SC004` and `SC006` with a deliberate gap at `SC005`, or whether SC005 should be resolved first so the early section can move leftward more continuously.

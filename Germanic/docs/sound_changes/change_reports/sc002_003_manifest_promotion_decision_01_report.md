# SC002-SC003 manifest promotion decision 01 report

## Decision summary

1. **SC002** was **not promoted**.
2. **SC003** **was promoted** into the manifest-backed backend layer.

## SC002 status and decision

### Chronology status

1. The chronology card is now validated from real early-rule first-break TSVs.
2. The earlier side is boundary-only at the left edge of the tested historical chain.
3. The later side breaks only at `SC094` Old English Remove Stars.
4. That later break is computationally real but non-historical, because `SC094` is an orthography-surface support stage.

### Source-support status

1. Kroonen still provides the only explicit statement that both the `dream` and `team` families lost `*g` before `*m` [@Kroonen2013, pp. 101, 511].
2. Orel supports the `dream` family through `*draumaz` [@Orel2003, p. 114] and the `team` family through `*tauxmaz` [@Orel2003, p. 403], but that remains lexical corroboration rather than a broader phonological discussion of `*gm > *m`.
3. No broader handbook-style or comparative-grammar treatment of the change was recovered in this pass.

### SC002 decision

**Not promoted.**

### Exact reason

1. The validated chronology result still yields no ordinary historical first-break boundary.
2. The source base remains narrow and etymological rather than a fuller phonological discussion.
3. SC002 therefore remains **backend-preparation only**.

## SC003 status and decision

### Chronology status

1. The chronology card is now validated from real early-rule first-break TSVs.
2. The earlier side is boundary-only after a safe move across SC002 to order `2`.
3. The later side has a real one-sided historical break at `SC044` OE Breaking.
4. The exact wrong-output diagnostics remain:
   - `*líznōjaną` -> `lirnian` instead of `liornian`
   - `*líznōθi` -> `lirnaþ` instead of `liornaþ`
   - `*líznô` -> `lirna` instead of `liorna`
   - `*mízdai` -> `merde` instead of `meorde`
5. That later boundary is historically interpretable but broad/far rather than tightly local.

### Stage-label review result

The best-supported historical label is now:

**post-PWGmc West Germanic rhotacism**

Reason:

1. Ringe and Taylor explicitly place rhotacism in the **post-PWGmc** sound-change layer and state that it was not uniform within WGmc [@RingeTaylor2014, pp. 98, 102].
2. They also note earlier that the change occurred independently in Norse and in WGmc [@RingeTaylor2014, p. 52].
3. Crist likewise argues that the merger cannot be inherited from Proto-Northwest Germanic and must follow earlier WGmc `*z`-deletion rules [@Crist2001, pp. 104-106; @Crist2002, pp. 1, 4].

Accordingly:

1. the historical prose was revised to use a cautious post-PWGmc / West Germanic framing;
2. the CAPR rule name `PGmcRhotacism` was retained as an **implementation label only**.

### SC003 decision

**Promoted.**

### Why promotion is now acceptable

1. The chronology card is validated and historically interpretable on its later side.
2. The stage-label issue is now resolved cautiously enough for backend use.
3. The source report and dossier layers now distinguish clearly between:
   - the CAPR rule name `PGmcRhotacism`; and
   - the historical interpretation post-PWGmc West Germanic rhotacism.
4. Remaining cautions are explicit: the later `SC044` boundary is broad/far, and rhotacism must stay distinct from final `*z` deletion.

## Files updated

### SC002 documentation

1. `Germanic/docs/sound_changes/change_reports/full/002-pgmc-gm-simplification.md`
2. `Germanic/docs/sound_changes/literature_dossiers/002-pgmc-gm-simplification.dossier.md`
3. `Germanic/docs/sound_changes/book_dossiers/002-pgmc-gm-simplification.book-dossier.md`

### SC003 documentation

1. `Germanic/docs/sound_changes/change_reports/full/003-pgmc-rhotacism.md`
2. `Germanic/docs/sound_changes/literature_dossiers/003-pgmc-rhotacism.dossier.md`
3. `Germanic/docs/sound_changes/book_dossiers/003-pgmc-rhotacism.book-dossier.md`
4. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC003-pgmc-rhotacism.md`

### Manifest/scaffold/index support

1. `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`
2. `Germanic/docs/sound_changes/change_reports/sound_change_half_scaffold.tsv`
3. `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
4. `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
5. `Germanic/docs/sound_changes/book_dossiers/sound_change_book_dossier_inventory.tsv`

### Decision report

1. `Germanic/docs/sound_changes/change_reports/sc002_003_manifest_promotion_decision_01_report.md`

## Manifest update

1. `report_manifest.tsv` **was updated**.
2. Added row: `003 | West Germanic rhotacism | SC003 | full/003-pgmc-rhotacism.md | full`
3. `SC002` was intentionally left out.

## Checks run and results

### Report style audit

Command:

```bash
python3 Germanic/tools/audit_sound_change_report_style.py
```

Result:

1. Passed.
2. Because the audit scopes itself to manifest-backed rows, the promoted SC003 report is now covered automatically.

### Manifest/scaffold consistency check

Command:

```bash
SOUND_CHANGE_VOLUME_OUTPUT_MD=/tmp/sc002_003_promotion_volume.md SOUND_CHANGE_COVERAGE_REPORT_MD=/tmp/sc002_003_promotion_coverage.md python3 Germanic/docs/assembly/build_sound_change_volume.py
```

Result:

1. Passed.
2. The temporary build wrote `43` assembled sound-change units, confirming that the new SC003 manifest row, scaffold row, chronology index row, and book-dossier inventory row are internally consistent.

### Manual style check for still-unmanifested SC002

Because SC002 remains outside the manifest, it is not covered automatically by the report-style audit. A manual heading check confirmed that `Germanic/docs/sound_changes/change_reports/full/002-pgmc-gm-simplification.md` still follows the required section skeleton from `STYLE_STANDARD.md`:

1. `Historical formulation`
2. `Source tradition`
3. `CAPR implementation`
4. `Place in the cascade`
5. `Order evidence`
6. `Interpretation`
7. `Remaining cautions`

## Scope confirmations

1. No reader-facing chapters were created.
2. No production FST files were changed.
3. The heavy first-break computation was not rerun.

## Next recommended step

1. Leave SC002 parked until a broader phonological source discussion of `*g` loss before `*m` is recovered.
2. If SC002 remains weak, move on to the next backend-preparation tranche only after deciding whether the left-edge backend layer should continue with another singleton or with a grouped early WGmc batch.

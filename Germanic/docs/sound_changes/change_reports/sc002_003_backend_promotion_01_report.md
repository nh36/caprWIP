# SC002-SC003 backend promotion 01 report

## Files created

### Source reports

1. `Germanic/docs/sound_changes/change_reports/full/002-pgmc-gm-simplification.md`
2. `Germanic/docs/sound_changes/change_reports/full/003-pgmc-rhotacism.md`

### Literature dossiers

1. `Germanic/docs/sound_changes/literature_dossiers/002-pgmc-gm-simplification.dossier.md`
2. `Germanic/docs/sound_changes/literature_dossiers/003-pgmc-rhotacism.dossier.md`

### Book dossiers

1. `Germanic/docs/sound_changes/book_dossiers/002-pgmc-gm-simplification.book-dossier.md`
2. `Germanic/docs/sound_changes/book_dossiers/003-pgmc-rhotacism.book-dossier.md`

### Chronology cards

1. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC002-pgmc-gm-simplification.md`
2. `Germanic/docs/sound_changes/order_tests/chronology_cards/SC003-pgmc-rhotacism.md`

### Audit

1. `Germanic/docs/sound_changes/change_reports/sc002_013_promotion_audit_01.md`

## Chronology-card status

1. No validated chronology cards already existed for SC002 or SC003.
2. Both chronology cards were created in this pass as **draft cards needing validation**.
3. The draft cards record the same current limitation: `order_sensitivity_first_break_batch_04_manifest.tsv` marks SC002 and SC003 as skipped because the runner does not yet reorder inside bundles or non-explicit chain positions.

## Manifest update

1. `Germanic/docs/sound_changes/change_reports/report_manifest.tsv` was **not** updated.

### Why the manifest was not updated

1. SC002 and SC003 still lack validated chronology/order-test evidence.
2. SC002 currently has only lexical/etymological source support and still needs a broader phonological discussion before it is strong enough for manifest promotion.
3. SC003 has much stronger source support, but its current `Proto-Germanic` stage label needs review against the literature before it should be treated as manifest-ready.
4. Because the chronology layer is still draft-only, neither row should yet be added with `STATUS=full`.

## Style-audit result

Command run:

```bash
python3 Germanic/tools/audit_sound_change_report_style.py
```

Result:

1. The manifest-backed report set still passes the current style audit.
2. Because SC002 and SC003 were **not** added to `report_manifest.tsv`, the audit script did not automatically include them.
3. The two new SC002/SC003 reports were drafted to the same fixed section order and report shape required by `Germanic/docs/sound_changes/change_reports/STYLE_STANDARD.md`.

## Remaining source and citation gaps

### SC002

1. Current support is mainly lexical and etymological: Kroonen on `*draugma-` / `*taugma-`, plus Orel on the dream family.
2. A broader comparative or handbook-style discussion of `*gm > *m` still needs to be found.
3. The `team` witness is lexically supported, but the source base is still narrow.

### SC003

1. The phenomenon itself is well supported by Hogg, Ringe and Taylor, and Crist.
2. The stage label still needs review, since Ringe and Taylor place the relevant rhotacism more cautiously than the inventory currently does.
3. A fuller backend pass should decide whether the inventory label remains acceptable or needs refinement before manifest entry.

## Remaining chronology/order-test gaps

1. SC002 needs explicit order-test infrastructure that can reorder it independently of the bundled Proto-Germanic consonant block.
2. SC003 needs the same.
3. Until such tests exist, no validated earlier/later boundaries or wrong-output diagnostics can be claimed.

## Next recommended backend promotion batch

1. `SC004-SC006` is the next safest backend batch.
2. SC004, SC005, and SC006 are already adjacent in the early Proto-West-Germanic zone, and none requires reader-facing prose yet.
3. SC005 should be carried forward with its existing `needs_human_review=yes` caution.

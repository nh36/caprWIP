# Production exception note — 2120 march / mearc

## Why batch 10 skipped the row

`production_batch_10_report.md` records that row `2120 march / mearc` was
skipped because the verified backlog `SOURCE_MATERIAL_PATHS` list contains a
filename/path problem: it points to
`dev_notes_slices/2120-marrow-mearg.md`, which is not a clean row-local march
file.

## Current source-material status

The correct row-local march material is **partly identifiable** from existing
files:

- `Germanic/docs/lexeme_reports/packets/2120-march-mearc.md`
- `Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md`

Those two files clearly belong to row `2120 march / mearc` and treat the row as
the noun `mearc`, not the related verb `mearcian`.

The dev-note side is less clean:

- `Germanic/docs/lexeme_reports/dev_notes_slices/2120-marrow-mearg.md` exists,
  but its filename is misleading.
- Its current contents are a replacement note for row `2120 march / mearc`, not
  a straightforward row-local `march-mearc` slice.

## What a future human pass should check

1. Confirm whether the misnamed dev-note slice should be replaced by a correctly
   named `2120-march-mearc` slice before drafting.
2. Confirm that the packet and research memo remain the intended row-local
   drafting basis.
3. Keep noun `mearc` distinct from related verb `mearcian` and from unrelated
   `mearg` material when the row is eventually drafted.

## Status of this cleanup pass

- No model entry was created for `2120` in this cleanup pass.
- The source identity is clear enough to justify a **separate future drafting
  task**, but this pass documents the exception rather than silently promoting it
  into a full model entry.

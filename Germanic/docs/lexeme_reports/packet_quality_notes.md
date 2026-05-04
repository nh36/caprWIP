# Packet quality notes

These evidence packets use conservative matching rules.

1. **Row-ID hits must be explicit.** Valid row-ID evidence requires forms such as `row 1934`, `Row 1934`, `ID 1934`, `row_id 1934`, or a clearly labelled markdown/table column for TSV row IDs. Bare numbers at the start of a line must **not** be treated as row IDs, because they may be dates or other unrelated numerals.
2. **Exact-pair hits must name both forms independently.** A packet only treats an `exact pair` hit as high-confidence when the exact `PROTOFORM` and the exact current `COUNTERPART` both appear as standalone forms, not as substrings inside longer forms.
3. **Superseded targets are diagnostic, not high-confidence.** If a hit mentions the current row’s `PROTOFORM` but also says `expected X` or `target X`, and `X` is not the current `COUNTERPART`, that hit should be classified as possibly stale or diagnostic evidence.

The goal is to avoid promoting outdated development notes or date-like numerals into high-confidence lexical evidence.

# Full lexical assembly alpha 02 report

## Summary

- Part headings now start on new pages in the regenerated PDF.
- Bold-form cleanup was implemented in the full assembly transformer.
- The malformed ten emphasis is fixed: the assembled output now reads cleanly as
  _\*tḗon_, written _tēon_.
- Markdown, TeX, and PDF were regenerated.
- Original model entries were not edited.

## Page-break changes

- Inserted raw LaTeX `\clearpage`.
- It is inserted immediately before every catalogue `## Part ...` heading in
  `build_full_lexical_volume.py`.
- All seven Parts were checked in the PDF. The part openings now begin on fresh
  pages:
  - Part I — page 2
  - Part II — page 44
  - Part III — page 48
  - Part IV — page 84
  - Part V — page 114
  - Part VI — page 117
  - Part VII — page 120

## Bold/emphasis cleanup

- The previous transformation used a brittle bold-demotion regex,
  `\*\*([^*]+)\*\*`, which could not handle bold spans containing reconstructed
  forms with internal `*`. In practice, that let some bold wrappers survive and
  also let the matcher mis-pair across nearby bold form spans.
- The transformation now uses a non-greedy single-line bold matcher and two
  assembly-stage checks:
  - unwrap bold spans that contain linguistic inline-code forms before inline-code
    conversion;
  - unwrap any leftover bolded linguistic markup after inline-code conversion.
- Inline-code handling was also widened to accept multiline backtick spans and
  normalize internal line breaks to spaces before converting them to ordinary
  italic linguistic forms.
- Bold text that does **not** look like linguistic form markup is left untouched.
  This pass therefore fixes form styling without rewriting non-form prose
  emphasis.

## Specific entry checks

- ten — OE tēon:
  - fixed
  - assembled Markdown now reads: _\*tḗon_, written _tēon_
  - PDF text extraction confirms the same clean phrase on page 45
- three — OE þrīe:
  - fixed
  - the formerly bolded forms now appear as ordinary italic forms in assembled
    Markdown
  - the derivational sentence now reads cleanly as _\*θréjez_ ... _þrīe_ and
    _\*θrije > \*θriie > þrīe_
- stem — OE stefn:
  - fixed
  - the formerly bolded forms now appear as ordinary italic forms in assembled
    Markdown
  - the derivational sentence now reads cleanly as _\*stéβn_, written _stefn_

## Output inspection

- PDF produced: **yes**
- page count: **126**
- citation links still present: **yes** (`1043` link annotations detected)
- bibliography still present: **yes**
- Unicode still OK: **yes**
- trace boxes still OK: **yes** (`147` boxed traces emitted in TeX)

## Remaining issues

- No page-break regressions were found after the `\clearpage` insertion.
- No obvious malformed emphasis artifacts remain in the assembled Markdown or TeX
  for the audited patterns (`**_`, `_**`, `__`, raw backtick form spans,
  `\textbf{\emph`, `\emph{\textbf`).
- Non-form prose emphasis can still remain where the source entry used it; this
  pass intentionally did not rewrite philological prose.
- LaTeX log capture is still not preserved automatically by the Docker wrapper, so
  overfull-box diagnostics are not yet collected in a durable artifact.

## Recommendation

**A. Alpha 02 style fixes are successful; proceed to broader visual/style review.**

## Scope confirmation

- no model-entry prose or metadata was edited
- no TSV, FST, `report_manifest.tsv`, compact trace, packet, dev-note, research
  memo, bibliography, OCR/reference, or citation-locator report files were edited
- changes were limited to the assembly script, regenerated full-alpha outputs, and
  this report

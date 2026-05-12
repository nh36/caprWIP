# Assembly pilot 08 report

## Summary

- Craft tilde issue confirmed: **yes**
- Craft model/support files changed: **yes**
- Other adjacent-starred-form candidates found: **2**
- Other candidates changed: **1**
- `link-citations: true` or equivalent metadata added: **yes**
- `pilot_assembled.md` regenerated: **yes**
- `pilot_assembled.tex` regenerated: **yes**
- `pilot_assembled.pdf` regenerated: **yes**
- Original model entries beyond confirmed mechanical fixes edited: **no**

## Tilde / separator audit

The craft entry had a genuine separator defect in current model-entry prose. The model entry said `Orel prints *kraftiz *kraftuz`, but the local evidence stack already preserved the intended pairing with a separator:

- the row-local research memo note records `Orel: *kraftiz ~ *kraftuz`
- the aligned TSV note records the same `*kraftiz ~ *kraftuz`
- the pilot/debug traces also preserve the same paired notation

Accordingly, the craft model entry was corrected to `*kraftiz ~ *kraftuz`. The craft source ledger was updated to match, and the paired implementation report now records the cleanup.

The separator audit over current `.model.md` prose found two additional adjacent-starred-form candidates:

1. **2168 sap / sæp** — **changed**
   - The model entry had `*sapōn *sapan`.
   - The row-local memo explicitly records Orel as `*sapōn ~ *sapan`.
   - The packeted quotation and DEV_NOTES slice also preserve the `~` form.
   - The model entry and source ledger were normalized to `*sapōn ~ *sapan`, and the implementation report records the cleanup.

2. **1959 bottom / botm** — **reviewed but not changed**
   - The model entry has `*budmaz *butmaz`.
   - The local Orel reference extract also appears as bare adjacency, and the row-local memo does not independently preserve a clearer separator.
   - Because the intended separator was not locally clear enough, this case was left unchanged in this pass.

No broad prose rewrite was performed. Only confirmed mechanical separator fixes were made.

## Citation hyperlink test

The pilot metadata was updated by adding:

- `link-citations: true`

No broader hyperlink styling pass was added. The build scripts were left unchanged.

Verification result: **citations are now live internal PDF links** in the rebuilt pilot PDF.

This was verified in two ways:

1. The generated LaTeX shows citation keys and bibliography entries wired through matching reference IDs, e.g. `\citeproc{ref-Kroonen2013}{...}` and `\bibitem{ref-Kroonen2013}`.
2. Direct PDF inspection with `pypdf` found **66** `/Link` annotations with internal `/GoTo` actions targeting citation destinations such as:
   - `cite.ref-Kroonen2013`
   - `cite.ref-Orel2003`
   - `cite.ref-ClarkHall1960`
   - `cite.ref-BosworthToller1898`

That confirms that in-text citations are clickable links to the bibliography layer under the current Pandoc/XeLaTeX build path.

## PDF inspection

The rebuilt pilot renders acceptably in the inspected output.

- **Craft** now displays `*kraftiz ~ *kraftuz` correctly in the PDF.
- The tilde survives Markdown -> LaTeX -> PDF rendering cleanly, with no obvious spacing or escaping artifact.
- The boxed derivation traces still render.
- The generated derivation summaries still render.
- The bibliography still appears.
- Unicode still renders correctly.

The craft page specifically shows:

- the generated summary unchanged in structure
- the boxed derivation trace intact
- the prose sentence `Orel prints *kraftiz ~ *kraftuz`
- working in-text citations on that page, including the Kroonen and Orel citations

## Remaining issues

- `1959 bottom / botm` remains a reviewed adjacent-starred-form case without change, because the intended separator is not yet clear enough from the local evidence.
- Citation links are now live, but no separate visual styling pass has been done; links remain under Pandoc's default hidden-link PDF behavior.
- No trace-box regression was observed.
- No citation-rendering regression was observed.

## Recommendation

**Decision: A. Cleanup successful; proceed to book architecture and class-based assembly design.**

This pass resolved the confirmed mechanical separator defects that had strong local support and successfully enabled live citation links in the pilot PDF without disturbing the current layout work.

## Scope confirmation

- No TSV source data, FST files, manifest files, compact trace files, packets, dev-note slices, research memos, bibliography files, OCR/reference files, or citation-locator reports were edited.
- Changes were limited to confirmed mechanical model/support corrections, pilot metadata, regenerated pilot outputs, and this report.

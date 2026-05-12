# Assembly pilot 04 report

## Summary

- Trace-table layout changed: **yes**
- Semicolon-joined trace cells removed from both sides: **yes**
- `pilot_assembled.md` regenerated: **yes**
- `pilot_assembled.tex` regenerated: **yes**
- `pilot_assembled.pdf` regenerated: **yes**
- Original model entries edited: **no**

## Trace-table rendering change

The old pilot-03 layout collapsed each trace-table cell into one semicolon-joined string. That made both columns read like compressed prose rather than as stepwise derivations.

The new layout rewrites each compact-trace cell into aligned change/form rows and renders the derivation trace as a four-column Markdown table:

| Earlier Germanic change | Form | Old English change | Form |
| :--- | :--- | :--- | :--- |
| ... | ... | ... | ... |

Each side is now parsed independently from the compact trace source's `<br>`-separated content, then aligned by row order. If one side has fewer steps than the other, the remaining cells on that side are left blank.

Stage labels are preserved in two ways:

1. Stages with no change remain explicit rows such as `Proto-West Germanic | [no change]`.
2. Stages with actual changes keep the stage label on the first change row for that stage, e.g. `Northwest Germanic: OE Ws Palatal Glide | *jéugunθ` and `Old English: Anglo Frisian Brightening | *θístilæs`.

This keeps stage structure visible without collapsing either side back into semicolon-separated prose.

## PDF inspection

The regenerated PDF shows the derivation trace near the top of each inspected entry, with the trace steps split into aligned change/form rows on both sides.

Specific checks:

1. **bake**: the Old English side now shows separate rows for `Anglo Frisian Brightening`, `OE A Restoration`, `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, and `OE Weak Tail Reduction`, each with its own form cell.
2. **bow / bēag**: the Old English side now shows `OE Au Fronting` and `OE Diphthong Leveling` as separate rows, not a joined string.
3. **thistle / þistles**: the Old English side now renders as aligned change/form rows equivalent to:
   - `Old English: Anglo Frisian Brightening` -> `*θístilæs`
   - `OE L Adjacent Syncope` -> `*θístlæs`
   - `OE Unstressed AE Merger` -> `*θístles`
4. **weapon / wǣpn**: the trace shows `Northwest Germanic: NWGmc Long E Lowering` on the earlier-Germanic side and `Old English: OE Heavy Syllable Nasal Apocope` on the Old English side as separate aligned entries.
5. **youth / ġeoguþ**: the earlier-Germanic side now renders as aligned change/form rows equivalent to:
   - `Northwest Germanic: OE Ws Palatal Glide` -> `*jéugunθ`
   - `NWGmc Nasal Spirant Lengthening` -> `*jéugūnθ`
   - `NWGmc Nasal Spirant Loss` -> `*jéugūθ`
   The Old English side also remains split into separate rows for `OE Diphthong Leveling` and `OE Unstressed Long Vowel Shortening`.

Additional rendering checks:

- Forms remain in normal text font and are italic, not monospaced code.
- Citations and bibliography still render.
- Unicode continues to render correctly in the regenerated PDF.

## Remaining issues

- The trace tables are still somewhat cramped in PDF, especially when a stage-prefixed change label is long.
- Some long change labels wrap over multiple lines inside the change column.
- The four-column layout is readable, but wide enough that spacing and proportion tuning would still improve it.
- No inspected trace table side still uses semicolon-separated change strings.
- No obvious regression to monospaced code font or stray bolding appeared in the trace tables.

## Recommendation

**Decision: A. Trace-table layout is now acceptable; proceed to one more general pilot style pass.**

The core trace-table problem is fixed: both sides now show one change per row with aligned form cells, and the inspected PDF examples for bake, bow, thistle, weapon, and youth all behave as intended. What remains is a broader style/tightness pass, not another trace-parser redesign.

## Scope confirmation

- No original model entries were changed.
- No TSV source data, FST files, manifest files, packets, dev-note slices, research memos, bibliography files, OCR/reference files, or citation-locator reports were edited.
- Changes were limited to `Germanic/docs/assembly/build_pilot.sh`, regenerated pilot outputs (`pilot_assembled.md`, `pilot_assembled.tex`, `pilot_assembled.pdf`), and this report.

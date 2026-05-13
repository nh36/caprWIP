# Full lexical assembly alpha 05 report

## Summary

- mixed inline-code typography was fixed at assembly level
- language/stage labels now remain roman in mixed linguistic spans
- linguistic forms remain italic in both pure-form and mixed spans
- Earlier Germanic trace wrapping was improved with wider label columns, a
  smaller central gutter in heavy cases, and selective no-break handling for
  short-ish long labels
- Markdown, TeX, and PDF were regenerated
- original model entries were not edited

## Inline-code typography

- The old problem was that `convert_inline_code()` treated non-code backtick
  spans too coarsely. Mixed spans such as `PNWGmc *brokiz > *breeci > OE bréc`
  could come through as if the whole span were one italic form, which wrongly
  italicized language/stage labels.
- The new assembly behavior is token-aware:
  - it preserves separators such as spaces, `>`, `~`, `/`, `,`, `;`, and `:`
  - it recognizes stage/language labels and leaves them roman
  - it italicizes only tokens identified as linguistic forms
- Labels kept roman include:
  - `PGmc`, `PWGmc`, `PNWGmc`, `NWGmc`, `WGmc`, `OE`, `WS`, `LWS`,
    `Anglian`, `West Saxon`, `Old English`, `Proto-Germanic`,
    `West Germanic`, and `Northwest Germanic`
- Forms are identified conservatively:
  - starred forms are italicized
  - tokens with OE/reconstructed diacritics are italicized
  - lowercase form tokens immediately after labels or derivational separators
    are italicized
  - connector words such as `and`, `or`, `from`, `to`, `through`, and `with`
    stay roman
- The representative `PNWGmc *brokiz > *breeci > OE bréc` pattern was checked in
  the regenerated prose via the breeches entry’s cited Ringe-Taylor chain
  (`PNWGmce *brokiz > *breeci > OE bréc` in the local source wording). The stage
  labels remain roman and only the forms are italic.
- A scan of the assembled Markdown found no ordinary-prose cases such as
  `_PNWGmc_`, `_PGmc_`, `_PWGmc_`, `_NWGmc_`, `_OE_`, `_Old English_`,
  `_West Germanic_`, or `_Proto-Germanic_`.

## Trace-box layout

- The old alpha-04 problem was asymmetrical: the Old English side had improved,
  but Earlier Germanic labels such as `NWGmc Final Long O Raising`,
  `PGmc Final Z Deletion`, and `NWGmc U Lowering` could still wrap sooner than
  they should.
- The updated layout keeps the compact paired structure from alpha 04, but
  changes width choice more symmetrically:
  - long-label awareness now explicitly includes `PGmc Final Z Deletion` and
    `NWGmc U Lowering`
  - heavy cases shrink the central gutter before forcing a short-ish label wrap
  - balanced heavy/heavy cases now give both sides wider usable widths
  - light/heavy cases now bias more strongly toward the heavy side
- Within each side, label columns were widened further and form columns narrowed
  slightly so label/form pairs stay close instead of drifting apart.
- Short-ish long labels now use a selective no-break wrapper:
  - `OE High Vowel Apocope`
  - `NWGmc Final Long O Raising`
  - `NWGmc Long E Lowering`
  - `PGmc Final Z Deletion`
  - `NWGmc U Lowering`
- Extra horizontal space still lives primarily in the middle gutter rather than
  between a change name and its resulting form.

## Specific PDF checks

- stem / stefn — page 72
  - `NWGmc Final Long O Raising` is now emitted as a protected single-line label
    and remains a compact pair with `*stébnu`
  - `PGmc B Allophony` and `OE High Vowel Apocope` remain visually close to
    `*stéβnu` and `*stéβn`
- three / þrīe — page 45
  - `PGmc Final Z Deletion` now stays a compact left-side pair with `*θréje`
  - Old English rows remain clean
- wasp / wæfs — page 46
  - `PGmc Final Z Deletion` now stays a compact left-side pair with `*wábsa`
  - the Old English sequence remains readable as close label/form pairs
- knob / cnobba — page 115
  - `NWGmc U Lowering *knóbbô` now reads as a clear pair
  - `OE Unstressed Long Vowel Shortening *knóbba` is improved, though this
    longest OE-side label can still wrap in a tight box
- beech / bōc — page 3
  - `OE High Vowel Apocope *bōk` now remains a clear pair without unnecessary
    wrapping
- bier / bǣr — page 4
  - `NWGmc Final Long O Raising *bḗru`
  - `NWGmc Long E Lowering *bǣru`
  - `OE High Vowel Apocope *bǣr`
  - all now read as clear label/form pairs
- adder / nǣdre — page 2
  - `OE Unstressed Long Vowel Shortening *nǣdræ` is improved by the wider OE
    label column, though this longest OE-side label may still wrap
- bake / bacan — page 2
  - `OE Heavy Syllable Nasal Apocope *bakan` is improved and reads as a clear
    pair

## Regression checks

- `>` notation remains: **yes**
- Part page breaks remain: **yes**
- References page/heading remains: **yes**
- citation links remain: **yes**
- bibliography remains: **yes**
- Unicode and trace boxes remain OK: **yes**

## Remaining issues

- the longest OE-side labels, especially `OE Unstressed Long Vowel Shortening`,
  can still wrap in some tight boxes such as adder and knob
- `NWGmc Stressed Monosyllable O Raising` remains long enough that some
  monosyllabic boxes may still need human visual review
- no bad language-label italics remain in the assembled prose, but a broader
  full-book visual sweep is still worthwhile for any residual trace edge cases

## Recommendation

**B. Mostly successful; fix specified remaining style issues first.**

## Scope confirmation

- no model-entry prose or metadata was edited
- no TSV, FST, `report_manifest.tsv`, compact trace, packet, dev-note, research
  memo, bibliography, OCR/reference, or citation-locator report files were
  edited
- changes were limited to assembly scripts, regenerated outputs, and this report

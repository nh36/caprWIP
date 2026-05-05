# Research memo — 2055 handle / handlian

## Starting point

- **ID:** 2055
- **CONCEPT:** handle
- **COUNTERPART:** handlian
- **PROTO:** *xándlōjaną
- **PROTOFORM:** *xándlōjaną
- **DERIVATION_CLASS:** regular
- **NOTE:** `Du handelen / G handeln are the verb.`

The live row is a note-bearing `regular` entry with no existing pilot/full lexeme report. Its `HISTORY` already shows the core project issue: the row was previously the noun `handle` and was later corrected to the verb `handlian`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace, which now gives `*xándlōjaną -> handlian`; and the later `DEV_NOTES.md` passage at §17.32.7, which explicitly treats `xándlōjaną -> handlian` as one of the TSV’s accepted class-III→II refashioned verb transponents.
- **Useful background:** the packet preserves the row history that the OE target used to be the noun `handle`; its bibliography candidate `Kroonen2013` is sensible; and the note about Dutch `handelen` / German `handeln` correctly points to the verbal cognate set.
- **Stale or superseded:** the packet’s older `DEV_NOTES` hit at lines 2821-2836 is from an earlier stage where the row still expected noun `handle` and FST output `handleian`. That material is diagnostic project history, not current row authority.
- **Irrelevant or misleading:** the packet’s `old_english_wiktionary.tsv` hit (`handle -> handle`) is the noun, not the verb; and the generic analysis/dossier `concept name` hits are just keyword noise on the English word “handle,” not lexeme-specific evidence for row 2055.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/lexeme_reports/coverage_audit.md`, which flags row 2055 as report-worthy because `NOTE` is non-empty.
- `Germanic/data/germanic-aligned-final.tsv` around rows 531/532/2055/530, confirming that the aligned set is the verbal set `handelen / handle / handlian / handeln` and that only the OE row carries the correction note.
- `Germanic/data/oe_known_problems.tsv`, which has no matching entry.
- `Germanic/docs/lexeme_reports/pilot/`, where I found no existing pilot report for this lexeme.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` 18700-18708, which distinguishes noun `*xandlan/*xandlō` > OE `handle` from verbal `*xandlōjanan` > OE `handlian`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` 7784-7788 and 15496-15499, which give later West/Northwest Germanic background forms `*handulona`, `*handulon`, and pre-OE `*handuldjan` on the way to OE `handlian`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` 81917-81928 and `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` 20501-20505, which separately attest noun `handle` and verb `handlian`/`handllan`.
- A live `old_english.bin` probe, which confirms `*xándlōjaną -> handlian`; the later-stage background forms from Ringe-Taylor are not accepted as live TSV/FST inputs, and noun-like comparators such as `*xándlōn` instead yield `handle`.

I found no full dossier or analysis file specifically named in the packet or TSV note for this lexeme.

## Reconstruction and early-stage forms

This row only stays clear if three levels are kept separate.

1. **Cognate-set proto / etymological verb family:** TSV `PROTO = *xándlōjaną`, matching the broader West Germanic verbal set.
2. **Project input form:** TSV `PROTOFORM = *xándlōjaną`, which is the live transducer input and now derives `handlian` directly in the current FST.
3. **OE target form:** `handlian`, the OE verb the row is intended to represent.

Repo-local reference materials also preserve a deeper staging that should not be collapsed into the TSV input slot. Orel distinguishes noun `*xandlan/*xandlō` from verb `*xandlōjanan`, while Ringe-Taylor gives later stages `*handulona > *handulon > *handuldjan > OE handlian`. Those later forms are useful historical background for the OE development, but they are not the current project input, and the live FST does not accept them as row inputs.

That means the TSV note/history should not be read as if `*handulōną` and `*xándlōjaną` were interchangeable labels for the same modelling slot. They belong to different descriptive levels.

## Old English philology

Repo-local dictionary evidence supports a real OE verb `handlian` distinct from the noun `handle`.

- Bosworth-Toller gives both noun `handle` and verb `handlian`.
- Clark Hall likewise separates noun `handle` from verb `handllan`/`handlian`.
- `old_english_wiktionary.tsv` only contributes the noun `handle`, so it is not evidence for the corrected verbal row.

The safe claim, then, is that row 2055 targets the OE infinitive/citation form `handlian`, not the noun `handle`. I found no repo-local basis for stronger dialect or manuscript-specific claims, so any final report should avoid them.

## Project problem and solution

The project problem was not a live sound-law failure but a lexeme-selection error. An earlier version of the row treated the OE member of this cognate set as noun `handle`; current row history, current TSV data, and current trace output all supersede that and treat the set as verbal.

The project solution should therefore be:

- keep the OE `COUNTERPART` as verbal `handlian`;
- keep `PROTO = PROTOFORM = *xándlōjaną` as the current project transponent/input;
- treat noun `handle` as a separate OE lexeme with separate noun-level proto background;
- explain in the eventual report that later forms like `*handulon` / `*handuldjan` are historical background, not replacements for the live TSV input.

## Paradigm probe

No paradigm probe is required.

This is not a paradigm-cell dispute like a `late_analogy` row, and the memo’s main issue is noun-versus-verb identification rather than uncertainty between competing OE cells. The current evidence already establishes the needed distinction: the live row input yields verbal `handlian`, while noun comparators yield noun outputs such as `handle`.

## Recommended final report

Recommend a short final report explaining that row 2055 was correctly reassigned from noun `handle` to verb `handlian`, distinguishing the live TSV transponent `*xándlōjaną` from the later historical background forms (`*handulona/*handulon/*handuldjan`) and from the separate OE noun `handle`.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** change recommended. The note should say explicitly that the row is the OE verb `handlian` (not noun `handle`) and should distinguish the live project input `*xándlōjaną` from later background forms such as `*handulon` / `*handuldjan` rather than compressing them into one label.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** change recommended. The old class-II table at `DEV_NOTES.md` 2821-2836 still preserves the superseded `handleian -> handle` stage for this row and should be marked as stale or updated so future packets do not over-promote it.
- **Dossier text:** no change recommended; I found no row-specific dossier text to update.

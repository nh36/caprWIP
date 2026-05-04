# Research memo — 1969 breeches / brēċ

## Starting point

- **ID:** 1969
- **CONCEPT:** breeches
- **COUNTERPART:** brēċ
- **PROTO:** *brōkiz
- **PROTOFORM:** *brōkiz
- **DERIVATION_CLASS:** regular
- **NOTE:** `Proto: *brekăną→*brōkiz (Kroonen *brōk- f. 'breeches', nom.pl.; i-umlaut ō→ē)`

This is a note-bearing `regular` row, so `coverage_audit.md` correctly marks it as needing eventual lexeme-report coverage. I found no existing pilot or full lexeme report for `breeches / brēċ`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing `*brōkiz -> brēċ`; the current trace snapshots in `docs/debug_snapshots/oe_full_trace_report.txt` and `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md`; and `Germanic/data/old_english_wiktionary.tsv`, which lists `breeches -> brēċ`.
- **Useful background:** the packet is right to preserve the deeper etymological note that Kroonen connects the noun to the verbal base `*brekăną`; and its bibliography candidates (`Kroonen2013`, `Campbell1959`, `SieversBrunner1965`, `Luick1914`) are sensible starting points.
- **Stale or superseded:** the packet’s `DEV_NOTES` and analysis hits are generic `i-umlaut` keyword collisions, not row-specific evidence. They should not be treated as live dossier authority for row 1969.
- **Irrelevant or misleading if over-read:** treating `*brekăną` as the row’s direct derivational input would be misleading. In the live FST, `*brekăną` derives `brecan`, not `brēċ`, so it is etymological background for the noun family, not the current OE modelling input for this row.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/lexeme_reports/coverage_audit.md`, which flags row 1969 as report-worthy because `NOTE` is non-empty.
- `Germanic/data/oe_known_problems.tsv`, which has no entry for row 1969 or this lexeme.
- `Germanic/docs/lexeme_reports/pilot/`, where I found no existing pilot report for `breeches / brēċ`.
- `Germanic/data/germanic-aligned-final.tsv` around rows 1514-1516 and 1969, confirming that the aligned cognate set currently uses `*brōkiz` across German, Dutch, English, and Old English.
- `Germanic/data/old_english_wiktionary.tsv`, which confirms `brēċ`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` 5685-5688, where Kroonen gives `*brōk-` and notes OE `brōc` with plural `brēċ`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` 7953-7957, where Orel gives `*brōkz` with OE `bróc`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` 12048, which explicitly gives `PNWGmc *brokiz ... > *breeci > OE bréc`.
- `docs/references/bright_anglo_saxon_reader.vision.txt` 1590-1593, which lists `brōc ... pl. brēc`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` 7407-7408 and 7702, which give `brēc fp. breeches` and `broc I. f. (? only in pl. brēc, q.v.)`.
- Live probing against `old_english.bin`, which gives `*brōkiz -> brēċ`, `*brōkō -> brōc`, and `*brekăną -> brecan`.

I did **not** find any full dossier or analysis file specifically named in the packet or TSV note for this lexeme, and I found no row-specific `DEV_NOTES` section beyond the packet’s generic keyword hits.

## Reconstruction and early-stage forms

This row is easiest to handle if three levels are kept separate:

1. **Deeper etymological background:** the note’s `*brekăną`, i.e. the verbal base from which Kroonen says the breeches noun was formed.
2. **Project cognate-set proto and modelling input:** TSV `PROTO = PROTOFORM = *brōkiz`, the plural-based form the current aligned set actually feeds to the OE transducer.
3. **OE target form:** `brēċ`.

The main point is that the row is **not** currently modelling OE directly from `*brekăną`. The live binary shows that `*brekăną` yields `brecan`, whereas `*brōkiz` yields `brēċ`. So for this row, `*brekăną` belongs in historical explanation, not in the derivational input slot.

The reference files also support keeping the stem/headword and the project input distinct. Kroonen’s dictionary entry is a stem-like headword (`*brōk-`), Orel gives a citation-type noun form (`*brōkz`), and Ringe & Taylor give the plural pathway `*brokiz > *breeci > OE bréc`. Those are not contradictions so much as different descriptive levels. The live row’s `*brōkiz` works well as the project input because the row is targeting the plural OE outcome.

## Old English philology

Repo-local sources support `brēċ` as an **attested plural form**, not as a reconstructed convenience spelling.

- `old_english_wiktionary.tsv` lists `brēċ`.
- Bright gives `brōc ... pl. brēc`.
- Clark Hall gives `brēc fp. breeches` and explicitly notes `broc` as a feminine form possibly only represented in the plural `brēc`.

That means the row should be described as targeting the OE plural `brēċ`, not as if it were simply a singular citation headword. The lexicographic background does connect it with singular `brōc`, but the repo evidence checked here consistently makes the plural relationship explicit. I found no repo-local basis for a stronger dialect or manuscript claim, so the final report should avoid one.

## Project problem and solution

The main project issue here is explanatory clarity, not an unresolved sound-law failure.

Phonologically, the current row is in good shape: the live cascade and live binary both derive `*brōkiz -> brēċ`. The confusion comes from the note’s compact wording, which compresses three different things into one line:

- the deeper verbal ancestor `*brekăną`;
- the noun headword/stem `*brōk-`;
- the actual row input `*brōkiz`.

The project solution should therefore be:

- keep `COUNTERPART = brēċ`;
- keep `PROTO = PROTOFORM = *brōkiz`;
- keep `DERIVATION_CLASS = regular`;
- explain explicitly that the row models the plural noun input that yields OE plural `brēċ`, while `*brekăną` is background etymology only.

## Paradigm probe

No paradigm probe is required.

This is not a `late_analogy` or unresolved-cell case where the row stands or falls on comparing multiple competing OE paradigm cells. The checked sources already show the relevant philological distinction, and the live binary already confirms the modelling distinction: `*brōkō -> brōc` versus `*brōkiz -> brēċ`.

If a later final report wants a small illustrative probe, the only useful optional contrast would be singular `*brōkō` (or `*brōkz`) against plural `*brōkiz`. But that is explanatory garnish, not a missing evidential step.

## Recommended final report

Recommend a concise final report stating that row 1969 intentionally models OE plural `brēċ` from plural input `*brōkiz`, while treating `*brekăną` and stem-level `*brōk-` as deeper etymological background rather than as interchangeable row inputs.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended.** The note should distinguish the deeper etymology (`*brekăną` / stem-level `*brōk-`) from the actual modelling input (`*brōkiz`) and should say plainly that the row targets plural OE `brēċ`.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** no change recommended; I found no row-specific `DEV_NOTES` discussion to clean up, only generic keyword hits.
- **Dossier text:** no change recommended; I found no row-specific dossier text to update.

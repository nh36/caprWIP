# Research memo — 2071 help / helpan

## Starting point

- **ID:** 2071
- **CONCEPT:** help
- **COUNTERPART:** `helpan`
- **PROTO:** `*xélpaną`
- **PROTOFORM:** `*xélpaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `OE target: help→helpan (inf. of str.v. class III; noun 'help' is in *xelpō row)`

The live row is already basically sound. The main issue is not a failed derivation, but keeping the verbal row `helpan` separate from the noun row `help` / `*xélpō` and from packet material that surfaces the noun as background noise.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row and the packet's compact derivation trace, which gives the current row input `*xélpaną` and current output `helpan`.
- **Useful background:** the packet's `DEV_NOTES` carry-over at `21013-21018`, which explains why the infinitive ends up as `helpan`, and `21774-21779`, which shows that breve-marked `*xélpăną` versus plain `*xélpaną` makes no difference for this row's output.
- **Stale or superseded / diagnostic only:** the packet's `*xélpăną` comparison and the `*hólpaną` rule-discussion spelling are useful engineering diagnostics, but they are not better lexical authority than the live TSV `*xélpaną`.
- **Irrelevant or misleading:** the packet's `old_english_wiktionary.tsv` hit `help -> help` is low-authority and belongs to the separate noun row, not to row 2071's verbal infinitive. The generic concept-name hits in `DEV_NOTES` and the unrelated dossier snippet are also not row-specific evidence.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` around rows 2071-2072 and the related German/Dutch/English verbal rows, confirming that `helpan` belongs to verbal cognate set 395 while noun `help` belongs to separate `*xélpō` row 2072 / cognate set 131.
- `Germanic/data/oe_known_problems.tsv` (checked; no row-specific entry).
- `Germanic/docs/lexeme_reports/coverage_audit.md`, confirming that row 2071 requires a report because of its non-empty `NOTE` and has no pilot/full report yet.
- `Germanic/docs/lexeme_reports/source_inventory.md`, which explicitly warns that `old_english_wiktionary.tsv` is convenient but low-authority.
- `docs/debug_snapshots/oe_full_trace_report.txt`, which shows the current derivation surfacing `helpan`.
- `docs/references/bright_anglo_saxon_reader.txt`, which cites `helpan` as a case where `e` remains before `l + consonant`, and lists the strong-verb series `helpan / healp / hulpon / holpen`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` and `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`, both of which support `helpan` as an OE verb headword and distinguish it from noun `help`.

No separate full dossier, analysis memo, or pilot lexeme report for this lexeme was found in the repo, and none was named in the packet or TSV note.

## Reconstruction and early-stage forms

Three levels should be kept separate even though two of them coincide here:

1. **Cognate-set proto / etymological headword:** verbal `*xélpaną`.
2. **Project input form for row 2071:** also `*xélpaną`; this row is not being rescued by switching to a different paradigm cell or alternate lexical input.
3. **OE target form:** `helpan`, the Old English infinitive/citation form.

The breve-marked `*xélpăną` seen in debugging material is only a probe variant, and the `*hólpaną` spelling in the rule discussion is a stage-specific engineering illustration. Neither is a reason to rewrite TSV `PROTO` or `PROTOFORM` away from the current `*xélpaną`.

## Old English philology

Repo-local philology supports a straightforward lexical split:

- **Verb:** `helpan`, the infinitive/citation form of a strong verb, with class-III style ablaut forms `healp`, `hulpon`, `holpen` in the local reference material.
- **Noun:** `help`, a separate lexical item handled elsewhere in the TSV (`*xélpō`, row 2072).

That distinction matters more than anything else for this memo. The packet's lexical-table hit for `help` is not evidence against `helpan`; it is evidence for the neighboring noun row. `Bright` also gives a useful phonological control: before `l + consonant`, `e` remains in `helpan` rather than breaking to `eo`, which matches the current target. On current repo evidence, `helpan` is attested as a dictionary headword, but I found no row-specific need to make any dialect or manuscript claim beyond that [@ClarkHall1960].

## Project problem and solution

The project problem here is lexical disambiguation, not an unresolved sound-change failure. Because English gloss **help** can point either to the noun or the verb, packets easily surface noun evidence that looks relevant but is not.

The current project solution is correct:

- keep row 2071 as the **verbal** row with `COUNTERPART` `helpan` and verbal proto `*xélpaną`;
- keep noun `help` in the separate `*xélpō` row;
- treat debug spellings such as `*xélpăną` only as conditioning tests, not as superior lexical forms.

## Paradigm probe

A paradigm probe is **not required** for this row. The memo does not depend on choosing a hidden paradigm cell or rescuing a bad citation form: the live citation-form input already yields the intended OE infinitive `helpan`.

If the eventual final report wants a little extra philological color, an **optional** probe could compare the infinitive with class-III comparators such as preterite singular `healp`, preterite plural `hulpon`, and past participle `holpen`, but that is not needed to settle the row.

## Recommended final report

Recommend a short final report stating that row 2071 represents the attested OE verbal infinitive `helpan` from verbal `*xélpaną`, that the current derivation is already regular, and that noun `help` evidence in packets belongs to the separate `*xélpō` row rather than to this verb row.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** minor clarification recommended. The current note is basically right, but `help→helpan` risks looking like noun-to-verb derivation; it should say more directly that row 2071 is the OE strong-verb infinitive `helpan`, while noun `help` belongs to separate row 2072 / `*xélpō`.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` or dossier text:** no change recommended. The relevant `DEV_NOTES` material is acceptable as background phonology, and no row-specific dossier text exists to clean up.

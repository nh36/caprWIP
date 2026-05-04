# Research memo — 1961 bow / bīeġan

## Starting point
- ID `1961`; CONCEPT `bow`; COUNTERPART `bīeġan`.
- TSV `PROTO` = `*báugijaną`; TSV `PROTOFORM` = `*báugijaną`; TSV `DERIVATION_CLASS` = `regular`.
- TSV note: `Kroonen *baugjan- wv. 'to (make) bend' → OE bīeġan; boga is the noun *bugan-`.
- The row is therefore not the strong verb `būgan` 'bow, bend' and not the noun `boga` 'bow'; it is the weak causative verb 'to bend, make bend'.

## Packet evidence assessment
- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*báugijaną → bīeġan`; the current trace-report snapshot where row 1961 already outputs `bīeġan`; and the Ringe & Taylor citation in `DEV_NOTES.md` (`PNWGmc *baugijana 'to bend (it)' > *béagjan > WS biegan`). These all align with the present project state.
- **Useful background:** the brief mention in `bugan-scufan-paradigm-cell-review.md` that row 1961 is the Class-I weak causative alongside the strong-verb and noun rows in the same cogset; and older DEV_NOTES discussion of `*gj → ʤ`, because it explains why the current FST gets this row right.
- **Stale or superseded:** `final_vowel_missing_analysis.md` and `non_firing_rules_analysis.md` preserve an older noun/verb conflation (`*baugjăną` with expected `boga`). Those are diagnostic history only; they are not current lexical guidance for row 1961.
- **Irrelevant or misleading:** the packet's lexical-table hit `bow = boga` from `old_english_wiktionary.tsv` is a different lexeme, namely the noun from `*bugan-`. It should not be used as evidence against `bīeġan`.

## Additional repo research
Checked beyond the packet: `Germanic/docs/DEV_NOTES.md` (lines 1750-1753, 8980, 9057-9076, 26619-26623, 26682-26683, 35061-35070, 35481-35490), `Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md`, `Germanic/docs/dossiers/bugun-scufun-attestation.md`, `Germanic/docs/analysis/final_vowel_missing_analysis.md`, `Germanic/docs/non_firing_rules_analysis.md`, `Germanic/data/oe_known_problems.tsv`, `Germanic/data/old_english_wiktionary.tsv`, and relevant reference files: Kroonen, Ringe & Taylor, Campbell, Bosworth-Toller, and Clark Hall. No pilot lexeme report for this exact lexeme was found; the adjacent memo for row 1962 was treated only as background.

## Reconstruction and early-stage forms
`*báugijaną` is both the TSV cognate-set proto and the row-specific project input form here; unlike row 1962, there is no paradigm-cell retargeting problem. The etymological dictionary source is Kroonen's causative `*baugjan-` 'to (make) bend', explicitly distinguished from the strong verb `*beugan- ~ *būgan-` and from the noun `*bugan-` 'bow' [@Kroonen2013]. Ringe & Taylor give the early northwest Germanic/OE path as `PNWGmc *baugijana > *béagjan > WS biegan, Kent. bégan, North. béga`, which is exactly the kind of staging the row is meant to represent [@RingeTaylor2014].

## Old English philology
The OE target is a verbal citation form, not a noun and not a preterite cell. Source spelling varies by editorial normalization: the project writes `bīeġan`, while handbook and dictionary sources typically print `biegan`, with non-WS variants `bégan` and `béga` [@RingeTaylor2014; @Campbell1959]. Bosworth-Toller has the verb under `bigan`, with examples such as `Ic bēge mīne cneówa` and `Se ord bīgde upp tō þām hiltum`, and explicitly compares Goth. `us-baugjan`, OS `bōgian`, and OHG `bougen`; Clark Hall cross-references `began` and `bygan` to `biegan` [@ClarkHall1960]. So the row's OE target is philologically ordinary and attested as a weak verb; the only real philological hazard is confusing it with the separate noun `boga` or the analogical strong verb `būgan`.

## Project problem and solution
The project problem was not an unresolved OE outcome but lexical conflation inside earlier mismatch analysis. Older scratch analyses treated `*baugjăną` as if it should have yielded the noun `boga`, which mixed a causative infinitive with a separate nominal lexeme. Current project materials have corrected that: the live row, current trace snapshots, and newer DEV_NOTES all agree that `*báugijaną` should yield `bīeġan`, with the noun handled separately in row 1963 and the strong verb handled separately in row 1962. The solution is therefore to preserve the present row as the causative weak verb and to treat older `boga` expectations as stale project history.

## Paradigm probe
A paradigm probe is **not required** for this memo. This row is not a paradigm-cell dispute, an analogical-retargeting case, or a known FST miss; the current system already returns `bīeġan`, and the main issue is lexeme disambiguation rather than cell selection. If a demonstrative probe were ever wanted anyway, it would be optional and should compare the causative infinitive `*báugijaną`, the strong-verb preterite `*báug`, and the noun `*búgô` across rows 1961-1963, but that would be a cross-row disambiguation exercise rather than a required paradigm probe for row 1961 itself.

## Recommended final report
Recommend a short final report stating that row 1961 is the regular weak causative `*báugijaną → OE bīeġan`/`biegan`, citing Kroonen and Ringe & Taylor, and explicitly warning that `boga` belongs to the noun row and `būgan` to the strong-verb row. Because `NOTE` is non-empty, the final report should preserve that disambiguation even though `DERIVATION_CLASS` is `regular`.

## Data-change recommendations
- **TSV `PROTO`:** no change.
- **TSV `PROTOFORM`:** no change.
- **TSV `COUNTERPART`:** no change.
- **TSV `DERIVATION_CLASS`:** no change.
- **TSV `NOTE`:** no required change; the existing note already captures the crucial noun/verb distinction succinctly.
- **`oe_known_problems.tsv`:** no change; there is no current known-problem entry for this row, and none is needed.
- **DEV_NOTES/dossier text:** no required change. Current DEV_NOTES and the dossier context already treat row 1961 correctly; the stale noun/verb conflation survives in older analysis scratch files rather than in the live dossier guidance.

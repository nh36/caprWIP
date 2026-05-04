# Research memo — 1949 bier / bǣr

## Starting point

- **ID:** 1949
- **CONCEPT:** bier
- **COUNTERPART:** `bǣr`
- **PROTO:** `*bḗrō`
- **PROTOFORM:** `*bḗrō`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Wiktionary: PGmc *bērō > OE bēr/bǣr (bier); *barwōn is wrong lexeme`

The live row has already corrected an older lexeme mix-up by replacing the earlier `*barwōn` analysis with `*bḗrō`, but the note still preserves source-history noise and the repo's supplementary lexical tables are not fully aligned on the OE headword spelling.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing the current project path `*bḗrō -> *bǣru -> bǣr`; and the fact that the live OE report snapshots now expect and output `bǣr`.
- **Useful background:** the packet's `old_english_wiktionary.tsv` hit `bier -> bēr`, which shows that a competing OE headword spelling is circulating in repo-local supplementary material.
- **Stale or superseded:** the packet's `DEV_NOTES` excerpts that still talk about `*barwōn` and modern English `bier` are diagnostic history from the English sandbox, not current OE row-level authority; they are useful for explaining how the lexeme was previously confused, but they do not override the live OE row. Older repo state also had row 1949 as `*barwōn -> bēr`, which is now superseded.
- **Irrelevant or misleading:** the packet's English-side KIT, /r/-loss, and breaking notes are about later English outputs, not about the OE citation form for this row; the absence of dossier/analysis hits in the packet means there is no hidden row-specific full analysis to privilege here.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/old_english_wiktionary.tsv` — supplementary table gives `bier -> bēr`.
- `Germanic/data/oe_known_problems.tsv` — no entry for this row or proto.
- `Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06` — preserves the older stale state `*barwōn -> bēr`.
- `Germanic/docs/non_firing_rules_analysis.md` — still has the stale diagnostic sample `*barwōn -> bearwōn (expected bēr)`.
- `Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt` and related trace snapshots — current project output is `bǣr` from `*bērō`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — `*bērō- f. 'bier'`, with OE `bar, bær`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — headword `bær ... 'bier'`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — headword `bær` with gloss and citations for the noun.

No pilot lexeme report for this row was found, and no packet-named dossier or analysis file existed to inspect.

## Reconstruction and early-stage forms

This row needs a simple three-way distinction:

1. **Cognate-set proto / etymological headword:** PGmc `*bērō-` 'bier' (TSV `PROTO` `*bḗrō` in the repo's accent notation). Repo-local Kroonen evidence supports this lexeme.
2. **Project input form for OE derivation:** the row uses the same form, `*bḗrō`, as TSV `PROTOFORM`; unlike paradigm-cell rows, there is no separate oblique or analogical input here.
3. **OE target form represented by the row:** the live row currently targets `bǣr`.

The abandoned alternative `*barwōn` should be treated as a stale lexeme assignment, not as a competing proto-stage of the same word. The current OE trace is internally coherent: long `ē` lowers to `ǣ` at the NWGmc/OE staging used by the project, and apocope then yields `bǣr`.

## Old English philology

The strongest repo-local lexical authority checked here is not the packet's Wiktionary-derived `bēr`, but Kroonen plus the OE dictionaries, which point to OE `bær` (and Kroonen also lists `bar`). That means:

- there is solid repo-local support for the **lexeme** 'bier' continuing PGmc `*bērō-`;
- there is repo-local support for an OE citation form written `bær`/`bar`;
- the packet's supplementary `bēr` hit is weaker and probably reflects stale or simplified table data rather than the best current lexical authority.

For the final report, `bǣr` should therefore be presented cautiously: it matches the live project derivation and is a plausible normalized long-vowel spelling, but the explicit dictionary/headword evidence checked in-repo is phrased as `bær` (and Kroonen also `bar`), not as a directly cited macronized `bǣr`. This is a headword-normalization issue, not a paradigm-cell issue.

## Project problem and solution

The real project problem was first a **wrong lexeme** (`*barwōn`), and now a milder **source-normalization mismatch**. The lexeme assignment has already been fixed correctly in the live row: `PROTO`/`PROTOFORM` now point to `*bḗrō`, and the OE transducer derives `bǣr` regularly.

What remains is to keep the report honest about evidence level. The project should treat `bǣr` as the row's current normalized OE target, while also saying that repo-local lexicographic authority is expressed as `bær`/`bar` and that the older `bēr` table entry is not the best evidence. In other words, the solution is explanatory cleanup, not a new paradigm workaround.

## Paradigm probe

No paradigm probe is required. This row is not a hidden oblique-cell solution, an analogy case, or an attested-variant paradigm choice of the `late_analogy`/`attested_variant` type. If anyone later wants extra reassurance, the only plausible probe would be a trivial citation-form check of the direct row input `*bḗrō`, but that would add little beyond the existing trace.

## Recommended final report

Recommend a short final report saying that row 1949 correctly rejects older `*barwōn` material, derives the OE form regularly from PGmc `*bērō-`, and should distinguish the live normalized project target `bǣr` from lexicographic spellings cited in repo-local sources (`bær`, also `bar` in Kroonen). It should explicitly treat the packet's `bēr` hit as supplementary/stale rather than as the main authority.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended; `*bḗrō` is the right lexeme-level proto for this row.
- **TSV `PROTOFORM`:** no change recommended; this row does not need a special paradigm-cell input.
- **TSV `COUNTERPART`:** no immediate change recommended. Keep `bǣr` unless the project decides to retarget dictionary-style citation spelling over normalized FST output; if that policy decision is made later, `bær` would be the stronger repo-local lexicographic candidate than `bēr`.
- **TSV `DERIVATION_CLASS`:** no change recommended; `regular` still fits the current row-level analysis.
- **TSV `NOTE`:** **change recommended** — replace the Wiktionary-only wording with a tighter note that cites the corrected lexeme (`*bērō-`), says older `*barwōn` history is stale, and notes that repo-local lexical authorities give OE `bær`/`bar` while the live project target is normalized `bǣr`.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no mandatory change for this row, but light cleanup of stale diagnostic prose such as `non_firing_rules_analysis.md` would reduce future packet noise by marking the old `*barwōn -> bēr` state as historical.

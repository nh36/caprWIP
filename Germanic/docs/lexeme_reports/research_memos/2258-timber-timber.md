# Research memo — 2258 timber / timber

## Starting point

- **ID:** 2258
- **CONCEPT:** timber
- **COUNTERPART:** timber
- **PROTO:** *tímrą
- **PROTOFORM:** *tímbrą
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** Kroonen *timbra- with *b; OE timber.

The live TSV already separates the cognate-set proto from the OE derivational input. No pilot lexeme report exists for this row, so the packet and wider repo evidence have to carry the memo stage directly.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing `*tímbrą -> timber`; the `DEV_NOTES.md` epenthetic-insertion section at 16666-16711, where `*timbrą -> timber` is treated as a regular OE epenthesis case; and the supplementary lexical hit in `old_english_wiktionary.tsv` listing OE `timber`.
- **Useful background:** the packet’s bibliography pointer to Kroonen; the generated trace excerpt showing that the current cascade derives `timber` from `*tímbrą`; and the packet’s note that no `oe_known_problems.tsv` entry matches this row.
- **Stale or superseded:** the packet’s background `DEV_NOTES.md:2324` hit about English attested-form harness failures (`sieve/singe/timber`) is diagnostic project history, not current OE-row authority; and older repo diagnostics such as `final_vowel_apocope_investigation.md` still treating `*timrą` as the direct starting point are superseded by the later TSV fix to `*tímbrą`.
- **Irrelevant or misleading:** generated debug snapshots that merely restate the TSV note are not independent evidence; and row-number-only hits such as the unrelated `2258` line references in other dossiers should not be read as lexical evidence for this noun.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 2320-2324 and 16666-16711.
- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` at 297.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` at the `timber` / `timbor` entry.

No full dossier or analysis file is named in the packet or the TSV note for this row, and no pilot report exists for `timber`.

The extra repo pass clarifies three things the packet alone does not. First, the live FST currently gives `*tímrą -> timer` but `*tímbrą -> timber`, so the inserted `b` is not cosmetic. Second, `final_vowel_apocope_investigation.md` preserves an older diagnostic stage (`*timrą -> timra (exp. timber)`) that should now be treated as historical rather than current. Third, Clark Hall supports `timber` as an OE headword and also records `timbor` as a variant/cross-reference, which matters for the philology section.

## Reconstruction and early-stage forms

This row needs the usual three-way distinction kept explicit.

1. **Cognate-set proto:** TSV `PROTO = *tímrą` is the lexeme-level etymological headword for the cognate set.
2. **Project input form:** TSV `PROTOFORM = *tímbrą` is the row-specific pre-OE input used for derivation, reflecting the `*timbra-` shape named in the note.
3. **OE target form:** `timber` is the OE form the row is meant to represent.

The crucial point is that `*tímbrą` is not a rival cognate-set proto replacing `*tímrą`. It is the project’s normalized pre-OE input for the Old English row, chosen because the row is modelling an early analogical or stem-expanded form with `b` already present. Under the live cascade that distinction matters materially: `*tímrą` now yields `timer`, while `*tímbrą` yields `timber`.

## Old English philology

Repo-local lexical evidence supports treating `timber` as an attested OE lemma, not as a reconstructed convenience form and not as an inflected paradigm-cell substitute. `old_english_wiktionary.tsv` lists `timber`, and Clark Hall gives `timber` as the dictionary headword with senses including ‘timber, building material’ and ‘building, structure’, while also listing `timbor` as a variant/cross-reference.

So the philological issue is not whether OE `timber` exists, but how its prehistory should be encoded in the project. The row’s target is an ordinary citation-form noun. The derivative verb `timbran/timbrian` appears elsewhere in repo reference material, but that is only supporting background and should not be confused with direct evidence for the noun row itself.

## Project problem and solution

The project problem is upstream, not OE-side. If the row were forced to run directly from the cognate-set proto `*tímrą`, the live FST would miss the target (`timer`, not `timber`). The current solution is therefore to preserve `PROTO = *tímrą` for the cognate set while using `PROTOFORM = *tímbrą` as the OE derivational input.

That is the right kind of intervention for this row. Once the `b`-bearing input is chosen, the rest of the derivation is ordinary: nasal apocope gives `*tímbr`, then OE epenthetic vowel insertion gives `*tímber`, yielding `timber`. This belongs in `early_analogy`, not `late_analogy`, because the special choice is a pre-OE stem/input selection rather than a late OE paradigm-cell rescue.

## Paradigm probe

No paradigm probe is required.

This is not a row where the outcome depends on choosing among OE inflectional cells such as nominative versus genitive or dative. The decisive contrast is earlier: cognate-set `*tímrą` versus derivational `*tímbrą`. If a future audit wants a control, a simple two-input comparison is enough; there are no missing OE paradigm cells that need probing for the present memo.

## Recommended final report

Recommend a concise final report that says row 2258 targets attested OE `timber`, keeps cognate-set `PROTO = *tímrą`, and explains that `PROTOFORM = *tímbrą` is the row-specific pre-OE input reflecting Kroonen’s `*timbra-` with `b`, needed before the ordinary OE epenthesis path can yield `timber`.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. `*tímrą` still works as the cognate-set proto distinct from the OE row input.
- **TSV `PROTOFORM`:** no change recommended. `*tímbrą` is the correct project input for the current row.
- **TSV `COUNTERPART`:** no change recommended. `timber` is the right OE target.
- **TSV `DERIVATION_CLASS`:** no change recommended. `early_analogy` is the correct class.
- **TSV `NOTE`:** change recommended. The note should say more explicitly that `PROTO` remains `*tímrą` for the cognate set, while `PROTOFORM = *tímbrą` is the row-specific OE input following Kroonen’s `*timbra-`.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES/dossier text:** light dossier cleanup is recommended. `DEV_NOTES.md` 16666-16711 is still current and useful, but `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` should be treated or labeled as historical for this lexeme because its `*timrą -> timra (exp. timber)` diagnostic no longer reflects the live row treatment.

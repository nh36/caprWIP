# Research memo — 2027 follow / fylġan

## Starting point

- **ID:** 2027
- **CONCEPT:** follow
- **COUNTERPART:** `fylġan`
- **PROTO:** `*fulgēną`
- **PROTOFORM:** `*fúlgijaną`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** Kroonen s.v. `*fulgēn-`: “OE fylg(e)an continue `*fulgjan-`”; R/T §2.3.1: “class I weak OE fylgan”. WS `folgian` is Class II from `*fulgēn-`.

The live TSV already distinguishes the comparative cognate-set headword from the OE-facing derivational input: `PROTO` remains the inherited `*fulgēną`, while `PROTOFORM` is the class-I input `*fúlgijaną`, producing current target `fylġan`. No pilot or full lexeme report for this row turned up in repo searches.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing `*fúlgijaną -> fylġan`; and the main `DEV_NOTES.md` analysis at `4402-4470`, which correctly distinguishes the inherited class-III/class-II background from the class-I OE-directed input and explains why `*fulgēną -> folgian` is not a regular infinitive pathway [@Kroonen2013; @RingeTaylor2014].

**Useful background:** the packet’s Kroonen and Ringe/Taylor excerpts; Campbell’s and Bright’s remarks that class-I `fylg(e)an` survives beside class-II `folgian`; and the dictionary material showing both headword zones in OE reference works [@Campbell1959; @BrightCassidyRingler1971; @ClarkHall1960; @BosworthToller1898].

**Stale or superseded:** the packet preserves older workflow states where row 2027 was still a live mismatch (`*fulgēną -> folgon`) and where an implementation note says `PROTO` itself was changed to `*fulgjăną`. That last claim is no longer current, because the live TSV now uses the better split `PROTO = *fulgēną` versus `PROTOFORM = *fúlgijaną`. Those passages are useful project history, but not final authority.

**Irrelevant or misleading:** the lack of an `oe_known_problems.tsv` entry is not evidence against the row; the packet’s `old_english_wiktionary.tsv` hit (`follow -> folgian`) is only lightweight dictionary background; and generic concept-name collisions elsewhere in the repo are not row-specific lexical evidence.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` around `3980-3988`, the full row-specific analysis at `4402-4470`, and the later implementation note at `4596-4600`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which still marks row 2027 as report-requiring.
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry).
- `Germanic/data/old_english_wiktionary.tsv` (`follow -> folgian` only; supplementary, not decisive).
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/bright_anglo_saxon_reader.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.

Direct search across `Germanic/docs/analysis/` and `Germanic/docs/dossiers/` did not turn up a row-specific full dossier or analysis file named in the packet or TSV note beyond `DEV_NOTES.md`, so there was no separate dossier to read for this lexeme.

Main findings from that extra pass:

- Kroonen’s comparative entry keeps the cognate-set under `*fulgen-/*fulgēn-`, but explicitly says ON `fylgja` and OE `fylg(e)an` continue a `*fulgjan-` formation [@Kroonen2013].
- Ringe/Taylor explicitly reconstruct a dual Northwest Germanic formation `*fulgija- ~ *fulgai-`, yielding OE `fylgan ~ folgian` [@RingeTaylor2014].
- Campbell and Bright both treat `fylgan/fylg(e)an` and `folgian` as side-by-side OE conjugational outcomes rather than a single unproblematic lemma [@Campbell1959; @BrightCassidyRingler1971].
- Clark Hall and Bosworth-Toller both preserve separate entries or cross-references for `folgian` and `fylgan/fylgean`, confirming that the OE lexicographic tradition does not collapse everything into one headword [@ClarkHall1960; @BosworthToller1898].

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** `*fulgēną` in the TSV, corresponding to Kroonen’s comparative `*fulgen-/*fulgēn-` lexeme [@Kroonen2013].
2. **Project input form:** `*fúlgijaną`, i.e. the class-I/j-present branch that older `DEV_NOTES.md` shorthand writes as `*fulgjăną`. This is the actual OE-facing derivational input for the row.
3. **OE target form:** `fylġan`, the normalized Old English citation form chosen for the class-I outcome.

Those levels should not be flattened. The row is **not** claiming that OE `fylġan` is the direct unchanged infinitive reflex of comparative `*fulgēną`. Rather, the comparative lexeme shows a split already recognized in the handbooks: one branch yields class-I `fylgan`, the other class-II `folgian` [@Kroonen2013; @RingeTaylor2014].

That is exactly why the live TSV split is better than the older `DEV_NOTES` implementation note that temporarily changed `PROTO` as well. `PROTO` should keep the cognate-set anchor; `PROTOFORM` should carry the OE-directed class-I input.

## Old English philology

This is an **attested OE lemma-level case**, not a reconstructed-OE target and not a special inflected-cell selection.

- `fylgan/fylgean/fylġan` is the class-I weak verb outcome.
- `folgian` is the parallel class-II outcome.
- The coexistence of both is old handbook material, not a modern repo invention [@Campbell1959; @BrightCassidyRingler1971; @RingeTaylor2014].

The important philological point is therefore not “which single form is real?” but “which OE formation is this row intended to represent?” Clark Hall and Bosworth-Toller both preserve `folgian` and `fylgan/fylgean` as distinct headword territory or explicit cross-reference space [@ClarkHall1960; @BosworthToller1898]. So the memo/report should not let the lightweight Wiktionary table’s `folgian` entry override the heavier comparative and handbook evidence for class-I `fylgan`.

The TSV target `fylġan` should be understood as a normalized OE orthographic representation of the class-I form (`fylgan/fylgean`), with palatal `<ġ>` used by project normalization. The memo should avoid making stronger manuscript or dialect claims than the checked repo sources require; the decisive point is the coexistence of class-I and class-II lemma forms, not a narrow manuscript argument.

## Project problem and solution

The project problem was a stem-selection problem, not a missing sound law.

- If the row is modeled directly as `*fulgēną -> folgian`, the pipeline yields `folgon`, not the desired infinitive.
- The repo’s later analysis showed that the regular OE class-I path is instead `*fúlgijaną -> fylġan`.
- `folgian` is then interpreted as the secondary class-II/literary remodelling tied to the `*fulgēn-/*fulgai-` side of the lexeme.

That makes the present row design sensible:

- keep `PROTO = *fulgēną` as the cognate-set headword;
- keep `PROTOFORM = *fúlgijaną` as the OE-directed derivational input;
- keep `COUNTERPART = fylġan` as the row’s intended OE target;
- keep `DERIVATION_CLASS = early_analogy`, because the special move is early stem/formation selection, not a late paradigm-cell switch.

The main remaining risk is explanatory. Without a clearer note/report, readers may think the project is simply denying OE `folgian`, when the actual claim is narrower: row 2027 chooses the class-I OE branch as its derivational target.

## Paradigm probe

No paradigm probe is required.

This row is not a true paradigm-cell case like the finite-cell entries. The decisive issue is the choice between competing OE **formations/lemmas** (`fylġan` versus `folgian`), not the selection of one inflectional cell from within a single paradigm. If a later appendix wants a small diagnostic table anyway, the useful contrasts would be:

- infinitive `*fúlgijaną -> fylġan`;
- diagnostic mismatch `*fulgēną -> folgon`;
- optional background finite cell `*fulgēþi -> folġeþ`.

But that would be explanatory background only, not a prerequisite for the final report.

## Recommended final report

Recommend a concise final report that says row 2027 keeps comparative `*fulgēną` as the cognate-set proto, derives the OE target from class-I `*fúlgijaną`, and treats `fylġan/fylgan` and `folgian` as parallel OE formations already recognized by Kroonen, Ringe/Taylor, Campbell, and the dictionaries. The final report should also note that older project history temporarily collapsed `PROTO` and `PROTOFORM`, but the live row now correctly keeps them distinct.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. Keep `*fulgēną` as the cognate-set headword.
- **TSV `PROTOFORM`:** no change recommended. Keep `*fúlgijaną` as the OE-facing class-I input.
- **TSV `COUNTERPART`:** no change recommended. Keep `fylġan` as the project’s normalized class-I OE target.
- **TSV `DERIVATION_CLASS`:** no change recommended. `early_analogy` is the right label for an early stem/formation choice.
- **TSV `NOTE`:** minor clarification recommended. It would help to say explicitly that `PROTOFORM` is the class-I input behind `fylġan`, while `folgian` is the parallel class-II/WS-type OE formation from the `*fulgēn-` side.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** cleanup recommended. The `4596-4600` implementation note should be marked more clearly as superseded in its `PROTO` claim, since the live TSV now restores the better `PROTO`/`PROTOFORM` split. Earlier mismatch-stage discussion can remain as history, but should not read as current state.
- **Dossier text:** no change recommended. No row-specific dossier text needing cleanup turned up beyond `DEV_NOTES.md`.

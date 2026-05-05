# Research memo — 2037 gall / ġealla

## Starting point

- **ID:** 2037
- **CONCEPT:** gall
- **COUNTERPART:** `ġealla`
- **PROTO:** `*gállą`
- **PROTOFORM:** `*gállô`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** empty

The live TSV already encodes the key split for this row: the cognate-set headword remains `*gállą`, but the OE derivational input is the weak masculine `*gállô`. The row `HISTORY` explains why that split was introduced: older TSV input `*gallą` produced bare `*ġeall`, whereas the weak n-stem input yields the expected OE form `ġealla`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact trace showing `*gállô -> ġealla`; and `DEV_NOTES.md` 3700-3709, which correctly explains the strong-neuter-to-weak-masculine correction and the successful live pipeline result.
- **Useful background:** the packet’s lexical-table hit in `old_english_wiktionary.tsv`; the packet’s pointer to `analysis/arestoration_r_l_research.md`, which is useful only for the broad phonological environment (“geminate *ll* + breaking”); and the packet’s bibliography cue for Kroonen.
- **Stale or superseded:** `DEV_NOTES.md` 3711-3713 is no longer current as written. It says the OE row now has `*gallô` in both `PROTOFORM` and `PROTO`, but the live TSV still has `PROTO = *gállą` and only `PROTOFORM = *gállô`. That line is project-history residue, not present row authority.
- **Irrelevant or misleading:** the packet’s “no manifest entry” notice and lack of an `oe_known_problems.tsv` hit are coverage metadata, not lexical evidence; and the packet’s `arestoration_r_l_research.md` table line by itself does not justify the stem-class decision.

So the packet is a good starting dossier, but not a final evidence base: it must be read against the live TSV and against the now-stale part of `DEV_NOTES.md`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` 3689-3714.
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md`.
- `Germanic/docs/dossier-shoulder-paradigm-survey-2026.md`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/oe_known_problems.tsv`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/luick_historische_grammatik.txt`.
- `docs/references/kaluza_historische_grammatik_englisch.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bright_anglo_saxon_reader.vision.txt`.
- a live binary comparator run against `backend/old_english.bin` for `*gállą` and `*gállô`.

Main findings from that extra pass:

- The current binary contrast is clean: `*gállą -> ġeall`, but `*gállô -> ġealla`.
- Kroonen gives the etymon as `*galla/ōn- m./f. 'bile'` and explicitly includes OE `gealla m.` [@Kroonen2013].
- Clark Hall gives `gealla (a, e) m. 'gall,' bile`, Bright gives `gealla, m., gall: ds. geallan`, and Bosworth-Toller records `gealla` glossed as Latin *fel*; together these support an attested weak masculine lexeme, not a reconstructed OE convenience form [@ClarkHall1960; @BrightCassidyRingler1971; @BosworthToller1898].
- Campbell, Luick, and Kaluza all cite `gealla` among the West Saxon/Kentish breaking forms before `ll`, while Campbell also contrasts Anglian `galla`; so the repo sources support `gealla/ġealla` as the row target and `galla` only as dialectal or variant background [@Campbell1959; @Luick1914; @Kaluza1906].
- `final_vowel_apocope_investigation.md` still contains the older diagnostic shorthand `*gallą -> ġealla`; that file is useful as workflow history only, not as current row authority.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / project headword:** `PROTO = *gállą`. This is the broader set label still shared by the neighbouring Dutch, English, and German rows in cognate set 205.
2. **Project input form used for derivation:** `PROTOFORM = *gállô`. This is the OE-facing weak masculine nominative singular used by the FST. It is the project-normalized citation form corresponding to Kroonen’s weak n-stem etymon `*galla/ōn-` / `*gallōn-`.
3. **OE target form:** `ġealla`, i.e. dictionary `gealla` in project-normalized palatal orthography.

The important memo point is that the current evidence does **not** support collapsing these levels. The row is not saying that the whole cognate set should be rewritten to weak-masculine `*gállô`; it is saying that the OE row must be derived from a weak n-stem input even though the cross-row cognate-set headword remains `*gállą`. That is why the stale `DEV_NOTES` wording about both columns changing should not be treated as final authority.

## Old English philology

`ġealla` is an attested OE lexeme, not a reconstructed target and not a special paradigm-cell substitute. The lexical evidence in Clark Hall, Bosworth-Toller, and Bright supports a weak masculine noun with oblique `geallan` [@ClarkHall1960; @BosworthToller1898; @BrightCassidyRingler1971].

Two philological cautions matter:

- The dictionary sources usually print undotted `gealla`; the TSV counterpart `ġealla` is the project’s normalized spelling for the same palatalized form, not a different lexeme.
- Campbell’s grammar explicitly contrasts West Saxon/Kentish `gealla` with Anglian `galla` [@Campbell1959]. So the final report may note variant/dialect background, but it should keep `ġealla` as the row target and should not treat `galla` as the target counterpart.

This is therefore a lemma-level OE noun with genuine lexical support, not an unattested reconstruction and not a late-cell workaround.

## Project problem and solution

The project problem was simple but important: older TSV input `*gállą` treated the OE word as a strong neuter a-stem and therefore lost the final vowel by heavy-syllable apocope, producing `ġeall`. That was a modelling error, not a sound-law failure inside the corrected weak-noun pathway.

The current project solution is coherent:

- keep `PROTO = *gállą` as the cognate-set label;
- use `PROTOFORM = *gállô` as the OE derivational input;
- derive `ġealla` regularly from that weak n-stem input;
- keep `DERIVATION_CLASS = early_analogy`, because the special move is upstream stem/class selection, not a late OE paradigm-cell substitution.

What remains messy is the surviving project prose, not the live row itself. `DEV_NOTES.md` still says both `PROTOFORM` and `PROTO` were changed, but the live TSV now shows the more careful and more useful split.

## Paradigm probe

No paradigm probe is required.

This is not a `late_analogy` case where the project must choose among OE nominative, genitive, dative, or plural cells. The decisive contrast is upstream and already visible in the live comparator run: `*gállą -> ġeall` versus `*gállô -> ġealla`. No missing paradigm cells need to be probed before a final report is written.

## Recommended final report

Recommend a concise final report that says OE `ġealla` is an attested weak masculine noun; that the row intentionally keeps cognate-set `PROTO = *gállą` distinct from derivational `PROTOFORM = *gállô`; that the old strong-neuter input was a project error yielding `ġeall`; and that stale `DEV_NOTES` wording about both columns changing is background history, not the current row state.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. `*gállą` is still defensible as the cognate-set headword as long as the memo/report explicitly distinguishes it from the OE-facing `PROTOFORM`.
- **TSV `PROTOFORM`:** no change recommended. `*gállô` is the right live derivational input.
- **TSV `COUNTERPART`:** no change recommended. Keep project-normalized `ġealla`.
- **TSV `DERIVATION_CLASS`:** no change recommended. `early_analogy` correctly describes an upstream stem/class choice rather than a late paradigm-cell rescue.
- **TSV `NOTE`:** change recommended. Add a short note stating that OE `ġealla` is weak masculine and is therefore derived from `PROTOFORM = *gállô`, while `PROTO = *gállą` remains the broader cognate-set label.
- **`oe_known_problems.tsv`:** no change recommended. This row is currently solved, not an open exception.
- **`DEV_NOTES` text:** change recommended. Update 3711-3713 so it no longer says that both `PROTOFORM` and `PROTO` are `*gallô`; it should reflect the live split between `PROTO = *gállą` and `PROTOFORM = *gállô`.
- **Dossier / analysis text:** no change required for a final report, but `final_vowel_apocope_investigation.md` should be treated as old diagnostic history if it is retained; no dedicated dossier rewrite is otherwise needed.

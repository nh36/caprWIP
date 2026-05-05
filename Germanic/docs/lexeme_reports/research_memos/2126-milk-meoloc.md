# Research memo — 2126 milk / meoloc

## Starting point

- **ID:** 2126
- **CONCEPT:** milk
- **COUNTERPART:** meoloc
- **PROTO:** *mélukz
- **PROTOFORM:** *mélukz
- **DERIVATION_CLASS:** regular
- **NOTE:** meoloc is the regular outcome; meolc reflects paradigm leveling from gen/dat (Campbell §390, R/T §6.6.4)

This is a note-bearing regular row, so it falls under the selective lexeme-report policy. I found no pilot or full lexeme report for this lexeme; the packet is the starting dossier, not the final authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet trace showing the current cascade `*mélukz -> meoloc`; and the later `DEV_NOTES` implementation decision that the project should accept `meoloc` as the regular output and treat `meolc` as the exceptional/leveled variant.
- **Useful background:** the packet’s milk section from `DEV_NOTES` lines 730-770; the packet’s reminder that `oe_known_problems.tsv` has no matching entry; and the lexical-table hit `old_english_wiktionary.tsv:187`, which is useful philological background because it shows dictionary-normalized `meolc`.
- **Stale or superseded:** the packet promotes the earlier `DEV_NOTES` mismatch framing `*melukz -> meoloc (expected meolc)` as high-confidence evidence. That is no longer the live project state, because the same `DEV_NOTES` section later records the resolved project decision: TSV updated to `meoloc`.
- **Irrelevant or misleading:** the packet’s low-confidence bibliography-key guesses are not lexical evidence, and the absence of dossier hits should not be read as absence of broader repo evidence; the reference files materially change the philological picture.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` §§684-894, including the early mismatch framing and the later implementation-status summary.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which lists row 2126 as report-requiring and still uncovered.
- `Germanic/data/oe_known_problems.tsv` — no entry for row 2126, `*mélukz`, `meoloc`, or `meolc`.
- `Germanic/data/old_english_wiktionary.tsv` — gives `meolc`, not `meoloc`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — gives usual WS `meolc < meoluc < *meluk`, Anglian `milc`, and later notes WS `meoluc` versus Anglian generalized `milc`.
- `docs/references/campbell_old_english_grammar.txt` — gives trisyllabic consonant-stem oblique forms `*milukiz, *miluki`, cites Anglian `milc`, and discusses `meoluc` / `meoloc`.
- `docs/references/legacy/etymological_dictionary_of_proto_germanic_kroonen.txt` — gives PGmc `*meluk-` with OE `meoloc, meolc`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — gives PGmc `*melukz` with OE `meolc, meoluc, milc`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — normalizes the noun under `meolc`.
- `docs/references/bright_anglo_saxon_reader.vision.txt` — includes accusative `meolc`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md` — background only, showing the generated output already follows the live row `meoloc`.

Main result of this wider pass: current project authority and dictionary normalization are not identical. The project has consciously retargeted the row to regular `meoloc`, but the repo’s lexical/reference files still show that `meolc` and `meoluc` remain important philological comparanda rather than obsolete noise.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction.

1. **Cognate-set proto / etymological headword:** the comparative lexica give PGmc `*meluk-` or `*melukz`, i.e. the milk noun as a Germanic cognate-set item. That is the etymological level.
2. **Project input form:** TSV `PROTOFORM = *mélukz`, the citation-form input now fed to the OE cascade.
3. **OE target represented by the row:** TSV `COUNTERPART = meoloc`, i.e. the project’s selected regular unsyncopated OE outcome for this row.

For the regular derivation, the repo’s trace is coherent: `*mélukz` loses final `-z`, then gives unstressed `u > o`, then OE back mutation / breaking yields `meoloc`. The competing forms belong to a different part of the history: oblique singular cells such as `*melukiz/*meluki` (Campbell’s pathway to Anglian `milc`, with umlauted/syncopated later stages) underlie the leveled syncopated tradition. So the lexeme has one regular citation-form pathway in the project and a separate oblique-cell pathway behind the `meolc/milc` side of the dossier.

## Old English philology

Philologically, this is **not** a case where `meoloc` is the only real OE form.

- **Attested vs reconstructed:** `meoloc` is not merely a project reconstruction; repo-local reference works do record unsyncopated OE forms (`meoloc` in Kroonen, `meoluc` in Orel and Ringe-Taylor). But the same sources also show that syncopated `meolc` and Anglian `milc` are real OE forms.
- **Citation/headword status:** Clark Hall, Bright, and `old_english_wiktionary.tsv` normalize the noun as `meolc`; Ringe-Taylor call `meolc` the usual WS form but derive it from earlier `meoluc`; Kroonen explicitly includes `meoloc` beside `meolc`. So the row’s `meoloc` should be treated as a supported unsyncopated variant chosen for project reasons, not as the uncontested dictionary headword.
- **Paradigm/cell status:** the row is meant to stand for the regular citation-form development from `*mélukz`, whereas `meolc`/`milc` belong to the oblique-singular / leveled side of the paradigm history.
- **Dialect status:** the repo sources support a real WS versus Anglian distinction. Ringe-Taylor and `DEV_NOTES` align unsyncopated `meoluc/meoloc` with WS and `milc` with Anglian generalization. WS also preserves syncopated `meolc`, so the dialect picture is not a simple binary replacement.

So the safest philological claim is: OE has a mixed dossier `meoloc/meoluc ~ meolc ~ milc`; the live row intentionally chooses the regular unsyncopated side of that dossier.

## Project problem and solution

The project problem was originally framed as an FST failure: the cascade produced `meoloc`, while the older target expectation was `meolc`. Current repo authority shows that this is no longer the intended reading.

The live project solution is:

- keep `*mélukz` as the citation-form input;
- keep `meoloc` as the row target because it is the regular unsyncopated outcome the cascade actually derives;
- treat `meolc` not as the form the deterministic row must hit, but as a syncopated/leveled variant associated with oblique singular history.

That means row 2126 is currently designed as a **regular derivation row for the unsyncopated OE variant**, not as a full lexical summary of every normalized dictionary headword. The main remaining risk is documentary, not derivational: packet readers can still be misled by stale `expected meolc` history or by dictionary files that normalize the lemma differently.

## Paradigm probe

A paradigm probe is **required**, because the report’s argument depends on comparing the citation-form input with the oblique cells that motivate the leveled `meolc/milc` tradition.

No built-in pilot probe exists for this lexeme yet. The missing probe should at minimum compare:

- **nom.sg.** `*mélukz` (current TSV citation-form input)
- **acc.sg.** `*méluk` if an endingless citation-form comparator is wanted
- **gen.sg.** `*mélukiz` (or the corresponding pre-OE umlauted/syncopated stage behind `milc`)
- **dat.sg.** `*méluki` (same rationale)

Plural cells are not the priority here. The real question is whether the oblique singular cells are the best explicit source for the syncopated `meolc/milc` variant that the note invokes.

## Recommended final report

Recommend a concise final report that says the live row intentionally tracks regular unsyncopated `meoloc` from `*mélukz`, while the broader OE dossier also contains syncopated `meolc` and Anglian `milc`, plausibly levelled from oblique singular forms. The report should explicitly mark older packet language expecting `meolc` as superseded project history, not current row design.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended. `meoloc` is a defensible project target for the regular unsyncopated variant, even though some dictionary-style sources normalize the lemma as `meolc` or `meoluc`.
- **TSV `DERIVATION_CLASS`:** no change recommended. Under the current project reading, this remains a regular row whose note exists to explain a competing leveled variant.
- **TSV `NOTE`:** **change recommended.** The present note is directionally right but too categorical and too compressed. It should say more explicitly that the project now selects regular unsyncopated `meoloc`, while `meolc`/`milc` belong to the syncopated leveled tradition and are not simply nonexistent.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** **minor DEV_NOTES cleanup recommended.** The later implementation-status lines already give the current decision, but the earlier `expected meolc` framing is still easy for packet generation to over-promote. A short “historical mismatch before retargeting” label in that section would make the chronology clearer. There is no dossier file to revise.

# Research memo — 2004 fast / festan

## Starting point

- **ID:** 2004
- **CONCEPT:** fast
- **COUNTERPART:** festan
- **PROTO:** `*fastēną`
- **PROTOFORM:** `*fástijaną`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** R/T: "festan 'to fix, to fasten' < *fæstjan" (Class I weak); "acquired stative meaning ['to fast'] by lexical confusion" with *fastēn-. OE fæstan has æ from analogy with adj. fæst.

The live TSV already separates the comparative cognate-set headword from the OE-facing derivational input: `PROTO` stays the Kroonen-style `*fastēną`, while `PROTOFORM` is the class-I OE-directed input `*fástijaną`, producing current target `festan`. No pilot or full lexeme report for this row appears to exist yet.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*fástijaną -> festan`; the later `DEV_NOTES.md` resolution section (`4617-4630`), where row 2004 is explicitly updated to `PROTOFORM = *fastjăną`/`*fástijaną`, `COUNTERPART = festan`, and `PROTO = *fastjăną` in the then-current shorthand; and the current coverage/debug material showing row 2004 as a report-requiring `early_analogy` row.
- **Useful background:** the packet's Kroonen excerpt for comparative `*fastēn-`; the Ringe/Taylor excerpt that OE 'to fast' is an originally class-I weak verb which acquired the stative meaning by lexical confusion; and the note that analogical `æ` in OE belongs to later levelling from the adjective `fæst` [@Kroonen2013; @RingeTaylor2014].
- **Stale or superseded:** the earlier packet-preserved `DEV_NOTES.md` material that still treated row 2004 as `*fastēną -> fastian`, a live mismatch, or an unresolved i-umlaut bug (`3862-3980`, `4474-4589`). Those passages are useful for project chronology, but they predate the later resolution and should not be treated as the current state of the row.
- **Irrelevant or misleading:** the absence of a manifest entry or `oe_known_problems.tsv` hit is not lexical evidence; and unrelated concept-name hits for English *fast* in other dossiers are noise, not row-specific support.

The packet is therefore useful only if read chronologically: it mixes current row state with now-superseded mismatch diagnostics.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` around the class-III-to-class-II discussion and the full row-2004 sequence (`3862-3980`, `4474-4635`).
- `Germanic/docs/lexeme_reports/coverage_audit.md` and the current debug snapshot reports, which confirm that row 2004 still requires lexeme-report coverage and currently derives `festan`.
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry).
- `Germanic/data/old_english_wiktionary.tsv` (only the adjective `fæst`, no decisive verbal entry).
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `Germanic/tools/oe_paradigm_probe.py`.

Main findings from that extra pass:

- Kroonen still supports the comparative headword `*fastēn-` with OE `fastian` in the cognate list, so the comparative proto and the OE project solution must be kept distinct rather than collapsed.
- Ringe/Taylor are the decisive repo-local source for the OE side: they explicitly say OE 'to fast' is an originally class-I weak verb and that the stative meaning was acquired by lexical confusion; elsewhere they also explain that analogical `æ` in this family is levelled from the adjective `fæst` rather than the direct sound-law outcome.
- Bosworth-Toller distinguishes `fæstan` ('make fast', 'entrust') from `festan` ('to fast'), while Clark Hall's OCR is less clean and partly merges the semantics under `fæstan`; together they show that the OE lexicographic tradition is not perfectly uniform and should not be oversimplified.
- No row-specific dossier or analysis file named in the packet or TSV note turned up beyond `DEV_NOTES.md`; no pilot/full report for this lexeme exists yet.

## Reconstruction and early-stage forms

This row needs the usual three-way distinction made explicit.

1. **Cognate-set proto / etymological headword:** `*fastēną`. This is the comparative lexeme represented by Kroonen's `*fastēn-`, matching the wider West Germanic set behind English/German/Dutch `fast`/`fasten` forms.
2. **Project input form:** `*fástijaną`. This is the OE-facing class-I input actually used by the project to derive the row. Older `DEV_NOTES.md` discussion often writes the same idea as `*fastjăną`; that shorthand is background history, not the live TSV notation.
3. **OE target form:** `festan`, the form currently represented by row 2004.

The central modelling point is that `PROTO` and `PROTOFORM` refer to different levels. The row is **not** claiming that OE straightforwardly continues comparative `*fastēną` as its direct lemma. Rather, the project keeps `*fastēną` as the cognate-set headword while selecting the class-I formation as the OE derivational input because that is what the repo's Ringe/Taylor evidence supports for the OE verb behind the 'fast' meaning.

## Old English philology

The philological situation is mixed but manageable if the distinctions stay explicit.

- The row targets a **lemma-level infinitive**, not a special paradigm cell.
- Ringe/Taylor's account is the key OE philological point: the fasting verb is tied to the class-I weak verb meaning 'make firm / fasten', with the stative meaning 'fast' arising by lexical confusion with the `*fastēn-` family [@RingeTaylor2014].
- The current target `festan` should not be presented as the only dictionary headword. Repo-local lexicography also preserves `fæstan/fǣstan`, and Ringe/Taylor explicitly treat OE `æ` here as analogical levelling from the adjective `fæst`, not the direct sound-law output.
- Conversely, the earlier packet claim that `festan` proved an i-umlaut bug is no longer the best reading. Campbell and Ringe/Taylor support the opposite interpretation: `e` is the regular phonological outcome for the class-I verb, while `æ` is the later analogical reshaping.
- No checked repo source required a strong dialect/manuscript claim for this row, so the memo stage should avoid over-assigning dialect labels.

So the safest philological framing is: OE shows a class-I verb underlying the project target `festan`, but mainstream citation practice may also surface the analogically remodelled `fæstan/fǣstan`; the memo/report must state that relationship instead of pretending the OE evidence is a single unproblematic headword.

## Project problem and solution

The project problem was that the comparative cognate-set verb and the OE lexical target are not the same derivational object.

- If the row is treated as direct OE continuation of comparative `*fastēną`, earlier project work drifted toward unattested or poorly supported `fastian`-type expectations and mismatch diagnostics.
- The later repo research instead shows that the OE fasting verb is modeled through a class-I formation (`*fástijaną` / older shorthand `*fastjăną`) whose meaning converged with the stative `*fastēn-` lexeme.

That makes the current project solution defensible:

- keep `PROTO = *fastēną` as the cognate-set label;
- use `PROTOFORM = *fástijaną` as the OE derivational input;
- keep `DERIVATION_CLASS = early_analogy`, because the decisive special move is upstream stem/formation selection, not a late finite-cell substitution;
- treat `festan` as the project's derivational target, while explaining in note/report prose that OE dictionary practice also has analogically remodelled `fæstan/fǣstan`.

The main remaining risk is explanatory, not structural: without a clearer note, readers may misread `festan` as if it were simply the ordinary attested OE headword with no analogical overlay.

## Paradigm probe

No paradigm probe is required.

This row is not a true paradigm-cell case like the `lifeþ` entry. The decisive choice is between the comparative headword `*fastēną` and the OE-specific derivational input `*fástijaną`, not between competing OE inflectional cells. The class-III finite forms discussed in `DEV_NOTES.md` (for example `*fastēþi -> fæsteþ`) are diagnostic background only; they are not the row's intended target and do not need a dedicated probe section for the memo stage.

## Recommended final report

Recommend a concise final report that says row 2004 keeps comparative `*fastēną` as the cognate-set proto but derives OE `festan` from class-I `*fástijaną`, following Ringe/Taylor's view that the OE fasting verb is an originally class-I weak verb whose stative meaning arose by lexical confusion with the `*fastēn-` family. The report should also state plainly that lexicographic OE often shows analogical `fæstan/fǣstan`, so the current row target is a project derivational choice rather than the only possible dictionary headword.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. `*fastēną` still works as the comparative cognate-set headword.
- **TSV `PROTOFORM`:** no change recommended. `*fástijaną` is the right OE-facing input; older `DEV_NOTES.md` `*fastjăną` wording should be treated as superseded notation, not as a reason to alter the live TSV.
- **TSV `COUNTERPART`:** no change recommended for now. Keep `festan` as the project's derivational target, but explain more clearly that OE dictionary/headword practice also has analogical `fæstan/fǣstan`.
- **TSV `DERIVATION_CLASS`:** no change recommended. `early_analogy` is the right label because the special move is early stem/formation selection, not a late paradigm-cell substitution.
- **TSV `NOTE`:** yes, clarification recommended. The note should say more directly that `festan` is the project target derived from the class-I input, while `fæstan/fǣstan` are the analogically remodelled OE headword forms; that would prevent readers from reviving the older "i-umlaut bug" interpretation.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** yes, cleanup recommended. The earlier mismatch/i-umlaut-bug passages for row 2004 should be marked more explicitly as superseded by the later `fastian resolution` section, so packet extraction does not keep promoting obsolete workflow state into near-current evidence.
- **Dossier / analysis text:** no change recommended. No row-specific dossier or analysis file requiring cleanup turned up beyond `DEV_NOTES.md`.

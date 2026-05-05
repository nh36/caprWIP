# Research memo — 2093 lead / lǣdan

## Starting point

- **ID:** 2093
- **CONCEPT:** `lead`
- **COUNTERPART:** `lǣdan`
- **PROTO:** `*láidijaną`
- **PROTOFORM:** `*láidijaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `R/T vol.2 13527-29: PGmc *laidijaną > OE lǣdan (to lead)`

The live row is the ordinary weak verb `lǣdan` ‘lead’, not the unrelated noun `lēad` found in the lightweight Wiktionary table. No pilot or full lexeme report for this exact lexeme turned up in repo searches; coverage audit still flags the row only because `NOTE` is non-empty.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing `*láidijaną -> lǣdan`; and the current derivational pathway with PWGmc `*lādijaną`, later `*lādjan`, and OE `lǣdan`. The packet’s `DEV_NOTES.md` hit at line 8982 is also current background, because it matches the present PGmc `*-ij-` notation and Ringe & Taylor’s citation `PGmc *laidijană 'to make go'` [@RingeTaylor2014].
- **Useful background:** the packet’s note that the stem is heavy (`laid-`, CVVC) and therefore belongs with the heavy-stem class-I weak verbs whose PGmc notation now uses `*-ij-`; that helps explain why the project input is `*láidijaną` rather than older shorthand `*laidjăną`.
- **Stale or superseded:** the packet’s `DEV_NOTES.md` hit at line 8726 is from a section explicitly marked superseded before the project adopted PGmc input notation. It is useful only as project history showing the older post-syncope shorthand `*laidjăną`, not as current row authority.
- **Irrelevant or misleading:** the packet’s `old_english_wiktionary.tsv` hit `lead -> lēad` is a different lexeme entirely and should not be used against the verbal target `lǣdan`; the concept-name hit in `compound_archaism_inventory.md` is just a false numerical/context collision, not lexical evidence; and the absence of an `oe_known_problems.tsv` entry is neutral, not probative.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` around `8763-8899` and `8972-9018` for the current PGmc `*-ij-` policy and the heavy-stem class-I list containing `*laidijăną`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which still marks row 2093 as report-requiring because of `NOTE`.
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry).
- Direct searches across `Germanic/docs/analysis/` and `Germanic/docs/dossiers/` for `2093`, `lǣdan`, and `laidijan`; no row-specific dossier or analysis file was found.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`, `docs/references/ringe_vol1_pie_to_pgmc.txt`, `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`, `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`, and `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.

Main findings from that extra pass:

- Ringe & Taylor explicitly give `PGmc *laidijang 'to make go' ... > PWGmc *laidijan 'to lead' > *ladjan > OE lǣdan` [@RingeTaylor2014].
- Ringe vol. 1 and Kroonen both support the comparative lexeme as PGmc `*laidijaną/*laidjan-` ‘to lead’ [@Ringe2006; @Kroonen2013].
- Clark Hall and Bosworth-Toller both treat `lædan` as an ordinary OE weak-verb headword meaning ‘lead, guide, conduct, carry, bring’, so the row is philologically straightforward at the lemma level [@ClarkHall1960; @BosworthToller1898].
- No separate row-specific pilot report, dossier, or known-problem file supersedes the live row.

## Reconstruction and early-stage forms

This row still needs the usual three-way distinction, even though two levels happen to coincide in the live TSV:

1. **Cognate-set proto:** `*láidijaną` in TSV `PROTO`, i.e. the comparative Proto-Germanic causative/weak-verb lexeme.
2. **Project input form:** `*láidijaną` again in TSV `PROTOFORM`; here the OE-facing derivational input is the same form as the cognate-set headword, so there is no special split like rows where `PROTO` and `PROTOFORM` diverge.
3. **OE target form:** `lǣdan`, the Old English infinitival citation form represented by the row.

The important early-stage distinction is therefore not `PROTO` versus `PROTOFORM`, but **PGmc input versus later intermediate shorthand**. Current project practice keeps the PGmc `*-ij-` form `*láidijaną`; older `DEV_NOTES` material also shows a post-syncope shorthand `*laidjăną`, but that is now superseded. Kroonen’s dictionary headword `*laidjan-` is compatible with the row as morphological shorthand, while Ringe & Taylor’s fuller `*laidijană` matches the current TSV notation more directly [@Kroonen2013; @RingeTaylor2014].

## Old English philology

This is an **attested OE lemma**, not a reconstructed target and not a special paradigm-cell selection. The target is the infinitive/citation form `lǣdan` (dictionary spelling often `lædan`), and the repo evidence does not require any stronger manuscript or dialect claim than that [@ClarkHall1960; @BosworthToller1898].

Two philological cautions matter:

- The row is the **verb** ‘to lead’, not the noun `lēad` ‘lead/metal’, so the local lexical-table hit is a red herring.
- The semantics in comparative sources may be glossed either as ‘to lead’ or as the causative ‘to make go’; those are not competing reconstructions for the row, but two ways of describing the same causative weak verb [@RingeTaylor2014; @Kroonen2013].

Nothing in the checked repo sources suggests that the OE target itself is problematic, unattested, dialect-smoothed, or analogically retargeted.

## Project problem and solution

The project problem here is mainly **source hygiene**, not derivational failure.

- The live row is already regular and already outputs `lǣdan`.
- The packet nevertheless surfaces one stale `DEV_NOTES` hit (`*laidjăną`) and one irrelevant lexical-table hit (`lēad`), both of which could mislead a later report if copied uncritically.
- The correct project reading is simple: row 2093 represents the regular OE reflex of PGmc `*láidijaną`, with current PGmc `*-ij-` notation preserved in both `PROTO` and `PROTOFORM`, and with `lǣdan` as the ordinary OE verbal target.

So the memo/report should not invent a special OE problem. Its job is to keep current evidence separate from superseded notation history and unrelated lexical noise.

## Paradigm probe

No paradigm probe is required.

This row is not a late-cell selection case, an unresolved mismatch, or a known unmodelled exception. The system already returns the expected infinitive `lǣdan`, and the only real memo task is evidential clarification. A probe would add little unless someone later wants a purely demonstrative class-I weak-verb appendix.

## Recommended final report

Recommend a short final report stating that row 2093 is a regular weak verb `*láidijaną -> OE lǣdan`, citing Ringe & Taylor and Kroonen for the PGmc causative/‘make go’ background and Clark Hall/Bosworth-Toller for the ordinary OE lemma. The report should explicitly dismiss the packet’s `lēad` lexical-table hit as irrelevant and treat older `*laidjăną` notation only as superseded project history.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no change required. The current note is brief but materially correct; the fuller distinctions belong in the eventual lexeme report rather than in the TSV cell.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** minor cleanup recommended. The superseded table containing `*laidjăną` is already labelled as old history in context, but a clearer inline note on the table row or section would reduce the chance that packet excerpts make it look current.
- **Dossier text:** no change recommended; no row-specific dossier text was found.

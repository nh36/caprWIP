# Research memo — 2230 summer / sumer

## Starting point

- **ID:** 2230
- **CONCEPT:** summer
- **COUNTERPART:** sumer
- **PROTO:** *súmaraz
- **PROTOFORM:** *súmaraz
- **DERIVATION_CLASS:** regular
- **NOTE:** Note: proto corrected *sumerăz→*sumarăz (Kroonen *sumara-, R/T *sumaraz both have *a). Both sumer and sumor attested (Kroonen); sumer is the regular reflex via a-fronting (R/T §5.1.2, §6.9.6). sumor has unexplained -o- (R/T §3.1.5).

This is a note-bearing `regular` row in `coverage_audit.md`. No standalone pilot/full lexeme report for this lexeme turned up; debug-snapshot prose is background only, not final authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet trace showing `*súmaraz -> sumer`; and the packet’s use of `analysis/arestoration_r_l_research.md` to show that row 2230 is unaffected by the A-restoration `r/l` issue because the stressed vowel is `*u`, not `*a`.
- **Useful background:** `analysis/unstressed_e_o_before_r.md` is still the main repo-local argument that `sumer` is the regular outcome and that `sumor` belongs to the messy unstressed `a/o` variation; the packet’s `old_english_wiktionary.tsv` hit is useful evidence for the common citation/headword tradition `sumor`.
- **Stale or superseded:** parts of `analysis/unstressed_e_o_before_r.md` are written from an older project state in which the TSV still had proto `*sumerăz` and target `sumor`; its action-item wording (“fix proto AND target”) is therefore historical workflow, not live row status. `DEV_NOTES.md` still preserves the obsolete proto string `*sumerăz` in a ProtoInput-failure list.
- **Irrelevant or misleading if over-read:** the packet’s repeated “key question” snippets from `unstressed_e_o_before_r.md` are useful framing, but not independent evidence; and the packet’s local lexical-table hit `sumor` should not be treated as disproving the live target `sumer`, because the repo’s dictionary/reference layer also preserves `sumer` and especially oblique `sumeres`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 2425.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/oe_known_problems.tsv` — no entry for row 2230.
- `Germanic/data/old_english_wiktionary.tsv` — gives citation/headword `sumor`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — `*sumara-`, OE `sumer, sumor`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — alternate proto `*sumeraz`, OE `sumer`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — PGmc `*sumaraz > OE sumor` in the handbook overview, plus the phonological sections cited in the row note.
- `docs/references/campbell_old_english_grammar.txt` — `sumor` under retention of root `u` before single `m`; useful for the first syllable, not for deciding medial `-e-/-o-`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — `sumor m., gs. sumeres, ds. sumera, sumere`.
- `docs/references/bright_anglo_saxon_reader.vision.txt` — `sumor (sumer), m.` with gen.sg. `sumeres`.
- `docs/references/luick_historische_grammatik.txt` and `docs/references/kaluza_historische_grammatik_englisch.txt` — later English reflex history with both `sumer/somer` and `sumeres/Someres` type evidence.
- No pilot lexeme report for summer is present under `Germanic/docs/lexeme_reports/pilot/`.

Main result of that wider pass: repo-local reference material supports a real split between the common dictionary/citation form `sumor` and an `e`-vocalism tradition (`sumer`, `sumeres`) that fits the project’s regular derivation.

## Reconstruction and early-stage forms

This row still needs the standard three-way distinction even though the live TSV repeats the same form in both proto columns.

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*súmaraz`, the project’s chosen PGmc headword for the lexeme.
2. **Project derivational input:** TSV `PROTOFORM` `*súmaraz`, i.e. the same lexeme-level input; this is not a paradigm-cell workaround row.
3. **OE target represented by the row:** `sumer`, the OE form the project currently chooses to represent the regular outcome.

The important reconstruction issue is not `PROTO` versus `PROTOFORM`, but which PGmc vocalism the project follows in the unstressed syllable. Repo-local sources are not unanimous: Kroonen has stem notation `*sumara-`, Ringe-Taylor has `*sumaraz`, but Orel gives `*sumeraz`. The live row has already chosen the Kroonen/Ringe-Taylor side, and the older project string `*sumerăz` survives only as stale history in some analysis/notes. That means the memo should treat current TSV `*súmaraz` as the active project input while acknowledging that at least one repo-local handbook preserves an alternate etymological reconstruction.

## Old English philology

- **Attested vs. reconstructed:** exact `sumer` is not merely a project invention; Kroonen lists OE `sumer, sumor`, Orel lists OE `sumer`, and Bright has `sumor (sumer)`. But the lexical-table and dictionary headword tradition still leans toward `sumor` as the ordinary citation form.
- **Citation form vs. inflected form:** Clark Hall and Bright are especially important because they both give oblique `sumeres`, and Clark Hall also gives datives `sumera, sumere`. So the repo’s strongest direct support for `e`-vocalism is not only the nominative variant `sumer`, but the oblique paradigm.
- **What Campbell does and does not settle:** Campbell’s `sumor` example is about retention of root `u` before single `m`; it does not decide the second-syllable `-o-` versus `-e-` problem. It is therefore relevant to the first syllable only.
- **Dialect/manuscript caution:** the repo-local sources checked here do not justify a strong dialectal claim such as “`sumer` is specifically West Saxon” or “`sumor` is specifically late”; the safer statement is that both spellings are in the tradition, with `sumer` matching the regular derivational path and `sumor` remaining the common lemma spelling.

The safest philological framing is therefore: common citation/headword `sumor`, attested competing `sumer`, and oblique evidence `sumeres/sumere` that strongly supports the row’s `e`-vocalism.

## Project problem and solution

The project problem is representational rather than computational. The FST already gives the row’s target `sumer`, so this is not a case of a broken derivation or a missing paradigm-cell workaround.

The issue is that the ordinary OE lexical tradition often cites `sumor`, while the project wants the regular derivational output from the chosen PGmc input. The current solution is coherent:

- keep `PROTO` and `PROTOFORM` at lexeme-level `*súmaraz`;
- keep `COUNTERPART = sumer` as the regularized/project-selected OE target;
- explain in the note and eventual report that `sumor` is also attested and is often the default citation form, but that its medial `-o-` is not what the project treats as the regular output of the sound-law pathway.

That is a genuine `regular` row with a philological note, not a `late_analogy` or paradigm-cell row.

## Paradigm probe

A paradigm probe is **not required** for the present recommendation.

Nothing in the current solution depends on selecting one paradigm cell over another, and the row already derives directly from lexeme-level `*súmaraz`. The decisive issue is the relation between regular derivational output `sumer` and competing attested citation form `sumor`, which is better handled as source commentary than as a probe table.

If the supervisor later wants an illustrative comparison, it would be optional background only: nom./citation tradition `sumor` beside attested/regularized `sumer`, with oblique `sumeres` as supporting evidence.

## Recommended final report

Recommend a short final report that says row 2230 keeps lexeme-level PGmc `*súmaraz` and selects OE `sumer` because repo-local phonological analysis treats `-e-` as the regular outcome, while `sumor` remains an attested and common dictionary headword with unexplained or later secondary `-o-`. It should explicitly mention oblique `sumeres` as supporting evidence and avoid claiming that `sumer` is the only attested OE form.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended; `sumer` is defensible as both the FST output and an attested `e`-variant.
- **TSV `DERIVATION_CLASS`:** no change recommended; `regular` still fits.
- **TSV `NOTE`:** **change recommended** for clarity. Keep the present conclusion, but tighten the wording so it explicitly says that `sumor` is the common citation/headword form, that `sumer` is the project-selected regular/attested variant, and that the older corrected proto notation should be harmonized with the live TSV spelling.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** **change recommended** in `Germanic/docs/DEV_NOTES.md` at 2425, where obsolete `*sumerăz` still appears in a live TODO example. No separate dossier text change is currently required; the packet did not identify a dedicated summer dossier, and the broader analysis files are usable so long as their stale action-item language is read as historical background.

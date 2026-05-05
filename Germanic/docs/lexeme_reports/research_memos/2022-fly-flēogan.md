# Research memo — 2022 fly / flēogan

## Starting point

- **ID:** 2022
- **CONCEPT:** fly
- **COUNTERPART:** `flēogan`
- **PROTO:** `*fléuganą`
- **PROTOFORM:** `*fléuganą`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `R/T 10088: PGmc *fleugaṇ > OE flēogan; flȳġe is derived form`

This is a note-bearing regular row, so it still needs lexeme-report treatment even though the live derivation is currently regular.

## Packet evidence assessment

- **Authoritative/current:** the packet’s live TSV row and compact derivation trace are current and internally consistent: `PROTO = PROTOFORM = *fléuganą`, `COUNTERPART = flēogan`, and the live trace gives `EXPECTED: flēogan`, `OUTPUTS: flēogan`.
- **Useful background:** the packet’s Ringe/Taylor-derived smoothing material is useful background for related dialectal or derived forms: repo-local evidence supports West Saxon `fléogan` beside Anglian `flégan`, and also related nominal material such as `fléoge/flége`. The packet’s `old_english_swadesh.tsv` hit is also useful because it cleanly supports verbal `to fly = flēogan`.
- **Stale or superseded:** the packet itself is fairly clean, but wider repo history preserves an older debugging stage where the row was being judged against `EXPECTED: flȳġe`; those mismatch snapshots are superseded by the current row note and current exact-match trace.
- **Irrelevant or misleading if taken at face value:** the packet’s `old_english_wiktionary.tsv` hit `fly = flȳġe` is not good authority for this row. The English gloss is category-ambiguous, and the row note already says `flȳġe` is a derived form rather than the verbal target. Likewise the `DEV_NOTES` hit on hypothetical `*fláugiz -> flīeġ` is background on a related derivative, not evidence that row 2022 should target anything other than `flēogan`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` 35460-35472.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md` 78-81 and 710-716.
- `Germanic/docs/non_firing_rules_analysis.md`.
- `Germanic/docs/debug_snapshots/oe_full_trace_report_2026-02-07_post_root_noun_fix.txt`.
- `Germanic/docs/debug_snapshots/oe_mismatch_report_2026-02-07_post_root_noun_fix.txt` and `oe_mismatch_report_2026-02-07_short_o_fix.txt`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/old_english_swadesh.tsv`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/bright_anglo_saxon_reader.vision.txt`.
- `docs/references/seebold_vergleichendes_woerterbuch.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.

Main findings from that wider check:

- There is **no dedicated dossier** and no existing pilot/full lexeme report for this lexeme in the repo.
- Ringe/Taylor in the local reference dump gives the core current evidence: `PGmc *fleugana 'to fly' ... > OE fléogan` (line 10088), and later explicitly distinguishes West Saxon `fléogan` from Anglian `flégan`, alongside related noun material `fléoge/flége` (line 17725).
- The local Campbell dump confirms relevant philological background but also shows why caution is needed: `flégan (W-S fliegan)` appears there for **“put to flight”**, not as authority to retarget row 2022 away from verbal `flēogan`.
- Bright and Seebold both support the ordinary strong-verb paradigm (`flēogan, flēag, flugon, flogen`), and Bright also has `fleogeð`; these are the most useful local confirmations that the row is about an attested verbal lexeme, not an isolated reconstruction.
- `old_english_swadesh.tsv` supports `to fly = flēogan`, while `old_english_wiktionary.tsv` gives `fly = flȳġe`; taken together, they show an English-gloss collision between the verb and a related derived/headword form.
- Older debug snapshots where `*fleugăną -> flēogan (expected flȳġe)` are best read as project-history evidence for that gloss collision, not as live evidence against the current row.

## Reconstruction and early-stage forms

For this row the project distinction is simple but still needs to be stated explicitly:

1. **Cognate-set proto:** `*fléuganą` / Ringe-Taylor-style `*fleugana`, the verbal etymon ‘to fly’.
2. **Project input form:** `*fléuganą`, identical here to TSV `PROTO`; there is no separate OE-only workaround input.
3. **OE target form:** `flēogan`, the verbal citation form represented by the row.

The important contrast is not between `PROTO` and `PROTOFORM`, which agree here, but between the **verbal** etymon/input and other related formations mentioned elsewhere in the repo:

- the noun-like/derived material `fléoge/flége` in Ringe/Taylor’s dialect table;
- the hypothetical i-stem derivative `*fláugiz -> flīeġ` in `DEV_NOTES`;
- the lexical-table form `flȳġe`, which the live TSV note already excludes as the row’s target.

Those forms are useful background for the lexeme family, but they should not be collapsed into the row’s own derivational input or target.

## Old English philology

`flēogan` is an **attested OE verb**, not a reconstructed-OE target. The repo’s local reference files support it as a citation-form strong verb with paradigm forms such as `flēag`, `flugon`, and `flogen`; Bright also gives `fleogeð`. The live row therefore belongs to the ordinary verbal lexeme, not to a special reconstructed-only category.

The main philological issue is **citation form vs. related derivative/headword material**:

- the row targets verbal infinitive/citation `flēogan`;
- related noun or derivative forms such as `fléoge/flége` or `flȳġe` are not the same target;
- Anglian `flégan` is dialect background, not the normalized counterpart currently selected for the row.

This also means the English gloss “fly” is potentially misleading if part of speech is left implicit. Repo-local lexical tables split between verbal `flēogan` and non-row `flȳġe`, so the final report should say explicitly that row 2022 is the **verb ‘to fly’**.

## Project problem and solution

The project problem here is not an unresolved sound change. It is a **lexeme-disambiguation problem** caused by the English gloss “fly” pointing to more than one Old English form in repo-local materials.

Older debug history shows exactly that confusion: earlier mismatch snapshots treated `flȳġe` as the expected target and therefore misread the regular verbal output `flēogan` as a failure. The current row note fixes the issue at the lexical level by stating that `flȳġe` is derived and that the row should target `flēogan`.

So the current project solution is the right one:

- keep `PROTO = *fléuganą`;
- keep `PROTOFORM = *fléuganą`;
- keep `COUNTERPART = flēogan`;
- keep the row as `regular`;
- mention `flȳġe`, `fléoge/flége`, and Anglian `flégan` only as related background forms, not as reasons to retarget the row.

## Paradigm probe

A paradigm probe is **not required** for the current memo.

The live issue is already settled by source discrimination: the row is about the attested verbal citation form `flēogan`, while `flȳġe` and similar forms belong to related but different lexical material. This is not a case where the project chose one paradigm cell over another to rescue the row.

If a later appendix wants an explanatory probe anyway, the most useful cells would be the verbal ones:

- infinitive / citation form;
- 3sg present (`fleogeð`);
- preterite singular (`flēag`);
- preterite plural (`flugon`);
- past participle (`flogen`).

But that would be optional exposition, not a prerequisite for the final report.

## Recommended final report

Recommend a short final report stating that row 2022 is a regular derivation of the **attested OE verb** `flēogan` from verbal `*fléuganą`, and that the note exists mainly to prevent confusion with related non-row forms such as `flȳġe`, `fléoge/flége`, and dialectal `flégan`.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no change required. The current note already captures the key project distinction by saying that `flȳġe` is derived rather than the row target. An optional future clarification could add “verb” explicitly, but the memo does not require a TSV edit.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change recommended. `DEV_NOTES` is only giving derivative-family background here, and there is no dedicated dossier to revise for this lexeme. Older mismatch/debug snapshots are historical and potentially misleading if read without context, but they are not themselves grounds for changing `DEV_NOTES` or dossier prose.

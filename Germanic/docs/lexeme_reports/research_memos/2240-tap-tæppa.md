# Research memo — 2240 tap / tæppa

## Starting point

- **ID:** 2240
- **CONCEPT:** tap
- **COUNTERPART:** tæppa
- **PROTO:** *táppô
- **PROTOFORM:** *táppô
- **DERIVATION_CLASS:** known_unmodelled
- **NOTE:** The live TSV note treats OE `tæppa` as an attested masculine n-stem nominative singular whose `æ` is analogical. The regular FST output from `*táppô` is `tappa` by A-restoration; no inherited nominal cell yields lautgesetzlich `tæpp-`, and the co-radical j-verb pathway yields `teppan`, not `tæppan`.

## Packet evidence assessment

**Authoritative/current in the packet:**

- The live TSV row, the compact derivation trace, and the matching `oe_known_problems.tsv` entry all agree on the current project position: `*táppô` is being kept as a documented analogical exception, not as an unresolved phonology bug.
- The packet's later `DEV_NOTES` material from `§17.10.16b-c` and `§17.27` is current and decisive. Those sections explicitly reject the j-verb rescue, keep the noun `*táppô`, and classify the row as `analogical_n_stem_levelling`.
- The packet's attestation snippets for `tæppa`, `tæppere`, and `tæppestre` are useful current philological evidence that the `tæpp-` root vocalism is real in OE.

**Useful background but not final authority:**

- `pilot/tap.md` is a good background summary of the present analysis, but it is still pilot prose.
- `Germanic/docs/analysis/arestoration_r_l_research.md` is relevant general support: it confirms that A-restoration across a single consonant like `p` is normal, so `*táppô > tappa` is exactly the sort of output the FST ought to give.
- The lexical-table hit in `old_english_wiktionary.tsv` is useful headword confirmation, but it is only supplementary.

**Stale or superseded material inside the packet:**

- The packet still includes the earlier `DEV_NOTES` discussion at `§3.155 ff.` / `§3.220 ff.` proposing an oblique n-stem rescue (`*tappăn > tæppan`). That is no longer the live analysis; the later revised sections explicitly say no nominal cell yields lautgesetzlich `tæpp-`.
- The packet also preserves the first `§17.10.16` proposal to reinterpret the row as j-verb `*táppjaną > tæppan`. `§17.10.16b` supersedes that proposal by probe result: the regular j-verb output is `teppan`, not `tæppan`.
- The hit at `DEV_NOTES` line 36670 (`*táppô ... now matching`) is diagnostic project history from a transient wrong-side-of-correct regression, not evidence for the lexeme's true analysis.

**Irrelevant or misleading packet material:**

- Most of the packet's generic keyword hits on `i-umlaut` or `A-restoration` in unrelated analysis/dossier files are not row-specific evidence and should not be weighted like the dedicated `tap` discussion.
- The packet's preserved older row number (`1202`) is just project-history numbering; the live aligned row is 2240.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md`:
  - `§3.155-3.253` for the earlier nominal-paradigm discussion;
  - `§17.10.16-17.10.16c` for the j-verb proposal, its probe failure, and the revised conclusion;
  - `§17.27` for the final ledger triage.
- `Germanic/data/oe_known_problems.tsv`, which now records `*táppô` as `exception / analogical_n_stem_levelling`.
- `Germanic/docs/lexeme_reports/pilot/tap.md`, treated as background only.
- `Germanic/docs/analysis/arestoration_r_l_research.md`, because the packet names it and it supports the regularity of `tappa`.
- `Germanic/data/old_english_wiktionary.tsv`.
- Direct reference checks in:
  - `docs/references/legacy/orel_handbook_germanic_etymology.txt`;
  - `docs/references/kroonen_2011_n_stems.vision.txt`;
  - `docs/references/legacy/fulk_comparative_grammar_early_germanic.txt`;
  - `docs/references/legacy/aconciseanglosa01hallgoog.txt`;
  - `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.

I did **not** find a dedicated tap-specific dossier beyond the packeted `DEV_NOTES` discussion and the pilot report. The main extra repo value comes from checking the later closure section, the known-problems ledger, and the dictionary/reference files directly.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction kept explicit.

- **Cognate-set proto / etymological headword:** the noun represented in the comparative sources as Orel `*tappòn` and in the live TSV as `*táppô`. This is the inherited n-stem lexeme heading the cognate set.
- **Project input form used for derivation:** also `*táppô` in the current row. The project is no longer claiming that some different inherited PGmc input solves the OE form.
- **OE target form represented by the row:** attested noun `tæppa`, specifically the nominative-singular headword/citation form, not an oblique `tæppan` and not a verbal infinitive.

The regular nominal path is the one the FST now gives: `*táppô > *tappō > *tappu > *tæppu > *tappu > tappa`, i.e. AFB followed by A-restoration before the back-vocalic ending. That is why `tappa` is the correct inherited output from the chosen input.

The key reconstruction point is that the repo's **current** position no longer accepts either of the older rescue routes:

- the older oblique-cell idea is now treated as mistaken project history, not as the live nominal analysis;
- the j-verb `*táppjaną` remains relevant only as a derivationally related background form, because its regular OE outcome is `teppan`.

So the present row is intentionally a case where cognate-set proto and project input stay the same (`*táppô`), while the OE target `tæppa` is acknowledged to be analogically remodelled.

## Old English philology

This is **not** a reconstructed-OE row. `tæppa` itself is a real OE noun form in the repo's local reference base.

- Orel gives OE `tæppa` under `*tappòn`.
- Kroonen's n-stem material likewise includes OE `tæppa`.
- Clark Hall gives `tæppa` as the noun headword and also lists `tæppere` and `tæppestre`.
- Hall's OCR `winteppere` supplies the expected tapster derivative in the same lexical family.

What the philology does **not** currently support in repo-local evidence is equally important:

- no secure local attestation was found for noun-oblique `tæppan`;
- no secure local attestation was found for a base verb `tæppan`;
- the memo should therefore not treat the old `tæppan` target as if it were the attested core OE form for this row.

The philological center of gravity is the noun headword `tæppa` with derivational family members in `tæppere` / `tæppestre`. The analogical `æ` is therefore a real OE fact, but its exact spread across the family is an inferred historical explanation, not a directly attested regular sound-law derivation.

## Project problem and solution

The project problem is not lexeme identity or dictionary attestation. It is that the attested OE noun has front `æ`, while the inherited phonological derivation from `*táppô` gives `tappa`.

The repo's current solution is coherent and should be preserved:

- keep the noun analysis rather than retargeting to an oblique noun form;
- keep `PROTO = PROTOFORM = *táppô`, because no better inherited input solves the target;
- keep `COUNTERPART = tæppa`, because that is the attested OE form the row really wants to represent;
- keep `DERIVATION_CLASS = known_unmodelled`, because the mismatch is historically intelligible but not something the FST should be expected to derive.

In short, row 2240 is now a worked example of a **documented analogical exception**. Earlier project phases tried to convert it into a clean regular match; the present repo state explicitly rejects those repairs.

## Paradigm probe

A fresh paradigm probe is **not strictly required** to settle this memo.

The decisive repo conclusion already comes from later `DEV_NOTES` analysis plus the known-problems ledger, and `pilot/tap.md` already contains a minimal contrastive probe showing `*táppô > tappa` and a representative oblique stem comparison that still fails to reach `tæpp-`.

If the eventual final report wants a compact diagnostic table, it would be enough to refresh or restate only these contrastive cells:

- noun nom.sg. `*táppô` -> expected `tappa`;
- representative n-stem oblique material (`*tappan-` / `*tappum-`) to show that nominal alternatives still do not yield `tæpp-`;
- rejected j-verb `*táppjaną` -> `teppan`.

But that would be explanatory background, not a search for a new TSV fix.

## Recommended final report

Recommend a concise final report that presents `tæppa` as an attested OE noun kept under `known_unmodelled`: distinguish the cognate-set noun `*táppô/*tappòn` from the rejected j-verb and oblique-cell rescue proposals, state that the regular inherited OE outcome is `tappa`, and explain that the attested `æ` is a later analogical reshaping plausibly connected with the wider `tæpp-` derivational family. The earlier `tæppan`-based rescue attempts should be mentioned only as superseded project history.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no essential change recommended. The live note already states the core current conclusion well.
- **`oe_known_problems.tsv`:** no change recommended. Its `analogical_n_stem_levelling` entry matches the best current repo conclusion.
- **`DEV_NOTES` text:** light cleanup recommended. The earlier oblique-cell and first j-verb rescue subsections should be marked a bit more explicitly as superseded, since packets still surface them prominently alongside the live conclusion.
- **Dossier text:** no change recommended. I did not find a separate tap-specific dossier needing revision.

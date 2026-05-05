# Research memo — 2186 show / sċēawian

## Starting point

- **ID:** `2186`
- **CONCEPT:** `show`
- **COUNTERPART:** `sċēawian`
- **PROTO:** `*skáwōjaną`
- **PROTOFORM:** `*skáwōjaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Normalized sċ: initial sc always [ʃ] in OE (Campbell §440).`

This is the ordinary OE lemma row for 'show', not one of the separate finite-cell companion rows (`2317 sċēawa`, `2318 sċēawaþ`).

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the compact derivation trace with exact current match `*skáwōjaną -> sċēawian`; the packet's exact-pair `DEV_NOTES` hit at `26631-26632`, which correctly states that Class II `*-ōjan-` has `*ō` between `*w` and `*j`; and the packet's lexical-table hit `show -> scēawian`.
- **Useful background:** the packet's copied `DEV_NOTES` material at `3648-3650`, because it preserves the older show-family debugging history and helps explain why the normalization note exists at all.
- **Stale or superseded:** `DEV_NOTES` `3648` is no longer a live mismatch; it still says `expected scēawian`, whereas the project now deliberately normalizes initial `sc-` to `sċ-`. The neighboring `3649-3650` lines are also older family history, not current authority for row 2186.
- **Irrelevant or misleading:** the packet's generic concept-name `DEV_NOTES` hits unrelated to `show` or row `2186` are noise, not lexical evidence. The absence of dossier/analysis hits in the packet is also not evidence against the row; it just means this lemma never required a dedicated dossier.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` rows `2186`, `2317`, and `2318`.
- `Germanic/docs/DEV_NOTES.md` at `2821-2834`, `2954-2994`, and `26631-26680`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.
- `docs/references/bright_anglo_saxon_reader.vision.txt`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/docs/lexeme_reports/research_memos/2317-show-(iptv.2sg)-sċēawa.md` and `2318-show-(3sg)-sċēawaþ.md` as background only.

Main findings from the extra check:

- `old_english_wiktionary.tsv` gives the lemma spelling `scēawian`.
- `bright_anglo_saxon_reader.vision.txt` also lists `scēawian (W. II.)` and gives related finite forms `scēawa` and prefixed `-sceawað`; this supports the show-family stem shape even though row `2186` itself is the infinitive lemma.
- `oe_known_problems.tsv` has no entry for this lexeme.
- No show-specific dossier, analysis memo, or pilot/full lexeme report exists for row `2186`; the only nearby materials are the separate research memos for rows `2317` and `2318`.

## Reconstruction and early-stage forms

Three levels need to stay separate:

1. **Cognate-set proto / row input:** for row `2186`, `PROTO` and `PROTOFORM` are both `*skáwōjaną`.
2. **Related project stem label for companion finite cells:** `*skawōną` belongs to rows `2317/2318`, not to this lemma row.
3. **OE target represented here:** project-normalized `sċēawian`, corresponding to source-spelled `scēawian`.

The important reconstruction point is that this is a Class II `*-ōjan-` verb. The repo's later `DEV_NOTES` correctly treat row `2186` as safe because `*ō` intervenes between `*w` and `*j`; this is therefore not one of the true `*aw+j` cases that feed the separate `ēa/ēġ` problem space. The current derivation trace `*skáwōjaną -> *skḗawōjaną -> ... -> sċēawian` is consistent with that analysis.

## Old English philology

- **Attested/source lemma:** repo-local lexical materials give `scēawian`, not a different headword.
- **Project-normalized target:** `sċēawian` is an editorial normalization of initial `sc-`, not a separate attested spelling.
- **Related inflected forms:** `Bright` lists imperative `scēawa` and prefixed 3sg `-sceawað`, which help anchor the family but should not be confused with the lemma row itself.

So the final report should distinguish clearly between source spelling (`scēawian`) and project normalization (`sċēawian`). I did not find a fuller manuscript or dialect dossier, so the report should avoid over-specific claims about dialect distribution or individual witnesses.

## Project problem and solution

The project problem here is mostly historical/debugging, not philological. Older `DEV_NOTES` show an earlier pipeline stage that produced `sċaweian` or treated `sc/sc̣` normalization inconsistently. Current project evidence shows that the lemma row itself is straightforward:

- keep row `2186` as the ordinary weak Class II infinitive `*skáwōjaną -> sċēawian`;
- keep rows `2317` and `2318` as separate finite-cell companions rather than folding them into the lemma row;
- treat the old missing-`ēa` and `sc/sċ` mismatch notes as superseded project history, not as a live lexical problem.

## Paradigm probe

**No separate paradigm probe is required for row `2186` itself.** Direct lemma evidence (`scēawian`) plus the current exact-match derivation trace already establish the row.

If the project later formalizes a reusable show-family probe, it should compare at least these cells:

- `*skáwōjaną -> sċēawian` (infinitive lemma)
- `*skáwô -> sċēawa` (imperative 2sg)
- `*skáwōθi -> sċēawaþ` (3sg present indicative)

That would be useful family infrastructure, but it is not a prerequisite for this lemma memo.

## Recommended final report

Recommend a short final report only: present row `2186` as the ordinary weak-Class-II lemma, distinguish source-spelled `scēawian` from project-normalized `sċēawian`, note that current project analysis treats `*skáwōjaną` as a regular `*-ōjan-` case with `*ō` between `*w` and `*j`, and demote older `sċaweian/scēawian` mismatch history to superseded debugging background.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no change recommended. The current note already captures the only live row-specific issue: project normalization of initial `sc-` to `sċ-`.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** change recommended for `DEV_NOTES`, not for dossier text. Older show-family notes at `2829`, `2960-2994`, and `3648-3650` should be marked as superseded debugging history or normalization history. No separate show-specific dossier text was found, so no dossier cleanup is currently needed.

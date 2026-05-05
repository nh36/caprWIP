# Research memo — 2095 learn / liornian

## Starting point

- **ID:** 2095
- **CONCEPT:** `learn`
- **COUNTERPART:** `liornian`
- **PROTO:** `*líznōjaną`
- **PROTOFORM:** `*líznōjaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Northumbrian form (Campbell §154.3 fn.3). WS leornian has analogical eo from paradigm leveling + io/eo merger (§296).`

This is a note-bearing `regular` citation-form row. The live TSV and compact trace both treat the row as the Northumbrian infinitive/citation-form companion to the same learn-family now represented elsewhere by row 2313 `liorna` and row 2314 `liornaþ`. I found no learn-specific pilot/full lexeme report; the only learn-family prose already in the repo is packet material, DEV_NOTES, analysis files, and the newer memos for the finite cells.

## Packet evidence assessment

**Authoritative/current**

- The live TSV row is the present project authority: it keeps `PROTO = PROTOFORM = *líznōjaną`, targets `liornian`, and leaves the row in `regular`.
- The packet's compact derivation trace is current implementation evidence: the live input derives to `liornian`.
- The packet's citation of Campbell via the row note is genuinely relevant philological evidence that the row is intentionally targeting the Northumbrian `io` form rather than standard WS `leornian`.

**Useful background**

- The packet's DEV_NOTES excerpts preserve the history of the earlier `leornian`/`liernian` debugging and are useful for understanding why this lexeme became a project problem.
- The packet's analysis hits from `meord_med_chronological_review.md` and `mismatch_dossier_mizdo_supplement.md` are good comparative background because they show that `leornian ~ liornian` had already become the repo's standard comparison case for `eo/io` variation.

**Stale or superseded**

- The packet's high-confidence DEV_NOTES recommendations to rewrite row 2095 as `*leznōjaną` / `leornian` are superseded by the live row. They record an abandoned WS-oriented workaround, not the current project state.
- `compound_archaism_inventory.md` case 6 is stale for the live TSV: it says the TSV now targets e-grade `*leznōn-` / `leornian`, but the live row instead keeps `*lizn-` and targets Northumbrian `liornian`.

**Irrelevant or misleading if over-read**

- The packet's `old_english_wiktionary.tsv` hit is useful only for lemma-style headword background; by itself it would mislead a reader into thinking the row should be changed back to `leornian`.
- Generic packet hits about `meord` or broader `z`-loss diagnostics are methodological parallels, not direct authority for what row 2095 should target now.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` around rows 2095, 2313, and 2314.
- `Germanic/docs/DEV_NOTES.md` at the 2026-04-07 `leornian` discussion and later extended-research section.
- `Germanic/docs/analysis/compound_archaism_inventory.md`.
- `Germanic/docs/analysis/meord_med_chronological_review.md`.
- `Germanic/docs/analysis/mismatch_dossier_mizdo.md`.
- `Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md`.
- `Germanic/data/oe_known_problems.tsv` (no learn entry).
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.txt`.
- `docs/references/bright_anglo_saxon_reader.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- The related memos `2313-learn-(iptv.2sg)-liorna.md` and `2314-learn-(3sg)-liornaþ.md` as background on the current learn-family project state, not as primary authority.

Main findings from that wider check:

- Campbell is the key OE authority in the repo: `leornian` has `eo` from later breaking of `e`, but Northumbrian also shows `io`; the variation is real and not a good single-form proof text for one sound law.
- Ringe-Taylor and Fulk still treat the comparative reconstruction with `*lizn-`, not with a default `*lezn-`.
- Brunner is useful for the OE-family distribution: he explicitly gives `leornian` and also Northumbrian `liorna`, and he treats the `eo/io` alternation as part of the same verb-family problem.
- Bright and Clark Hall show the lexicographic/headword issue clearly: the usual dictionary headword is `leornian`, but variant `liornian` belongs in the same lexical entry.
- No learn-specific `oe_known_problems.tsv` entry or separate learn dossier currently overrides the live TSV row.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction.

1. **Cognate-set proto / etymological headword:** the comparative tradition in the repo remains `*liznōn-` / `*lizn-`, reflected in the TSV's lexeme-level `PROTO` `*líznōjaną`.
2. **Project input form for this row:** also `*líznōjaną`; unlike rows 2313 and 2314, row 2095 does not switch to a special finite-cell `PROTOFORM`.
3. **OE target represented by the row:** Northumbrian citation-form `liornian`.

So the live row is not claiming that `liornian` is the only OE reflex, and it is not claiming that the comparative proto itself has been rewritten to e-grade `*lezn-`. Rather, the project currently keeps the inherited `*lizn-` cognate-set labeling and uses it to derive the Northumbrian-side OE target directly. The older e-grade `*leznōjaną` proposal is best treated as superseded project history introduced to force the WS comparator `leornian`, not as the current comparative reconstruction.

## Old English philology

- **Attested vs. reconstructed:** the philological issue is not whether OE `liornian` is a fabricated form; the issue is that the lexeme is attested with dialectal `eo/io` variation, while dictionary-style citation tends to privilege `leornian`.
- **Citation form vs. finite forms:** row 2095 is the infinitive/citation-form row; the related finite-cell rows are 2313 `liorna` and 2314 `liornaþ`.
- **Headword issue:** repo-local lexical tables (`old_english_wiktionary.tsv`, Clark Hall, Bright) default to `leornian` as the dictionary headword, sometimes with `liornian` as an explicit variant. That means a final report must say clearly that row 2095 is choosing the Northumbrian citation-form variant, not correcting the dictionaries.
- **Dialect status:** Campbell and the grammatical sources support real Northumbrian `io` forms. But the repo does not yet assemble a full manuscript dossier for the infinitive itself, so the report should say “Northumbrian form/variant” without over-claiming narrower manuscript detail.

## Project problem and solution

The project's older problem was framed as “how do we force WS `leornian` instead of FST `liernian`?” That led to two kinds of now-stale repo history: proposals to change the root to `*lezn-`, and attempts to treat the row as if its main job were to reproduce the WS comparator directly.

The live row solves a different problem:

1. keep the learn lexeme under the comparative `*lizn-` family;
2. keep row 2095 as a citation-form row rather than a paradigm-cell workaround;
3. target the regular Northumbrian-side outcome `liornian`;
4. treat WS `leornian` as the analogically levelled/headword comparator that must be discussed in prose, not forced into this row's `COUNTERPART`.

On the current evidence, that solution is sound. The row is derivationally regular for its chosen target, and the remaining work is explanatory cleanup: future report text needs to tell readers that `leornian` is the mainstream lexicographic headword while `liornian` is the specific OE variant this row encodes.

## Paradigm probe

A paradigm probe is **not required**.

This row is not a hidden oblique-cell or finite-cell rescue case; `PROTOFORM` already matches the citation-form input, and the live compact trace already derives the target directly. I did run a manual family check in `oe_paradigm_probe.py`, and it confirmed that `*líznōjaną -> liornian` while the stale DEV_NOTES comparator `*leznōjaną` instead yields `leornian`; that is useful reassurance, but not a sign that row 2095 needs a formal saved paradigm probe before reporting.

## Recommended final report

Recommend a concise final report that presents row 2095 as the Northumbrian citation-form member of the `learn` family: keep comparative `*lizn-` distinct from the row's OE target, explain that standard lexicographic OE is usually `leornian`, and treat the older `*lezn-` rewrite as superseded project history only.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended; keep the cognate-set proto in the `*lizn-` family.
- **TSV `PROTOFORM`:** no change recommended; this row does not need a special paradigm-cell input.
- **TSV `COUNTERPART`:** no change recommended; `liornian` is the intended Northumbrian target for the live row.
- **TSV `DERIVATION_CLASS`:** no change recommended; `regular` still fits because the row is a citation-form dialect choice, not a paradigm-cell workaround.
- **TSV `NOTE`:** **small change recommended.** Keep the Campbell-based dialect point, but rewrite the note so it explicitly says that the row targets the Northumbrian citation-form variant `liornian`, while standard WS/Mercian headword usage is `leornian`.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** **change recommended.** Old sections that still say row 2095 “should” be rewritten to e-grade `*leznōjaną` / `leornian`, or that the TSV “now targets” e-grade `leornian`, should be marked superseded or revised in `DEV_NOTES.md`, `compound_archaism_inventory.md`, and the learn-precedent remarks in the `mēd/meord` dossier files.

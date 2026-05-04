# Research memo — 2313 learn (iptv.2sg) / liorna

## Starting point

- **ID:** 2313
- **CONCEPT:** `learn (iptv.2sg)`
- **COUNTERPART:** `liorna`
- **PROTO:** `*liznōjaną`
- **PROTOFORM:** `*líznô`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** `Northumbrian iptv.2sg. Uses io from regular breaking; WS leorna has leveled eo.`

This row is not the OE citation-form lexeme row for “learn.” The repo’s ordinary lemma-style OE row is 2095 `learn / liornian`, while row 2313 is a selected finite paradigm cell with a separate `PROTOFORM`. I found no learn-specific pilot/full lexeme report in `Germanic/docs/lexeme_reports/pilot/`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing `*líznô -> liorna`; and the current note that the row intentionally targets Northumbrian `io` rather than West Saxon `eo`.
- **Useful background:** the packet’s `DEV_NOTES` excerpts on the earlier `leorna/leornian` mismatch, because they preserve the project history of why this lexeme family was investigated so heavily.
- **Stale or superseded:** the packet’s `DEV_NOTES` recommendation to rewrite row 2313 as `*leznō / *leznô -> leorna`. That was a project workaround for an earlier West-Saxon-targeting phase, not current authority for the live row; it is also weaker than the comparative evidence, which continues to favor `*lizn-`, not `*lezn-`.
- **Irrelevant or misleading:** the packet’s generic breaking hits and unrelated `meord`-family parallels are methodological background only. They help with chronology, but they are not direct evidence that row 2313 itself should be rewritten.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` around rows 2095 and 2313-2314.
- `Germanic/docs/DEV_NOTES.md` at 2950-2980 and 14648-14918.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/tools/oe_paradigm_probe.py`, plus live manual probe runs.
- `docs/references/campbell_old_english_grammar.txt` (§123 fn.2, §154 fn.3, §202).
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` (weak-verb discussion listing `liornian ~ leornian`).
- `docs/references/brunner_1965_altenglische_grammatik.txt` (§84, §417 anm. 10).
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.
- `docs/references/kilday_2024_crists_law_smiths_law_wizen.txt`.
- `Germanic/docs/analysis/meord_med_chronological_review.md` and `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md` as background on the `meord/leornian` type and on WS-vs.-Anglian diphthong behavior.

Main findings from that wider check:

- `old_english_wiktionary.tsv` gives only the lemma `leornian`, confirming that row 2313 is a finite-cell row, not a dictionary-headword row.
- Brunner explicitly notes `leornian, nordh. auch liorna`, which is the best repo-local support I found for the specific Northumbrian finite form.
- Campbell treats West Saxon `leornian`/`leorna` as the `eo` side of a broader `io ~ eo` variation, and he does **not** make `*lezn-` the etymological solution.
- Ringe-Taylor, Kroonen, and Fulk all continue to treat the comparative reconstruction with `*lizn-`/`*liznōn-`, not `*lezn-`.
- No learn-specific dossier file turned up, and no `oe_known_problems.tsv` entry currently covers this lexeme.

## Reconstruction and early-stage forms

This row requires a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** `*liznōjaną` in the TSV, matching the broader comparative tradition that reconstructs the learn-verb with `*lizn-` (Kroonen `*liznōn-`; Fulk likewise `*lizn-`; Ringe-Taylor with `*lizn-`-based weak-verb alternants).
2. **Project input form for this row:** `*líznô`, i.e. the imperative singular paradigm cell, not the lexeme-level citation form.
3. **OE target form represented by the row:** `liorna`, a Northumbrian finite form.

For row 2313 itself, the current derivation is straightforward:

`*líznô -> *lírnô -> *líornô -> *líorna -> liorna`

That path fits the row’s present target: rhotacism gives `rn`, regular breaking yields `io`, and late unstressed shortening gives final `-a`.

The competing `*lezn-` proposal belongs to project history, not to the comparative reconstruction. It was introduced to force West Saxon `leorn-` directly, but the repo-local scholarly sources do not treat `*lezn-` as the default proto for this lexeme family. For this row, `*leznô` is best treated only as an abandoned WS-oriented workaround.

## Old English philology

- **Attested/cited headword vs. finite form:** repo-local lexical tables and dictionaries give `leornian` as the headword; row 2313 instead targets the imperative singular `liorna`.
- **Dialect distinction:** Brunner’s grammar explicitly supports a Northumbrian `liorna`, while Campbell explains why West Saxon shows `eo` (`leornian`, by implication `leorna`) where Northumbrian can preserve `io`.
- **Citation-form issue:** `liorna` should not be presented as the ordinary OE dictionary lemma for “learn.” It is a selected finite paradigm cell.
- **Manuscript/detail caution:** I found secondary grammatical support for Northumbrian `liorna`, but not a full repo-local dossier with manuscript-by-manuscript documentation. The eventual final report should therefore say “Northumbrian form” confidently, but avoid over-specific source claims not yet assembled in the repo.

## Project problem and solution

The project problem was originally framed too narrowly as “why does `*liznô` not give West Saxon `leorna`?” That led to the `*lezn-` workaround in `DEV_NOTES`.

The current row solves a different and better-defined problem:

- keep the lexeme-level comparative proto with `*lizn-`;
- use a paradigm-cell `PROTOFORM` `*líznô`;
- target the regular Northumbrian finite outcome `liorna`;
- treat West Saxon `leorna` as the analogically levelled comparator, not as the row’s target.

On the live evidence, that solution is sound. It respects the comparative reconstruction, matches the current FST output, and aligns with the row note’s explicit Northumbrian-vs.-WS distinction.

## Paradigm probe

**Yes — a paradigm probe is required.** This is a paradigm-cell row, and `oe_paradigm_probe.py` still has no built-in saved spec for `learn / liorna`.

A live manual probe is already informative:

- `*líznô -> liorna` ✓
- `*leznô -> leorna`
- `*líznōjaną -> liornian`
- `*líznōθi -> liornaþ`

So the decisive contrast is now clear: the inherited `*líznô` uniquely matches the current row target `liorna`, while the earlier `*leznô` proposal instead produces the West Saxon-style comparator `leorna`.

Because the standardized probe is still missing, the formal built-in probe should at minimum cover these cells:

- **infinitive comparator:** row 2095 `*líznōjaną -> liornian`
- **imperative 2sg:** row 2313 `*líznô -> liorna`
- **present 3sg comparator:** row 2314 `*líznōθi -> liornaþ`
- **optional expansion:** present 2sg if/when the probe workflow gets an agreed input template for that cell

## Recommended final report

Recommend a concise final report that presents row 2313 as a deliberate Northumbrian imperative-cell companion to the learn lexeme: keep `PROTO = *liznōjaną`, distinguish row-level `PROTOFORM = *líznô`, identify `liorna` as the selected OE finite target, mention West Saxon `leorna` only as the analogically levelled comparator, and explicitly treat the older `*lezn-` proposal as superseded project history rather than current evidence.

## Data-change recommendations

- **TSV `PROTO`:** **no change recommended.** Keep the cognate-set proto in the `*lizn-` family; do **not** rewrite this row to `*lezn-`.
- **TSV `PROTOFORM`:** **no change recommended.** `*líznô` is the right project input for the current Northumbrian imperative target.
- **TSV `COUNTERPART`:** **no change recommended.** `liorna` matches both the current live derivation and the repo-local Northumbrian grammatical evidence.
- **TSV `DERIVATION_CLASS`:** **no change recommended.** `late_analogy` still works for a non-lemma paradigm-cell row created because the ordinary West Saxon lexeme family shows analogical leveling.
- **TSV `NOTE`:** **minor change recommended.** The note is basically right, but it should say a bit more explicitly that `liorna` is a selected Northumbrian imperative-cell target rather than the lemma, and that `leorna` is only the West-Saxon comparator.
- **`oe_known_problems.tsv`:** **no change recommended.**
- **`DEV_NOTES` text:** **change recommended.** The 2026-04-07 `*lezn-` recommendation should be marked more explicitly as superseded/background-only now that the live row targets Northumbrian `liorna` and the comparative reconstruction remains `*lizn-`.
- **Dossier text:** **no change recommended.** I found no learn-specific dossier text that needs row-level cleanup.

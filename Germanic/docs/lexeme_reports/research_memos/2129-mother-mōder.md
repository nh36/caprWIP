# Research memo — 2129 mother / mōder

## Starting point

- **ID:** 2129
- **CONCEPT:** mother
- **COUNTERPART:** mōder
- **PROTO:** *mōdēr
- **PROTOFORM:** *mōdēr
- **DERIVATION_CLASS:** regular
- **NOTE:** Note: mōder is the regular nom.sg. reflex (cf. dat.sg. mēder < *mōdri). R/T §7.2.1: modor ~ -ur has suffixal vowel leveled from oblique cases (analogical).

This is a note-bearing regular row in `coverage_audit.md`. No standalone pilot/full lexeme report for this lexeme turned up; generated debug-snapshot prose is background only, not final authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet trace showing `*mōdēr -> mōder`; and `analysis/unstressed_e_o_before_r.md`, which is the clearest current repo-local argument that suffixal `-er` is the regular outcome while `modor/modur` reflects analogical levelling in r-stem kinship nouns.
- **Useful background:** the packet’s lexical-table hits (`old_english_wiktionary.tsv`, `old_english_swadesh.tsv`) showing the ordinary headword tradition `mōdor`; the `DEV_NOTES.md` r-stem-kinship material; and the packet’s reminder that no `oe_known_problems.tsv` entry exists for this row.
- **Stale or superseded as row authority:** generated debug snapshots that merely echo the live TSV note; and packet snippets inherited from unrelated dossiers, especially the `swester/swustor` material, which are methodological parallels rather than direct authority on row 2129.
- **Irrelevant or misleading if over-read:** `analysis/arestoration_r_l_research.md` on late West Saxon `*mēddor` is not evidence that exact row target `mōder` is attested; it is a separate late analogical/doubling phenomenon. Likewise, lexical-table `mōdor` hits are excellent attestation evidence but not direct support for the current exact counterpart string `mōder`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 33096-33112, 34004-34024, and 42727-42733.
- `Germanic/docs/analysis/unstressed_e_o_before_r.md`.
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/old_english_wiktionary.tsv`, `Germanic/data/old_english_swadesh.tsv`, and `Germanic/data/oe_known_problems.tsv`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/hogg_vol1.txt`.

Main findings from that wider pass:

- Kroonen and Orel both keep the lexeme-level proto as PGmc `*mōdēr/*mōder-`; there is no repo-local evidence that TSV `PROTO` or `PROTOFORM` is wrong.
- The philological split is between **regular reconstructed OE nominative** `mōder` and the transmitted/headword tradition `mōdor/modor`. `old_english_wiktionary.tsv`, `old_english_swadesh.tsv`, Kroonen, Orel, Clark Hall, and Bosworth-Toller all point to `mōdor/modor` as the ordinary dictionary form.
- Ringe-Taylor explicitly says that in these back-vocalic kinship terms “the vowel of the suffixal syllable has generally been replaced by u or its later reflex,” citing early Mercian `modur` and early West Saxon `modor ~ -ur`; that is the strongest repo-local support for treating `-or/-ur` as analogical rather than primary.
- Clark Hall and Campbell both preserve oblique `mēder`, and Campbell’s r-stem paradigm gives nom./acc. `médor` beside dat. `mēder`, which fits the TSV note’s use of the oblique as evidence for regular suffixal `-e`.
- No `oe_known_problems.tsv` entry exists, and no existing manual pilot report settles the row differently.

## Reconstruction and early-stage forms

This row still needs the standard three-way distinction, even though the live TSV currently repeats the same proto string in both proto columns.

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*mōdēr`, the PGmc kinship noun ‘mother’.
2. **Project derivational input:** TSV `PROTOFORM` `*mōdēr`, the same lexeme-level proto, because the row is not currently using an oblique paradigm cell as its input.
3. **OE target represented by the row:** `mōder`, i.e. the project’s regularized nominative outcome.

At the sound-change level the repo-local story is straightforward: the unstressed suffixal `*ē` lowers in Northwest Germanic, shortens, and merges to `e` in Old English, so the cascade yields `mōder`. The real disagreement is not proto reconstruction, but whether the row should represent that regularized output or the attested citation/headword form `mōdor`.

The oblique evidence matters, but only as supporting philology: `*mōdri -> mēder` is not the row’s derivational input, yet it helps show why `-e-` is the regular inherited vocalism in the suffix while `-o-/-u-` can be read as later paradigm levelling.

## Old English philology

- **Attested vs. reconstructed:** repo-local lexical and dictionary sources support `mōdor/modor` as the attested citation form and `mēder` as an oblique form. Exact nominative `mōder` is not strongly directly attested in the repo-local evidence and should be treated as a reconstructed or normalized regular outcome if retained.
- **Citation form vs. inflected form:** Clark Hall gives `mōdor (e²) ... ds. mēder`; Campbell’s r-stem paradigm likewise has nom./acc. `médor` and dat. `mēder`. So the row’s note is philologically sensible, but it depends on distinguishing citation `mōdor` from oblique `mēder`.
- **Dialect/manuscript status:** Ringe-Taylor’s evidence is for early Mercian `modur` and early West Saxon `modor ~ -ur`, not for clean direct attestation of `mōder` as the ordinary headword. The memo should therefore avoid presenting `mōder` as a straightforward manuscript citation form.
- **Late secondary material:** Campbell’s late West Saxon `*mēddor` belongs to a separate later analogical/gemination phenomenon and should not be confused with either the regular inherited target or the ordinary dictionary headword.

The safest philological framing is therefore: attested lexical tradition `mōdor/modor`, oblique evidence `mēder`, and project-selected regularized nominative `mōder`.

## Project problem and solution

The project problem here is not an FST failure. The cascade already gives the regular outcome `mōder` from `*mōdēr`.

The real issue is representational:

1. the live row currently chooses the **regular inherited nominative outcome**;
2. the ordinary attested headword tradition is **`mōdor/modor`**, shaped by analogical levelling in the r-stem paradigm; and
3. the note uses oblique `mēder` to explain why the project nevertheless prefers `mōder`.

That solution is coherent, but it means the row is behaving less like an ordinary attested `regular` entry and more like a **reconstructed/normalized OE target chosen for sound-law transparency**. If the project wants the regular inherited form, keeping `COUNTERPART = mōder` is defensible; but the row should then say more explicitly that exact `mōder` is the project’s normalized regular target, not simply the ordinary attested dictionary lemma.

## Paradigm probe

A paradigm probe is **not required** for the present recommendation.

The decisive question is classificatory and philological, not whether some untested paradigm cell yields the target. The row already derives directly from lexeme-level `*mōdēr`, and the supporting oblique `mēder` evidence is a source argument rather than a missing paradigm-cell implementation problem.

If the supervisor later wants a compact comparison, it would be better presented as a source note than as a required probe table: nom.sg. `*mōdēr -> mōder`, attested citation/headword `mōdor/modor`, and oblique `*mōdri -> mēder`.

## Recommended final report

Recommend a short final report that says row 2129 models **reconstructed regular nominative** `mōder` from PGmc `*mōdēr`, while the attested lexical tradition is `mōdor/modor` with oblique `mēder`; it should explain that `-or/-ur` in the kinship r-stems is treated in repo-local sources as analogical levelling and should avoid claiming unqualified direct attestation for exact `mōder`.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no immediate change recommended **if** the project intends this row to represent the regularized inherited nominative. A retargeting to attested `mōdor` would be a different editorial choice, not something forced by the current derivational evidence.
- **TSV `DERIVATION_CLASS`:** **change recommended** from `regular` to `reconstructed_oe`, because exact `mōder` is best supported here as a reconstructed/normalized regular OE target rather than as the ordinary directly attested headword.
- **TSV `NOTE`:** **change recommended.** The note should say explicitly that `mōder` is the project’s regularized nominative target, that attested lexical sources usually give `mōdor/modor`, and that oblique `mēder` supports the inherited `-e-` vocalism behind the normalization.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no major change recommended. `analysis/unstressed_e_o_before_r.md` already captures the current repo-local reasoning well enough; the main needed clarification is in the row metadata, not in the broader dossier prose.

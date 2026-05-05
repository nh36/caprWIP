# Research memo — 2217 still / stillan

## Starting point

- **ID:** 2217
- **CONCEPT:** still
- **COUNTERPART:** `stillan`
- **PROTO:** `*stéllijaną`
- **PROTOFORM:** `*stéllijaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `OE stillan wv. 'to still, calm' matches verb form of Du. stillen, G stillen; stille is adj.`

The live row is already a regular weak-verb derivation. The main interpretive issue is lexical framing: the cognate set mixes English adjective `still` with West Germanic verbal reflexes, and the row note itself signals that OE `stille` is the adjective while this row targets the verb `stillan`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row and the packet's compact derivation trace, which agree that `*stéllijaną` currently derives straightforwardly to OE `stillan`.
- **Useful background:** the row note is worth preserving because it already warns that OE adjective `stille` is related but not the row's target.
- **Stale or superseded:** the packet's `DEV_NOTES` hit at line 8730 (`*stelljăną -> stillan`) belongs to a superseded stage of the Sievers'-Law discussion. The same `DEV_NOTES` section later marks that view as **SUPERSEDED** and adopts PGmc-style heavy-stem `*-ij-` inputs instead, which matches the live TSV.
- **Irrelevant or misleading:** the packet's `old_english_wiktionary.tsv` hit `still -> stille` is adjective-only evidence, not evidence against the verbal target; and the packet's "possibly stale or diagnostic" concept-name hits are unrelated string matches on *still*, not row-2217 lexical evidence.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` around rows 1395-1397 and 2217.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/docs/DEV_NOTES.md` 8564-8760 and 8903-9043 on Sievers'-Law notation and the later decision to keep heavy-stem `*-ijăną` inputs.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`.

Main findings:

- No row-specific dossier, analysis memo, or pilot lexeme report for this lexeme was found, and none was named in the packet or TSV note.
- `oe_known_problems.tsv` has no entry for this row, so the project is not treating `stillan` as a live exception or mismatch.
- `DEV_NOTES` preserves both an older post-leveling `*stelljăną` discussion and a later explicit reversal; for the memo, the later "SUPERSEDED" / "Implementation Status" material is the current project position.
- Clark Hall lists OE `stillan` as a verb and `stille` as the adjective, while Bosworth-Toller gives extensive evidence for the prefixed verbal family `ge-stillan` and related forms [@ClarkHall1960; @BosworthToller1898].
- Kluge treats German `still` and `stillen` as closely related West Germanic material, with the verb derived alongside the adjective; that supports using `stille` as background only, not as the OE target of this row [@KlugeSeebold2011].

## Reconstruction and early-stage forms

This row needs the usual three-way distinction:

1. **Cognate-set proto / project lexeme headword:** TSV `PROTO` `*stéllijaną`, i.e. the verbal j-formation currently used for the set.
2. **Project derivational input:** TSV `PROTOFORM` `*stéllijaną`, identical here to `PROTO`.
3. **OE target represented by the row:** `stillan`, the weak-verb infinitive/citation form.

The key chronological caution is that the live row uses a **PGmc-style heavy-stem `*-ij-` input**, not the later post-syncope shape `*stelljăną` discussed in older `DEV_NOTES`. That later shape is useful historical background, but it is not the current project input. Conversely, OE adjective `stille` and Kluge's West Germanic adjective material belong to a related lexeme family, not to the row's actual OE target.

## Old English philology

Repo-local philology supports a simple distinction:

- **Verb target:** Clark Hall has `stillan` as the OE weak verb headword "to be still; quiet, calm, appease, hush" [@ClarkHall1960].
- **Related adjective:** the same dictionary separately lists `stille` as the adjective "still, quiet, calm" [@ClarkHall1960].
- **Attested verbal family:** Bosworth-Toller's fullest evidence in the repo is under prefixed `ge-stillan`, with meanings such as stopping, silencing, calming, and allaying [@BosworthToller1898].

So the row's OE target should remain the **verbal citation form** `stillan`. The packet's adjective-only lexical-table hit is too weak and too lexically different to overturn that. I found no repo-local basis for making stronger claims about dialect, manuscript distribution, or a need to reconstruct a different OE target.

## Project problem and solution

This is not a sound-change failure. The current derivation already reaches `stillan`, and the row does not belong in an exception class.

The real project problem is **lexical cross-talk**:

- the concept label/English row point toward adjective `still`;
- the Dutch/German and OE row are verbal;
- packet background includes both the verb and the adjective;
- and one packeted `DEV_NOTES` hit preserves a superseded pre-decision notation stage.

The right project solution is therefore:

- keep row 2217 as the **verb** row with `COUNTERPART` `stillan`;
- keep `PROTO` / `PROTOFORM` as `*stéllijaną`;
- treat adjective `stille` as related background only;
- and clarify the row note so later report generation does not flatten adjective and verb into one OE target.

## Paradigm probe

A paradigm probe is **not required** for this row. The project is not rescuing the entry through a hidden paradigm cell, analogical substitution, or reconstructed OE-stage workaround; the live proto input already yields the intended infinitive `stillan`.

## Recommended final report

Recommend a short final report saying that row 2217 is a regular OE weak-verb row: PGmc-style `*stéllijaną` is the current project input, the live derivation produces `stillan`, older `DEV_NOTES` references to post-syncope `*stellj-` are superseded project history, and OE adjective `stille` should be mentioned only as a related but non-target lexeme.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** change recommended. The current note is directionally correct but too compressed about the adjective/verb split. It should say more explicitly that row 2217 targets the OE weak verb `stillan`, while `stille` is only the related adjective and not the row's OE counterpart.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no change required for this row. The relevant `DEV_NOTES` section already marks the older `*stelljăną` position as superseded, and no row-specific dossier text was found.

# Research memo — 2260 token / tācn

## Starting point

- **ID:** 2260
- **CONCEPT:** token
- **COUNTERPART:** tācn
- **PROTO:** *táikną
- **PROTOFORM:** *táikną
- **DERIVATION_CLASS:** regular
- **NOTE:** Proto: oblique *taiknăn→*taikną (n. a-stem nom.sg.; Kroonen)

The live row is a regular derivation with a non-empty note, so it needs memo-level clarification even though the FST already matches the target. No pilot or full lexeme report for this lexeme exists in the repo.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet trace showing `*táikną -> tācn`; and `DEV_NOTES.md` §17.18.7, which is the current project decision for this cluster class and explicitly retains `tācn` among the ten attested unbroken targets.
- **Useful background:** the packet's excerpts from `DEV_NOTES.md` §17.18.1 and §17.18.3 on parasite-vowel chronology, attestation, and the `tācn ~ tācen / tācnes` contrast; `old_english_wiktionary.tsv`; and the bibliography pointers toward Campbell, Hogg, Brunner, Bülbring, Kroonen, and Orel.
- **Stale or superseded:** `DEV_NOTES.md` §17.18.4-§17.18.5 as live-row guidance. Those options were real project history, but §17.18.7 later resolved the matter by keeping `tācn` unchanged and moving only `þistle` to a different paradigm cell.
- **Irrelevant or misleading:** treating the packet as if it were complete for current policy. It does not surface the later §17.18.7 resolution, so packet-only reading can wrongly suggest that row 2260 is still under active consideration for retargeting to `tācen` or `tācnes`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` §17.18.1-§17.18.7 and the later precedent note at §17.19 (`30775ff.`).
- `Germanic/data/oe_known_problems.tsv` (no entry for this row).
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` (`*taikna-`).
- `docs/references/orel_handbook_germanic_etymology.vision.txt` (`*taiknan`).
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` (PGmc `*taikna` > PWGmc `*taikn`).
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` (`tācen ... tacon, tăcun = tācen`).
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt` (§§152, 155, 160: `tācen`, `tācn`, `tācnes`).
- `docs/references/bulbring_altenglisches_elementarbuch.txt` (§445: late WS `tācn ~ tācen` variation).
- `Germanic/docs/dossier-medial-u-lowering-conditioning-2026.md` (negative control only: `tācn` is not evidence for medial-`u` conditioning).

No full dossier or analysis file was named in the packet or TSV note for this lexeme, so the extra pass had to come from `DEV_NOTES` and the repo reference texts.

## Reconstruction and early-stage forms

This row needs a three-way distinction even though TSV `PROTO` and `PROTOFORM` are currently identical.

1. **Cognate-set proto / etymological headword:** repo reference works cite the lexeme as `*taikna-` (Kroonen) or `*taiknan` (Orel). Those are source-level etymological headwords.
2. **Project input form for derivation:** the TSV uses `*táikną` as the actual derivational input. The note's "oblique *taiknăn→*taikną" is project shorthand for the neuter a-stem nominative-like form being fed into the OE derivation.
3. **OE target form:** `tācn` is the Old English form represented by the row: an attested unbroken simplex form, not the later broken spelling `tācen`.

The phonological chain itself is straightforward and current: PGmc/early project input `*táikną` > PWGmc `*tākną` by `ai` monophthongization > OE `*tākn` after final nasal/apocope > written `tācn`. `Ringe-Taylor` independently supports the key intermediate point that PGmc `*taikna` yields PWGmc `*taikn`.

## Old English philology

The central philological issue is not whether `tācn` is real, but what kind of real form it is.

- **Attested unbroken form:** `DEV_NOTES.md` §17.18.3 treats `tācn` as directly attested, especially in poetic/early material (`Beowulf` is cited there).
- **Attested broken form:** the same `DEV_NOTES` section and the grammar references show that `tācen` is also well attested and becomes the dominant late-WS/prose spelling.
- **Attested oblique form:** `tācnes` is the regular unbroken oblique form; Brunner explicitly gives `tācen - tācnes` as the textbook contrast.
- **Dictionary/headword issue:** Clark Hall normalizes the headword as `tācen`, while the `DEV_NOTES` summary says DOE lemmatizes `tācn`. So lexicographic practice is mixed, and the row should not pretend that `tācn` is the only possible citation form.
- **Register/dialect issue:** the repo's current policy intentionally treats `tācn` as an early/poetic/Anglian-compatible target, not as the majority late-WS prose spelling.

So the safest philological statement is: `tācn` is an attested OE form and a valid project target, but it is a deliberately selected unbroken register-form within a lexeme whose later prose and some dictionary traditions prefer `tācen`.

## Project problem and solution

The project problem was a class-level one, not a row-2260 mismatch. Words with word-final obstruent + sonorant clusters can show a later parasite vowel in OE (`tācen`), but the current FST does not generalize that rule for `-Cl/-Cn/-Cm#`.

For row 2260, that is now a resolved design choice rather than an open bug. `DEV_NOTES.md` §17.18.7 records the user's decision to keep the ten attested unbroken rows, including `tācn`, and to solve only `þistle` by moving it to an attested oblique cell. So row 2260 is intended to represent an attested unbroken simplex target, not the prose-majority broken headword and not an oblique workaround.

## Paradigm probe

No paradigm probe is required.

This row is not missing a derivation and is not currently being solved by a paradigm-cell switch. The real issue is explanatory: the final report should explain why the dataset keeps `tācn` despite the well-attested competing spelling `tācen`.

If the class were ever reopened, the cells worth probing would be **Nom/AccSg `tācn`**, **Nom/AccSg `tācen`** as the late broken competitor, and **GenSg `tācnes`** as the invariant unbroken control. But that is not a blocking need for the present memo.

## Recommended final report

Recommend a concise final report saying that row 2260 deliberately retains attested unbroken `tācn` as the project target for the early/poetic/Anglian side of the `tācn ~ tācen / tācnes` paradigm, while distinguishing the project input `*táikną` from the source-literature headwords `*taikna-/*taiknan`.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. Although source works cite `*taikna-` / `*taiknan`, the live `*táikną` is consistent with the project's derivational formatting and is not a row-specific defect.
- **TSV `PROTOFORM`:** no change recommended. The current derivational input already produces the intended target.
- **TSV `COUNTERPART`:** no change recommended. `tācn` is the right live target under the resolved project policy.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` is correct for the selected target.
- **TSV `NOTE`:** **change recommended.** The current note explains the proto-side morphology but not the philological reason the row keeps `tācn` instead of the common broken form `tācen`. It should add one explicit sentence saying that the dataset deliberately retains the attested unbroken early/poetic form for this cluster class.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no substantive change recommended. `DEV_NOTES.md` §17.18.7 already states the current authority clearly; the main problem is that the packet did not surface that later decision, not that the underlying note is wrong.

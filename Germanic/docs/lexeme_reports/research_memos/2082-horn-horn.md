# Research memo — 2082 horn / horn

## Starting point

- **ID:** 2082
- **CONCEPT:** horn
- **COUNTERPART:** horn
- **PROTO:** *xúrną
- **PROTOFORM:** *xúrną
- **DERIVATION_CLASS:** regular
- **NOTE:** Proto: oblique *xurnăn→*xurną (n. a-stem nom.sg.; Kroonen)

This is a note-bearing regular row. No pilot lexeme report for this lexeme was found under `Germanic/docs/lexeme_reports/pilot/`, and `coverage_audit.md` flags row 2082 as needing report coverage because the TSV `NOTE` is non-empty.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*xúrną -> horn`; the absence of an `oe_known_problems.tsv` entry; and the lexical-table confirmation that OE `horn` is the intended lemma. The packet's phonological trace is fully consistent with the live project treatment of this row as a regular derivation.

**Useful background:** the packet's `DEV_NOTES.md` excerpts at 21458 and 23669 are good current background for the general chronology `*hurną/*horna > *horn`; the bibliography candidate `[@Kroonen2013]` is genuinely relevant; and the lexical-table hits are helpful as lemma-level confirmation.

**Stale or superseded:** none of the packet's explicit hits is badly stale, but the note itself compresses comparative morphology into wording that can be misread as though the live row ought to feed oblique `*xurnăn` into the FST. That is background etymology, not the current active TSV input.

**Irrelevant or misleading:** the packet's `DEV_NOTES.md` quotation at 12687 about Older Runic `horna` is not direct lexical authority for OE `horn`; it is evidence about NWGmc chronology. It should not be weighted like dictionary evidence for the OE target form.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/oe_known_problems.tsv` — no entry for row 2082, `*xúrną`, or `horn`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — confirms this row needs report coverage because of `NOTE`, not because of a modelling failure.
- `docs/refs.bib` — confirms usable keys `[@Kroonen2013]`, `[@Orel2003]`, `[@ClarkHall1960]`, `[@BosworthToller1898]`, and `[@BrightCassidyRingler1971]`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` and `docs/references/legacy/etymological_dictionary_of_proto_germanic_kroonen.txt` — give comparative PGmc `*hurna-` n. with OE `horn` [@Kroonen2013].
- `docs/references/orel_handbook_germanic_etymology.vision.txt` and `docs/references/legacy/orel_handbook_germanic_etymology.txt` — give `*xurnan` sb.n. with OE `horn` [@Orel2003].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`, `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`, and `docs/references/bright_anglo_saxon_reader.vision.txt` — all support ordinary OE `horn` as the lemma/headword [@ClarkHall1960; @BosworthToller1898; @BrightCassidyRingler1971].
- `Germanic/docs/DEV_NOTES.md` at 5338-5350, 5609-5615, 12686-12690, 21451-21460, 18357-18363, and 23660-23675 — useful for the chronology of NWGmc lowering and final-vowel loss, but not a dedicated dossier for this lexeme.
- `Germanic/tools/oe_paradigm_probe.py` — confirms that the probe tool exists and has no built-in `horn / horn` specification, which is acceptable here because this row is not a paradigm-cell case.

No full dossier or analysis file for this lexeme was named in the packet or TSV note. Repo search did surface `horn` strings in unrelated dossier files (`dossier-shoulder-2026.md`, `dossier-shoulder-lautgesetz-2026.md`, `dossier-datpl-route-xy-deepdive-2026.md`), but those are false positives or compound examples, not direct evidence for row 2082.

## Reconstruction and early-stage forms

This row still needs the standard three-way distinction:

1. **Cognate-set proto / etymological headword:** comparative dictionaries cite lemma-style PGmc `*hurna-` [@Kroonen2013] or `*xurnan` [@Orel2003]. Those are dictionary headword conventions for the cognate set.
2. **Project input form:** TSV `PROTO` and `PROTOFORM` are both `*xúrną`, the nominative/accusative-singular style form the project actually feeds into the derivation pipeline.
3. **OE target form:** `horn`, the ordinary OE citation form [@ClarkHall1960; @BosworthToller1898; @BrightCassidyRingler1971].

The TSV note's `oblique *xurnăn→*xurną` is therefore best read as comparative-morphological background: it explains that Kroonen's etymological discussion distinguishes an oblique stem from the nominative singular, but the live row itself is not using the oblique form as its active derivational input. The packet trace and the current DEV_NOTES chronology both support the live project choice to derive the citation form from `*xúrną`.

## Old English philology

`horn` is directly attested in the repo's lexical materials, so this is not a reconstructed-OE case. Clark Hall gives `horn` as a normal noun headword [@ClarkHall1960], Bosworth-Toller preserves ordinary attestation for the noun [@BosworthToller1898], and Bright's glossary explicitly lists `horn, m.` with plural `hornas` [@BrightCassidyRingler1971].

The checked comparative dictionaries also show a small but real category distinction worth keeping straight in the final report: Kroonen and Orel cite a Proto-Germanic neuter headword, while the OE lexical sources in the repo treat `horn` as a masculine lemma [@Kroonen2013; @Orel2003; @ClarkHall1960; @BrightCassidyRingler1971]. That should be presented as lexicographic/philological background, not as a reason to reinterpret the row as a paradigm-cell workaround.

Nothing in the checked repo materials supports a special dialectal restriction, manuscript-only target, or oblique-only OE survival. The row targets the ordinary citation form `horn`.

## Project problem and solution

The project problem here is representational rather than derivational. The live derivation `*xúrną -> horn` already works, but the TSV note invokes Kroonen's oblique `*xurnăn`, which can invite the wrong inference that the row ought to be modelling an oblique PGmc cell or some hidden paradigm selection.

The current project solution is the right one: keep row 2082 as a **regular** derivation with `PROTO = PROTOFORM = *xúrną`, and treat the note's `*xurnăn` only as comparative background about the stem history. Older Runic `horna` examples in `DEV_NOTES.md` are useful chronology evidence for NWGmc lowering and final-vowel loss, but they are not competing OE targets and do not require a different TSV analysis.

## Paradigm probe

A paradigm probe is **not required** for this row. The live row does not depend on choosing among competing OE paradigm cells; the selected input already yields the intended attested citation form.

If someone later wanted a purely explanatory appendix, the optional comparison would be `*xúrną -> horn` versus an oblique background form such as `*xurnăn`, but that is not needed to justify the current row.

## Recommended final report

Recommend a brief final report saying that row 2082 is regular: the project derives attested OE `horn` directly from `*xúrną`, while Kroonen/Orel headword notation and the note's oblique `*xurnăn` are comparative background only. It should also mention that Older Runic `horna` citations are chronology evidence, not direct OE lexical authority.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended** — clarify that the live row intentionally derives OE `horn` from nominative/accusative `*xúrną`, while Kroonen's oblique `*xurnăn` is comparative background only. As written, the note can be misread as if the oblique should feed the row.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change recommended. The relevant `DEV_NOTES.md` passages are acceptable as chronology/background evidence if treated that way, and there is no dedicated horn dossier text that needs cleanup from the materials checked.

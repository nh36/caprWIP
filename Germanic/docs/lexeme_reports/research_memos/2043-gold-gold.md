# Research memo — 2043 gold / gold

## Starting point

- **ID / concept / counterpart:** 2043, **gold**, **gold**.
- **TSV `PROTO`:** `*gúlθą`.
- **TSV `PROTOFORM`:** `*gúlθą`.
- **`DERIVATION_CLASS`:** `regular`.
- **Current TSV note:** `R/T §5.1.3 p.171: *gulθa-/*gulda- may reflect Verner's alternation or regular PWGmc *lθ→*ld; either gives OE gold`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` marks the row as requiring lexeme-report coverage because `NOTE` is non-empty, but there is **no pilot lexeme report** for this lexeme in `Germanic/docs/lexeme_reports/pilot/`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row and the packet's compact derivation trace are current and row-specific. The same is true of the packet's `DEV_NOTES` material at `Germanic/docs/DEV_NOTES.md:1334-1356`, which states the current project position: `gold` is one of the cases where the implemented `*lþ > ld` treatment already yields the correct OE form even though Ringe-Taylor also allow a Verner-style alternation.
- **Useful background:** the packet's `notable_findings.md` excerpt is helpful for the separate vowel history, since it confirms that OE `gold` belongs to the ordinary group showing NWGmc/OE `u > o` before a non-high following vowel. The `old_english_wiktionary.tsv` hit is also useful as a quick confirmation that `gold` is an OE lexical item.
- **Stale or superseded:** there is no clearly superseded row-specific packet evidence here. The main risk is not stale material but over-reading generic concept-name hits.
- **Irrelevant or misleading:** the packet's `DEV_NOTES` hits at `:2342-2346` are about modern English RP/non-rhotic IPA normalization and have nothing to do with OE `gold`. The packet's hit in `analysis/four_complex_tsv_items.md` is a false positive from the phrase “a gold coin,” not evidence about this lexeme. Those items should not shape the memo.

## Additional repo research

Files checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md`
- `Germanic/docs/lexeme_reports/coverage_audit.md`
- `Germanic/data/oe_known_problems.tsv`
- `Germanic/data/old_english_wiktionary.tsv`
- `Germanic/fsts/germanic.txt`
- `Germanic/docs/analysis/notable_findings.md`
- `Germanic/docs/analysis/four_complex_tsv_items.md`
- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md`
- `Germanic/docs/dossier-shoulder-2026.md`
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- `docs/references/campbell_old_english_grammar.txt`
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`

Main findings from that wider pass:

- `oe_known_problems.tsv` has **no entry** for this lexeme, which matches the row's current status as a solved regular derivation rather than a live modelling failure.
- `Germanic/fsts/germanic.txt` explicitly encodes `PWGmcLThVoicing` as the current project rule for word-internal `*lþ > ld`, and its comments name `*gulþa-/*gulda-` as exactly the sort of ambiguous case where either explanation yields the same OE outcome.
- `Ringe & Taylor` treat OE `gold` as continuing an alternation `*gulþa- ~ *gulda-` while also placing it in the same discussion as regular West Germanic `*lþ > ld`; this supports keeping the note's ambiguity rather than forcing a single prehistoric story.
- `Campbell` independently confirms the vowel side of the derivation (`gold` among regular OE lowered `o` forms) and separately lists `gold` among forms whose `d` can be understood beside Gothic `þ`.
- `Kroonen` also gives the pair `*gulþa- ~ *gulda-`, but adds that a classic Verner singular/plural explanation is awkward for `gold` because the noun lacked a plural. That is useful etymological background, not a reason to change the live row.
- `Clark Hall`, `Bosworth-Toller`, and `old_english_wiktionary.tsv` all support `gold` as a genuine OE headword.
- `final_vowel_apocope_investigation.md`, `dossier-shoulder-2026.md`, and `four_complex_tsv_items.md` mention `gold` only incidentally; they are background or false-positive material, not row authority.

## Reconstruction and early-stage forms

This row is straightforward only if three levels stay distinct.

1. **Cognate-set proto / etymological headword:** TSV `PROTO = *gúlθą`.
2. **Project input form used for derivation:** TSV `PROTOFORM = *gúlθą`.
3. **OE target form:** `gold`, the attested Old English lemma represented by the row.

The historical ambiguity comes between stages 1 and 3, not from a live TSV mismatch:

- scholarly background allows either a paired proto `*gulþa- ~ *gulda-` or a derivation in which the project input `*gúlθą` passes through regular PWGmc `*lþ > ld`, yielding an early-stage `*gúldą`;
- the project currently chooses the second modelling strategy, because `PWGmcLThVoicing` already derives the right consonantism from the live input;
- the additional NWGmc/OE lowering `*u > o` before a non-high following vowel then gives the vocalism behind OE `gold`.

So `*gúldą` is best treated as a **diagnostic intermediate stage**, not as a proposed replacement for TSV `PROTOFORM`. Changing the TSV input to `*gúldą` would collapse an intentionally preserved historical ambiguity into the modelling input for no practical gain.

## Old English philology

- **Attested vs. reconstructed:** `gold` is attested, not a reconstructed convenience form. Repo-local dictionary materials and `old_english_wiktionary.tsv` all support it directly.
- **Citation form vs. inflected form:** the row targets the citation form `gold`. Bosworth-Toller also shows inflected uses such as `goldes`, but nothing in the checked materials suggests that the row should target any oblique cell instead.
- **Morphological/headword status:** `Clark Hall` labels `gold` as a neuter noun headword, and `Bosworth-Toller` treats it as the ordinary OE lexical item for 'gold'.
- **Dialect/manuscript caution:** the checked repo materials support the lemma securely, but they do not require any narrower dialectal or manuscript claim for this row.
- **Philological upshot:** the OE side is not the problem. The only real issue is how to narrate the prehistoric source of medial `-ld-` while keeping the attested OE lemma separate from the comparative alternation behind it.

## Project problem and solution

The project problem is explanatory, not corrective. The row already derives to the intended OE target, and there is no evidence that it belongs in `known_unmodelled`, `attested_variant`, or an analogy-driven class.

The current project solution is the right one:

- keep `PROTO = *gúlθą` as the cognate-set proto;
- keep `PROTOFORM = *gúlθą` as the actual derivational input;
- keep `COUNTERPART = gold` as the attested OE target;
- keep the note as a concise reminder that the prehistoric `-ld-` may reflect either alternation `*gulþa-/*gulda-` or the regular project rule `*lþ > ld`.

In other words, this is a **regular but note-bearing** row. The note explains why the row is worth discussing, but it does not signal a present modelling defect.

## Paradigm probe

**No paradigm probe is required.**

This row does not depend on choosing among competing OE paradigm cells, and the live issue is not a missing inflectional form but the prehistoric explanation of `-ld-`. The attested citation form is already the target, and the current derivation strategy reaches it.

## Recommended final report

Recommend a short final report stating that OE `gold` is an attested lemma, that the project correctly derives it from live input `*gúlθą` via the existing `*lþ > ld` machinery plus regular lowering to `o`, and that the note should preserve the scholarly ambiguity between inherited `*gulþa-/*gulda-` alternation and the regular West Germanic consonant development.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` is appropriate.
- **TSV `NOTE`:** no change recommended. The current note already captures the real issue without overstating it as a modelling failure.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` or dossier text:** no change recommended. The relevant `DEV_NOTES` discussion remains current, and the other checked dossier/analysis mentions are incidental rather than wrong.

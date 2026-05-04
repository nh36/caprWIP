# Research memo — 1975 calf / ċealf

## Starting point

- **ID:** 1975
- **CONCEPT:** calf
- **COUNTERPART:** ċealf
- **PROTO:** *kálbaz
- **PROTOFORM:** *kálbaz
- **DERIVATION_CLASS:** regular
- **NOTE:** WS palatalized initial (R/T §6.4.1 rule 1: k before front vowel)
- **HISTORY:** `TSV: cealf → ċealf;`
- `coverage_audit.md` lists this row as report-required because the TSV `NOTE` is non-empty and no manual report yet covers it.

## Packet evidence assessment

**Authoritative/current:**
- The live TSV row is clear that the project currently wants the normalized target `ċealf`, not plain `cealf`.
- The packet's compact derivation trace is current and coherent for the modelling path `*kálbaz > ċealf`: breaking before `*lC` and regular initial palatalization yield the present project target.
- `arestoration_r_l_research.md` is current supporting analysis for this row's place in the breaking-conditioned set: `kálbaz > ċealf` is explicitly treated as unaffected by the A-restoration fix.

**Useful background:**
- `DEV_NOTES.md` 30604-30620 usefully classifies row 1975 among the `*-aCl-*` / `*-aCr-*` items where breaking, not A-restoration, is the real issue.
- `DEV_NOTES.md` 36628-36633 is useful background confirming that breaking-conditioned rows like this one were expected to remain stable under the later restoration cleanup.
- The packet's analysis hit at `arestoration_r_l_research.md` 728 is useful only as a classification summary (`breaking before *lC*`), not as independent philological evidence.

**Stale or superseded:**
- The packet's own "possibly stale or diagnostic" `arestoration_r_l_research.md` row-list hit is indeed diagnostic rather than primary evidence; it repeats a later classification pass, not a lexical source.
- More importantly, older project diagnostics in `non_firing_rules_analysis.md` still say `*kalbăz -> ċealb (expected cealf)`, which predates the TSV history entry that changed the project target from `cealf` to `ċealf`. That older expectation should not be treated as current authority.

**Irrelevant or misleading if taken too literally:**
- The `old_english_wiktionary.tsv` packet hit is not usable lexical evidence here: its `OE_FORM` for "calf" is `ọmọ`, so for this row it is plainly bad metadata rather than support for any OE form.
- The packet's Campbell quotation at `DEV_NOTES.md` 15273 only mentions "d.s. calf" inside a discussion of `io > eo`; it is not evidence that this row's citation form, dialect label, or dotted spelling is correct.
- The packet can mislead if one forgets that `ċealf` is the **project's normalized target**, whereas the repo's dictionary and grammar sources normally cite plain `cealf`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 30604-30620 and 36628-36633.
- `Germanic/docs/analysis/arestoration_r_l_research.md` at 527-528 and 724-729.
- `Germanic/docs/non_firing_rules_analysis.md` at 435-455.
- `Germanic/docs/dossiers/g-palatalisation-conditioning.md` at 118-125 and 139-153.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/kaluza_historische_grammatik_englisch.txt`.

No pilot lexeme report for this item appears to exist yet.

## Reconstruction and early-stage forms

The row's **project input** is straightforward: TSV `PROTO` and `PROTOFORM` are both `*kálbaz`, i.e. the singular PGmc form used by the cascade for this citation-form derivation.

The broader **cognate-set proto background** is slightly richer than the row itself. Kroonen [@Kroonen2013] gives a neuter entry `*kalbiz-` while also describing an older s-stem `*kalbaz`, plural `*kalbizō`; Orel [@Orel2003] instead cites `*kalbaz` sb.m./n. That disagreement matters for lexeme-level background, but it does **not** require changing this row's modelling input, because the row is deriving the singular OE headword, not reconstructing the whole inherited paradigm.

For early OE staging, the important distinction is:

- **comparative/cognate-set background:** an old s-stem with singular/plural alternation (`*kalbaz` alongside plural material in `*-iz-`);
- **project input form:** `*kálbaz`;
- **project OE target:** `ċealf`;
- **attested dictionary headword usually cited in repo sources:** `cealf`.

The segmental chronology is consistent with the repo's current analyses: front-vowel conditioning allows initial palatalization of `*k`, and breaking before `*lC` yields `ea`, so the project's normalized output `ċealf` corresponds to attested `cealf` with palatalization made explicit.

## Old English philology

The philological evidence in the repo supports plain **`cealf`** as the ordinary dictionary/headword spelling, not dotted `ċealf`. Clark Hall [@ClarkHall1960] has `cealf I. (æ, e) ... (nap. cealfru)`; Bosworth-Toller gives `caelf/cealf`, plus oblique and plural forms such as `calfur`, `cealfru`, and `cealfas`. Campbell [@Campbell1959] and Brunner [@SieversBrunner1965] both give a normal WS singular paradigm `cealf, cealfes, cealfe`, with plural `cealfru, cealfra, cealfrum`.

These sources also show that the lexeme has important inherited paradigm history: Fulk [@Fulk2018] treats `cealf` as one of the residual former s-stems that inflect as neuter a-stems in the singular but keep `-r-` in the plural; Ringe/Taylor [@RingeTaylor2014] discuss Anglian/Mercian forms such as `celf`, `calfur`, and `calferu`. So this lexeme is philologically richer than an ordinary flat a-stem, even though the current row itself only targets the citation-form singular.

The key caution for the final report is therefore not attestation but representation. `ċealf` is best read as the project's normalized spelling for a palatalized initial consonant; the attested lemma in the repo's lexicographic and grammatical sources is normally `cealf`, with variants such as `celf` / `cælf` in some traditions. The memo should not turn the dotted spelling into a claim about manuscript orthography.

## Project problem and solution

The project problem here is mainly one of **representation and source framing**, not an unresolved derivational bug.

Historically, project diagnostics treated this row as if the target were plain `cealf`; the live TSV history now records that the row was intentionally changed to `ċealf` in order to mark regular palatalization. Separately, the A-restoration research shows that this lexeme belongs to the breaking-conditioned set and is not one of the rows endangered by the restoration-rule cleanup.

So the present project solution is:

1. keep the row as a **regular** derivation;
2. keep `*kálbaz` as the modelling input for the singular citation form;
3. understand `ċealf` as the project's normalized target, while acknowledging that the repo's handbook/dictionary evidence usually cites `cealf`.

The final report should therefore explain the normalization choice rather than presenting `ċealf` as though it were the only directly attested OE headword.

## Paradigm probe

No paradigm probe is required.

Reason: the row is not selecting among competing paradigm cells to justify the target form; the current issue is citation-form normalization (`cealf` vs project `ċealf`) plus regular breaking/palatalization chronology. The inherited plural forms (`cealfru`, `calfur`, etc.) are important philological background, but they are not a current FST-selection problem of the kind `oe_paradigm_probe.py` was designed to settle.

## Recommended final report

Recommend a **short** final lexeme report that:

- distinguishes comparative s-stem background from the row's actual input `*kálbaz`;
- states that the row's `ċealf` is a project-normalized representation of attested `cealf`;
- notes regular initial palatalization plus breaking before `*lC`;
- briefly mentions the inherited `-r-` plural background (`cealfru`, `calfur`) without turning it into the row's target problem;
- omits a paradigm-probe subsection.

## Data-change recommendations

- **TSV `PROTO`:** no change.
- **TSV `PROTOFORM`:** no change.
- **TSV `COUNTERPART`:** no change. `ċealf` is consistent with the project's current normalized use of dotted palatal consonants; the report should explain the normalization rather than reverting the row automatically.
- **TSV `DERIVATION_CLASS`:** no change.
- **TSV `NOTE`:** **change recommended.** The current note should say explicitly that the row's dotted `ċ-` is a project normalization of dictionary `cealf`, and it should mention that `ea` here is also the regular breaking outcome before `*lC`, not just "k before front vowel" in isolation.
- **`oe_known_problems.tsv`:** no change.
- **`DEV_NOTES` text:** no change required.
- **dossier text:** no change required.

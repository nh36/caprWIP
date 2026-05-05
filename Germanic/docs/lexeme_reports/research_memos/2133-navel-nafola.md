# Research memo — 2133 navel / nafola

## Starting point

- **ID / concept / counterpart:** 2133, **navel**, **nafola**.
- **Live TSV row:** `PROTO=*nablô`, `PROTOFORM=*nábulô`, `DERIVATION_CLASS=early_analogy`, with a note explaining the split between Kroonen’s citation/headword shape and the Ringe & Taylor pre-syncope input needed for the FST (`Germanic/data/germanic-aligned-final.tsv:788`).
- **Immediate project situation:** the row is no longer a live mismatch. The packet’s compact trace already shows the current derivation `*nábulô → nafola`, with OE unstressed-u lowering, Anglo-Frisian brightening, A-restoration, and final weak-tail shortening all yielding the target (`Germanic/docs/lexeme_reports/packets/2133-navel-nafola.md:17-41`).
- **Core distinctions that must be preserved:**
  - **cognate-set proto / etymological lemma:** `*nablô` (Kroonen-style headword convention);
  - **project input form for derivation:** `*nábulô` (R/T-style pre-syncope form);
  - **OE target represented by the row:** nominative singular **nafola**, not the broader OE lexical set as a whole.

## Packet evidence assessment

- **Authoritative/current:**
  - the live TSV row and the packet’s live derivation trace (`germanic-aligned-final.tsv:788`; packet lines 17-41);
  - the DEV_NOTES material showing that Option A was adopted in substance: keep `PROTO=*nablô`, change/keep `PROTOFORM=*nábulô`, and treat `*nábulô → nafola` as the correct derivation (`Germanic/docs/DEV_NOTES.md:30695-30844`, especially 30781-30844; 30973-30997; 31716-31723).
- **Useful background:**
  - the packet’s R/T quotations for `*nabulō > *næbula > OE nafola` and the word-index entry `nafola ~ -ela` (`Germanic/docs/DEV_NOTES.md:30221-30258`);
  - the packet’s A-restoration and unstressed-vowel analysis hits, especially `arestoration_r_l_research.md`, `unstressed_e_o_before_r.md`, `un-to-on-chronology.md`, and `widuwe-u-preservation.md`;
  - the lexical-table confirmation that **nafola** is an attested OE form (`Germanic/data/old_english_wiktionary.tsv:194`).
- **Stale or superseded:**
  - the early proto-form note that still treated `*nabulô` as only a possible future need (`Germanic/docs/DEV_NOTES.md:2995-2999`);
  - the section status line “awaiting Option-selection by user”, which is now historical rather than current (`Germanic/docs/DEV_NOTES.md:30160-30169`);
  - the mismatch-progress-log entry for the change, which is useful chronology but not current authority (`Germanic/docs/DEV_NOTES.md:10414-10418`).
- **Irrelevant or misleading:**
  - `analysis/mismatch_dossier_mizdo.md` is only methodological cross-reference, not evidence about OE *nafola* itself (`Germanic/docs/analysis/mismatch_dossier_mizdo.md:20-24`);
  - `compound_archaism_inventory.md` is useful as project history, but its navel case mixes categories: it calls the item a “strong ō-stem” yet also speaks of n-stem obliques, so it is not reliable as final philological wording (`Germanic/docs/analysis/compound_archaism_inventory.md:126-140`).

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` at the navel dossier and appendix (`2995-2999`, `30158-30844`, `30973-31723`);
- `Germanic/data/oe_known_problems.tsv` (**no matching entry for row 2133 / nafola**);
- `Germanic/data/old_english_wiktionary.tsv:194`;
- full files named in the packet / note:
  - `Germanic/docs/analysis/arestoration_r_l_research.md`;
  - `Germanic/docs/analysis/compound_archaism_inventory.md`;
  - `Germanic/docs/analysis/notable_findings.md`;
  - `Germanic/docs/analysis/unstressed_e_o_before_r.md`;
  - `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`;
  - `Germanic/docs/dossiers/un-to-on-chronology.md`;
  - `Germanic/docs/dossiers/widuwe-u-preservation.md`;
  - `Germanic/docs/analysis/mismatch_dossier_mizdo.md`.

Main results from that wider check:

- The repo’s strongest current consensus is the **split solution**: `*nablô` is retained as the cross-Germanic lemma, but `*nábulô` is the correct FST input (`Germanic/docs/DEV_NOTES.md:30781-30812`, `30992-30997`).
- The larger A-restoration research file confirms that a single intervening **l** is not a blocker; R/T’s own `*nabulē > *næbula > OE nafola` is explicitly cited there (`Germanic/docs/analysis/arestoration_r_l_research.md:10-31`, `149-160`).
- The unstressed-vowel file confirms that **nafola → nafela** is a later OE reduction/merger phenomenon, not evidence that `nafela` is the only legitimate target (`Germanic/docs/analysis/unstressed_e_o_before_r.md:27-34`, `124-139`).
- Luick-style chronology files treat **nafola** as a textbook example of West Saxon lowering of medial `u` to `o` before a single consonant, while also implying that Anglian and some early spellings preserve more `u` (`Germanic/docs/dossiers/un-to-on-chronology.md:157-180`; `Germanic/docs/dossiers/widuwe-u-preservation.md:1737-1759`).
- No pilot or full lexeme report for this lexeme appears to exist in `Germanic/docs/lexeme_reports/`; only the packet and coverage audit mention it.

## Reconstruction and early-stage forms

The row only makes sense if three levels are kept separate.

1. **Cognate-set proto / etymological lemma:** `*nablô`.
   - This is the project’s Kroonen-style headword convention, reflecting the cross-Germanic lemma and the PIE-style `*h₃nobʰ-l-on-` analysis without committing the live OE derivation to a medial vowel in the citation form (`Germanic/docs/DEV_NOTES.md:30184-30220`, `31277-31310`).
2. **Project derivational input:** `*nábulô`.
   - DEV_NOTES §17.19 and §17.19.10 explicitly conclude that R/T’s `*nabulō` is right **as the FST input**, because A-restoration applies to `*næbulō > *nabulō` across a single consonant, not across a `bl` cluster (`Germanic/docs/DEV_NOTES.md:30481-30508`, `30695-30812`, `30973-30997`).
3. **OE target form for this row:** **nafola**.
   - This is the early/cleaner OE nominative singular output of that derivation, before the later and more common West Saxon reduction to **nafela** (`Germanic/docs/DEV_NOTES.md:30565-30575`, `30834-30844`).

On the origin of the medial vowel, the repo’s appendix does **not** claim the literature is unanimous. It instead shows a real disagreement:

- Streitberg/Ringe-style analysis: inherited `*u` from syllabic-resonant resolution (`Germanic/docs/DEV_NOTES.md:31152-31183`);
- EWA/Brunner/Luick/Kroonen-style analysis: secondary or epenthetic vowel at some prehistory stage (`Germanic/docs/DEV_NOTES.md:31184-31310`).

For memo purposes, that dispute matters chiefly because it explains why `PROTO` and `PROTOFORM` should remain distinct. The project does **not** need to resolve the PIE/PGmc historical source of the medial vowel in order to justify the live OE derivation.

## Old English philology

- **Attested vs. reconstructed:** the relevant OE forms are attested, not invented. The repo repeatedly treats **nafola**, **nafela**, and Corpus **nabula** as manuscript spellings of the same lexeme at different reduction stages (`Germanic/docs/DEV_NOTES.md:30565-30570`, `30834-30844`; `Germanic/docs/analysis/unstressed_e_o_before_r.md:27-34`, `124-139`).
- **Citation form vs. lexical set:** the row targets nominative singular **nafola** specifically. That should not be collapsed with the broader lexical dossier `nafola / nafela / nabula`, nor with oblique n-stem forms such as **nafolan** listed in DEV_NOTES Option D (`Germanic/docs/DEV_NOTES.md:30762-30779`).
- **Target choice:** the packet and repo evidence support keeping **nafola** as the project’s target, while noting that **nafela** is the majority later West Saxon form and **nabula** preserves the earlier medial vowel more directly (`Germanic/docs/DEV_NOTES.md:30252-30258`, `30565-30575`, `30834-30844`).
- **Dialect/manuscript status:** the safest phrasing is “`nafela` is the majority later WS form; `nafola` is an earlier / less reduced OE spelling also explicitly recognised in the repo sources.” The evidence reviewed here does **not** justify stronger manuscript claims than that.
- **Dictionary/headword issue:** Kroonen’s OE citation in the etymological entry is **nafela**, but that is a dictionary/headword practice within a broader cognate entry, not a reason to replace the project’s narrower OE target once the project has deliberately chosen the earlier derivational stage (`Germanic/docs/DEV_NOTES.md:30189-30191`, `30834-30844`).

## Project problem and solution

The original project problem was a mismatch: with `PROTOFORM=*náblô`, the FST produced **næfla**, because the derivation lacked the medial vowel and therefore never matched the intended R/T-style pathway (`Germanic/docs/DEV_NOTES.md:30160-30169`).

The current solution is not a paradigm-cell workaround and not a rule rewrite. It is a **proto-input correction**:

- keep `PROTO=*nablô` for cross-Germanic alignment;
- use `PROTOFORM=*nábulô` as the derivational input;
- keep the OE target **nafola** as the row’s intended nominative singular outcome.

That solution is attractive because it makes the word **regular from the chosen input**. DEV_NOTES is explicit that the A-restoration rule itself is already correct for this case and that a paradigm-cell switch would be more invasive without philological gain (`Germanic/docs/DEV_NOTES.md:30762-30779`).

The remaining project-level ambiguity is classificatory: calling the row `early_analogy` is not a very good description of what is happening. The target **nafola** is not an analogical OE repair; it is the repo’s preferred earlier / less reduced OE stage of a regular derivation from `*nábulô`.

## Paradigm probe

A paradigm probe is **not required**.

Reason:

- the live issue was solved at the **input-form** level, not by choosing a different paradigm cell;
- DEV_NOTES explicitly considered and rejected an oblique-cell switch (`nafolan`, `nafolena`, `nafolum`, etc.) as unnecessary (`Germanic/docs/DEV_NOTES.md:30762-30779`);
- the row’s memo problem is philological classification and explanatory prose, not uncertainty about whether the FST can produce the right nominative target from the endorsed input.

Accordingly, there are no missing probe cells that must be generated before a final report can be written.

## Recommended final report

The eventual `### Lexeme report` should be short and should center on three points only: (1) the distinction between `PROTO=*nablô` and `PROTOFORM=*nábulô`; (2) the regular R/T-style derivation to nominative **nafola**; and (3) the OE attested doublet/triplet **nafola / nafela / nabula**, explaining that the TSV chooses the earlier/less-reduced nominative target rather than the later majority WS spelling.

## Data-change recommendations

- **TSV `PROTO`:** **no change recommended.** Keep `*nablô` as the cognate-set / cross-Germanic lemma.
- **TSV `PROTOFORM`:** **no change recommended.** Keep `*nábulô`; this is the correct project input form.
- **TSV `COUNTERPART`:** **no change recommended.** Keep **nafola** as the target represented by this row.
- **TSV `DERIVATION_CLASS`:** **change recommended: `early_analogy` → `regular`**, unless the project is intentionally using `early_analogy` as a broad administrative bucket for “earlier OE stage chosen over later levelling/reduction.” Philologically, the chosen target is regular from the chosen input and is not best described as analogical.
- **TSV `NOTE`:** **light change recommended.** The current note correctly explains the `PROTO`/`PROTOFORM` split, but it would be better if it also said explicitly that OE attests **nafola**, **nafela**, and **nabula**, and that the row keeps **nafola** because it is the cleaner output of the selected derivational pathway.
- **`oe_known_problems.tsv`:** **no change recommended.** I found no separate known-problems entry that now needs maintenance.
- **`DEV_NOTES` text:** **change recommended.** Section §17.19 still contains the now-stale status line “awaiting Option-selection by user” and should be refreshed to reflect that Option A has already been adopted in practice (`Germanic/docs/DEV_NOTES.md:30160-30169`).
- **Dossier / analysis text:** **change recommended.** `compound_archaism_inventory.md` should be cleaned up because Case 5 mixes stem labels and overstates the “oblique paradigm cell” framing for navel (`Germanic/docs/analysis/compound_archaism_inventory.md:126-140`). `mismatch_dossier_mizdo.md:23` also appears to have the wrong section cross-reference (`§17.20` for nafola instead of the navel section).

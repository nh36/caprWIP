# Research memo — 2087 knob / cnobba

## Starting point

- **ID:** 2087
- **CONCEPT:** `knob`
- **COUNTERPART:** `cnobba`
- **PROTO:** `*knúppaz`
- **PROTOFORM:** `*knúbbô`
- **DERIVATION_CLASS:** `reconstructed_oe`
- **NOTE:** “Unattested Old English cognate; likely *cnobba based on ME knob (Chaucer) and Frisian knobbe.”

The live row currently treats this as a reconstructed unattested OE form chosen to match the voiced branch behind Middle English `knob`.

## Packet evidence assessment

**Authoritative/current in the packet:**

- The live TSV row is authoritative for the **current project state**: row 2087 is presently encoded as `*knúbbô → cnobba`, with `reconstructed_oe`.
- The packet correctly captures the April 2026 `DEV_NOTES.md` change that moved the row away from older `*knuppăz → cnopp` mismatch history and into a working `*knúbbô → cnobba` derivation.

**Useful background but not final authority:**

- The packet's `DEV_NOTES` excerpts and `docs/references/knob_email_2026-01-22.txt` are useful for one specific point: **`*cnobba` was proposed as the likely unattested OE form directly ancestral to ME `knob`**, and `cnæp` should be kept out of this family.
- The packet is also useful in preserving the distinction between a voiced weak-noun branch (`*knubb-`) and a voiceless `*knupp-` branch.

**Stale or superseded inside the packet:**

- As a philological basis for the OE row itself, the packet is now incomplete and effectively superseded by repo-local lexicographic evidence it does **not** surface. Direct reference files in the repo show OE `cnopp/cnoppa` material, so the packet's practical conclusion that the OE slot must stay unattested `cnobba` is too narrow.
- The packet's April 2026 solution solved an FST mismatch, but it did so by prioritizing the **direct prehistory of PDE `knob`** over the best-attested **Old English counterpart**.

**Irrelevant or misleading packet material:**

- The `widuwe-u-preservation.md` hit is not knob evidence; it only notes that `knob_email_2026-01-22.txt` belongs to a different topic than that dossier.
- The absence of hits in `old_english_wiktionary.tsv` and `old_english_swadesh.tsv` should not be mistaken for evidence that OE lacked any relevant form; those tables are supplementary and are not exhaustive lexicography.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at the January 2026 note and the April 2026 `cnobba` section.
- `docs/references/README_knob.md`.
- `docs/references/knob_email_2026-01-22.txt`.
- `docs/references/kroonen_2011_n_stems.vision.txt`, which gives:
  - “Swab. knaupe m. ‘knob' < `*knūbban-`: OE `cnoppa` m. 'knob' < `*knuppan-`”
  - `*knuppa(n)` with OE `cnoppa` m. 'bunch'.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`, which has `cnop[p] (?) a knob, button`.
- `docs/references/anglosaxonoldeng00wrig.txt` and `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`, which preserve compound `wullknoppa / wullcnoppa`.
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry).
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/old_english_swadesh.tsv` (no useful row-specific support).

I found **no pilot lexeme report** for this lexeme. The strongest new evidence beyond the packet is the direct repo-local lexicographic material for **OE `cnopp/cnoppa`**, which the packet omitted.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / broader comparative label:** the live TSV still uses `*knúppaz`, the wider “knob/knopf/knoop” family label.
2. **Project input form:** the live row currently uses `*knúbbô`, a voiced weak-noun input chosen to derive reconstructed `cnobba`.
3. **OE target form:** the current target is unattested `cnobba`.

Repo-local reference evidence, however, points to a different OE-side solution. Kroonen's n-stem material distinguishes:

- a voiced weak branch `*knūbban-`, relevant to Swabian `knaupe` and to the later voiced branch behind ME `knob`;
- a voiceless weak branch `*knuppan-`, for which he explicitly cites OE `cnoppa`.

So the central reconstruction issue is not “can `*knúbbô` yield `cnobba`?”—it can—but “which branch should the OE row represent?” For an **Old English counterpart row**, the repo's stronger evidence favors the attested/lexicographically supported **voiceless OE branch** `cnopp/cnoppa`, not reconstructed voiced `cnobba`.

## Old English philology

The packet's philology is too pessimistic for the OE side. Repo-local evidence supports:

- **Bosworth-Toller:** `cnop[p] (?)` glossed ‘knob, button’;
- **Kroonen 2011 n-stems:** OE `cnoppa` m. ‘knob’ / ‘bunch’;
- **compound evidence:** `wullknoppa / wullcnoppa` ‘tuft of wool’.

That does **not** prove that OE had the exact voiced form `cnobba`; it points the other way. The attested or lexically normalized OE material is **voiceless `cnopp/cnoppa`**, while `cnobba` remains a reconstruction for the later voiced branch.

The main philological distinction is therefore:

- **attested or lexicographically supported OE counterpart:** `cnopp/cnoppa`;
- **reconstructed direct antecedent to later ME `knob`:** `*cnobba`;
- **dictionary/lemma issue:** Bosworth-Toller preserves a gloss form `cnop[p]`, while Kroonen normalizes the noun as weak masculine `cnoppa`; the latter is the better project-style citation form if the row is retargeted to an OE lemma.

I found no repo basis for a dialect-specific claim here.

## Project problem and solution

The project problem is that row 2087 currently answers the wrong question.

It currently models: “What unattested OE form would continue the **voiced** branch behind ME `knob`?” Hence `*knúbbô → cnobba`.

But the OE aligned row should instead answer: “What is the best **Old English counterpart** available in repo-local evidence?” On that question, the stronger answer is not unattested `cnobba`, but attested or lexically supported **`cnopp/cnoppa`**.

So the best project solution is:

- stop treating row 2087 as a `reconstructed_oe` placeholder for direct PDE ancestry;
- retarget it to OE **`cnoppa`** as the project citation form, with `cnopp` and `wullcnoppa` noted as supporting evidence;
- explain in the note/report that **ME `knob` likely continues a voiced sibling branch** (`*knubb-`), while the best-recoverable OE counterpart in the repo is the voiceless `cnopp/cnoppa` branch.

## Paradigm probe

A paradigm probe is **not required** to settle the memo's main conclusion. The decisive issue is lexical/philological evidence, not a hidden paradigm-cell rescue.

If the editors later want a small diagnostic probe for documentation, the useful cells would be:

- **nom.sg. weak noun:** `*knúppô` (expected `cnoppa`);
- **oblique stem:** `*knúppan` (to show the ordinary weak-noun stem shape);
- optionally the reconstructed voiced comparator `*knúbbô` (yielding `cnobba`) only as contrastive background.

But that probe would be explanatory, not decision-making.

## Recommended final report

Recommend a concise final report saying that the current `cnobba` row preserves a superseded project choice aimed at the voiced ME `knob` branch, but repo-local lexicography supports OE `cnopp/cnoppa` instead; the final report should recommend treating `cnoppa` as the OE target and `*cnobba` only as a comparative/reconstructed sibling branch.

## Data-change recommendations

- **TSV `PROTO`:** **change recommended.** If the row is retargeted to the attested OE weak noun, `PROTO` should no longer present the row as if its main citation form were the strong `*knúppaz`; the cleaner row-level proto is the weak-noun citation form `*knúppô` (or the repo's preferred equivalent weak-noun notation).
- **TSV `PROTOFORM`:** **change recommended** from `*knúbbô` to the voiceless weak-noun input `*knúppô`.
- **TSV `COUNTERPART`:** **change recommended** from `cnobba` to `cnoppa`.
- **TSV `DERIVATION_CLASS`:** **change recommended** from `reconstructed_oe` to `regular`, assuming the row is retargeted to `*knúppô → cnoppa`.
- **TSV `NOTE`:** **change recommended.** The note should say that OE evidence points to `cnopp/cnoppa`, while `*cnobba` belongs only to the reconstructed voiced branch behind later ME `knob`.
- **`oe_known_problems.tsv`:** no change recommended; this is not an `oe_known_problems` item once the row is retargeted.
- **`DEV_NOTES` text:** **change recommended.** The April 2026 `cnobba` section should be marked as incomplete/superseded by the later memo-stage conclusion that repo-local lexicography supports OE `cnopp/cnoppa`.
- **Dossier / reference-note text:** **change recommended.** `docs/references/README_knob.md` should be updated so its “bottom line” no longer implies that OE lacked a usable counterpart altogether; it should distinguish unattested `*cnobba` from attested/lexically supported `cnopp/cnoppa`.

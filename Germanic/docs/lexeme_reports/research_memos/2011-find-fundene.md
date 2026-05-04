# Research memo — 2011 find / fundene

## Starting point

- **ID:** 2011
- **CONCEPT:** find
- **COUNTERPART:** `fundene`
- **PROTO:** `*fínθaną`
- **PROTOFORM:** `*fúnðanǭ`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** the row already says this is the attested strong past participle **acc.sg.m.** cell, cites Bosworth-Toller for `fundene`, cites Hall for `tō-fundennes`, and states explicitly that bare nom.sg. `funden` is analogical.

The live row already separates the three levels correctly in principle: cognate-set proto `*fínθaną`, project input `*fúnðanǭ`, and OE target `fundene`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the compact derivation trace `*fúnðanǭ -> fundene`; and `DEV_NOTES §§17.10.30–32`, especially the sharpened source audit and the implemented Path α result.
- **Useful background:** `DEV_NOTES` around the original March `findan` problem, because it explains why the project left the infinitive and moved to a participial cell in the first place; the packet’s bibliography-key suggestions are also useful.
- **Stale or superseded:** earlier project history that treated past-ptc nom.sg. `funden` from `*funđanaz/*fúnðanaz` as the clean regular solution. `§17.10.30` explicitly overturns that by showing that nom.sg. `-en` is analogical, not the sound-law outcome [@Campbell1959; @Luick1914; @SieversBrunner1965].
- **Irrelevant or misleading:** generic packet hits on unrelated `find` strings or on methodological notes not specific to row 2011. Under `packet_quality_notes.md`, old development hits are diagnostic only unless they align with the live row and the later decision sections.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at the original `findan` discussion (why the row left the infinitive) and at `§§17.10.29–32`
- `Germanic/data/oe_known_problems.tsv` — no entry for this row/proto
- `Germanic/data/old_english_wiktionary.tsv` — supplementary lemma evidence for `findan`
- `Germanic/tools/oe_paradigm_probe.py` plus a manual probe run for this row
- `Germanic/docs/analysis/compound_archaism_inventory.md` for the standing project methodology on paradigm-cell targeting
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` and `docs/references/legacy/anglosaxondictio00tolluoft.txt`
- `docs/references/legacy/aconciseanglosa01hallgoog.txt`

No separate full dossier or pilot lexeme report exists for this lexeme in the repo at present.

## Reconstruction and early-stage forms

Three levels must stay distinct:

1. **Cognate-set proto:** `*fínθaną`, the inherited lexeme behind English `find`, Dutch `vinden`, German `finden`, and OE `findan`.
2. **Project input form:** `*fúnðanǭ`, not a rival lexeme but a selected **oblique strong participial cell** chosen because both the Verner consonant and the medial-vowel fronting are regular there.
3. **OE target form:** `fundene`, the attested OE reflex of that selected cell.

The crucial reconstruction choice is therefore not between two different etyma, but between two different paradigm cells. `DEV_NOTES §§17.10.30–32` shows that `*fúnðanaz` would give regular `fundan`, not `funden`; the fronted vowel requires a heterosyllabic/intervocalic `n`, hence the move to `*fúnðanǭ` [@RingeTaylor2014; @Campbell1959].

## Old English philology

`findan` is the ordinary OE citation lemma; `old_english_wiktionary.tsv` is fine as supplementary confirmation of that point. But row 2011 does **not** target the infinitive lemma. It targets an inflected past-participle form.

The philological distinction supported by repo-local evidence is:

- **Attested inflected target:** `fundene`, directly cited in Bosworth-Toller (`Beón þā herigeata swā fundene`) [@BosworthToller1898].
- **Corroborating derivative evidence:** Hall’s `tō-fundennes`, which confirms an inflected `funden(n)-` participial stem, though not by itself the exact same syntactic cell [@ClarkHall1960].
- **Analogical citation-form participle:** `funden`, the common dictionary form, treated in the handbooks as levelled from oblique cells [@Campbell1959; @Luick1914; @SieversBrunner1965].
- **Regular but unattested-for-project-purposes comparator:** `fundan` from nominative `*fúnðanaz`; `DEV_NOTES §17.10.31` found no direct OE attestation for that form in the repo’s reference library.

So the row should not be described as “OE `findan`” or even simply “OE `funden`.” It is specifically an attested oblique participial form chosen because it preserves the regular sound-law pathway.

## Project problem and solution

The project first discovered that infinitive `*finþaną` cannot yield OE `findan` by pure sound law: North Sea Germanic nasal spirant lengthening gives `*fīþan`, while OE `findan` has the voiced Verner alternant levelled in from other cells. That is why the project moved away from the infinitive and toward a paradigm cell with regular `*ð > d`.

The first pass treated past-ptc `*funđanaz/*fúnðanaz -> funden` as that clean solution. The later source audit in `§17.10.30` shows that this was only half right: the consonant is regular there, but bare participial `-en` is itself analogical. The current solution in `§17.10.32` is the correct refinement: keep the participial strategy, but use an **oblique** cell `*fúnðanǭ -> fundene`, where both the Verner consonant and the medial-vowel fronting are regular.

## Paradigm probe

A paradigm probe **is required** for this row, and the packet is right to flag that. There is still **no built-in row-specific probe spec** in `oe_paradigm_probe.py`, so the project’s formal probe remains missing.

A manual probe run is already informative:

- `nom.sg.m. *fúnðanaz -> fundan` (non-match)
- `acc.sg.m. *fúnðanǭ -> fundene` (unique match)
- `nom.pl.m. *fúnðanai -> +?`
- `gen.sg.m. *fúnðanas -> +?`

So the decisive contrast has been checked, but the missing formal probe spec should at minimum cover:

- **nom.sg.m.** `*fúnðanaz`
- **acc.sg.m.** `*fúnðanǭ`
- **nom.pl.m.** `*fúnðanai`
- **gen.sg.m.** `*fúnðanas`

If a securely usable dat.sg. reconstruction is wanted, that would be the next optional cell to add.

## Recommended final report

Recommend a final report that says: the cognate-set proto remains `*fínθaną`, the selected project input is oblique participial `*fúnðanǭ`, and the OE target `fundene` is an attested inflected form chosen because it is the only repo-supported cell that is lautgesetzlich for both the Verner consonant and the fronted medial vowel. The report should explicitly treat `funden` as analogical background, not as the row’s target.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no immediate change required; it is already substantially correct. At most, a minor future cleanup could mention more explicitly that Hall is corroborative stem evidence rather than a direct token of the exact same cell.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` or dossier text:** minor cleanup recommended in `DEV_NOTES` only. The earlier March/early-Path-α history should be marked even more explicitly as superseded wherever it still makes `funden` look like the regular endpoint. No separate dossier text needs change because no row-specific dossier exists.

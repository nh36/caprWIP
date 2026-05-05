# Research memo — 2077 hold / healdan

## Starting point

- **ID:** 2077
- **CONCEPT:** hold
- **COUNTERPART:** `healdan`
- **PROTO:** `*xáldaną`
- **PROTOFORM:** `*xáldaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `R/T vol.2 10729: PGmc *haldaną > WS OE healdan (with breaking)`

This is a note-bearing `regular` row. `coverage_audit.md` lists it as lexeme-report-requiring, and no pilot/full lexeme report for this item was found.

## Packet evidence assessment

**Authoritative/current in the packet:**

- The live TSV row is authoritative for the present project choice: row 2077 targets WS-style `healdan`, with `PROTO = PROTOFORM = *xáldaną` and `DERIVATION_CLASS = regular`.
- The compact derivation trace is current implementation evidence. It shows the live cascade deriving `healdan` from the project input by ordinary brightening + breaking chronology, and the trace output matches the current target.
- The packet's excerpts from `ws_vs_anglian_dialect_differences.md` are genuinely relevant philological evidence, because they quote the standard handbook contrast WS `healdan` versus Anglian/Mercian `haldan`.

**Useful background but not final authority:**

- The exact-pair `DEV_NOTES.md` hit at line 30623 is useful as a current internal classification (`breaking`), but it is a summary table, not independent lexical authority.
- The verification hit at `DEV_NOTES.md` 10561 is useful for confirming that the present FST output is stable.
- `old_english_swadesh.tsv` is supplementary support that the repo elsewhere normalizes “to hold” as `healdan`.
- The packet's `arestoration_r_l_research.md` hit is useful only as a broader row-list showing that 2077 belongs to the ordinary `*a + lC` breaking set.

**Stale or superseded / diagnostic only:**

- The packet's many generic `breaking` keyword hits from unrelated dossiers and analyses are diagnostic search residue, not row-level evidence for `healdan`.
- The row-list material in `arestoration_r_l_research.md` is a later audit classification, not the source on which the lexeme choice should rest.

**Irrelevant or misleading if taken literally:**

- The packet's `old_english_wiktionary.tsv` hit is actively misleading here: it gives OE `hold`, which is not the row's counterpart and should not outweigh the handbook evidence for `healdan`.
- Packet hits on unrelated uses of the English word “hold” (for example the separate `*habjan-` discussion in `DEV_NOTES.md`) are concept-name collisions, not evidence for row 2077.
- The packet can also mislead if one treats `healdan` as “the OE form” without saying that `haldan` is the normal Anglian/Mercian counterpart; the row is specifically choosing the WS/Kentish side of a real dialect split.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at the row-summary line 30623 and verification line 10561.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md` at §§2.1, 4, and 10.
- `Germanic/docs/analysis/arestoration_r_l_research.md` around the affected-row list.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/oe_known_problems.tsv` — no entry for row 2077.
- `Germanic/data/old_english_swadesh.tsv` (`to hold -> healdan`).
- `Germanic/data/old_english_wiktionary.tsv`, which instead gives the misleading form `hold`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` at 10729-10731 and 12670-12672.
- `docs/references/campbell_old_english_grammar.txt` at 4445-4468.
- `docs/references/hogg_vol1.txt` at 20357-20359.
- `docs/references/bright_anglo_saxon_reader.txt` at 2815-2820.

No pilot lexeme report for `hold / healdan` appears to exist yet.

## Reconstruction and early-stage forms

This row needs the usual three-way distinction.

1. **Comparative/cognate-set proto:** comparative sources in the repo cite the lexeme as PGmc `*haldaną` / `*haldana` “to hold, keep, protect” (Ringe-Taylor's text has `*haldana`; the TSV note paraphrases `*haldaną`).
2. **Project input form:** the live TSV uses the internally encoded `*xáldaną` for both `PROTO` and `PROTOFORM`. That is the form actually fed into the OE derivation cascade.
3. **OE target represented by the row:** attested WS/Kentish `healdan`, not the Anglian/Mercian variant `haldan`.

Ringe-Taylor's chronology is helpful here: PGmc `*haldana` > PWGmc `*haldan` > pre-OE `*heldan` > WS/Kentish `healdan`, while Mercian keeps `haldan` and Northumbrian has `halda`. So the important distinction is not between competing proto reconstructions inside the row; it is between the project's encoded PGmc-style input and the specific OE dialect target the row has chosen.

## Old English philology

This is **not** a reconstructed-OE case. Repo-local grammar and reader sources treat `healdan` as the standard WS citation form and contrast it directly with Anglian/Mercian `haldan`.

- Campbell explicitly lists normal WS `healdan` and says the corresponding Anglian forms are `all, haldan, &c.`
- Hogg states the rule more generally: fronted `/ae/` was retracted to `/a/` in Anglian before `l + consonant`, which is the environment behind `haldan`.
- Ringe-Taylor likewise gives WS/Kentish `healdan`, Mercian `haldan`, Northumbrian `halda`.
- Bright's reader gives the ordinary strong-verb citation form and principal parts `healdan, heold, heoldon, healden`, confirming that the row is about the normal infinitive/headword, not a special paradigm-cell rescue.

So the philological caution here is about **dialect and headword framing**, not attestation. A final report should say that `healdan` is the attested WS citation form chosen by the project, while `haldan` is a genuine non-WS counterpart. It should not treat the misleading lexical-table form `hold` as OE evidence, and it should not invent narrower manuscript claims than the repo sources actually support.

## Project problem and solution

There is no live derivational bug for row 2077. The FST already outputs `healdan`, and the row is correctly in the regular breaking class.

The project problem is explanatory: the terse TSV note says only “WS OE healdan (with breaking),” while the packet also surfaces misleading lexical-table noise and concept-name collisions. Without clarification, future packet readers could miss that this row is specifically a **WS/Kentish target chosen against an Anglian/Mercian doublet**.

The current project solution should therefore be:

1. keep row 2077 as a **regular** derivation;
2. keep `healdan` as the OE target for this row;
3. explain explicitly in the eventual report that `haldan` is the Anglian/Mercian counterpart, not a correction to the row;
4. treat `old_english_wiktionary.tsv`'s `hold` only as bad supplementary metadata, not as lexical authority.

## Paradigm probe

A paradigm probe is **not required**.

This row is not a hidden paradigm-cell problem. The issue is the dialect interpretation of the citation form, and the repo's sources already agree that the relevant contrast is WS `healdan` versus Anglian/Mercian `haldan`. Bright's principal-parts table is useful background, but there is no sign that a different OE cell needs to be probed to justify the target.

## Recommended final report

Recommend a short final lexeme report that presents 2077 as an ordinary `*a + lC` breaking case: project input `*xáldaną` yields WS `healdan`, while Anglian/Mercian `haldan` is the expected non-WS doublet. The report should distinguish comparative proto, project input, and OE target clearly, and it should mention the `heold / healden` strong-verb paradigm only as brief philological background, not as a paradigm-probe problem.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended; `healdan` is the correct WS target for the current row.
- **TSV `DERIVATION_CLASS`:** no change recommended; `regular` is correct.
- **TSV `NOTE`:** **small change recommended.** Keep the present Ringe-Taylor basis, but rewrite the note so it explicitly says that the row targets **WS/Kentish `healdan`**, contrasting with Anglian/Mercian `haldan`. That would make the dialect choice clearer and reduce future packet confusion.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** no change required.
- **Dossier text:** no change required.

---
row_id: 2261
concept: tongs
counterpart: tang
proto: *tángō
protoform: *tángō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/compound_archaism_inventory.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2261 tongs / tang

## Current row state

- The live OE row now reads `CONCEPT = tongs`, `COUNTERPART = tang`, `PROTO = *tángō`, `PROTOFORM = *tángō`, and `DERIVATION_CLASS = regular`; the row note explicitly says that Épinal-Erfurt c.700 attests Anglian nominative singular `tang`, that `tang` is the lautgesetzlich nominative singular of PGmc `*tangō`, and that later/southern `tange` is analogical [Germanic/data/germanic-aligned-final.tsv:2261-2261].
- `PROTO` and `PROTOFORM` are intentionally **not split** in the live row. `PROTO = *tángō` is the comparative PGmc headword; `PROTOFORM = *tángō` is also the actual OE-facing derivational input; `COUNTERPART = tang` is the attested OE target now preferred for the row [Germanic/data/germanic-aligned-final.tsv:2261-2261].
- That means the current row is **not** using the earlier diagnostic cell-switch idea `*tángǭ` / `*tángōn` for an oblique singular. Those forms survive only inside DEV_NOTES as explored alternatives for deriving `tange`, not as the live row policy [Germanic/docs/DEV_NOTES.md:32710-32820,32864-33040].
- No row-specific packet, research memo, or pilot file was found during slice preparation. The clearest existing support file outside DEV_NOTES is the shared methodological inventory entry that records this row as an accepted precedent for targeting an early Anglian lautgesetzlich form over a later analogical lemma [Germanic/docs/analysis/compound_archaism_inventory.md:118-122].

## Development-note summary

This row has a real document history, and the replacement slice needs to keep the phases separate. The **current** row policy is simple: `PROTO = *tángō`, `PROTOFORM = *tángō`, `COUNTERPART = tang`. The old mismatch state arose only because the row used to target `tange` while still feeding the FST the nominative singular strong-ō-stem input `*tángō`, which regularly yields `tang`, not `tange` [Germanic/docs/DEV_NOTES.md:32251-32297; Germanic/data/germanic-aligned-final.tsv:2261-2261].

DEV_NOTES is explicit about the underlying morphological distinction. If one starts from strong feminine `*tangō-`, then heavy-stem nominative singular `*-ō` undergoes regular apocope in Old English, so `*tángō > tang` [@Campbell1959, §§585-586; Germanic/docs/DEV_NOTES.md:32542-32592]. By contrast, `tange` can only be obtained lautgesetzlich from other cells or another stem class: either an oblique singular of the same strong ō-stem (`AccSg` or `DatSg`) or the nominative singular of a weak feminine `ōn`-stem [Germanic/docs/DEV_NOTES.md:32289-32295,32594-32631]. That distinction is exactly why the row once looked problematic and why the present slice must state PROTO vs. PROTOFORM vs. COUNTERPART explicitly rather than flattening everything into “PGmc *tángō > OE tang(e).”

The OE attestation dossier in DEV_NOTES is stronger than the compressed TSV note suggests. Hall, Bosworth-Toller, and Holthausen all co-lemmatize `tang` and `tange` for ‘tongs, forceps’; DEV_NOTES quotes Hall's headword as `tang, tange (o)` and then separates the forms by paradigm cell and chronology [Germanic/docs/DEV_NOTES.md:32301-32312; @ClarkHall1960, s.v. tang]. The section is careful not to overclaim: `tang` is the glossarial nominative singular, `tange` occurs both as glossary lemma and as oblique singular in prose, and `tangan` is the diagnostically important weakened dative singular that shows an OE-internal weak-feminine reanalysis in at least part of the tradition [Germanic/docs/DEV_NOTES.md:32313-32336]. The attestation chronology then matters decisively: the earliest secure form is **Épinal-Erfurt c.700 `tang`**, while `tange` and especially `tangan` are later and disproportionately West-Saxon; DEV_NOTES therefore concludes that the early/Anglian evidence favors `tang` as the original nominative singular and treats `tange` as a later southern or analogically generalized form [Germanic/docs/DEV_NOTES.md:32343-32362; @Pheifer1974].

The comparative evidence pushes the same way. OHG `zanga` and OS `tanga` are ordinary strong feminine ō-stems, not weak feminine n-stems; Old Frisian `tange` and Middle Dutch `tange` are also regular, but regular **for their own dialect histories**, because those languages weaken inherited final `-a` to `-e` in the nominative singular of feminine ō-stems [Germanic/docs/DEV_NOTES.md:32364-32427]. DEV_NOTES therefore treats OFris/MDu `tange` as a false friend for Old English: their `-e` does not license OE `tange` as a regular nominative singular reflex. At the PGmc level Kroonen reconstructs only `*tangō- f. 'tongs'`, with OE `tang(e)` listed under that single strong feminine lexeme and no separate PGmc `*tangōn-` for the implement [Germanic/docs/DEV_NOTES.md:32431-32450; @Kroonen2013]. Orel likewise separates strong `*tanō` ‘tongs’ from weak `*tanō(n)` ‘spit of land, pointed end’; crucially, DEV_NOTES notes that Orel does **not** list OE `tang(e)` under the weak entry for ‘tongs’ [Germanic/docs/DEV_NOTES.md:32469-32502; @Orel2003, p. 401]. Holthausen is the only source in the dossier that squarely entertains a weak-feminine analysis for OE, and even there the reanalysis is OE-internal, not a reason to back-project a different PGmc lemma [Germanic/docs/DEV_NOTES.md:32514-32521].

Campbell's paradigm is the formal core of the whole discussion and should be preserved nearly in full. DEV_NOTES reproduces the heavy-versus-light feminine ō-stem pattern from Campbell §585: heavy nominative singular has zero ending (`lār`), while the oblique singulars have `-e` (`lāre`) [Germanic/docs/DEV_NOTES.md:32548-32561; @Campbell1959, §585]. The follow-up quotation from §586 gives the historical endings and explains that strong-feminine `AccSg *-ǭm` and `DatSg *-ai` yield OE `-e`, whereas heavy `NomSg *-ō` yields zero by apocope [Germanic/docs/DEV_NOTES.md:32563-32582; @Campbell1959, §586]. DEV_NOTES then applies the rule directly: `tang-` is unambiguously a heavy stem (`CVCC`, short vowel plus `ng` cluster), so the nominative singular outcome is exactly `tang` [Germanic/docs/DEV_NOTES.md:32584-32592]. This is the linguistic reason the live row can remain `regular` even after the target switch.

DEV_NOTES also keeps a careful record of the roads not taken. Sections `§17.20.6.1–6.3` reject three tempting rescues: back-projecting a weak PGmc `*tangōn-`, keeping the row on the later lemma `tange`, or treating the word as inherited pluralia tantum [Germanic/docs/DEV_NOTES.md:32633-32704]. None survives scrutiny. The weak-stem hypothesis lacks comparative support; the plural-tantum hypothesis fails because the singular is alive throughout Germanic and inside OE itself; and keeping `tange` as the row target is admitted to be philologically possible only as a policy choice favoring the later dictionary lemma over the earlier regular form [Germanic/docs/DEV_NOTES.md:32635-32704].

One point must be labelled as **superseded**, not silently erased. Earlier in the same dossier, `§17.20.8` recommended Option A.1: keep target `tange` and switch the row's protoform to an accusative-singular strong-ō-stem cell `*tángǭ` / late-PGmc proxy `*tángōn`, since that cell does yield `tange` by regular sound change [Germanic/docs/DEV_NOTES.md:32780-32820]. DEV_NOTES later reverses that. The revised implementation section `§17.20.10` says there is no reason to “trick” the FST with an oblique-cell protoform when the regular nominative singular `tang` is itself directly attested in the earliest Anglian evidence [Germanic/docs/DEV_NOTES.md:32864-33040]. The live row and the present slice therefore treat Option A.1 as historically informative project archaeology, but not as current authority.

The current decision is thus the same one already condensed in the TSV note and in the shared methodological inventory. Option C was adopted: keep `PROTO` and `PROTOFORM` as `*tángō`, change the OE target from `tange` to `tang`, and explain the divergence from Wiktionary's inherited lemma by citing the older Anglian nominative singular as the better lautgesetzlich target [Germanic/docs/DEV_NOTES.md:32898-33040; Germanic/data/germanic-aligned-final.tsv:2261-2261; Germanic/docs/analysis/compound_archaism_inventory.md:118-122]. This row is therefore not a weak-feminine exception and not an unresolved mismatch. It is a settled target-selection case: prefer the early attested regular form over the later analogical lemma.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-32251-32297

- Source heading: `§17.20  *tángō → tange: paradigm cell or stem-class question?`; `§17.20.1  The mismatch and the FST behaviour (current state)`
- Source line or section hint: `lines 32251-32297`
- Fragment type: `lexeme_specific`
- Status: `current_as_problem_definition`
- Issue tags: `proto_vs_target`; `strong_ō_stem`; `oblique_cell_options`; `mismatch_origin`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the cleanest statement of the original mismatch and still the best place to explain the row's category. DEV_NOTES lays out the probe table explicitly: `*tángō -> tang`, `*tángô -> tanga`, `*tángōn -> tange`, `*tángōz -> tanġe`, then states the consequence in plain language: the chosen protoform `*tángō` is the regular nominative singular input of a heavy strong feminine ō-stem, whereas the old target `tange` matches either an oblique cell or a weak-feminine nominative singular [Germanic/docs/DEV_NOTES.md:32273-32295]. For future indexing this fragment is valuable because it already encodes the PROTO/PROTOFORM/COUNTERPART distinction that the live row now resolves by changing the counterpart, not the protoform.

### DEV_NOTES:line-32299-32362

- Source heading: `§17.20.2  The OE paradigm of tang(e)`; `§17.20.2.1  Dialect and chronology`
- Source line or section hint: `lines 32299-32362`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `attestation`; `dialect_split`; `chronology`; `weak_reanalysis`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the strongest row-local attestation dossier. DEV_NOTES preserves Hall's direct wording `tang, tange (o)` and then separates `tang`, `tange`, and `tangan` by function rather than treating them as undifferentiated spelling variants [Germanic/docs/DEV_NOTES.md:32301-32336; @ClarkHall1960, s.v. tang]. The crucial current conclusion comes in the chronology note: Épinal-Erfurt c.700 has `tang` as the earliest secure attestation, while `tange` and `tangan` are later and more southern, so the early/Anglian record supports `tang` as the original nominative singular and makes `tange` a later analogical or reanalyzed form [Germanic/docs/DEV_NOTES.md:32343-32362; @Pheifer1974]. If only one lexeme-specific anchor is indexed, this is one of the best candidates.

### DEV_NOTES:line-32364-32521

- Source heading: `§17.20.3  Comparative evidence (OHG zanga, ON tǫng, OS/OFris)`; `§17.20.4  PGmc reconstruction: ō-stem vs ōn-stem`
- Source line or section hint: `lines 32364-32521`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `comparative_evidence`; `reconstruction`; `false_friend_cognates`; `n_stem_rejection`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the philological backbone behind the target switch. DEV_NOTES reviews OHG `zanga`, OS `tanga`, OFris `tange`, MDu `tange`, and ON `tǫng`, then explains why only some of those are probative for OE nominative-singular shape [Germanic/docs/DEV_NOTES.md:32364-32427]. The decisive comparative point is double: Kroonen reconstructs only strong feminine `*tangō-` for ‘tongs’, and Orel's weak `*tanō(n)` belongs to a different lexeme (‘spit of land, pointed end’), not to the tool-name [Germanic/docs/DEV_NOTES.md:32431-32502; @Kroonen2013; @Orel2003, p. 401]. Holthausen's OE-internal weak reanalysis is retained, but only as a later OE development, not as a reason to change the PGmc input [Germanic/docs/DEV_NOTES.md:32514-32521].

### DEV_NOTES:line-32542-32704

- Source heading: `§17.20.5  Apocope in light vs heavy ō-stems (Campbell §584ff.)`; `§17.20.6  Paradigm cell candidates that yield OE tange`
- Source line or section hint: `lines 32542-32704`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `Campbell`; `heavy_stem_apocope`; `cell_diagnostics`; `why_not_n_stem`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the best formal-linguistic justification for the live row. DEV_NOTES reproduces Campbell's heavy ō-stem pattern—heavy nominative singular zero, oblique singular `-e`—and then applies it directly to `tang-` as a heavy `CVCC` stem [Germanic/docs/DEV_NOTES.md:32548-32592; @Campbell1959, §§585-586]. The next subsection maps the actual paradigm cells that can yield `tange`, identifying only `AccSg *tangǭ` and `DatSg *tangai/*tangǣ` as unpalatalized routes, then uses that fact to reject the idea that OE `tange` requires reconstructing a PGmc weak feminine [Germanic/docs/DEV_NOTES.md:32594-32660]. The same passage also rejects the plural-tantum idea and makes clear that keeping `tange` as lemma would be a target-selection choice, not a statement about regular sound change [Germanic/docs/DEV_NOTES.md:32662-32704].

### DEV_NOTES:line-32864-33040

- Source heading: `§17.20.10  Implementation plan (Option C — revised)`
- Source line or section hint: `lines 32864-33040`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `live_row_policy`; `target_switch`; `attested_Anglian`; `precedent`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the current row-policy fragment and the most directly actionable authority for the live TSV state. DEV_NOTES explicitly says that the earlier cell-switch plan is superseded, that `tang` is both the lautgesetzlich nominative singular and the earliest securely attested Anglian form, and that the `spere/speoru` precedent applies “in reverse direction”: prefer the early attested regular form over the later analogical dictionary lemma [Germanic/docs/DEV_NOTES.md:32871-32903]. It then specifies the operational decision—change the row target from `tange` to `tang`, leave `PROTOFORM = *tángō` unchanged, make no `germanic.txt` change, and document the Wiktionary divergence in the note [Germanic/docs/DEV_NOTES.md:32900-33040]. For `index.tsv`, this is the strongest anchor for the final accepted row policy.

### DEV_NOTES:line-32780-32820

- Source heading: `§17.20.8  Recommendation`
- Source line or section hint: `lines 32780-32820`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `accusative_cell_switch`; `option_A1`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment should be kept only as labeled history. At that stage DEV_NOTES recommended changing the protoform to `*tángǭ` / `*tángōn` so that the row could keep target `tange` while remaining “lautgesetzlich” through the accusative-singular pathway [Germanic/docs/DEV_NOTES.md:32782-32820]. The later `§17.20.10` revision explicitly rejects that workaround because the nominative singular `tang` is itself securely attested and already what the FST produces [Germanic/docs/DEV_NOTES.md:32864-33040].

## Superseded or diagnostic material

- The main superseded material is not the strong-ō-stem analysis itself, but the earlier attempt to preserve late lemma `tange` by changing the row's protoform to an oblique cell. That proposal is philologically interesting because it correctly identified where `tange` comes from inside the paradigm, but it is no longer current row policy [Germanic/docs/DEV_NOTES.md:32780-32820,32864-33040].
- DEV_NOTES also preserves OE-internal weak-feminine reanalysis (`tangan` etc.) as real evidence, but that evidence should not be mistaken for support to reconstruct PGmc `*tangōn-` for ‘tongs’. Current authority is stricter: weak behavior is a later OE development layered on top of inherited strong feminine `*tangō-` [Germanic/docs/DEV_NOTES.md:32323-32336,32484-32521].
- The shared methodological inventory in `compound_archaism_inventory.md` is useful but secondary. It records the outcome—target early Anglian `tang`, not later analogical `tange`—without replacing the full lexeme-specific argument in DEV_NOTES [Germanic/docs/analysis/compound_archaism_inventory.md:118-122].

## Open questions for later work

- If `index.tsv` is updated later, the safest anchors are the attestation/chronology block `32299-32362` and the final row-policy block `32864-33040`; together they capture both why `tang` is philologically preferable and why the row was actually switched.
- If a later full report wants a compact contrast table, keep three levels distinct: inherited strong-feminine nominative singular `*tángō > tang`; inherited strong-feminine oblique singular `*tangǭ/*tangai > tange`; and later OE weak-feminine reanalysis visible in `tangan`. DEV_NOTES supports all three, but only the first defines the live row.
- If better BT / DOE corpus access is added later, the only likely refinement would be quantification of how often `tange` is nominative singular versus generalized oblique or weak-feminine usage. That could sharpen the history of the analogical spread, but it is unlikely to overturn the current row target because the early Anglian `tang` attestation is already decisive [Germanic/docs/DEV_NOTES.md:32821-32862].

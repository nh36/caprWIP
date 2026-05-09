---
row_id: 2293
concept: will
counterpart: willa
proto: *wéljô
protoform: *wéljô
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2293-will-willa.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2293-will-willa.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2293 will / willa

## Current row state

- The live row is `2293 | will | willa | *wéljô | *wéljô | regular`, with the note `Kroonen *weljan- 2 m. 'will, wish' → OE willa m.; cf. G Wille, Du. wil (noun); willan is the verb 'to want' (belongs with *waljăną)` [Germanic/data/germanic-aligned-final.tsv:1407-1407].
- The immediately adjacent verbal row remains separate in the live TSV: `2292 | will | willan | *wéljaną | *wéljaną | regular` [Germanic/data/germanic-aligned-final.tsv:1405-1405]. That row adjacency is itself part of the evidence state here: the dataset already distinguishes noun `willa` from verb `willan`, and the slice must preserve that separation rather than re-merging them under English *will*.
- `PROTO` and `PROTOFORM` coincide in the live row, but they still need to be kept distinct from `COUNTERPART`. In current project usage, `PROTO = PROTOFORM = *wéljô` is the OE-facing derivational input encoded in the row, whereas `COUNTERPART = willa` is the Old English noun outcome; neither cell should be silently replaced by the dictionary headword shapes `*weljan- 2` or `*weljōn` [Germanic/data/germanic-aligned-final.tsv:1407-1407; @Kroonen2013, p. 578; @Orel2003, p. 453].
- `coverage_audit.md` marks the row as one of the regular rows that still warranted documentation because of the note field: `| 2293 | will | willa | regular | yes | - | - | - | NOTE |` [Germanic/docs/lexeme_reports/coverage_audit.md:169-169]. This slice therefore replaces missing row-local DEV_NOTES prose rather than extending an already settled lexeme report chain.
- Row-specific support files do exist and should stay linked: `Germanic/docs/lexeme_reports/packets/2293-will-willa.md` and `Germanic/docs/lexeme_reports/research_memos/2293-will-willa.md`. No clearly row-specific dossier, analysis memo, or pilot file was located in the expected support directories during this pass [Germanic/docs/lexeme_reports/packets/2293-will-willa.md:1-221; Germanic/docs/lexeme_reports/research_memos/2293-will-willa.md:1-106].
- Comparative dictionaries support the noun lexeme and the noun/verb split more clearly than DEV_NOTES does. Kroonen distinguishes `*weljan- 1 s.v. 'to want' ... OE willan` from `*weljan- 2 m. 'will, wish' ... OE willa ... Du. wil ... G Wille` [@Kroonen2013, p. 578; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29294-29314]. Orel likewise distinguishes the noun entry `*weljōn sb.m. ... OE willa` [@Orel2003, p. 453; docs/references/orel_handbook_germanic_etymology.vision.txt:49949-49952]. Kluge gives German `Wille` from `g. *weljOn m. ... ae. willa` [@Kluge2002; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:98945-98950]. Clark Hall separately lists noun `willa m. I. mind, will, determination, purpose ... desire, wish, request` and verb `willan (y) ... to 'will,' be willing, wish, desire` [@ClarkHall1960; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48525-48558].

## Detailed development-note summary

No surviving DEV_NOTES block directly treats row `2293` as a noun row. The packet's `_None_` for direct DEV_NOTES hits was therefore substantially right as a row-local claim: there is no dedicated noun memo in `Germanic/docs/DEV_NOTES.md` that says, in so many words, `*wéljô -> willa` [Germanic/docs/lexeme_reports/packets/2293-will-willa.md:48-60]. The material that does survive in DEV_NOTES is thinner, shared, and explicitly verbal.

The first usable fragment is the later syncope note for `*weljaną -> willan`. DEV_NOTES explains the `OELAdjacentSyncope` restriction and warns that the medial-position constraint is needed to avoid “deleting root vowels in words like `*weljaną` → `willan`” [Germanic/docs/DEV_NOTES.md:877-884]. That is not noun evidence, but it is still materially relevant for row `2293` because it shows the repo's current rule discussion already treats the verbal lexeme as a separate object with its own proto input `*weljaną`. The noun row should therefore not reuse this fragment as if it described `*wéljô`; its value is contrastive.

The second usable fragment is the later targeted-form success list: `weljăną → willan ✓ (was willen)` [Germanic/docs/DEV_NOTES.md:9508-9516]. Again, the fragment is about the verb row, not the noun row. But it confirms an important project-level fact: when DEV_NOTES discusses the lexeme family under active repair, it does so under the verbal row `2292`, not under noun row `2293`. For this slice, that matters because it blocks an easy but misleading inference that the noun row must be reconstructed from the same `*-janą` evidence.

Taken together, the surviving DEV_NOTES material supports a conservative replacement note rather than a rich noun dossier. The live row itself says noun `willa` belongs with Kroonen's noun entry `*weljan- 2 m. 'will, wish'` [Germanic/data/germanic-aligned-final.tsv:1407-1407]. Kroonen's own dictionary confirms that separation by giving `OE willan` under `*weljan- 1` and `OE willa` under `*weljan- 2` [@Kroonen2013, p. 578; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29294-29314]. Orel and Kluge point in the same direction but with a nominal reconstruction shape (`*weljōn` / `*weljOn`) rather than the row's derivational input `*wéljô` [@Orel2003, p. 453; docs/references/orel_handbook_germanic_etymology.vision.txt:49949-49952; @Kluge2002; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:98945-98950]. The safest summary is therefore: the row is a noun row with a sound-change input already chosen by the project, but the row-local DEV_NOTES basis is thin and mostly negative/contrastive.

That thinness also explains why the distinction among `PROTO`, `PROTOFORM`, and `COUNTERPART` has to be written out explicitly here. `PROTO` and `PROTOFORM` are both the project's derivational `*wéljô`; they are not simply identical to Kroonen's stem citation `*weljan- 2` or Orel's `*weljōn` [Germanic/data/germanic-aligned-final.tsv:1407-1407; @Kroonen2013, p. 578; @Orel2003, p. 453]. `COUNTERPART`, by contrast, is the normalized Old English noun `willa`, which Clark Hall treats separately from `willan` [@ClarkHall1960; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48529-48558]. The row only stays intelligible if those three levels remain distinct.

The main diagnostic problem is the tail end of the live note: `willan is the verb 'to want' (belongs with *waljăną)` [Germanic/data/germanic-aligned-final.tsv:1407-1407]. Repo-local comparative evidence does not support that clause as current authority. Kroonen's verb entry is `*weljan- 1 s.v. 'to want' ... OE willan`, and the noun entry is `*weljan- 2 m. 'will, wish' ... OE willa`; the same entry explicitly says `See also *weljan- 2 and *waljan-` rather than identifying `willan` with `*waljan-` [@Kroonen2013, p. 578; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29294-29314]. The slice should therefore preserve the noun/verb distinction but treat the `*waljăną` clause as superseded diagnostic wording, not as reliable lexeme assignment.

The resulting working-note position is conservative. Row `2293` still looks regular as encoded. No surviving DEV_NOTES prose requires changing `COUNTERPART = willa`, and the live TSV plus Kroonen/Orel/Kluge/Clark Hall all agree that the noun lexeme exists and is distinct from the verb [Germanic/data/germanic-aligned-final.tsv:1407-1407; @Kroonen2013, p. 578; @Orel2003, p. 453; @Kluge2002; @ClarkHall1960]. What is missing is a row-explicit noun DEV_NOTES anchor. Until such an anchor exists, the row should be documented as a noun/verb disambiguation case whose best surviving DEV_NOTES material is indirect.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-877-884

- Fragment type: `phenomenon_context_for_related_lexeme`
- Status: `current_but_indirect_for_row_2293`
- Issue tags: `noun_verb_split`; `syncope`; `negative_evidence`; `row_2292_context`
- Recommended next use: `cite_only_when_explaining_why_2293_must_not_be_collapsed_into_2292`
- Shared with row IDs: `2292`

DEV_NOTES states that the medial-position condition on `OELAdjacentSyncope` is required to avoid “deleting root vowels in words like `*weljaną` → `willan`” [Germanic/docs/DEV_NOTES.md:877-884]. For row `2293`, the value of this fragment is explicitly contrastive. It shows that the active DEV_NOTES discussion of this lexeme family is centered on the verbal pathway `*weljaną -> willan`, not on the noun row `*wéljô -> willa`. That makes the fragment useful as a boundary marker: it is strong evidence for keeping row `2292` separate, but weak evidence for indexing row `2293` itself.

### DEV_NOTES:line-9508-9516

- Fragment type: `shared_probe_result_for_related_lexeme`
- Status: `current_but_indirect_for_row_2293`
- Issue tags: `verification`; `verb_row_exact_match`; `noun_verb_split`; `row_2292_context`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2292`

The later success block records `weljăną → willan ✓ (was willen)` and closes with `All 6 targeted forms now match their expected OE targets` [Germanic/docs/DEV_NOTES.md:9508-9516]. This is again valuable mainly for what it excludes. The repaired form is the verb `willan`, and the block does not mention noun `willa` or project input `*wéljô`. It therefore supports the claim that DEV_NOTES already had a distinct verbal problem/history for row `2292`, while row `2293` lacked a parallel noun-specific narrative.

## Superseded or diagnostic material

- The final clause of the live row note — `willan is the verb 'to want' (belongs with *waljăną)` — should be treated as superseded diagnostic wording, not as dependable current etymological authority [Germanic/data/germanic-aligned-final.tsv:1407-1407]. Kroonen instead separates `*weljan- 1 ... OE willan` from `*weljan- 2 ... OE willa`, while merely cross-referring `*waljan-` as another lexeme [@Kroonen2013, p. 578; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29294-29314].
- The packet's lexical-table hit `will | willan` in `old_english_wiktionary.tsv` is verb-only evidence and should not be upgraded into noun support for row `2293` [Germanic/docs/lexeme_reports/packets/2293-will-willa.md:66-73]. It remains useful only as a reminder that English *will* is lexically ambiguous inside the dataset.
- The packet's `DEV_NOTES hits: None` remains accurate if read narrowly as `no row-explicit noun passage`; it is incomplete only in the broader sense that nearby DEV_NOTES material does mention the related verb `willan` [Germanic/docs/lexeme_reports/packets/2293-will-willa.md:48-60; Germanic/docs/DEV_NOTES.md:877-884,9508-9516].
- No row-specific dossier or analysis file currently needs to be carried forward here. The absence of such files is part of the evidence state, not a gap in this slice [Germanic/docs/lexeme_reports/research_memos/2293-will-willa.md:41-47].

## Open questions for later work

- If the live TSV note is ever revised, the safest repair would be to preserve the noun/verb split while replacing the `*waljăną` clause with wording aligned to Kroonen's `*weljan- 1` versus `*weljan- 2` distinction [Germanic/data/germanic-aligned-final.tsv:1407-1407; @Kroonen2013, p. 578].
- If a final lexeme report is ever drafted, it should probably cite the noun directly from Clark Hall (`willa m. ... will, determination ... desire, wish`) and keep `willan` as a separate comparator entry rather than letting the verb dominate the evidence base [@ClarkHall1960; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48529-48558].
- If `index.tsv` is reconsidered later, only weak line anchors currently exist in DEV_NOTES, and both of them are verb-side anchors (`877-884`, `9508-9516`). They are useful for documenting the noun/verb split, but not strong enough to pretend that DEV_NOTES preserves a noun-specific row-2293 analysis.

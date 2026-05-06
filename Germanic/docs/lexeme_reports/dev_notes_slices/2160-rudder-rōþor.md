---
row_id: 2160
concept: rudder
counterpart: rōþor
proto: *rōθraz
protoform: *rōθraz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2160 rudder / rōþor

## Current row state

- CONCEPT: `rudder` [Germanic/data/germanic-aligned-final.tsv:892-892]
- COUNTERPART: `rōþor` [Germanic/data/germanic-aligned-final.tsv:892-892]
- PROTO: `*rōθraz` [Germanic/data/germanic-aligned-final.tsv:892-892]
- PROTOFORM: `*rōθraz` [Germanic/data/germanic-aligned-final.tsv:892-892]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:892-892]
- The live TSV row carries no row-specific explanatory note beyond source markers, and `PROTO`/`PROTOFORM` are still identical; there is no separate row-level workaround input or alternate paradigm-cell target in the current data [Germanic/data/germanic-aligned-final.tsv:890-893].
- `oe_known_problems.tsv` has no entry for row `2160`, `rudder`, `rōþor`, or `*rōθraz`; the lexeme is not currently tracked as an exception, wontfix item, or unresolved OE mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- `old_english_wiktionary.tsv` maps English `rudder` directly to OE `rōþor`, so the row target is also the ordinary repo-local OE lemma source rather than a special replacement target [Germanic/data/old_english_wiktionary.tsv:221-221].
- Coverage infrastructure still lists row `2160` as uncovered and regular, with no packet, research memo, or dossier attached yet; that is why the metadata links in this slice remain blank [Germanic/docs/lexeme_reports/coverage_audit.md:331-331].
- The current published OE derivation trace already reaches the target cleanly: `PROTO: *rōθraz`, `EXPECTED: rōþor`, `OUTPUTS: rōþor`, with the concrete pathway `*rōθraz` → `*rōθra` (PGmc Final Z Deletion) → `*rōθr` (PWGmc Final Bare A Loss) → `*rōθor` (OE Epenthetic Vowel) [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3730-3750].

## Development-note summary

No dedicated current `DEV_NOTES.md` dossier survives for row `2160`. That absence matters because the row is not sitting in the project's exception machinery: the live TSV keeps `PROTO = PROTOFORM = *rōθraz`, the OE target is still `rōþor`, `oe_known_problems.tsv` does not flag the lexeme, and the current derivation trace already matches the row exactly [Germanic/data/germanic-aligned-final.tsv:890-893; Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3730-3750]. The replacement note therefore has to be built from securely relevant shared DEV_NOTES material plus current row context, not from a lost row-specific mismatch discussion.

The most useful shared DEV_NOTES material is the parasitic-vowel/epenthesis discussion for word-final obstruent + sonorant clusters. DEV_NOTES states that after WGmc/OE syncope the NomSg/AccSg of masculine and neuter a-stems can end in such clusters, and that late OE then develops a parasite vowel, specifically `o` after back stressed vowels: `fugol, wuldor, wundor, māþum, bōsom` [Germanic/docs/DEV_NOTES.md:29855-29866]. A later clarification says the same rule affects only word-final `CR` clusters created by prior apocope, giving examples such as `*fugl > fugol`, `*snotr > snotor`, and `*wuldr > wuldor` [Germanic/docs/DEV_NOTES.md:30578-30582]. That is exactly the structure shown by the live trace for row `2160`: once `*rōθraz` loses final `-z` and then final bare `-a`, the row reaches word-final `*rōθr`, and the OE epenthetic vowel stage yields `*rōθor` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3737-3750]. For this row, `rōþor` is therefore not a special rescue spelling; it is the regular OE resolution of a back-vocalic final `-θr` cluster.

DEV_NOTES also preserves a close comparator that makes the cluster mechanics explicit. In the `wether` discussion, the note says the reconstructable PGmc neuter a-stem nom.sg. `*wíθrą` develops by ordinary rule sequence: `*wíθrą → *wéþrą`, then loss of final nasalized `*ą`, then `OEEpentheticInsertion` before word-final `*r`, producing `weþer` [Germanic/docs/DEV_NOTES.md:21587-21603]. The exact vowel history is different from `rudder`, but the structural point is the same and directly relevant: DEV_NOTES already treats a final `-þr` cluster as something OE resolves by epenthesis after final-vowel loss, not as a lexeme-specific irregularity. Row `2160` differs mainly in having a back long vowel, so the row trace's `*rōθr → *rōθor` aligns with the shared `o-after-back-vowel` parasitic pattern rather than with front-vocalic `weþer` [Germanic/docs/DEV_NOTES.md:29859-29861,21592-21596; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3743-3750].

The only late DEV_NOTES material that mentions `þ/ð` more generally is diagnostic rather than philological. In the English-sandbox audit, DEV_NOTES says proto entries with `þ/ð/ai/eu` still fail at `ProtoInput`, citing `*brōþēr` among the examples and noting that brace-diphthong and thorn/eth coverage is still incomplete there [Germanic/docs/DEV_NOTES.md:1817-1824]. For row `2160`, that should be preserved only as tooling history. It does **not** imply uncertainty about the OE row itself, because the published OE derivation trace already accepts `*rōθraz` and outputs `rōþor` regularly [Germanic/docs/DEV_NOTES.md:1824-1824; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3730-3750].

## Relevant DEV_NOTES fragments

No securely attachable dedicated row-specific `DEV_NOTES` section survives for `2160`. The fragments below are nevertheless sufficient for replacement working-note purposes because they explain the exact mechanism visible in the live trace and identify the only potentially misleading tooling note.

### DEV_NOTES:line-29855-29866

- Fragment type: `phenomenon_context_for_lexeme`
- Source heading: `§17.18.7` parasitic-vowel discussion for final obstruent + sonorant clusters
- Source line or section hint: `lines 29855-29866`
- Status: `current`
- Issue tags: `epenthesis`; `parasite_vowel`; `final_cluster`; `back_vowel`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main current DEV_NOTES authority for the surface shape `rōþor`. DEV_NOTES says that after syncope OE can inherit word-final obstruent + sonorant clusters in masculine/neuter a-stems, and that late OE then develops a parasite vowel, with `o` after back stressed vowels: `fugol, wuldor, wundor, māþum, bōsom` [Germanic/docs/DEV_NOTES.md:29855-29866]. Even though `rudder` is not named in that list, the live trace for row `2160` matches the same environment exactly: `*rōθraz` loses `-z`, then final bare `-a`, leaving `*rōθr`, and the OE stage inserts the vowel that surfaces as `rōþor` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3739-3750].

The later restatement of the same rule is also important because it prevents overbroad reinterpretation. DEV_NOTES says the rule affects only word-final `CR` clusters created by apocope, giving `*fugl > fugol`, `*snotr > snotor`, and `*wuldr > wuldor` as the model cases [Germanic/docs/DEV_NOTES.md:30578-30582]. For row `2160`, that pins down the row-level claim very precisely: the `-or` of `rōþor` belongs to ordinary OE epenthesis after final-cluster creation, not to a separate inherited suffix and not to an ad hoc repair invented for this lexeme.

### DEV_NOTES:line-21587-21603

- Fragment type: `phenomenon_context_for_lexeme`
- Source heading: `Why *wíθrą is the right target`
- Source line or section hint: `lines 21587-21603`
- Status: `current`
- Issue tags: `theta_cluster`; `final_vowel_loss`; `epenthetic_insertion`; `comparandum`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This fragment is a strong comparator because it spells out the same structural derivation with a final `-þr` cluster. DEV_NOTES says `*wíθrą` is a real PGmc neuter a-stem form and gives the rule sequence explicitly: `*wíθrą → *wéþrą`, final `*ą` loss to `*wéþr`, then `OEEpentheticInsertion` before word-final `*r`, producing `weþer` [Germanic/docs/DEV_NOTES.md:21587-21596]. The fragment therefore confirms that, inside current project reasoning, final `-þr` does not remain unbroken in OE citation form once the final vowel is lost.

For row `2160`, the comparator is not evidence that `rōþor` and `weþer` share identical vowel histories; they do not. Its value is narrower and safer: it shows that DEV_NOTES already accepts the sequence “final-vowel loss creates final `-þr`; OE epenthesis resolves the cluster” as ordinary historical machinery [Germanic/docs/DEV_NOTES.md:21592-21599]. Combined with the back-vowel parasiting note and the live row trace, that makes `*rōθr → *rōθor` a securely project-internal regular development rather than an unsupported guess [Germanic/docs/DEV_NOTES.md:29859-29861; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3743-3750].

### DEV_NOTES:line-1817-1824

- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Source heading: `English core probe audit`
- Source line or section hint: `lines 1817-1824`
- Status: `diagnostic_only`
- Issue tags: `english_sandbox`; `protoinput`; `thorn_eth_support`; `tooling_gap`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This fragment is relevant only because row `2160` also contains inherited thorn material. DEV_NOTES says that proto entries with `þ/ð/ai/eu` still fail at `ProtoInput`, naming `*brōþēr` among the examples, and frames that as a limitation of the English sandbox lexicon/encoding coverage rather than as a historical claim about the lexemes themselves [Germanic/docs/DEV_NOTES.md:1817-1824]. If older project discussion says words with `þ` could not be validated there, this is the note being referred to.

For `rudder`, the fragment must stay fenced off as diagnostic only. The live OE trace already accepts `*rōθraz` and outputs `rōþor` without mismatch [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3730-3750]. So this DEV_NOTES note should be cited, if at all, only to explain why some English-sandbox audit work could not use thorn-bearing forms as validation probes at that time; it is not current authority against the live OE row.

## Superseded or diagnostic material

There is no securely attested row-specific superseded protoform, alternate OE target, or abandoned paradigm-cell rescue for `2160` in the current repo materials. The only diagnostic material worth preserving is the English-sandbox `ProtoInput` note about incomplete `þ/ð` support [Germanic/docs/DEV_NOTES.md:1817-1824]. That note explains a tooling blind spot, not a problem with the OE row's present derivation.

The row history that should remain primary is therefore simple and current: `*rōθraz` is still both `PROTO` and `PROTOFORM`, the live OE row still targets `rōþor`, and the published trace already shows the regular project-internal pathway `*rōθraz → *rōθra → *rōθr → *rōθor` [Germanic/data/germanic-aligned-final.tsv:892-892; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3730-3750].

## Open questions for later work

- If a packet or memo is later created, keep the row-level claim narrow: no current evidence in `DEV_NOTES.md` requires changing `PROTO`, `PROTOFORM`, or OE target; the working value of the slice is to preserve the regular `final -θr > -þor` epenthesis story, not to reopen the lexical reconstruction [Germanic/data/germanic-aligned-final.tsv:892-892; Germanic/docs/DEV_NOTES.md:29855-29866,21587-21603].
- If future indexing work requires securely attachable **row-specific current authority**, row `2160` may remain a no-index slice, because the usable DEV_NOTES support is shared phenomenon material plus one diagnostic tooling note rather than a dedicated rudder dossier [Germanic/docs/DEV_NOTES.md:29855-29866,21587-21603,1817-1824].
- If the English-sandbox thorn/eth support is later completed, add any successful validation only as infrastructure confirmation. It should not be presented as a change in the historical analysis, since the OE derivation trace already treats `rōþor` as regular now [Germanic/docs/DEV_NOTES.md:1824-1824; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3730-3750].

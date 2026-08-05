# Post-rename integrity report

Scope: book-level consequences of introducing the EAF stage/scope ontology during
the behaviour-neutral relabelling phase (branch `historical-cascade-order`). This
report closes the integrity items raised by that phase. It records no
sound-change or cascade change; the frozen lexical baseline is unchanged
(`outputs_sha256 = aaf19ba9…480e`, 372 matched / 8 mismatched). All findings
below are downstream consequences of *regenerating generated artifacts from the
corrected sources*, diagnosed here — the FST behaviour is provably identical
(rename gate B).

## 1. Index Verborum: recovery of 204 EAF intermediate forms

### 1.1 What happened

`build_index_verborum.STAGE_FORM_RE` enumerates the historical stage-label
prefixes it recognises in the compact derivation trace
(`oe_derivation_class_trace_report.compact.md`). Before the fix it listed
`PGmc | PWGmc | NWGmc | OE | West Saxon | Anglo Frisian | …` but **not** the new
`EAF` prefix introduced by the relabelling. Consequently the intermediate forms
emitted at the five EAF trace stages were no longer parsed as stage forms, so
`excluded_intermediate_trace_forms()` dropped from 1277 to 1073 entries — i.e.
**204 Early-Anglo-Frisian intermediate forms were no longer being recognised as
trace-stage forms**. Because the Index Verborum excludes recognised trace-stage
forms, an unrecognised intermediate form would fall through to the broad-prose
candidate path and could be indexed as if it were a lexical form.

The fix (commit `88dfecf0`) added `EAF | Early Anglo-Frisian` to `STAGE_FORM_RE`
and to `stage_to_language` (→ `preoe`). `check_index_verborum.py`
(`assert_intermediate_trace_forms_excluded`) then passes: all 204 forms are
recognised, excluded from the printable index, and absent from the print rows as
`source_scope = trace_stage`.

### 1.2 Proof that every one of the 204 is an internal stage form, not lexical

Three independent properties establish this for the whole set:

1. **Reconstruction marker.** All 204 forms carry the leading `*` reconstruction
   marker (0 exceptions). Attested Old English lexical forms in the index are
   unstarred; the two form-spaces are disjoint keys.
2. **Trace provenance.** Every form is emitted by an intermediate EAF FST stage
   (`source_scope` would be `trace_stage`), i.e. it is the state of a proto form
   *between* rules, never the final Old English surface output of any lexeme.
3. **No collision with an indexed form.** No `*`-marked EAF form equals any
   indexed form (of any language). See §2 for the single de-asterisked
   near-collision (`*dæg` vs. attested `dæg`), which the marker keeps distinct.

These are the intermediate outputs of the EAF-corridor rules on ordinary corpus
lexemes (e.g. `*bækaną` is 'bake' after Anglo-Frisian brightening, before A-
restoration and the later OE changes complete the derivation to `bacan`). They
are historical-stage artefacts of the derivation, not indexable headwords.

### 1.3 Grouping by source rule and trace stage

| Rule | Trace stage label | Forms |
| --- | --- | --- |
| SC043 `EAFBrightening` | `EAF Brightening` | 87 |
| SC020 `EAFFinalZDeletion` | `EAF Final Z Deletion` | 107 |
| SC026 `EAFNasalSpirantLengthening` | `EAF Nasal Spirant Lengthening` | 3 |
| SC027 `EAFNasalSpirantLoss` | `EAF Nasal Spirant Loss` | 3 |
| SC012 `EAFLThVoicing` | `EAFL Th Voicing` | 4 |
| **Total** | | **204** |

(The `EAFLThVoicing` identifier renders as the trace label `EAFL Th Voicing`; the
`EAF` prefix still matches `STAGE_FORM_RE`.)

Full enumeration (unique reconstructed forms per stage), reproducible via
`build_index_verborum.excluded_intermediate_trace_forms()` filtered to headings
beginning `EAF`:

### SC043 EAFBrightening — trace stage `EAF Brightening` (87 forms)

`*brándæs`, `*bánnæs`, `*bæ`, `*bækaną`, `*bælgi`, `*bærd`, `*bærjæs`, `*bæstą`, `*dæg`, `*dæl`, `*flæskǭ`, `*flæxsą`, `*fædǣr`, `*fældaną`, `*fællaną`, `*færaną`, `*færn`, `*fæstijaną`, `*fēowær`, `*græbaną`, `*græsą`, `*gællô`, `*gærną`, `*gæsti`, `*kræft`, `*kælb`, `*læppô`, `*mánnæs`, `*mækô`, `*mækō`, `*mækōjaną`, `*mælt`, `*mærku`, `*mærǭ`, `*mæst`, `*mæxti`, `*næbolô`, `*næbu`, `*nægl`, `*nætilǭ`, `*nættją`, `*næxti`, `*ræstǣ`, `*skæftą`, `*slæxaną`, `*spærrô`, `*spærōjaną`, `*strækkijaną`, `*stæb`, `*swánæs`, `*swælwǭ`, `*sæku`, `*sælbu`, `*sæltą`, `*sæpą`, `*sættjaną`, `*súmær`, `*tæppô`, `*wæbs`, `*wædaną`, `*wægn`, `*wækaną`, `*wældaną`, `*wældu`, `*wærpą`, `*wærtǭ`, `*wæskaną`, `*wætær`, `*wæxsaną`, `*wæxsą`, `*wḯ`, `*xlædaną`, `*xlæxxjaną`, `*xræbn`, `*xwæl`, `*xámæræs`, `*xæbok`, `*xæbǣ`, `*xæggj`, `*xæglą`, `*xægô`, `*xældaną`, `*xællu`, `*xærbistu`, `*xærm`, `*xæsl`, `*xúnægą`

### SC020 EAFFinalZDeletion — trace stage `EAF Final Z Deletion` (107 forms)

`*brōki`, `*brūdi`, `*bálgi`, `*bárda`, `*bébru`, `*bókka`, `*bóttma`, `*búrdi`, `*bōgu`, `*bōk`, `*bōsma`, `*dránki`, `*dráuma`, `*dága`, `*dála`, `*déli`, `*dāga`, `*dāli`, `*dḗdi`, `*fláux`, `*flāski`, `*flōdu`, `*fríund`, `*fárna`, `*féldu`, `*fíngra`, `*físka`, `*fógla`, `*fóxsa`, `*fúnxsti`, `*fúrxtīna`, `*grúndu`, `*gánga`, `*gáns`, `*gásti`, `*géfti`, `*gāsta`, `*knéxta`, `*kráfta`, `*króppa`, `*kwédu`, `*kálba`, `*kámba`, `*láuka`, `*lókka`, `*lústu`, `*lā`, `*lūs`, `*málta`, `*másta`, `*máxti`, `*méluk`, `*mōda`, `*mḗnō`, `*nágla`, `*náudi`, `*rástō`, `*ráuka`, `*rókka`, `*rúgi`, `*rō`, `*skéldu`, `*skíllinga`, `*skúldrum`, `*skā`, `*snāwa`, `*spḗnu`, `*strángi`, `*stráuma`, `*stába`, `*stámna`, `*stókka`, `*stórka`, `*stórma`, `*stāna`, `*stōla`, `*sáuma`, `*súmara`, `*sāwi`, `*táuma`, `*tḯdi`, `*wábsa`, `*wágna`, `*wáldu`, `*wéga`, `*wéxti`, `*wíntru`, `*wólfa`, `*wúrmi`, `*xrábna`, `*xwála`, `*xábuka`, `*xággja`, `*xándu`, `*xárbistu`, `*xárma`, `*xásla`, `*xélma`, `*xér`, `*xúnda`, `*xā`, `*xāma`, `*xōda`, `*xōfa`, `*ófna`, `*āna`, `*ḗla`

### SC026 EAFNasalSpirantLengthening — trace stage `EAF Nasal Spirant Lengthening` (3 forms)

`*fūnxsti`, `*gōns`, `*jéugūn`

### SC027 EAFNasalSpirantLoss — trace stage `EAF Nasal Spirant Loss` (3 forms)

`*fūxsti`, `*gōs`, `*jéugū`

### SC012 EAFLThVoicing — trace stage `EAFL Th Voicing` (4 forms)

`*fáldaną`, `*félduz`, `*gúldą`, `*wálduz`

## 2. Forms requiring human judgment

Exactly one form warrants a note. The EAF Brightening intermediate `*dæg`
(post-brightening state of 'day') de-asterisks to the string `dæg`, which is also
the attested Old English form of 'day' present in the printed index. They remain
**distinct index keys** because the reconstructed intermediate keeps its `*`
marker (`*dæg`, language `preoe`) whereas the attested headword is unstarred
(`dæg`, language `oe`); the index keys on `(language, form)` including the marker.
No merging or masking occurs, and `check_index_verborum` confirms `*dæg` is
excluded from the printable index. No other form in the 204 has an unstarred
collision with an indexed lexical form. No change to indexing behaviour is
required.

## 3. The additional `stem` occurrence

### 3.1 Why the regenerated trace places `stem` in a mismatch bucket

Stem's derivation is:

```
PROTO:    *stámnaz
EXPECTED: stefn        (attested OE, model file 2216-stem-stefn.model.md)
OUTPUTS:  stamn        (what the production cascade actually derives)
```

The model derives `stamn`; the attested Old English is *stefn*. The model does
not produce the front vowel / cluster development that yields `stefn`, so the
regenerated full trace classifies `stem` in the mismatch bucket
`fronting_missing_no_trigger`. This is **not new behaviour**: `stem` is one of the
eight documented mismatches in the frozen baseline
(`cascade_baseline_summary.json`: 372 matched, 8 mismatched — buck, fowl, fire,
rust, **stem**, tap, wolf, wool). The previously *committed* trace snapshot was
stale: it listed `stem` under `exact_match (373)`, contradicting the frozen
baseline. Regenerating the snapshot from the current FST (mandatory, because the
trace carried former rule names) corrected the count to `exact_match (372)` + 8
mismatches = 380, matching the baseline. Rename gate B confirms `outputs_sha256`
is unchanged, so the correction is orthogonal to the relabelling — it is a
snapshot-staleness fix exposed by the required regeneration, not a cascade or
data change.

### 3.2 The single downstream index consequence

Once `stem` sits in a mismatch bucket, the trace surfaces its selected proto
input `*stámnaz` as a `trace_proto_input` occurrence in addition to its existing
`lexical_protoform` occurrence. This is the **only** new occurrence introduced
across the entire migration (see §5): the `*stámnaz` book emission's
`source_occurrence_count` rises 1 → 2.

## 4. Narrowness of the `stem` fingerprint allowlist entry

`Germanic/docs/book/index_semantic_fingerprint_allowlist.tsv` contains a single
`add` entry:

```
add  pgmc    *stámnaz  selected_input  trace_proto_input  stem — OE stefn  <note>
```

It is maximally specific: it pins **all six** semantic-key fields — language
`pgmc`, form `*stámnaz`, role `selected_input`, scope `trace_proto_input`, and
heading `stem — OE stefn`. It therefore whitelists exactly one occurrence key and
cannot absorb any unrelated addition (a different form, role, scope, language, or
heading would not match). `check_reader_facing_semantics.py` additionally rejects
stale `add` entries (a form already in the baseline) and stale `remove` entries,
so the allowlist cannot silently accumulate dead exceptions. Any second, genuinely
unexpected drift would still fail the fingerprint check.

## 5. Pre- vs post-migration book-index emission comparison

Comparison of `index_verborum_book_emissions.tsv` at the pre-migration base
(`a5e9ce12`) vs the migrated tip:

| Metric | Pre | Post | Δ | Classification |
| --- | --- | --- | --- | --- |
| Emission rows | 1865 | 1865 | 0 | unchanged |
| Distinct emission displays | 804 | 804 | 0 | none added, none removed |
| Total source occurrences | 2031 | 2032 | +1 | the single `stem`/`*stámnaz` occurrence (§3) |
| Displays with changed `source_occurrence_count` | — | — | 1 | only `*stámnaz` (1 → 2) |
| Index Verborum print-main rows | 2264 | 2265 | +1 | the same `*stámnaz` occurrence |
| Book occurrences | 2031 | 2032 | +1 | same; `source_not_in_book` unchanged at 233 |
| Print-excluded / unique-printed | 88 / 1061 | 88 / 1061 | 0 | unchanged |

**Every** book-index difference across the whole relabelling + EAF-ontology
migration reduces to the single diagnosed `stem` proto-input occurrence. The 204
recovered EAF forms remain correctly excluded and therefore contribute **zero**
emissions. No emission entry was added, removed, or re-attributed on account of a
rename; renamed stage labels changed the *labels* attached to trace-sourced
occurrences but not which occurrences are emitted.

## 6. Conclusion

No indexing behaviour is changed by this report. The two exposed items — the EAF
`STAGE_FORM_RE` gap and the stale `stem` bucketing — were fixed at their generator
sources and reconciled against the frozen lexical baseline, which is unchanged.
The only book-index delta is the +1 `stem`/`*stámnaz` occurrence, fully diagnosed
and narrowly allowlisted.

# Canonical CAPR stage and scope ontology

CAPR represents two **separate** historical axes for every sound-change rule.
Conflating them is the root cause of the misleading internal identifiers this
migration corrects.

## 1. Chronological stage (internal Foma identifier prefix + `hist_stage`)

The internal Foma identifier normally encodes the rule's position in CAPR's
English-line historical model:

```
PGmc  →  PNWGmc  →  PWGmc  →  EAF  →  OE
```

| Prefix | Meaning |
| --- | --- |
| `PGmc`   | A change internal to, or leading to, Proto-Germanic. |
| `PNWGmc` | A change leading from Proto-Germanic to Proto-Northwest Germanic. |
| `PWGmc`  | A change leading from Proto-Northwest Germanic to Proto-West Germanic. |
| `EAF`    | Early Anglo-Frisian: CAPR's operational post-PWGmc, pre-OE chronological corridor on the English line. |
| `OE`     | A change leading to, or occurring within, Old English. |

Old English dialect-specific forms are used where historically appropriate:
`OEWs`, `OEKt`, `OEMc`, `OENb`.

**`EAF` is a modelling stage.** It is an operational chronological corridor for
developments that sit after Proto-West Germanic and before Old English on the
English line. It does **not** assert that every EAF-labelled development was
exclusively Anglo-Frisian, nor that every scholar accepts a discrete
Proto-Anglo-Frisian node. It is a bracket for "post-PWGmc, pre-OE, English-line",
inside which the precise sub-classification (e.g. West Germanic vs North Sea
Germanic) is carried by the **scope** axis, not the stage prefix.

**The prefix is never derived from executable cascade position.** A historically
Old English rule keeps its `OE...` prefix even when a technical dependency forces
it to execute unusually early (e.g. `OEWsPalatalGlide` runs before u-lowering).
Conversely, an EAF-stage rule keeps `EAF...` even if it executes late.

## 2. Historical scope (`hist_scope`, reader-facing description)

Geographical / genealogical distribution is a **separate** field. Canonical
scope values:

```
pan_germanic  pan_pnwgmc  pan_wgmc  north_wgmc  north_sea_germanic
anglo_frisian  english_specific  west_saxon  kentish  mercian  northumbrian
```

**"Ingvaeonic"** is retained as a *traditional scholarly label* associated with
`north_sea_germanic`. It is **not** a separate CAPR chronological stage and never
appears as a `hist_stage` value.

A rule may therefore be, for example:

- internal stage `EAF`, reader-facing scope "West Germanic" (SC003, SC020);
- internal stage `EAF`, reader-facing scope "Northern West Germanic" (SC012);
- internal stage `EAF`, reader-facing scope "North Sea Germanic / traditionally
  Ingvaeonic" (SC026, SC027);
- internal stage `EAF`, reader-facing scope "Anglo-Frisian" (SC043).

## 3. Reader-facing names

Reader-facing titles use the historically most accurate conventional or
scope-based description — **not** a bare expansion of the internal prefix:

| Internal identifier | Reader-facing title |
| --- | --- |
| `EAFRhotacism` | West Germanic rhotacism |
| `EAFLThVoicing` | Northern West Germanic *lþ*-voicing |
| `EAFNasalSpirantLoss` | North Sea Germanic nasal-spirant loss |
| `PNWGmcULowering` | Proto-Northwest Germanic u-lowering |

Historical stages are spelled out in reader-facing prose: "Proto-Northwest
Germanic", "Proto-West Germanic", "Early Anglo-Frisian", "Old English". Bare
"NWGmc" is not used in final reader-facing prose for Proto-Northwest Germanic.

## 4. Exceptions

- An established descriptive or eponymous identifier may remain **without** a
  stage prefix where that is clearer — e.g. `SieversLawSyncope`. A prefix that is
  *present* must be historically accurate.
- A rule whose stage or historical granularity is **unresolved** is not renamed
  (SC004 conflation; SC064 stage). SC numbers are stable throughout.

## 5. Relationship to this migration

The canonical targets for every rule are recorded in
`rename_migration_manifest.tsv` (`former_* → canonical_*`, with
`migration_status` ∈ {pending, completed, deferred, not_required}). This ontology
**supersedes** the earlier proposed canonical names in
`historical_correction_dossier.md` (e.g. the earlier `WGmcRhotacism`,
`NSGNasalSpirant*` proposals are replaced by the stage-prefixed `EAFRhotacism`,
`EAFNasalSpirant*`). The reader-facing titles are unchanged from the dossier's
scope-based descriptions.

Legacy metadata values `nwgmc` / `pan_nwgmc` are migrated per-rule to `pnwgmc` /
`pan_pnwgmc`; the West-Germanic-line reclassifications adopt `eaf` with a scope
that carries the precise distribution. After the last migration, the legacy
values are removed and only the canonical stage values (`pgmc`, `pnwgmc`,
`pwgmc`, `eaf`, `oe`) and scope values remain (task section 9).

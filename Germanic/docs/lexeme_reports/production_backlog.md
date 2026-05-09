# Old English lexeme-report production backlog

This is the working production backlog for the lexical write-up phase. It is **not** a list of all OE words, and rows with source material are **still missing production reports** until they are promoted into `report_manifest.tsv` as `pilot` or `full`.

## Current counts

- Total OE rows with real counterpart: **380**
- Rows requiring lexeme report under the selective-report policy: **148**
- Manifest-backed production reports: **11**
- Source material available but no manifest-backed production report: **136**
- No source material found: **1**
- Regular rows with empty NOTE outside the production-report requirement: **232** (231 already have supporting material, including the separately tracked format-test manifest entry; 1 currently has none)

## Working principle

- This backlog follows the **selective-report policy** in `report_schema.md`, not an “every word gets a standalone report” policy.
- **Non-regular rows** come before regular rows with NOTE.
- **Source material is not final prose**: packets, dev-note slices, research memos, and batch summaries still need to be turned into schema-conformant reports.
- The production unit is one entry at a time: **evidence packet -> schema-conformant report -> review -> manifest update**.
- Existing manifest-backed pilots are a review/upgrade layer, not part of the missing-production backlog.

## P0: Rows with no source material found

The sole current P0 row is a required regular-with-NOTE entry that still needs explicit source-material preparation before drafting can begin.

| ID | CONCEPT | COUNTERPART | Class | Source material | REASON |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2055 | handle | handlian | regular | — | Audit currently shows no linked source material for this required row; nearby row 2054 absorbs handle-named files, so source-material reassignment or regeneration should happen before drafting. |

Recommendation: before drafting `2055 handle / handlian`, do a targeted packet/source-material pass and confirm whether the handle-named packet/slice/memo files should be reassigned from adjacent row `2054 hand` or regenerated cleanly.

## P1: Non-regular rows missing production reports

These are the main missing-production backlog: non-regular rows with source material already available, but still no manifest-backed production report.

### late_analogy

| ID | CONCEPT | COUNTERPART | Source material | Audit basis |
| :--- | :--- | :--- | :--- | :--- |
| 1962 | bow | bēag | dev_notes_slices/1962-bow-bēag.md<br>research_memos/1962-bow-bēag.md | NOTE, DERIVATION_CLASS=late_analogy |
| 1980 | cow | cȳ | dev_notes_slices/1980-cow-cȳ.md<br>packets/1980-cow-cȳ.md<br>research_memos/1980-cow-cȳ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2011 | find | fundene | dev_notes_slices/2011-find-fundene.md<br>packets/2011-find-fundene.md<br>research_memos/2011-find-fundene.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2034 | fright | fyrhte | dev_notes_slices/2034-fright-fyrhte.md<br>packets/2034-fright-fyrhte.md<br>research_memos/2034-fright-fyrhte.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2053 | hammer | hameres | dev_notes_slices/2053-hammer-hameres.md<br>packets/2053-hammer-hameres.md<br>research_memos/2053-hammer-hameres.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2058 | have | hæfeþ | dev_notes_slices/2058-have-hæfeþ.md<br>packets/2058-have-hæfeþ.md<br>research_memos/2058-have-hæfeþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2068 | heaven | heofon | dev_notes_slices/2068-heaven-heofon.md<br>dev_notes_slices/deferred_sound_change_material.md<br>packets/2068-heaven-heofon.md<br>research_memos/2068-heaven-heofon.md<br>research_memos/batch_07_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2107 | live | lifeþ | dev_notes_slices/2107-live-lifeþ.md<br>packets/2107-live-lifeþ.md<br>research_memos/2107-live-lifeþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2119 | man | mannes | dev_notes_slices/2119-man-mannes.md<br>research_memos/2119-man-mannes.md<br>research_memos/batch_08_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2124 | meed | meorde | dev_notes_slices/2124-meadow-mǣd.md<br>research_memos/2124-meed-meorde.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2140 | night | niht | dev_notes_slices/2140-night-niht.md<br>research_memos/2140-night-niht.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2152 | rest | ræste | dev_notes_slices/2152-rest-ræste.md<br>packets/2152-rest-ræste.md<br>research_memos/2152-rest-ræste.md<br>research_memos/batch_09_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2183 | shoulder | sċuldrum | dev_notes_slices/2183-shoulder-sċuldrum.md<br>packets/2183-shoulder-sċuldrum.md<br>research_memos/2183-shoulder-sċuldrum.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2184 | shove | sċēaf | dev_notes_slices/2184-shove-sċēaf.md<br>packets/2184-shove-sċēaf.md<br>research_memos/2184-shove-sċēaf.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2309 | make (iptv.2sg) | maca | dev_notes_slices/2309-make-iptv-2sg-maca.md<br>packets/2309-make-(iptv.2sg)-maca.md<br>research_memos/2309-make-(iptv.2sg)-maca.md<br>research_memos/batch_11_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2310 | make (3sg) | macaþ | dev_notes_slices/2310-make-(3sg)-macaþ.md<br>packets/2310-make-(3sg)-macaþ.md<br>research_memos/2310-make-(3sg)-macaþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2311 | bore (iptv.2sg) | bora | dev_notes_slices/2311-bore-(iptv.2sg)-bora.md<br>packets/2311-bore-(iptv.2sg)-bora.md<br>research_memos/2311-bore-(iptv.2sg)-bora.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2312 | bore (3sg) | boraþ | dev_notes_slices/2312-bore-(3sg)-boraþ.md<br>research_memos/2312-bore-(3sg)-boraþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2313 | learn (iptv.2sg) | liorna | dev_notes_slices/2313-learn-iptv-2sg-liorna.md<br>research_memos/2313-learn-(iptv.2sg)-liorna.md<br>research_memos/batch_12_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2314 | learn (3sg) | liornaþ | dev_notes_slices/2314-learn-(3sg)-liornaþ.md<br>research_memos/2314-learn-(3sg)-liornaþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2315 | lick (iptv.2sg) | licca | dev_notes_slices/2315-lick-iptv-2sg-licca.md<br>packets/2315-lick-(iptv.2sg)-licca.md<br>research_memos/2315-lick-(iptv.2sg)-licca.md<br>research_memos/batch_13_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2316 | lick (3sg) | liccaþ | dev_notes_slices/2316-lick-(3sg)-liccaþ.md<br>research_memos/2316-lick-(3sg)-liccaþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2317 | show (iptv.2sg) | sċēawa | dev_notes_slices/2317-show-(iptv.2sg)-sċēawa.md<br>packets/2317-show-(iptv.2sg)-sċēawa.md<br>research_memos/2317-show-(iptv.2sg)-sċēawa.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2318 | show (3sg) | sċēawaþ | dev_notes_slices/2318-show-(3sg)-sċēawaþ.md<br>research_memos/2318-show-(3sg)-sċēawaþ.md<br>research_memos/batch_14_summary.md | NOTE, DERIVATION_CLASS=late_analogy |

### early_analogy

| ID | CONCEPT | COUNTERPART | Source material | Audit basis |
| :--- | :--- | :--- | :--- | :--- |
| 1965 | brand | brandes | dev_notes_slices/1965-brand-brandes.md<br>packets/1965-brand-brandes.md<br>research_memos/1965-brand-brandes.md | DERIVATION_CLASS=early_analogy |
| 1968 | breast | brēost | dev_notes_slices/1968-breast-brēost.md<br>packets/1968-breast-brēost.md<br>research_memos/1968-breast-brēost.md | DERIVATION_CLASS=early_analogy |
| 1990 | dill | dile | dev_notes_slices/1990-dill-dile.md<br>packets/1990-dill-dile.md<br>research_memos/1990-dill-dile.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2004 | fast | festan | dev_notes_slices/2004-fast-festan.md<br>packets/2004-fast-festan.md<br>research_memos/2004-fast-festan.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2016 | flask | flasce | dev_notes_slices/2016-flask-flasce.md<br>packets/2016-flask-flasce.md<br>research_memos/2016-flask-flasce.md | DERIVATION_CLASS=early_analogy |
| 2027 | follow | fylġan | dev_notes_slices/2027-follow-fylġan.md<br>packets/2027-follow-fylġan.md<br>research_memos/2027-follow-fylġan.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2037 | gall | ġealla | dev_notes_slices/2037-gall-ġealla.md<br>packets/2037-gall-ġealla.md<br>research_memos/2037-gall-ġealla.md | DERIVATION_CLASS=early_analogy |
| 2086 | knight | cniht | dev_notes_slices/2086-knight-cniht.md<br>packets/2086-knight-cniht.md<br>research_memos/2086-knight-cniht.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2088 | lade | hladan | dev_notes_slices/2088-lade-hladan.md<br>packets/2088-lade-hladan.md<br>research_memos/2088-lade-hladan.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2090 | lap | lappa | dev_notes_slices/2090-lap-lappa.md<br>packets/2090-lap-lappa.md<br>research_memos/2090-lap-lappa.md | DERIVATION_CLASS=early_analogy |
| 2092 | laugh | hliehhan | dev_notes_slices/2092-laugh-hliehhan.md<br>packets/2092-laugh-hliehhan.md<br>research_memos/2092-laugh-hliehhan.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2109 | loam | lām | dev_notes_slices/2109-loam-lām.md<br>packets/2109-loam-lām.md<br>research_memos/2109-loam-lām.md | DERIVATION_CLASS=early_analogy |
| 2114 | lung | lungen | dev_notes_slices/2114-lung-lungen.md<br>packets/2114-lung-lungen.md<br>research_memos/2114-lung-lungen.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2133 | navel | nafola | dev_notes_slices/2133-navel-nafola.md<br>packets/2133-navel-nafola.md<br>packets/2186-show-sċēawian.md<br>research_memos/2133-navel-nafola.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2134 | neck | hnecca | dev_notes_slices/2134-neck-hnecca.md<br>packets/2134-neck-hnecca.md<br>research_memos/2134-neck-hnecca.md | DERIVATION_CLASS=early_analogy |
| 2136 | needle | nǣdl | dev_notes_slices/2136-needle-nǣdl.md<br>packets/2136-needle-nǣdl.md<br>research_memos/2136-needle-nǣdl.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2143 | nose | nosu | dev_notes_slices/2143-nose-nosu.md<br>packets/2143-nose-nosu.md<br>research_memos/2143-nose-nosu.md | DERIVATION_CLASS=early_analogy |
| 2168 | sap | sæp | dev_notes_slices/2168-sap-sæp.md<br>packets/2168-sap-sæp.md<br>research_memos/2168-sap-sæp.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2169 | sea | sǣ | dev_notes_slices/2169-sea-sǣ.md<br>packets/2169-sea-sǣ.md<br>research_memos/2169-sea-sǣ.md<br>research_memos/batch_26_summary.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2189 | sieve | sife | dev_notes_slices/2189-sieve-sife.md<br>packets/2189-sieve-sife.md<br>research_memos/2189-sieve-sife.md | DERIVATION_CLASS=early_analogy |
| 2205 | spare | sparian | dev_notes_slices/2205-spare-sparian.md<br>packets/2205-spare-sparian.md<br>research_memos/2205-spare-sparian.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2212 | staff | stæf | dev_notes_slices/2212-staff-stæf.md<br>packets/2212-staff-stæf.md<br>research_memos/2212-staff-stæf.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2216 | stem | stefn | dev_notes_slices/2216-stem-stefn.md<br>packets/2216-stem-stefn.md<br>research_memos/2216-stem-stefn.md<br>research_memos/batch_29_summary.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2235 | swan | swanes | dev_notes_slices/2235-swan-swanes.md<br>packets/2235-swan-swanes.md<br>research_memos/2235-swan-swanes.md<br>research_memos/batch_30_summary.md | DERIVATION_CLASS=early_analogy |
| 2252 | thousand | þūsend | dev_notes_slices/2252-thousand-þūsend.md<br>packets/2252-thousand-þūsend.md<br>research_memos/2252-thousand-þūsend.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2258 | timber | timber | dev_notes_slices/2258-timber-timber.md<br>packets/2258-timber-timber.md<br>research_memos/2258-timber-timber.md<br>research_memos/batch_32_summary.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2268 | wake | wacan | dev_notes_slices/2268-wake-wacan.md<br>packets/2268-wake-wacan.md<br>research_memos/2268-wake-wacan.md<br>research_memos/batch_33_summary.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2274 | water | wæter | dev_notes_slices/2274-water-wæter.md<br>packets/2274-water-wæter.md<br>research_memos/2274-water-wæter.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2284 | whale | hwæl | dev_notes_slices/2284-whale-hwæl.md<br>packets/2284-whale-hwæl.md<br>research_memos/2284-whale-hwæl.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2286 | whine | hwīnan | dev_notes_slices/2286-whine-hwīnan.md<br>packets/2286-whine-hwīnan.md<br>research_memos/2286-whine-hwīnan.md | DERIVATION_CLASS=early_analogy |
| 2296 | withy | wīþiġ | dev_notes_slices/2296-withy-wīþiġ.md<br>packets/2296-withy-wīþiġ.md<br>research_memos/2296-withy-wīþiġ.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2302 | world | weorold | dev_notes_slices/2302-world-weorold.md<br>packets/2302-world-weorold.md<br>research_memos/2302-world-weorold.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2308 | youth | ġeoguþ | dev_notes_slices/2308-youth-ġeoguþ.md<br>packets/2308-youth-ġeoguþ.md<br>research_memos/2308-youth-ġeoguþ.md<br>research_memos/batch_37_summary.md | NOTE, DERIVATION_CLASS=early_analogy |

### attested_variant

| ID | CONCEPT | COUNTERPART | Source material | Audit basis |
| :--- | :--- | :--- | :--- | :--- |
| 2242 | ten | tēon | dev_notes_slices/2242-ten-tēon.md<br>research_memos/2242-ten-tēon.md | NOTE, DERIVATION_CLASS=attested_variant |
| 2254 | three | þrīe | dev_notes_slices/2254-three-þrīe.md<br>packets/2254-three-þrīe.md<br>research_memos/2254-three-þrīe.md<br>research_memos/batch_06_summary.md | NOTE, DERIVATION_CLASS=attested_variant |
| 2273 | wasp | wæfs | dev_notes_slices/2273-wasp-wæfs.md<br>packets/2273-wasp-wæfs.md<br>research_memos/2273-wasp-wæfs.md | NOTE, DERIVATION_CLASS=attested_variant |

### reconstructed_oe

| ID | CONCEPT | COUNTERPART | Source material | Audit basis |
| :--- | :--- | :--- | :--- | :--- |
| 2087 | knob | cnobba | dev_notes_slices/2087-knob-cnobba.md<br>packets/2087-knob-cnobba.md<br>research_memos/2087-knob-cnobba.md | NOTE, DERIVATION_CLASS=reconstructed_oe |
| 2227 | strew | strīeġan | dev_notes_slices/2227-strew-strīeġan.md<br>research_memos/2227-strew-strīeġan.md | NOTE, DERIVATION_CLASS=reconstructed_oe |

### unexplained_unmodelled

| ID | CONCEPT | COUNTERPART | Source material | Audit basis |
| :--- | :--- | :--- | :--- | :--- |
| 2030 | fowl | fugol | dev_notes_slices/2030-fowl-fugol.md<br>research_memos/2030-fowl-fugol.md | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2162 | rust | rust | dev_notes_slices/2162-rust-rust.md<br>dev_notes_slices/PILOT_SUMMARY.md<br>research_memos/2162-rust-rust.md<br>research_memos/batch_04_summary.md | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2298 | wolf | wulf | dev_notes_slices/2298-wolf-wulf.md<br>packets/2298-wolf-wulf.md<br>research_memos/2298-wolf-wulf.md | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2300 | wool | wull | dev_notes_slices/2300-wool-wull.md<br>packets/2300-wool-wull.md<br>research_memos/2300-wool-wull.md | NOTE, DERIVATION_CLASS=unexplained_unmodelled |

## P2: Regular rows with NOTE but missing production reports

These rows are lower priority than the non-regular backlog, but they still require production reports because the TSV NOTE is non-empty.

| ID | CONCEPT | COUNTERPART | Source material |
| :--- | :--- | :--- | :--- |
| 1934 | bake | bacan | dev_notes_slices/1934-bake-bacan.md<br>packets/1934-bake-bacan.md<br>research_memos/1934-bake-bacan.md |
| 1942 | beech | bōc | dev_notes_slices/1942-beech-bōc.md<br>packets/1942-beech-bōc.md<br>research_memos/1942-beech-bōc.md |
| 1943 | begin | beġinnan | dev_notes_slices/1943-begin-beġinnan.md<br>packets/1943-begin-beġinnan.md<br>research_memos/1943-begin-beġinnan.md |
| 1949 | bier | bǣr | dev_notes_slices/1949-bier-bǣr.md<br>packets/1949-bier-bǣr.md<br>research_memos/1949-bier-bǣr.md |
| 1951 | birth | byrd | dev_notes_slices/1951-birth-byrd.md<br>packets/1951-birth-byrd.md<br>research_memos/1951-birth-byrd.md |
| 1954 | bone | bān | dev_notes_slices/1954-bone-bān.md<br>packets/1954-bone-bān.md<br>research_memos/1954-bone-bān.md |
| 1958 | both | bū | dev_notes_slices/1958-both-bū.md<br>packets/1958-both-bū.md<br>packets/1962-bow-bēag.md<br>research_memos/1958-both-bū.md |
| 1961 | bow | bīeġan | dev_notes_slices/1961-bow-bīeġan.md<br>packets/1961-bow-bīeġan.md<br>research_memos/1961-bow-bīeġan.md |
| 1969 | breeches | brēċ | dev_notes_slices/1969-breeches-brēċ.md<br>research_memos/1969-breeches-brēċ.md |
| 1975 | calf | ċealf | dev_notes_slices/1975-calf-ċealf.md<br>packets/1975-calf-ċealf.md<br>research_memos/1975-calf-ċealf.md |
| 1979 | corn | corn | dev_notes_slices/1979-corn-corn.md<br>packets/1979-corn-corn.md<br>research_memos/1979-corn-corn.md |
| 1987 | deed | dǣd | dev_notes_slices/1987-deed-dǣd.md<br>research_memos/1987-deed-dǣd.md |
| 1992 | door | dor | dev_notes_slices/1992-door-dor.md<br>packets/1992-door-dor.md<br>research_memos/1992-door-dor.md |
| 2003 | fare | faran | dev_notes_slices/2003-fare-faran.md<br>packets/2003-fare-faran.md<br>research_memos/2003-fare-faran.md |
| 2007 | fell | fell | dev_notes_slices/2007-fell-fell.md<br>packets/2007-fell-fell.md<br>research_memos/2007-fell-fell.md<br>research_memos/batch_15_summary.md |
| 2008 | fern | fearn | dev_notes_slices/2008-fern-fearn.md<br>packets/2008-fern-fearn.md<br>research_memos/2008-fern-fearn.md |
| 2009 | field | feld | dev_notes_slices/2009-field-feld.md<br>packets/2009-field-feld.md<br>research_memos/2009-field-feld.md |
| 2022 | fly | flēogan | dev_notes_slices/2022-fly-flēogan.md<br>packets/2022-fly-flēogan.md<br>research_memos/2022-fly-flēogan.md |
| 2028 | forlorn | lēosan | dev_notes_slices/2028-forlorn-lēosan.md<br>packets/2028-forlorn-lēosan.md<br>research_memos/2028-forlorn-lēosan.md |
| 2038 | gang | gang | dev_notes_slices/2038-gang-gang.md<br>packets/2038-gang-gang.md<br>research_memos/2038-gang-gang.md<br>research_memos/batch_17_summary.md |
| 2041 | give | ġiefan | dev_notes_slices/2041-give-ġiefan.md<br>packets/2041-give-ġiefan.md<br>research_memos/2041-give-ġiefan.md |
| 2043 | gold | gold | dev_notes_slices/2043-gold-gold.md<br>packets/2043-gold-gold.md<br>research_memos/2043-gold-gold.md |
| 2046 | grave | grafan | dev_notes_slices/2046-grave-grafan.md<br>packets/2046-grave-grafan.md<br>research_memos/2046-grave-grafan.md |
| 2049 | guest | ġiest | dev_notes_slices/2049-guest-ġiest.md<br>packets/2049-guest-ġiest.md<br>research_memos/2049-guest-ġiest.md |
| 2051 | hair | hǣr | dev_notes_slices/2051-hair-hǣr.md<br>packets/2051-hair-hǣr.md<br>research_memos/2051-hair-hǣr.md |
| 2057 | harvest | hierfest | dev_notes_slices/2057-harvest-hierfest.md<br>research_memos/2057-harvest-hierfest.md |
| 2069 | hedge | heġġ | dev_notes_slices/2069-hedge-heġġ.md<br>packets/2069-hedge-heġġ.md<br>research_memos/2069-hedge-heġġ.md |
| 2070 | helm | helm | dev_notes_slices/2070-helm-helm.md<br>packets/2070-helm-helm.md<br>research_memos/2070-helm-helm.md |
| 2071 | help | helpan | research_memos/2071-help-helpan.md |
| 2075 | hind | hind | dev_notes_slices/2075-hind-hind.md<br>packets/2075-hind-hind.md<br>research_memos/2075-hind-hind.md |
| 2077 | hold | healdan | dev_notes_slices/2077-hold-healdan.md<br>research_memos/2077-hold-healdan.md |
| 2082 | horn | horn | dev_notes_slices/2082-horn-horn.md<br>packets/2082-horn-horn.md<br>packets/2251-thorn-þorn.md<br>research_memos/2082-horn-horn.md<br>research_memos/batch_21_summary.md<br>research_memos/batch_31_summary.md |
| 2093 | lead | lǣdan | dev_notes_slices/2093-lead-lǣdan.md<br>packets/2093-lead-lǣdan.md<br>research_memos/2093-lead-lǣdan.md |
| 2095 | learn | liornian | dev_notes_slices/2095-learn-liornian.md<br>packets/2095-learn-liornian.md<br>research_memos/2095-learn-liornian.md<br>research_memos/batch_22_summary.md |
| 2100 | lid | hlid | dev_notes_slices/2100-lid-hlid.md<br>packets/2100-lid-hlid.md<br>research_memos/2100-lid-hlid.md |
| 2102 | light | līehtan | dev_notes_slices/2102-light-līehtan.md<br>research_memos/2102-light-līehtan.md |
| 2104 | linden | lind | dev_notes_slices/2104-linden-lind.md<br>packets/2104-linden-lind.md<br>research_memos/2104-linden-lind.md<br>research_memos/batch_23_summary.md |
| 2120 | march | mearc | dev_notes_slices/2120-marrow-mearg.md<br>packets/2120-march-mearc.md<br>research_memos/2120-march-mearc.md |
| 2126 | milk | meoloc | dev_notes_slices/2126-milk-meoloc.md<br>packets/2126-milk-meoloc.md<br>research_memos/2126-milk-meoloc.md |
| 2129 | mother | mōder | dev_notes_slices/2129-mother-mōder.md<br>research_memos/2129-mother-mōder.md |
| 2138 | net | nett | dev_notes_slices/2138-net-nett.md<br>packets/2138-net-nett.md<br>research_memos/2138-net-nett.md |
| 2141 | nightmare | mare | dev_notes_slices/2141-nightmare-mare.md<br>packets/2141-nightmare-mare.md<br>research_memos/2141-nightmare-mare.md<br>research_memos/batch_25_summary.md |
| 2155 | coat | rocc | dev_notes_slices/2155-coat-rocc.md<br>packets/2155-coat-rocc.md<br>research_memos/2155-coat-rocc.md |
| 2179 | sheep | sċēap | dev_notes_slices/2179-sheep-sċēap.md<br>packets/2179-sheep-sċēap.md<br>research_memos/2179-sheep-sċēap.md<br>research_memos/batch_27_summary.md |
| 2181 | shilling | sċilling | dev_notes_slices/2181-shilling-sċilling.md<br>dev_notes_slices/2218-stilt-stilte.md<br>packets/2181-shilling-sċilling.md<br>research_memos/2181-shilling-sċilling.md |
| 2186 | show | sċēawian | dev_notes_slices/2186-show-sċēawian.md<br>research_memos/2186-show-sċēawian.md |
| 2196 | sleep | slǣpan | dev_notes_slices/2196-sleep-slǣpan.md<br>packets/2196-sleep-slǣpan.md<br>research_memos/2196-sleep-slǣpan.md<br>research_memos/batch_28_summary.md |
| 2198 | smear | smierwan | dev_notes_slices/2198-smear-smierwan.md<br>research_memos/2198-smear-smierwan.md |
| 2202 | span | spannan | dev_notes_slices/2202-span-spannan.md<br>packets/2202-span-spannan.md<br>research_memos/2202-span-spannan.md |
| 2204 | spar | spearra | dev_notes_slices/2204-spar-spearra.md<br>packets/2204-spar-spearra.md<br>research_memos/2204-spar-spearra.md |
| 2217 | still | stillan | dev_notes_slices/2217-still-stillan.md<br>packets/2217-still-stillan.md<br>research_memos/2217-still-stillan.md |
| 2230 | summer | sumer | dev_notes_slices/2230-summer-sumer.md<br>packets/2230-summer-sumer.md<br>research_memos/2230-summer-sumer.md |
| 2232 | sunder | sundrian | dev_notes_slices/2232-sunder-sundrian.md<br>packets/2232-sunder-sundrian.md<br>research_memos/2232-sunder-sundrian.md |
| 2234 | swallow | swealwe | dev_notes_slices/2234-swallow-swealwe.md<br>packets/2234-swallow-swealwe.md<br>research_memos/2234-swallow-swealwe.md |
| 2238 | swine | swīn | dev_notes_slices/2238-swine-swīn.md<br>packets/2238-swine-swīn.md<br>research_memos/2238-swine-swīn.md |
| 2248 | think | þenċan | dev_notes_slices/2248-think-þenċan.md<br>packets/2248-think-þenċan.md<br>research_memos/2248-think-þenċan.md |
| 2251 | thorn | þorn | dev_notes_slices/2251-thorn-þorn.md<br>research_memos/2251-thorn-þorn.md |
| 2257 | tide | tīd | dev_notes_slices/2257-tide-tīd.md<br>packets/2257-tide-tīd.md<br>research_memos/2257-tide-tīd.md |
| 2260 | token | tācn | dev_notes_slices/2260-token-tācn.md<br>research_memos/2260-token-tācn.md |
| 2263 | town | tūn | dev_notes_slices/2263-town-tūn.md<br>packets/2263-town-tūn.md<br>research_memos/2263-town-tūn.md |
| 2266 | wade | wadan | dev_notes_slices/2266-wade-wadan.md<br>packets/2266-wade-wadan.md<br>research_memos/2266-wade-wadan.md |
| 2270 | warp | weorpan | dev_notes_slices/2270-warp-weorpan.md<br>packets/2270-warp-weorpan.md<br>research_memos/2270-warp-weorpan.md |
| 2272 | wash | wascan | dev_notes_slices/2272-wash-wascan.md<br>packets/2272-wash-wascan.md<br>research_memos/2272-wash-wascan.md |
| 2276 | wax | weaxan | dev_notes_slices/2276-wax-weaxan.md<br>research_memos/2276-wax-weaxan.md |
| 2277 | way | weġ | dev_notes_slices/2277-way-weġ.md<br>packets/2277-way-weġ.md<br>research_memos/2277-way-weġ.md |
| 2278 | weapon | wǣpn | dev_notes_slices/2278-weapon-wǣpn.md<br>packets/2278-weapon-wǣpn.md<br>research_memos/2278-weapon-wǣpn.md |
| 2293 | will | willa | dev_notes_slices/2293-will-willa.md<br>packets/2293-will-willa.md<br>research_memos/2293-will-willa.md |
| 2294 | wind | windan | dev_notes_slices/2294-wind-windan.md<br>packets/2294-wind-windan.md<br>research_memos/2294-wind-windan.md |
| 2297 | wold | weald | dev_notes_slices/2297-wold-weald.md<br>research_memos/2297-wold-weald.md |
| 2305 | yarn | ġearn | dev_notes_slices/2305-yarn-ġearn.md<br>packets/2305-yarn-ġearn.md<br>research_memos/2305-yarn-ġearn.md |

## P3: Existing manifest-backed pilot reports

These rows already have manifest-backed production reports. They should later be reviewed for possible promotion to `full`, but they are **not** part of the missing-production backlog and should not be casually rewritten.

### Current pilot production reports

| ID | CONCEPT | COUNTERPART | Class | Status | Production path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1936 | ban | bannes | late_analogy | manifest_pilot | pilot/ban.md |
| 1946 | berry | berġes | late_analogy | manifest_pilot | pilot/berry.md |
| 1959 | bottom | botm | early_analogy | manifest_pilot | pilot/bottom.md |
| 1973 | buck | bucc | unexplained_unmodelled | manifest_pilot | pilot/buck.md |
| 1981 | craft | cræft | early_analogy | manifest_pilot | pilot/craft.md |
| 1983 | cud | cwedu | attested_variant | manifest_pilot | pilot/cud.md |
| 2013 | fire | fȳre | known_unmodelled | manifest_pilot | pilot/fire.md |
| 2151 | reek | rēac | reconstructed_oe | manifest_pilot | pilot/reek.md |
| 2203 | span | spanne | late_analogy | manifest_pilot | pilot/span.md |
| 2240 | tap | tæppa | known_unmodelled | manifest_pilot | pilot/tap.md |
| 2250 | thistle | þistles | late_analogy | manifest_pilot | pilot/thistle.md |

### Current format-test manifest entry

| ID | CONCEPT | COUNTERPART | Class | Status | Production path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1933 | adder | nǣdre | regular | format_test | pilot/adder.md |

## Recommended model-entry candidates

- **2183 shoulder / sċuldrum** (late_analogy): Late-analogy dat.pl. case with the richest packet in the backlog; best single stress test for paradigm-cell handling and schema discipline.
- **1980 cow / cȳ** (late_analogy): Clean root-noun oblique-cell case with a dedicated analysis dossier; strong late-analogy candidate with manageable scope.
- **2053 hammer / hameres** (late_analogy): Gen.sg. oblique-form solution with attested hamor/hamer alternants; ideal for distinguishing citation proto from FST input.
- **1958 both / bū** (regular): Regular row but unusually rich lexical note; tests how the final prose separates OE evidence, ModE headword history, and project-specific note history.
- **2302 world / weorold** (early_analogy): Early-analogy compound/transponent case with a clear PROTO vs PROTOFORM split; good model for explaining compound-specific inputs without reopening phonology.

Read existing pilot `2013 fire / fȳre` alongside these candidates as a **comparison benchmark**, not as the automatic final model; it is already a pilot and may reflect an earlier prose style.

## Proposed 10-entry pilot batch

This batch is designed to test the full spread of report types before wider production. It includes exactly 10 entries: 2 `late_analogy`, 2 `early_analogy`, 2 `regular` with NOTE, 1 `attested_variant`, 1 `reconstructed_oe`, 1 `unexplained_unmodelled`, and 1 existing manifest-backed pilot as a review benchmark.

| ID | concept | counterpart | class | source material | why in pilot batch | exception agent |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2183 | shoulder | sċuldrum | late_analogy | dev_notes_slices/2183-shoulder-sċuldrum.md<br>packets/2183-shoulder-sċuldrum.md<br>research_memos/2183-shoulder-sċuldrum.md | Dat.pl. paradigm-cell case with explicit packet evidence and a real paradigm-probe requirement; strongest late-analogy stress test. | yes |
| 1980 | cow | cȳ | late_analogy | dev_notes_slices/1980-cow-cȳ.md<br>packets/1980-cow-cȳ.md<br>research_memos/1980-cow-cȳ.md | Root-noun oblique-cell solution with explicit dat.sg. evidence and a dedicated analysis memo; good contrast with shoulder. | maybe |
| 2027 | follow | fylġan | early_analogy | dev_notes_slices/2027-follow-fylġan.md<br>packets/2027-follow-fylġan.md<br>research_memos/2027-follow-fylġan.md | Clear Class II citation vs Class I inherited-form split with a well-documented Mercian/Northumbrian target. | no |
| 2296 | withy | wīþiġ | early_analogy | dev_notes_slices/2296-withy-wīþiġ.md<br>packets/2296-withy-wīþiġ.md<br>research_memos/2296-withy-wīþiġ.md | Suffix-etymology correction from *-ijaz to *-agą gives a rich but bounded early-analogy case for the pilot batch. | no |
| 1958 | both | bū | regular | dev_notes_slices/1958-both-bū.md<br>packets/1958-both-bū.md<br>packets/1962-bow-bēag.md<br>research_memos/1958-both-bū.md | Regular row with dense note/history content; useful for testing concise schema-conformant prose on a non-analogical but philologically messy entry. | no |
| 2095 | learn | liornian | regular | dev_notes_slices/2095-learn-liornian.md<br>packets/2095-learn-liornian.md<br>research_memos/2095-learn-liornian.md<br>research_memos/batch_22_summary.md | Regular row with dialectal selection and ablaut-grade discussion; good test of how much philology a regular report should retain. | maybe |
| 2273 | wasp | wæfs | attested_variant | dev_notes_slices/2273-wasp-wæfs.md<br>packets/2273-wasp-wæfs.md<br>research_memos/2273-wasp-wæfs.md | Strong attestation dossier for retargeting to the earliest OE form; ideal attested-variant pilot. | no |
| 2087 | knob | cnobba | reconstructed_oe | dev_notes_slices/2087-knob-cnobba.md<br>packets/2087-knob-cnobba.md<br>research_memos/2087-knob-cnobba.md | Compact reconstructed-OE case with explicit unattested-status note and a bounded supporting argument. | maybe |
| 2300 | wool | wull | unexplained_unmodelled | dev_notes_slices/2300-wool-wull.md<br>packets/2300-wool-wull.md<br>research_memos/2300-wool-wull.md | Documented exception with no plausible paradigm escape route; useful pilot for the “genuine exception” write-up style. | maybe |
| 2013 | fire | fȳre | manifest_pilot_benchmark | pilot/fire.md | Existing manifest-backed pilot report to review as a style benchmark before promoting any new entries to production prose. | no |

## Exception-agent triggers

- Use a separate exploratory agent only when the packet exposes a **real gap**, not just because the entry is difficult.
- Trigger an exception agent when there is **source disagreement not resolved in the packet**.
- Trigger an exception agent when there is **no clear attestation for the OE target** or when the target appears to have shifted without a settled rationale.
- Trigger an exception agent when there is an **unexplained `PROTO` / `PROTOFORM` mismatch** that the packet does not already resolve.
- Trigger an exception agent for a **late_analogy** row when the report depends on a paradigm probe that the packet has not already made persuasive.
- Trigger an exception agent for an **unexplained_unmodelled** row when the current label may be either too weak or too strong for the evidence packet.

## Next recommended task

After this backlog is accepted, the next task should be to produce **one polished model lexeme entry** from the recommended candidate list and use that result to set the prose standard before any wider batch drafting.

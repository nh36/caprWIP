# Research memo — 1968 breast / brēost

## Starting point

- **ID:** 1968
- **CONCEPT:** breast
- **COUNTERPART:** brēost
- **PROTO:** *brústz
- **PROTOFORM:** *bréustą
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** -

The live row already encodes a three-way distinction: cognate-set `PROTO = *brústz`, OE derivational input `PROTOFORM = *bréustą`, and attested OE target `brēost`. The central memo question is whether that distinction is current and justified, or whether older project history pushing `*breustą` into other columns should be treated as superseded.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing that current input `*bréustą` yields `brēost`; and the lexical-table support in `old_english_wiktionary.tsv` and `old_english_swadesh.tsv` for attested OE `brēost`.
- **Useful background:** the packet’s `DEV_NOTES.md:5924-6006` section, which correctly assembles the scholarly reason that OE belongs with thematic `*breusta-` rather than root-noun `*brust-`; and the packet’s verification snippet confirming `breustą -> brēost`.
- **Stale or superseded:** the packet’s older diagnostic hit at `DEV_NOTES.md:1717`, where `*brustz` produced `brust/burst`, is debugging history from the pre-fix state, not current row authority. Also stale as live-row evidence is `DEV_NOTES.md:15917-15990`, which describes an intermediate TSV state where `PROTOFORM` and `PROTO` were assigned differently from the present row.
- **Irrelevant or misleading:** the absence of dossier/analysis hits is not evidence against the row; and the packet should not be read as proving that `PROTO`, `PROTOFORM`, and the OE target all ought to collapse to the same form. For this lexeme, that collapse is exactly the issue under review.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 1715-1718, 5924-6006, 10400, and 15917-15990.
- `Germanic/data/oe_known_problems.tsv` — no entry for this row or lexeme.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — `*breusta-` and `*brust-` entries.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — `*breustan` and `*brustz` entries.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — `PNWGmc *breusta ‘breast’ ... > OE bréost`.
- `docs/references/campbell_old_english_grammar.txt` — `OS breost` as a standard `eu > eo` comparison point.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — headword `brēost`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — full `breóst` entry and inflectional examples.
- Current binary check with `old_english.bin`: `breustą -> brēost`, `brustz -> burst`.

No full dossier or analysis file specifically named in the packet or TSV note was identified for this lexeme, and no pilot lexeme report exists for `breast / brēost`.

## Reconstruction and early-stage forms

This row only makes sense if three different levels are kept separate.

1. **Cognate-set proto / project headword:** TSV `PROTO` `*brústz`, the root-noun formation that still underlies the broader cognate set in this packet cluster (compare the neighbouring English, Dutch, and German rows).
2. **Project input form for OE derivation:** TSV `PROTOFORM` `*bréustą`, the thematic e-grade formation required to derive OE `brēost` in the current cascade.
3. **OE target form:** attested citation-form `brēost`.

Repo-local reference evidence supports that distinction. Kroonen separates `*breusta-` n. ‘breast, chest’ (ON `brjóst`, OE `breost`, OFri. `briast`, OS `briost`) from root-noun `*brust-`, and says the two are in an unclear ablaut relation with largely complementary dialectal distribution. Orel likewise gives `*breustan` for the OE/ON/OFris/OS set and `*brustz` separately for Gothic/OFris/MLG/OHG. Ringe & Taylor explicitly cite `PNWGmc *breusta ... > OE bréost`.

So the live row’s split is defensible: `PROTO` names the broader cognate-set headword, while `PROTOFORM` names the OE-relevant early-stage variant. The stale March-April 2026 note history matters only as chronology. It shows that the project initially treated this as a bad-input mismatch and briefly experimented with moving `*breustą` into other columns before the current `PROTO`/`PROTOFORM` distinction settled.

## Old English philology

`brēost` is an attested Old English lexeme, not a reconstructed WS convenience form and not an inflected-cell workaround. `old_english_wiktionary.tsv`, `old_english_swadesh.tsv`, Clark Hall, and Bosworth-Toller all support the citation form `brēost`/`breóst`.

The philological caution is grammatical, not attestational. Clark Hall labels `brēost` `nmf.` and notes that it is usually plural; Bosworth-Toller likewise notes that the word occurs in all three genders and can be used in the plural/dual for a single person. So the memo should not overstate a single fixed gender analysis. But none of that undermines the row’s target: the row is clearly aimed at the bare lexical form `brēost`, not at some specific oblique cell.

No specific manuscript or dialect restriction needs to be claimed from the checked repo sources. The safest statement is simply that `brēost` is a well-attested OE lexeme whose vowel points to the `*breusta-` formation.

## Project problem and solution

The original project problem was a false phonology alarm created by feeding OE from the wrong proto formation: `*brustz` gave `burst`, which looked like missing breaking. The later source review showed that this was not primarily a sound-law failure. OE `brēost` belongs to the `*breusta-` branch, where `*eu` regularly yields OE `ēo`.

The current row therefore looks basically right in design. It is not a `late_analogy` paradigm-cell rescue. It is an `early_analogy` / early-formation choice: keep the cognate-set headword `*brústz`, but derive OE from `*bréustą`, the variant that actually leads to `brēost`.

What still needs improvement is not the core solution but the project’s explicitness. The live TSV note is blank, and the surviving `DEV_NOTES` chronology can easily mislead a packet into thinking the present recommendation is to rewrite every column to `*breustą`. The memo evidence does not support that stronger claim. It supports keeping the column distinction clear.

## Paradigm probe

No paradigm probe is required.

This is not a missing-OE-cell problem. The decisive contrast is upstream between `*brústz` and `*bréustą`, not between nominative, genitive, dative, or plural OE cells. The current binary sanity check (`breustą -> brēost` versus `brustz -> burst`) is sufficient for the memo stage.

## Recommended final report

Recommend a concise final report that says OE `brēost` is an attested lexeme belonging to the thematic/ablaut `*breusta-` formation, while the row intentionally keeps cognate-set `PROTO = *brústz` distinct from derivational `PROTOFORM = *bréustą`. Older `DEV_NOTES` that assign `*breustą` to other columns should be treated as project chronology, not as final authority.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. Keeping `*brústz` as the cognate-set/project headword is defensible if `PROTOFORM` continues to encode the OE-specific variant.
- **TSV `PROTOFORM`:** no change recommended. `*bréustą` is the right derivational input for OE `brēost`.
- **TSV `COUNTERPART`:** no change recommended. `brēost` is the correct OE target.
- **TSV `DERIVATION_CLASS`:** no change recommended. `early_analogy` fits an upstream formation/ablaut selection better than `late_analogy` or `regular`.
- **TSV `NOTE`:** **change recommended** — add a short note explaining that OE reflects thematic `*breusta-/*breustą`, so `PROTOFORM` intentionally differs from cognate-set `PROTO *brústz`.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES/dossier text:** **change recommended** — lightly clean up or cross-reference the March-April 2026 `DEV_NOTES` sections so they state clearly that earlier “change PROTO / correct PROTOFORM” discussions are historical debugging stages, whereas the live row now distinguishes `PROTO = *brústz` from `PROTOFORM = *bréustą`.

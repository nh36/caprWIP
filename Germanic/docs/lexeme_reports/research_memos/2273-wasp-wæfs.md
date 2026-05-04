# Research memo — 2273 wasp / wæfs

## Starting point
- ID `2273`; CONCEPT `wasp`; COUNTERPART `wæfs`.
- Live TSV `PROTO` = `*wábsaz`; live TSV `PROTOFORM` = `*wábsaz`; TSV `DERIVATION_CLASS` = `attested_variant`.
- TSV note says the row was retargeted from late West Saxon `wæsp` to earliest attested OE `wæfs`, citing Épinal-Corpus `waefs`, Bülbring §484 Anm.3, Fulk §6.5, and Brunner §193,3; it also explains the later doublet chain `wæfs > wæps > wasp`.
- No standalone pilot/full report exists for this lexeme in `Germanic/docs/lexeme_reports/pilot/`; generated debug-snapshot material is background only, not final authority.

## Packet evidence assessment
- **Authoritative/current:** the live TSV row; the packet's compact derivation trace `*wábsaz -> wæfs`; and the packet's `DEV_NOTES §17.47` extracts showing that the current project decision is to target `wæfs`, not older `wæsp`.
- **Useful background:** the packet's lexical-table hit from `old_english_wiktionary.tsv`, because it explains why a dictionary-style `wæsp` headword could have been mistaken for the row target; and the packet's bibliography-key suggestions, which correctly point to repo-local Fulk/Brunner material.
- **Stale or superseded:** the packet's older diagnostic history in which `wæsp` is still the expected target; the dry-run regression snippet (`wabsăz -> wafs (should be wæsp)`); and any packet language that treats the earlier mismatch state as if it were still live evidence.
- **Irrelevant or misleading if over-weighted:** the packet's blanket statement that a paradigm probe is required; this row is a lexical-variant chronology problem, not an unresolved inflectional-cell selection problem. `old_english_wiktionary.tsv` is also misleading if its headword-like `wæsp` is treated as better authority than the handbook-backed retargeting to `wæfs`.

## Additional repo research
Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at the full `§17.47` section and the older dry-run regression note.
- `Germanic/tools/oe_paradigm_probe.py` to confirm whether any built-in probe spec already exists for this lexeme.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/oe_known_problems.tsv`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and debug snapshots under `Germanic/docs/debug_snapshots/`.
- Repo-local reference extracts in `docs/references/`: `bulbring_altenglisches_elementarbuch.txt`, `brunner_1965_altenglische_grammatik.txt`, `clark_hall_concise_anglo_saxon_dictionary.vision.txt`, and `fulk_comparative_grammar_early_germanic.vision.txt`.

No separate dossier or analysis file was named in the packet or TSV note beyond `DEV_NOTES §17.47`, so there was no further full dossier to audit.

Main findings from that wider check:

- Bülbring's text explicitly gives late WS `wasp` from `wæps`, itself from Corpus `waefs`.
- Brunner §193,3 explicitly says the oldest monuments still have `fs` spellings (`Ep. Corp. waefs`) and treats `fs > ps` as a restricted development.
- Brunner §204,3 then treats `ps > sp` in `wæsp/wasp` as a later West Saxon metathesis restricted to a small dialect area.
- Clark Hall lemmatizes `wæps`, with `wæfs` and `wæsp` as cross-references, which confirms that dictionary headword practice does not by itself identify the earliest or project-best target.
- `oe_paradigm_probe.py` has no built-in wasp spec, but that absence does not create a real evidence gap here.

## Reconstruction and early-stage forms
This row still needs a three-way distinction even though the live TSV uses the same string in both proto columns.

1. **Cognate-set proto / comparative headword:** `*wábsaz`, the PGmc lexeme behind the wider Germanic set.
2. **Project input form for OE derivation:** also `*wábsaz`, because the current OE row is modelling the regular phonological development of that same stem.
3. **OE target form represented by the row:** attested early OE `wæfs` (orthographic `waefs` in the Épinal-Corpus evidence).

The important chronological staging is `*wábsaz > *wábsa > *wæbs > *wæβs > wæfs`. The later forms `wæps` and `wæsp/wasp` are not alternative proto inputs; they are later OE developments after lexically restricted metathesis. So the project should not collapse cognate-set proto, derivational input, and the later dictionary/headword variants into one undifferentiated chain.

## Old English philology
`wæfs` should be treated as an attested OE form, not as a reconstructed convenience output. The strongest repo-local philological support is the direct `waefs` evidence cited by Bülbring and Brunner from the Épinal-Corpus glossaries.

The variant set matters:

- **earliest attested form:** `waefs` / normalized `wæfs`;
- **later metathesized form:** `wæps`;
- **later West Saxon/dialectally restricted form:** `wæsp` / `wasp`.

Clark Hall's lemma practice (`wæps`, with cross-references from `wæfs` and `wæsp`) shows that dictionary normalization and earliest attestation are not the same thing. The row therefore intentionally selects one attested variant from a real OE variant set; it is not claiming that `wæps` or `wæsp` are unreal, only that they are later and less suitable as the project's base target.

## Project problem and solution
The project problem was not a broken sound change. The OE cascade already produced the regular early form `wæfs`; the mismatch came from having targeted the later doublet `wæsp`.

The current solution is the right one:

- keep `COUNTERPART = wæfs`;
- keep the row as an `attested_variant` entry, since the project is choosing one attested form from a wider attested set;
- do **not** add general `fs > ps` or `ps > sp` rules merely to recover late, lexically restricted variants.

This is the same kind of target-selection correction described in `DEV_NOTES §17.47`: prefer the directly attested, lautgesetzlich early OE form when the later headword-like form depends on restricted late metathesis.

## Paradigm probe
No paradigm probe is required.

This row is not a hidden genitive/dative/plural cell case and not a `late_analogy`-style paradigm-selection problem. The dispute is entirely about which **citation-form lexical variant** the row should target (`wæfs` versus later `wæps/wæsp`), and the decisive evidence already comes from handbook and glossary chronology rather than from missing paradigm-cell testing.

## Recommended final report
Recommend a concise final report that says row 2273 intentionally targets attested early OE `wæfs`/`waefs` from regular `*wábsaz`, while distinguishing later attested doublets `wæps` and late-WS `wæsp/wasp` as lexically restricted metatheses that should be mentioned in prose, not promoted to the row's primary target.

## Data-change recommendations
- **TSV `PROTO`:** no change recommended; keep `*wábsaz`.
- **TSV `PROTOFORM`:** no change recommended; keep `*wábsaz`.
- **TSV `COUNTERPART`:** no change recommended; keep `wæfs`.
- **TSV `DERIVATION_CLASS`:** no change recommended; `attested_variant` still fits.
- **TSV `NOTE`:** no substantive change recommended; the live note already captures the chronology and project choice. At most, a later editorial tightening could mention more explicitly that `waefs` is the attested spelling behind normalized `wæfs`, but this is optional.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no required change. `DEV_NOTES §17.47` already functions as the authoritative current dossier, and no separate dossier file was identified. Older regression snippets are historical background only, but they do not require cleanup for this memo to be usable.

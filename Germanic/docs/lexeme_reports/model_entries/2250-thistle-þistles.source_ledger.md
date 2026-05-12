# Source extraction ledger — thistle / þistles

This ledger records the evidence used for the P3 rewrite from pilot material.

| Source | Form(s) given | Claim relevant to the entry | Citation key available? | Where this claim was found locally | Confidence / review note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TSV row 2250 and compact trace | `PROTO *θéstilaz`; `PROTOFORM *θístilas`; `*θístilas -> þistles` | Establish the comparative headword, selected gen.sg. input, and live output. | no | `Germanic/data/germanic-aligned-final.tsv`; `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md` | high |
| Pilot report and research memo | `*θéstilaz -> þistl`; `*θístilas -> þistles`; `þistel`; `þistles` | Confirm that the entry is now a gen.sg. paradigm-cell solution and that the pilot needs a current-format rewrite. | no | `Germanic/docs/lexeme_reports/pilot/thistle.md`; `Germanic/docs/lexeme_reports/research_memos/2250-thistle-þistles.md` | high |
| DEV_NOTES slice and packet | `þistel`; `þistles`; `*θéstilaz`; `*θístilas` | Preserve the cluster-noun policy and the specific move to the gen.sg. cell. | no | `Germanic/docs/lexeme_reports/dev_notes_slices/2250-thistle-þistles.md`; `Germanic/docs/lexeme_reports/packets/2250-thistle-þistles.md` | high |
| Orel | `*þe(x)stilaz`; OE `þistel` | Supplies the comparative `*e`-grade headword background. | yes — `Orel2003` | `docs/references/legacy/orel_handbook_germanic_etymology.txt`; memo | high |
| Kluge-Seebold | `*þistila-`; daughter-language `i` forms | Supplies the competing `*i`-grade comparative tradition behind the selected input. | yes — `KlugeSeebold2011` | `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`; memo | high |
| Clark Hall | `ðistel` | Confirms the simplex Old English headword tradition. | yes — `ClarkHall1960` | `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | high |
| Campbell | `hrefn`, `tacn`, `wépn`, `botm`; parasite-vowel discussion | Supplies the phonological contrast between broken simplex forms and unbroken cluster forms in comparable nouns. | yes — `Campbell1959` | `docs/references/campbell_old_english_grammar.txt`; memo | high; local file prints `tdcn` once at line 9975, but gives `tacn token` clearly at line 14506 and cross-references `tdcn` as the same word |

## Citation-locator pilot 01 note

- Verified page locators in the local reference files for `Orel2003` (p. 458),
  `ClarkHall1960` (p. 326), and `Campbell1959` (p. 151).
- `KlugeSeebold2011` was checked, but the local text file preserves the `Distel`
  entry without a reliable nearby page marker, so the model entry keeps that
  citation broad in this pilot.

## Notes

- The local reference files checked here support simplex `þistel/ðistel` more directly than the exact gen.sg. `þistles`; the exact inflected target is better documented in the row-local memo, packet, and DEV_NOTES material than in the compact dictionaries.
- No Campbell Google Vision-backed file was available locally; the correction from `tdcn` to `tacn` rests on the clearer internal Campbell occurrence `tacn token` and the file's own cross-reference to `tdcn`.
- No unresolved OCR or encoding artifact was reproduced in final prose.

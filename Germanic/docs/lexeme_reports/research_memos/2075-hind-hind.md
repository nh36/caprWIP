# Research memo — 2075 hind / hind

## Starting point

Row 2075 is `CONCEPT=hind`, `COUNTERPART=hind`, `PROTO=*xéndjō`, `PROTOFORM=*xéndjō`, `DERIVATION_CLASS=regular`. The TSV `NOTE` already states the core issue: Kroonen gives `*hindō-` f. ‘hind (deer)’, yielding OE `hind` f., and `hindan` ‘from behind’ is the wrong lexeme. The current compact derivation trace agrees with the row and now outputs `hind`.

## Packet evidence assessment

Authoritative/current packet material: the live TSV row and the current derivation trace are the main evidence. They show that the project’s present modelling input is `*xéndjō` and that the live OE outcome is `hind`, not `hindan`.

Useful background: the packet’s `old_english_wiktionary.tsv` hit is useful as a warning sign, because it shows where the noun has been confused with the unrelated OE adverb/preposition `hindan`.

Stale or superseded: the packet itself does not include stale dossier material, but it omits older repo documents that still mention `*xendjō → hindan`; those older mentions are diagnostic history only, not current authority.

Irrelevant or misleading if over-read: the `old_english_wiktionary.tsv` lookup is supplementary only and is misleading here if treated as evidence for the noun row.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/lexeme_reports/source_inventory.md` and `report_schema.md` for source hierarchy and the required `PROTO`/`PROTOFORM`/target distinction.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`, which has `*hindō-` f. ‘hind’ and explicitly lists OE `hind` f. [@Kroonen2013].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`, which separates noun `hind(y) f. ‘hind, female deer’` from `hindan` ‘from behind, behind, in the rear’ [@ClarkHall1960].
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`, which likewise has separate entries for noun `hind` and adverb/preposition `hindan` [@BosworthToller1898].
- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` and `Germanic/docs/germanic_transducer_report.md`, both of which preserve older diagnostic statements expecting `hindan`; these are stale project history, not current lexical evidence.
- `Germanic/data/oe_known_problems.tsv`, `Germanic/docs/DEV_NOTES.md`, `Germanic/docs/analysis/`, and `Germanic/docs/dossiers/`: no dedicated current problem entry or dossier for this lexeme.
- `Germanic/docs/lexeme_reports/pilot/`: no existing pilot report for this lexeme.

## Reconstruction and early-stage forms

The cognate-set headword in the external etymological source is Kroonen’s `*hindō-` f. ‘hind’ [@Kroonen2013]. The project’s row, however, uses `*xéndjō` in both `PROTO` and `PROTOFORM`, and the live trace treats that as the modelling input (`Proto Input: *xéndjō`). The present pipeline then derives NWGmc `*xéndju` and OE `*çindju > *çindj > *çind`, surfacing as `hind`.

So three levels must be kept distinct:

1. cognate-set proto/headword: `*hindō-`;
2. project derivational input: `*xéndjō`;
3. OE target lexeme: noun `hind`.

Older repo notes that say `*xendjō → hindan` are not alternative reconstructions of the same noun; they are evidence of an earlier project misidentification.

## Old English philology

The OE target here is the noun `hind` ‘female deer’, not the adverb/preposition `hindan` ‘from behind, behind’. Kroonen’s dictionary gives OE `hind` under `*hindō-` [@Kroonen2013]. Clark Hall and Bosworth-Toller both support the same lexical split: `hind` is the deer noun, while `hindan` is a separate adverb/preposition [@ClarkHall1960; @BosworthToller1898].

That means the packet’s `old_english_wiktionary.tsv` match (`hind → hindan`) is a headword/template problem, not philological authority for row 2075. It may be useful as a diagnostic of why the row acquired a note, but it should not be cited as evidence for the noun lexeme.

## Project problem and solution

The project problem is not phonological failure in the current row; the live derivation already reaches `hind`. The real issue is lexeme disambiguation. A supplementary lookup table and some older internal diagnostic prose confused the noun `hind` with `hindan` ‘from behind’.

The project solution should therefore be: keep row 2075 tied to noun `hind`, keep the current derivational path that now outputs `hind`, and treat all `hindan` material as evidence about a different OE lexeme unless a source explicitly discusses the deer noun.

## Paradigm probe

No paradigm probe is required. This is a `regular` row, and the issue is lexical disambiguation rather than analogical inflection or a disputed paradigm cell.

## Recommended final report

The eventual `### Lexeme report` should be short. It should distinguish Kroonen’s cognate-set headword `*hindō-` from the project’s modelling input `*xéndjō`, note that the current pipeline now derives OE `hind`, and explain with dictionary support that `hindan` belongs to a different OE lexeme [@Kroonen2013; @ClarkHall1960; @BosworthToller1898]. No substantive paradigm section is needed.

## Data-change recommendations

- **TSV `PROTO`**: no change recommended now.
- **TSV `PROTOFORM`**: no change recommended now.
- **TSV `COUNTERPART`**: no change recommended.
- **TSV `DERIVATION_CLASS`**: no change recommended.
- **TSV `NOTE`**: no change required; it already captures the essential disambiguation.
- **`oe_known_problems.tsv`**: no change recommended; this is not a current unresolved modelling failure.
- **`DEV_NOTES` / dossier text**: no change recommended, because there is no dedicated current DEV_NOTES or dossier entry for this lexeme.

However, I do recommend ancillary cleanup outside those fields: `Germanic/data/old_english_wiktionary.tsv` should be reviewed for its misleading `hind → hindan` mapping, and older historical-diagnostic prose in `Germanic/docs/germanic_transducer_report.md` and `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` should be corrected or explicitly marked as superseded so they do not continue to look like live lexical evidence.

# Citation-locator rescue pilot 02 report

## Summary

- Unresolved citation occurrences investigated: **14**
- Resolved with page locators: **13**
- Left broad because passage/page could not be verified: **1**
- Left broad because a page locator would be misleading: **0**
- Model entries changed: **4**
- Model entries unchanged: **1**

This rescue pass stayed limited to the five unresolved pilot-01 entries. No OCR
line number, file offset, or search-result position was used as a locator.

## Difficult-source inventory

The detailed source inventory is in
`Germanic/docs/lexeme_reports/model_entries/citation_locator_source_inventory.md`.

In brief:

- `Campbell1959` is usable now, but only claim by claim: the printed page number
  must be recovered in the same local span as the cited passage.
- `BosworthToller1898` is more usable than pilot 01 suggested when the needed
  supplement entry is present, because the file has explicit `=== page N ===`
  markers.
- `Luick1914` is page-marked cleanly and can be localized safely with layered
  lemma-plus-topic searches.
- `RingeTaylor2014` remains a high-confidence source.
- `KlugeSeebold2011` remains blocked: the `Distel` entry is isolable, but the
  page number is not.

## Entry-by-entry results

### 1962 bow / bēag

- Unresolved citations investigated: `Campbell1959` (2), `BosworthToller1898`
- Search methods used: `Class II`, `au`, `preterite`, `bugan`, `bēag`, normalized
  and OCR-tolerant variants
- Source files consulted:
  `campbell_old_english_grammar.txt`,
  `bosworth_toller_anglo_saxon_dictionary.vision.txt`
- Locator outcome:
  `Campbell1959, 53`; `BosworthToller1898, 122`
- Model-entry changes made: localized all formerly broad citations in the file
- Remaining unresolved citations: none

### 1981 craft / cræft

- Unresolved citations investigated: `BosworthToller1898`
- Search methods used: line-start headword search for `cræft` plus nearby entry
  inspection
- Source files consulted:
  `bosworth_toller_anglo_saxon_dictionary.vision.txt`
- Locator outcome: `BosworthToller1898, 145`
- Model-entry changes made: localized the formerly broad Bosworth-Toller
  citation
- Remaining unresolved citations: none

### 2030 fowl / fugol

- Unresolved citations investigated:
  `RingeTaylor2014` (2), `Campbell1959` (3), `BosworthToller1898`,
  `Luick1914`
- Search methods used:
  exact OE forms (`fugol`, `fugel`, `fogol`), reconstructed forms
  (`*fuglaz`, `*fogl`), technical terms (`lowering`, `parasite vowel`,
  `labial`), and normalized/OCR-friendly variants (`fuzol`, `folzian`)
- Source files consulted:
  `ringe_taylor_linguistic_history_vol2.txt`,
  `campbell_old_english_grammar.txt`,
  `bosworth_toller_anglo_saxon_dictionary.vision.txt`,
  `luick_historische_grammatik.txt`
- Locator outcome:
  `RingeTaylor2014, 42–43`, `345`, `47`;
  `Campbell1959, 43`, `150`;
  `BosworthToller1898, 282`;
  `Luick1914, 148`
- Model-entry changes made: localized every formerly broad citation in the file
- Remaining unresolved citations: none

### 2250 thistle / þistles

- Unresolved citations investigated: `KlugeSeebold2011`
- Search methods used:
  `Distel`, `distil`, `distila`, `thistil`, `*þist`, and nearby entry
  inspection
- Source files consulted:
  `kluge_seebold_etymologisches_woerterbuch.txt`
- Locator outcome: passage isolated, page not verified
- Model-entry changes made: none
- Remaining unresolved citations: `KlugeSeebold2011`

### 2278 weapon / wǣpn

- Unresolved citations investigated: `Campbell1959` (2)
- Search methods used:
  `wǣpen`, `wapen`, `wǣpn`, `wǣpnes`, `wépn`, `weapon`,
  `parasite vowel`, and cluster-noun examples
- Source files consulted:
  `campbell_old_english_grammar.txt`
- Locator outcome:
  `Campbell1959, 150`; `Campbell1959, 226–227`
- Model-entry changes made:
  localized the Campbell citations and narrowed the Campbell-backed wording to
  the cluster-noun behavior that the local file actually shows
- Remaining unresolved citations: none

## Successful rescues

- `1962-bow-bēag.model.md`:
  `[@Campbell1959]` -> `[@Campbell1959, 53]`
- `1981-craft-cræft.model.md`:
  `[@BosworthToller1898]` -> `[@BosworthToller1898, 145]`
- `2030-fowl-fugol.model.md`:
  `[@RingeTaylor2014; @Campbell1959]` ->
  `[@RingeTaylor2014, 42–43; @Campbell1959, 43]`
- `2278-weapon-wǣpn.model.md`:
  broad Campbell support ->
  `[@Campbell1959, 150; @Campbell1959, 226–227]` after narrowing the claim to
  cluster-noun behavior

## Unresolved cases

- `2250-thistle-þistles.model.md` / `KlugeSeebold2011`
  - **Outcome:** left broad
  - **Why:** passage found, page marker unreliable
  - **Exact problem:** the local text isolates the `Distel` entry, but the nearby
    source span preserves only a form-feed boundary and no citable numeric page
    label

No other unresolved case from pilot 01 remained unresolved after this rescue
pass.

## Recommendation for next locator phase

**Decision: A. Full-corpus high-confidence-source pass is safe now.**

Reasoning:

1. The clean page-marked sources were already safe after pilot 01.
2. Rescue pilot 02 shows that `Campbell1959`, `BosworthToller1898`, and
   `Luick1914` are not globally unusable; they can be localized safely when the
   search is layered and the page marker is confirmed in place.
3. The only clearly blocked source in this scoped set is `KlugeSeebold2011`,
   where passage recovery is possible but page recovery is not.

Recommended next sequence:

1. Full-corpus pass over high-confidence sources:
   `Kroonen2013`, `Orel2003`, `ClarkHall1960`, `RingeTaylor2014`, `Fulk2018`,
   `Seebold1970`, `BrightCassidyRingler1971`
2. Claim-by-claim locator pass for recoverable conditional sources:
   `Campbell1959`, `BosworthToller1898`, `Luick1914`
3. Quarantine/source-preparation list:
   `KlugeSeebold2011` and any future case where the passage can be found but the
   page number cannot be demonstrated from the local source

## Scope confirmation

- Changed model entries were limited to:
  `1962-bow-bēag.model.md`,
  `1981-craft-cræft.model.md`,
  `2030-fowl-fugol.model.md`,
  `2278-weapon-wǣpn.model.md`
- Updated support files were limited to the five scoped source ledgers and the
  paired reviewer checklists / implementation reports for the four changed model
  entries.
- New files were limited to this report and
  `citation_locator_source_inventory.md`.
- `2250-thistle-þistles.model.md` was inspected but not changed.
- `docs/refs.bib` and the local reference files were read only.
- No TSV source data, FST files, `report_manifest.tsv`, pilot reports, packets,
  dev-note slices, research memos, bibliography data, derivation traces,
  writing-skill files, or model entries outside the five scoped entries were
  changed.

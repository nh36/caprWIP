# Citation-locator source inventory

## Difficult-source inventory for rescue pilot 02

| Citation key | Local file(s) checked | Source type | Page markers present? | Exact page-marker format | Marker position relative to content | OCR line numbers clearly separate from page numbers? | Best search strategy | Better local OCR / Google Vision version found? | Page locators usable now? | Preparation needed / note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `Campbell1959` | `docs/references/campbell_old_english_grammar.txt` | grammar-like | yes, but only after passage-level verification | form-feed plus printed page number in OCR (`150`, `§ 114 ... 43`, `§ 133 ... 53`) | after the form-feed/header block and before the running page text | yes | search exact forms plus section terms (`Class II`, `parasite vowel`, `weapon`, `fugol`), then confirm the printed page number in the same local span | no better local OCR / Vision file found | yes, claim by claim | Safe for targeted citation rescue, but not for bulk automatic localization. |
| `BosworthToller1898` | `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` | dictionary-like (supplement) | yes | `=== page N ===` | before page content | yes | search headwords at line start plus normalized variants (`bugan`, `cræft`, `fugel`), then map to the nearest preceding page marker | local source PDF exists, but no better local OCR / Vision text of the base dictionary was found | yes, when the supplement headword or addendum line is present | The local text is the supplement, not the full base dictionary; base-dictionary-only claims would still need another source or manual PDF review. |
| `Luick1914` | `docs/references/luick_historische_grammatik.txt` | grammar-like | yes | `--- PAGE N ---` | before page content | yes | search exact and normalized forms (`fuzol`, `fugol`, `wolcen`, `folzian`) plus technical terms (`Labial`, `u`, `o`, `Senkung`) | no better local OCR / Vision file found | yes, claim by claim | Safe for targeted rescue where the passage can be isolated directly. |
| `KlugeSeebold2011` | `docs/references/kluge_seebold_etymologisches_woerterbuch.txt` | dictionary-like | no reliable numeric page label at the checked entry | form-feeds occur, but the `Distel` passage has no stable nearby page number | n/a | yes; there are no OCR line numbers in the file, but standalone digits in prose/bibliography cannot be trusted as page labels | search headword at line start plus daughter-language forms (`Distel`, `distil`, `distila`, `thistil`, `*þist`) | no better local OCR / Google Vision file found | no | Passage isolated, page not verified. A page-marked OCR/PDF or direct human page check is needed before final-page localization. |
| `RingeTaylor2014` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | handbook-like | yes | `### PAGE N` | before page content | yes | search exact forms plus sound-change labels (`fuglaz`, `lowered`, `epenthesis`) and verify against the explicit page header | no better local OCR / Vision file found | yes | Cleanest difficult-source case; the residual `fowl / fugol` citations can now be localized reliably. |

## Notes by source

### Campbell1959

- Reliable rescue depends on reading the local OCR in place, not on a blind regex
  pass. The page number is recoverable, but only when the relevant paragraph and
  the nearby printed page label are inspected together.
- This source is usable now for a careful locator pass, but it is still a
  conditional source rather than a bulk-safe one.

### BosworthToller1898

- The local text is explicitly the **Supplement**, which explains why some common
  headwords are absent and why earlier pilot searches were uneven.
- When the supplement does contain the needed entry line, page recovery is
  straightforward because the page markers are explicit.

### Luick1914

- The local file has clean page headers and is more recoverable than pilot 01
  suggested.
- The main risk is not page recovery but claim drift: the search should target
  both the lemma and the phonological discussion around it.

### KlugeSeebold2011

- The `Distel` entry is easy to isolate, but the local text does not preserve a
  citable page number near the entry.
- This is the clearest remaining source-preparation problem from the rescue
  pilot.

### RingeTaylor2014

- The unresolved `fowl / fugol` case did not require a different source, only a
  better decomposition of the claim into general lowering, epenthesis, and
  residual unlowered-`u` discussion.

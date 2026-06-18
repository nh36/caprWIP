# Reader-facing chronology confidence audit 01

## Current basis

1. Latest commit inspected: `1524a14d docs: smooth reader-facing local section 19`.
2. Source chronology tables: `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv` and `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`.
3. Reader-facing reference build: `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md`.
4. Terminology note: this audit avoids the older shorthand for search-limited cases and instead states directly when the test does not constrain one side.

## Chronology-confidence table

| SC number | reader-facing title | current order | diagnostic failure if moved earlier? | diagnostic failure if moved later? | nearest earlier diagnostic constraint | nearest later diagnostic constraint | constraint class | literature/source rationale needed? | notes for final prose |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SC003` | West Germanic rhotacism | `3` | no | yes | none in current test; search runs to the start of the tested early sequence at `SC002` | `SC044` (order `44`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC004` | Proto-West-Germanic ai-monophthongization | `4` | no | yes | none in current test; the search begins at the start of the tested expanded sequence | `SC036` (order `36`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC005` | Unstressed \emph{*a}-raising before final \emph{*m} | `5` | no | yes | none in current test; search runs to the start of the tested expanded sequence at `SC004` | `SC017` (order `17`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | Keep the inflectional pre-`m` setting central and treat the later `SC017` relation as broad/far, not close. |
| `SC006` | Early i-apocope | `6` | no | yes | none in current test; search runs to the start of the tested expanded sequence at `SC004` | `SC034` (order `34`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC007` | Lowering of final bimoric \emph{*ō} before \emph{*r} | `7` | no | yes | none in current test; search runs to the start of the tested expanded sequence at `SC004` | `SC043` (order `43`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC008` | Assimilation of coronal consonants before \emph{*w} | `8` | no | yes | none in current test; search runs to the start of the tested expanded sequence at `SC004` | `SC031` (order `31`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC009` | \emph{ij}-contraction in \emph{friend} | `9` | no | yes | none in current test; search runs to the start of the tested expanded sequence at `SC004` | `SC032` (order `32`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | Keep the `friend` family at the center and say plainly that the later `SC032` relation does not make this a productive law. |
| `SC010` | West Germanic j-gemination | `10` | no | yes | none in current test; search runs to the start of the tested expanded sequence at `SC004` | `SC011` (order `11`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the tight SC010/SC011 seam directly; extra source rationale is secondary. |
| `SC011` | Syllabic \emph{*j} after final-vowel loss | `11` | yes | no | `SC010` (order `10`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the tight SC010/SC011 seam directly and add only a short note on the trace-light later side. |
| `SC012` | \emph{lþ}-voicing | `12` | no | no | none in current test; search runs to the start of the tested expanded sequence at `SC004` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | Add a source-based sentence on northern-West-Germanic scope and say the test does not identify a close ordering constraint. |
| `SC013` | Dental hardening | `13` | no | no | none in current test; search runs to the start of the tested expanded sequence at `SC004` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | Say the placement rests on the comparative history of dental hardening, not on a diagnostic local seam. |
| `SC014` | Monophthongization of unstressed \emph{*ai} | `14` | no | no | none in current test; search stops at bundled `PWGmcChanges` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | Strengthen the source-based explanation of why it opens the unstressed-vowel prelude even though the test does not fix it. |
| `SC015` | Leveling of early unstressed front vowels | `15` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC036` (order `36`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC016` | West Saxon palatal glide before back vowels | `16` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC017` (order `17`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC017` | Lowering of \emph{*u} before following non-high vowels | `17` | yes | yes | `SC016` (order `16`) | `SC019` (order `19`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC018` | Raising of final stressed monosyllabic \emph{*ō} | `18` | no | no | none in current test; search stops at bundled `PWGmcChanges` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | Keep it as a historically legible note whose place is justified by the general vowel history rather than by the test. |
| `SC019` | Raising of final unstressed long \emph{*ō} | `19` | yes | yes | `SC017` (order `17`) | `SC020` (order `20`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC020` | Deletion of word-final \emph{*z} | `20` | yes | yes | `SC019` (order `19`) | `SC040` (order `40`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC021` | Raising of unstressed \emph{*o} before later \emph{*u} | `21` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC040` (order `40`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC022` | Dissimilation of \emph{mn} sequences | `22` | no | no | none in current test; search stops at bundled `PWGmcChanges` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | Final prose should not claim more than a descriptive `mn` dissimilation tendency unless the literature case is strengthened. |
| `SC023` | Loss of n-stem \emph{*n} in final position | `23` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC047` (order `47`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC024` | Lowering of long \emph{ē} before non-nasal consonants | `24` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC056` (order `56`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC025` | Rounding of long \emph{ē} before nasals | `25` | no | no | none in current test; search stops at bundled `PWGmcChanges` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | Explain the nasal-vowel setting from the literature; do not claim that the test fixes the placement. |
| `SC026` | Lengthening before nasal plus spirant | `26` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC027` (order `27`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC027` | Loss of the nasal before spirants | `27` | yes | no | `SC026` (order `26`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC028` | Loss of preconsonantal \emph{*x} | `28` | no | no | none in current test; search stops at bundled `PWGmcChanges` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | Keep the `x`-loss background visible and say the current test does not supply a close relative chronology. |
| `SC029` | Glide formation in \emph{*awj} | `29` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC030` (order `30`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC030` | Fronting of \emph{*au} | `30` | yes | yes | `SC029` (order `29`) | `SC032` (order `32`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC031` | Simplification of \emph{*ww} sequences | `31` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC034` (order `34`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC032` | Leveling of diphthongal outputs | `32` | yes | yes | `SC030` (order `30`) | `SC040` (order `40`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC033` | Long \emph{ēow} before following vowels and weak endings | `33` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC044` (order `44`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC034` | Long \emph{ēaw} before following vowels | `34` | yes | yes | `SC031` (order `31`) | `SC043` (order `43`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC035` | Reduction of prefixal \emph{*a} | `35` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC043` (order `43`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC036` | Raising of medial \emph{*a} between stress peaks | `36` | yes | yes | `SC019` (order `19`) | `SC040` (order `40`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC037` | Syncope of compound linking vowels | `37` | no | technical only | none in current test; search stops at bundled `PWGmcChanges` | technical marker `SC038` (order `38`) | diagnostic support only against a technical marker | yes — technical-marker evidence cannot carry the historical prose alone | Say that the current test only breaks against a technical stage and the historical placement must be justified from surrounding changes and sources. |
| `SC039` | Combinative \emph{*u}-umlaut in \emph{wi}-forms | `39` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC040` (order `40`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC040` | Lowering of medial unstressed \emph{*u} | `40` | yes | yes | `SC039` (order `39`) | `SC072` (order `72`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC041` | Loss of final bare \emph{*a} | `41` | yes | yes | `SC020` (order `20`) | `SC046` (order `46`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC042` | Unrounding of the surviving bimoric \emph{*ō} | `42` | yes | yes | `SC020` (order `20`) | `SC043` (order `43`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC043` | Fronting of low \emph{*a} outside nasal environments | `43` | yes | yes | `SC042` (order `42`) | `SC044` (order `44`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC044` | Breaking before \emph{h}, \emph{rC}, and \emph{lC} | `44` | yes | yes | `SC043` (order `43`) | `SC045` (order `45`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC045` | Palatalization of velar fricatives beside front vowels | `45` | yes | yes | `SC044` (order `44`) | `SC060` (order `60`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC046` | Restoration of \emph{*a} before following back vowels | `46` | yes | yes | `SC043` (order `43`) | `SC048` (order `48`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC047` | Heavy-syllable nasal apocope of final \emph{*ą} | `47` | yes | yes | `SC034` (order `34`) | `SC048` (order `48`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC048` | Secondary nasalization before final \emph{*n} | `48` | yes | yes | `SC047` (order `47`) | `SC059` (order `59`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC049` | Distribution of \emph{*b} after vowels and liquids | `49` | yes | no | `SC037` (order `37`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC050` | Sievers-law syncope | `50` | no | yes | none in current test; search stops at bundled `PWGmcChanges` | `SC052` (order `52`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC051` | Palatalization of \emph{*sk} to \emph{*sc} | `51` | yes | yes | `SC046` (order `46`) | `SC056` (order `56`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC052` | Velar palatalization before front vowels | `52` | yes | yes | `SC050` (order `50`) | `SC055` (order `55`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC053` | Loss of \emph{*w} after velars | `53` | no | no | none in current test; search stops at bundled `PWGmcChanges` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | If retained as a distinct step, say openly that the local placement is mostly a residual bridge choice plus thin comparative support. |
| `SC054` | Loss of \emph{*w} before final \emph{*i} | `54` | yes | yes | `SC020` (order `20`) | `SC063` (order `63`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC055` | The composite i-umlaut rule | `55` | yes | yes | `SC052` (order `52`) | `SC056` (order `56`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC056` | West Saxon palatal diphthongization | `56` | yes | no | `SC055` (order `55`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC057` | Coalescence of velar + \emph{*j} clusters | `57` | yes | no | `SC052` (order `52`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC058` | Nasal dissimilation in short-vowel environments | `58` | no | no | none in current test; search stops at bundled `PWGmcChanges` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | Use the lexical evidence honestly and avoid implying that the literature gives a chapter-sized chronology claim. |
| `SC059` | Back mutation before labials and liquids | `59` | yes | yes | `SC048` (order `48`) | `SC078` (order `77`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC060` | West Saxon palatal umlaut before \emph{*h}-clusters | `60` | yes | no | `SC055` (order `55`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC061` | Reduction of final nasal weak-tail endings | `61` | yes | no | `SC023` (order `23`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC063` | High-vowel apocope after heavy syllables and in trisyllables | `63` | yes | yes | `SC055` (order `55`) | `SC072` (order `72`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC064` | Loss of stem-final \emph{*n} after long \emph{*ī} | `64` | yes | yes | `SC041` (order `41`) | `SC072` (order `72`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC065` | Medial syncope before dentals after heavy syllables | `65` | no | no | none in current test; search stops at bundled `PWGmcChanges` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | Explain the broader post-apocope tail setting; do not claim that the current test isolates a nearest neighbor for this rule. |
| `SC066` | L-adjacent syncope in medial syllables | `66` | yes | yes | `SC055` (order `55`) | `SC068` (order `68`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC067` | Dental assimilation in newly formed clusters | `67` | no | no | none in current test; search stops at bundled `PWGmcChanges` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | Final prose should probably treat this as cleanup inside the corridor unless stronger external chronology is found. |
| `SC068` | Preconsonantal degemination before sonorants | `68` | yes | no | `SC066` (order `66`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC069` | Early shortening of unstressed \emph{*ō} before nasals | `69` | yes | no | `SC023` (order `23`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC070` | Early fronting of unstressed \emph{*a} | `70` | yes | yes | `SC052` (order `52`) | `SC071` (order `71`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC071` | Later shortening of unstressed \emph{*ō} | `71` | yes | no | `SC070` (order `70`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC072` | Shortening of unstressed long vowels | `72` | yes | yes | `SC064` (order `64`) | `SC073` (order `73`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC073` | Merger of unstressed \emph{*æ} with \emph{*e} | `73` | yes | yes | `SC072` (order `72`) | `SC085` (order `84`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC074` | First medial unstressed-\emph{i} lowering | `74` | yes | yes | `SC072` (order `72`) | `SC075` (order `75`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC075` | Preservation of medial unstressed \emph{*i} before \emph{*ng} | `75` | yes | no | `SC074` (order `74`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC076` | Reduction of prefixal \emph{*i} in unstressed position | `76` | no | no | none in current test; search stops at bundled `PWGmcChanges` | none in current test; search reaches the current right-hand limit at `SC087` | no diagnostic constraint in either tested direction | yes — primary placement must come from linguistic and source-based reasoning | A short source-backed note is enough; the current test does not identify a nearest ordering constraint on either side. |
| `SC078` | Reduction of remaining weak-tail vowels | `77` | yes | yes | `SC070` (order `70`) | `SC086` (order `85`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC079` | Loss of \emph{*j} after heavy syllables | `78` | yes | yes | `SC055` (order `55`) | `SC080` (order `79`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC080` | Simplification of final geminates | `79` | yes | no | `SC079` (order `78`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC081` | Strengthening of \emph{*j} after front diphthongs | `80` | yes | yes | `SC055` (order `55`) | `SC082` (order `81`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC082` | Intervocalic vocalization of \emph{*j} | `81` | yes | yes | `SC081` (order `80`) | `SC083` (order `82`) | two-sided diagnostic support | no — internal test already gives a close rationale | State both directions of failure directly; extra source rationale is supportive rather than essential. |
| `SC083` | Contraction of unstressed \emph{ei} | `82` | yes | no | `SC082` (order `81`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC085` | Loss of intervocalic \emph{*h} | `84` | yes | yes | `SC073` (order `73`) | `SC086` (order `85`) | broad computational window | yes — explain why the modeled position is preferred inside a wide diagnostic range | State both diagnostic directions, but make clear that one or both constraints are broad/far rather than a tight local seam. |
| `SC086` | Contraction of the resulting hiatus | `85` | yes | no | `SC085` (order `84`) | none in current test; search reaches the current right-hand limit at `SC087` | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |
| `SC087` | Metathesis of \emph{*r} with a following short vowel | `86` | yes | no | `SC044` (order `44`) | none in current test; search reaches `-` (order `86`) | one-sided diagnostic support plus runner/search limitation on the other side | yes — explain the unconstrained side and the search limit | State the supported side directly and say the current finite-state test does not identify a nearest ordering constraint on the other side before the search limit. |

## First-priority review of rules not fixed by the current order test

### `SC012` — \emph{lþ}-voicing

1. The literature places the `lþ > ld` development in a northern-West-Germanic / West-Germanic consonant history rather than in an unqualified pan-PWGmc law.
2. The current local sources do not supply a close relative chronology argument; they mainly support the reality and scope of the change itself.
3. The evidence is comparative reconstruction and handbook phonology, not a witness-driven ordering argument.
4. CAPR places it in the same early zone, but the exact stage label is sharper than the source tradition warrants.
5. Final prose should gain one short sentence making the source-based placement explicit. Follow-up category: **Needs a small prose clarification**.

### `SC013` — Dental hardening

1. Ringe and Taylor place dental hardening in early West Germanic as a systemic change in the status of `*d`.
2. The local files do not rely on a relative chronology argument between named neighboring rules; the placement is chiefly a matter of consonant-system history.
3. The evidence is comparative reconstruction and early phonological system description.
4. CAPR places the rule in the same general area, and the current chapter already states that the test does not fix a local seam.
5. This case does not urgently need more chronology research. Follow-up category: **Needs no further chronology research**.

### `SC014` — Monophthongization of unstressed \emph{*ai}

1. The literature places unstressed `*ai` monophthongization in the broad early Northwest-Germanic reshaping of unstressed vowels.
2. The local sources do not provide a close relative chronology argument for the exact slot; they justify the change as part of the opening unstressed-vocalic prelude.
3. The evidence is comparative reconstruction plus early unstressed-vowel system history.
4. CAPR places the rule in the same general area, but the finite-state test does not identify a nearest constraint on either side.
5. A short source-based chronology sentence would help the final prose. Follow-up category: **Needs a small prose clarification**.

### `SC018` — Raising of final stressed monosyllabic \emph{*ō}

1. The literature places stressed monosyllabic `*ō`-raising in the ordinary early Northwest-Germanic / Old English long-vowel history.
2. The local sources do not give a specific neighboring sound change that fixes the rule more closely than the current position.
3. The evidence is handbook phonology and general vowel-history framing, not a diagnostic interaction with another rule.
4. CAPR places it in the same region and uses it as a contextual note before the stronger SC019-SC020 area.
5. The existing source basis is sufficient; the final prose only needs to stay candid about the lack of internal constraint. Follow-up category: **Needs a small prose clarification**.

### `SC022` — Dissimilation of \emph{mn} sequences

1. The literature places `mn` dissimilation as a descriptive pattern rather than as a strongly bounded chronological law.
2. The local sources do not give a close relative chronology argument.
3. The evidence is descriptive morphology / lexicography around `month`-type material rather than an interaction with a named neighboring change.
4. CAPR keeps the rule in the right general region, but the current slot is not strongly fixed by either the test or the handbook tradition.
5. This is one of the thinner chronology-justification cases. Follow-up category: **Needs literature check before final wording**.

### `SC025` — Rounding of long \emph{ē} before nasals

1. The literature places long-`ē` nasal rounding in the broader early Northwest-Germanic nasal-vowel region.
2. The local files do not produce a close relative chronology argument for the exact position.
3. The evidence is comparative vowel history and lexical examples such as `moon` / `month`, not a direct ordering interaction.
4. CAPR places it in the same broad area, but the precise slot is not fixed by the test.
5. This is another thin source-based chronology case. Follow-up category: **Needs literature check before final wording**.

### `SC028` — Loss of preconsonantal \emph{*x}

1. The literature places preconsonantal `x`-loss in the broad lead-in to the glide/fronting zone rather than at a sharply defined local seam.
2. The local sources do not give a close relative chronology argument for the exact slot.
3. The evidence is broad `x`-loss background and comparative derivations, not a single ordering test against a neighboring rule.
4. CAPR places it as the left preface to the SC029-SC030 core, which matches the current source-based reading well enough.
5. The final prose mainly needs to say that the test does not fix the slot closely. Follow-up category: **Needs a small prose clarification**.

### `SC053` — Loss of \emph{*w} after velars

1. The literature places the relevant `*ngw > *ng` material only thinly, mainly through comparative derivations such as `*singwan > singan`.
2. The local sources do not provide a close relative chronology argument at all; SC054 carries the positive chronology in the pair.
3. The evidence is narrow comparative reconstruction rather than a robust independent chapter tradition.
4. CAPR places SC053 in the right local stretch, but the dossiers openly describe it as residual bridge material and partly implementation-heavy.
5. This is one of the clearest cases where source-based chronology remains under-explained. Follow-up category: **Needs literature check before final wording**.

### `SC058` — Nasal dissimilation in short-vowel environments

1. The literature places the relevant nasal-dissimilation outcomes as scattered lexical facts inside broader discussions of umlaut, suffixal development, and related changes.
2. The local sources do not give a close relative chronology argument for the exact rule.
3. The evidence is lexical and comparative rather than a chapter-sized chronology claim.
4. CAPR keeps the rule explicit, but the dossiers already say the placement is modest and not fixed by the test.
5. The final prose may need one clearer sentence about that modest source basis, but deeper research is not the top priority. Follow-up category: **Needs a small prose clarification**.

### `SC065` — Medial syncope before dentals after heavy syllables

1. The literature places medial syncope in the broader post-apocope tail and late weak-vowel reduction zone.
2. The local files do not isolate a positive local boundary for SC065 itself.
3. The evidence is the broad corridor `SC063 -> post-apocope tail -> SC066-SC068 -> SC072`, with morphology and late weak-tail system history doing most of the work.
4. CAPR places SC065 in the same general zone, but the dossier says the specific rule is historically plausible more by setting than by tight direct support.
5. This is a high-priority source-justification case for final wording. Follow-up category: **Needs literature check before final wording**.

### `SC067` — Dental assimilation in newly formed clusters

1. The literature places the broader history as late syncope plus downstream cluster cleanup, not as a sharply independent `SC067` law.
2. The local sources do not give a close relative chronology argument for SC067 itself.
3. The evidence is mainly broad corridor logic plus CAPR-specific segmentation after syncope.
4. The dossiers state most explicitly that the exact three-stage segmentation is largely CAPR sharpening and that SC067 may work better as an internal bridge note than as a coequal anchor.
5. This is the clearest case for questioning the current model-level presentation if stronger historical wording is desired. Follow-up category: **Needs model/order reconsideration**.

### `SC076` — Reduction of prefixal \emph{*i} in unstressed position

1. The literature places prefix `i`-reduction in the late unstressed-vowel and prefix-vowel history of Old English.
2. The local sources do not give a close relative chronology argument for the exact slot, but they do make the development historically legible.
3. The evidence is source-backed prefix-vowel history rather than a diagnostic interaction with another named change.
4. CAPR places it in the same late weak-tail region, and the dossiers explicitly describe it as a case where source support outruns chronology.
5. The final prose mostly needs one more source-based chronology sentence. Follow-up category: **Needs a small prose clarification**.

## Prioritized follow-up

### Needs no further chronology research

1. `SC013` — the source basis is already strong and the current prose already says the test does not fix a local seam.

### Needs a small prose clarification

1. `SC012`
1. `SC014`
1. `SC018`
1. `SC028`
1. `SC058`
1. `SC076`

### Needs literature check before final wording

1. `SC022`
1. `SC025`
1. `SC053`
1. `SC065`

### Needs model/order reconsideration

1. `SC067` — the current local files already say the exact segmentation is mostly CAPR sharpening and may not deserve coequal historical weight.

## Handoff

1. **Tightly constrained by the internal order test:** the clearest local seams include `SC017`, `SC019`, `SC030`, `SC032`, `SC034`, `SC040`, `SC042`, `SC043`, `SC044`, `SC046`, `SC048`, `SC051`, `SC052`, `SC055`, `SC066`, `SC070`, `SC072`, `SC074`, `SC079`, `SC081`, `SC082`, and `SC085`.
2. **One-sided support:** many rules have one real diagnostic side and one unconstrained side, especially `SC003-SC011`, `SC015`, `SC016`, `SC021`, `SC023`, `SC024`, `SC026`, `SC027`, `SC029`, `SC031`, `SC033`, `SC035`, `SC039`, `SC049`, `SC050`, `SC056`, `SC057`, `SC060`, `SC061`, `SC068`, `SC069`, `SC071`, `SC075`, `SC080`, `SC083`, `SC086`, and `SC087`.
3. **Not fixed by the current order test:** `SC012`, `SC013`, `SC014`, `SC018`, `SC022`, `SC025`, `SC028`, `SC053`, `SC058`, `SC065`, `SC067`, and `SC076`.
4. **Most urgent source-based chronology work:** `SC022`, `SC025`, `SC053`, `SC065`, and especially `SC067`.
5. **Reader-facing chronology prose to revise next:** yes — the weakest cases should gain short source-based placement sentences, with highest priority on `SC012`, `SC014`, `SC022`, `SC025`, `SC053`, `SC065`, `SC067`, and `SC076`.

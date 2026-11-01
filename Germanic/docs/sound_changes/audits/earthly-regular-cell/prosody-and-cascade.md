# Earthly: prominence and the current cascade

Research base: `8f7713c39f26a7f81ef04d29d54070f1b83ab0e0`.
This is an experiment, not a sound-change adjudication or an adoption.
The complete inputs, definitions, orders, outputs, nonfirings and internal
operations are in the final v11 `results.json.gz`. No production definition
is changed; v11 contains 43 candidate/control inputs.

## What the sources establish

Hogg (1992, inspected in the 2011 reissue: 49–50, §2.89) explicitly includes
*-cund* among suffixes historically derived from compound constituents.
He distinguishes their historical compound stress from their later treatment
with subordinate stress when the constituent is disyllabic through formation
or inflection. This supports investigating inflected forms; it does not
directly attest either the Proto-Germanic grave or the stress of any particular
*eorþcund* token. Printed page 49 was checked against the PDF image, not just
the searchable text.

McCully and Hogg (1990: 323–333, especially 330–333) supply the earlier
research's quantity-sensitive, domain-sensitive analysis, rather than a
mechanical alternation of strong and weak syllables. The earlier dossier
records its direct reading of their final revised condition: branching heads,
or a branching foot at the left edge of the domain, distinguish *æþelingas*
from *cyningas* and *rīdende* from *wesende*. The present investigation
reuses that recorded reading. The previously hashed PDF was not found in the
available library or session artifacts; a fresh request to the publisher's
PDF endpoint returned HTML, not a PDF. No new direct reading of that
inaccessible copy is claimed. Bibliographic identity is DOI
`10.1017/S0022226700014699`, *Journal of Linguistics* 26(2), 315–339.

Goering (2023: 79–84, §§4.5.1.1–4.5.2) independently supplies the important
quantity distinction. An initial light syllable and following heavy syllable
can occupy the licensed initial foot together; they cannot simply be split
into a light primary foot and a medial secondary foot. Conversely, after an
initial heavy foot, a subsequent nonfinal heavy syllable can head a medial
foot. Final footing and final stress are separate issues. The analysis thus
supports the contrast between *eorþ.cun.des* and *we.rul.des*, without moving
the inherited-accent stripping operation. Pages 83–84 were also inspected
as a PDF image.

Goering's final-overheavy discussion is a qualification, not a blanket
instruction to stress all final closed syllables. His evidence concerns
partly stressed final *-ing* and *-end*, with limited alternatives involving
extrametricality or an extension of the trimoraic licence. This is a reason
to test a general final-overheavy sensitivity, but not independent proof
that every final *-cund* underwent exactly the same treatment.

Hogg (1996: 8–11, especially 9–10 and 11 n.7) explicitly warns that
“tertiary stress” can become an explanatory diacritic rather than an
independently represented phonological property. The present experiment
therefore computes prominence from the string and weight, not from a
*-cund* flag. His labial-nasal qualification also excludes a blanket
preservation before dental *n*: ordinary *-un* becomes *-on*. The retained
*u* of *-full* may have additional segmental support, but that discussion
does not supply a dental-nasal exemption for *-cund*.

Hogg (1992/2011: 239–241, §§6.55–6.58) distinguishes lowering from retained
phonetic [u], manuscript dialect and date, and the preserving environments
before *m*, *ng*, *k*, finally, and after stressed *u*. Early Northumbrian
retention is not authority for assigning that dialect to the Oxford gloss.
Nor can a dialectal or metrical observation automatically establish speech
stress in the target. The earlier dossier's Minkova and Zhou (2023: 86–90)
caution about deriving speech stress directly from metre remains in force.

## What `FootCtx` actually does

The live `OEStressFootContext` recognizes a pretonic syllable before a
positively marked primary-stressed root and introduces `*ᶠ`. `FootCtx(T)`
then passes that first pretonic syllable through without applying `T`, and
applies `T` to the remaining domain; without the marker it applies `T`
normally. Neither helper syllabifies the word, counts moras, constructs all
Old English feet, nor independently determines medial prominence.

The private `RFoot` is additional experimental computation. It compulsorily
marks syllable boundaries, assigns the explicitly listed maximal onsets,
accommodates an initial H or initial L plus another syllable, and marks
eligible nonfinal closed-syllable nuclei. `RLate` composes that projection
with the unchanged SC040 lowering and immediately decodes its temporary
grave symbols. These graves are technical annotations, not continued
inheritance or a second historical loss of the original compound accent.
SC038 occurs exactly once in every tested model, at its production position.

This is a projection adequate to the tested short-*u* question, not a
complete cyclic stress grammar. Its onset list is an explicit assumption;
the single-onset sensitivity gives the same relevant complete predictions.
Its marking inventory is the five short vowels *a e i o u*; it does not
claim a complete prominence representation for every Old English vowel,
long nucleus, boundary or phrase. The earlier internal syllabifier's
formal diagnostic discrepancy and the unrelated parser ambiguity for
`biu` remain disclosed in the preserved earlier dossier.

## Current SC065, SC066 and SC068

Genuine `adjudicate.py SCNNN --prepare` and
`--preflight --for investigate --json` were used for all three existing SCs.
Their current accepted conclusions, not old experimental failures, govern
the comparison.

| SC | Current operation | Effect on the serious earthly cells |
| --- | --- | --- |
| SC065 | Retained *i*-only, pre-dental heavy-syllable syncope | No firing. The genitive has no relevant medial *i*; the *-aizōz* feminine ending still has long *ē* before *r*. |
| SC066 | Reformulated *i*-only, pre-*l* weight/open-syllable syncope; short *ie* class corrected | No firing: the relevant ending contains *r*, not *l*. |
| SC068 | Retained pre-sonorant *tt/nn* degemination | No firing: none of these inputs presents the required geminate. |

The full traces confirm these nonfirings. The changed *ie* weight class
likewise does not alter the serious earthly strings. Their accepted
chronology is untouched. No new historical edge is inferred from the
experiment's insertion order.

## Complete-cell results

The following are exact experimental serializations. Whether a particular
ending's `n` is an actual consonant or a source's nasalization notation must
be settled morphologically, not inferred from the result. Those diagnostics
do not replace the source-critical reconstructions in `morphology.md`.

| Input | Current cascade | Earlier prominence | Additional sensitivity | Meaning |
| --- | --- | --- | --- | --- |
| `*érθa-kùnðas` | eorþcondes | eorþcundes | Same under every tested sensitivity | Complete genitive succeeds; the current first stem-vowel divergence is SC040. |
| `*érθa-kunðas` | eorþocundes | eorþocundes | Still fails | Without the independently assumed compound accent, the linking vowel is not removed. |
| `*érθa-kùnðasa` | Parser rejection | eorþcundes with private generic ending coverage | Same | Optional-final-*a* genitive alternative; not needed for the preferred *-as*. |
| `*érθa-kùnðes` | Parser rejection | eorþcundes with private coverage | Same | Distinct neuter genitive alternative, not a manufactured masculine ending. |
| `*érθa-kùnðaizōz` | eorþcondere | eorþcundere | eorþcundre with the private r-syncope slice | Retained *u* and the extra ending vowel are separate problems. |
| `*érθa-kùnðizōz` | eorþcyndere | eorþcyndere | Still eorþcyndere | The *i* causes umlaut; replacing *-aiz-* with *-iz-* is not an automatic solution. |
| `*érθa-kùnðōn` | eorþconde | eorþcunde | Same | A successful ending serialization; not proof that Genesis is feminine accusative or that literal final *n* is the right PGmc notation. |
| `*érθa-kùnðanōn` | Parser rejection | eorþcundene with private coverage | Still eorþcundene | The masculine accusative diagnostic retains *u* but has the wrong complete ending. |
| `*érθa-kùnðaz` | eorþcond | eorþcond | eorþcund with final-overheavy sensitivity | Success requires the extra, qualified final-prominence hypothesis. |
| `*érθa-kùnðan` | eorþcondan | eorþcundan | Same | Literal-*n* diagnostic, not documentary evidence or proof of the correct neuter reconstruction. |
| `*érθa-kùnðą` | eorþcond | eorþcond | eorþcund only with final-overheavy sensitivity | Correct strong-neuter nasalized short ending, not the Genesis weak adjective. |
| `*érθa-kùnðanǭ` | eorþcondene | eorþcundene | Same | Correct strong-masculine-accusative nasalization still leaves the extra ending vowel. |
| `*érθa-kùnðǭ` | eorþconde | eorþcunde | Same under every prominence sensitivity | Preferred weak-neuter cell: Fulk's OE-relevant bimoric nasal *-ōⁿ* is faithfully represented; no parser or ending correction is needed. |
| `*érθa-kùnðaimiz` | Parser rejection | eorþcundem with private generic ending coverage | Same | Newly recovered dative's full ending is not derived as *-um*; corresponding *godcund* gives *godcundem*. |
| `*érθa-kùnðôⁿ` | Parser rejection | Parser rejection | Same | Unsupported quantity trial prompted by a corrected misreading; not Fulk's OE-neuter reconstruction. Its raw earlier evidence is retained. |

All 109 physical stages, including rejections and unchanged stages, are
recorded for every serious cell. Four independent composed Foma finals
agree with component replay. The genitive's changed developmental skeleton
is dental hardening, linking-vowel syncope, the one inherited-accent strip,
unstressed ending fronting, breaking, merger of the ending to *e*, computed
medial prominence protecting *u* at SC040, and ordinary surface rendering.
The preferred weak-neuter chain instead shortens final nasal-long `ǭ`
to `æ` at physical step 85 and merges it to `e` at step 86, with the
same independently computed medial protection. It needs neither the
Oxford r-syncope slice nor final-overheavy prominence. Matching complete
`*gúða-kùnðǭ` gives *godcunde*, not merely an isolated suffix success.
The precise strings, rather than an anachronistic modern spelling at every
step, are in the full results and mechanically exported cell traces.

## The Oxford ending: a new result, not an adopted repair

Ringe and Taylor (2014: 264–265, §6.7.3) explicitly connect the feminine
genitive/dative and genitive-plural endings to ordinary loss of the
unstressed medial vowel. Their discussion of rare unsyncopated *-e-*
identifies epenthesis or errors, not a compulsory paradigm with *-ere*.
Campbell (1959: 159–160, §§388, 392) separately supplies medial vowel
loss before liquids and later loss following the reduction of half-stress.

At the current SC065 site, however, the *-aizōz* experiment is still
`*-kundērǣ`. Its later shortening produces `*-kundere`, after SC065 and
SC066. The private `RRSlice` tests a headed-vowel-plus-consonants,
short-*e/æ*, pre-*r* open-syllable slice immediately after that shortening.
It produces *eorþcundre* and *godcundre* without a case, suffix or lexical
condition. Genuine negatives retain the vowel when the tested preceding
flank is light, when no following vowel exists, and when the target is
still long. Its scope is an experimental slice, not a full syllabification-
aware implementation of all the handbooks' syncope.

This result overturns “the extra vowel is computationally insoluble”,
not “the morphology and chronology have been settled”. It requires
separate source-critical treatment of the pronominal ending's history,
early remodelling versus shortening, and the legitimacy of this late
phonological slice. None of SC065/066/068 is changed. Successful spelling
alone is not a reason to promote it, nor is this an independently proved
chronology edge.

## Controls and protected populations

The ordinary projection protects medial *u* in direct *godcundne* and
*godcundre* controls, but not final *u* in uninflected *godcund*. The
complete old masculine-accusative diagnostic gives *godcundene*, while the
feminine-genitive diagnostic gives *godcundere* until the r-syncope
sensitivity. These are honest ending failures, not a demonstration that
the genitive's medial *u* requires a suffix-specific exception.

The final-overheavy sensitivity additionally predicts uninflected
*godcund* and *eorþcund* and protects the relevant *-full* control. It
does not give an independent second head to the initial-LH *cyning* or
*world* controls. The ordinary and expanded prominence operations and
the composed r-syncope slice all pass formal forward-functionality tests.
No claim of inverse uniqueness is made.

Every model accepts all 390 selected inputs and keeps 382 correct outputs
and the same eight mismatches. All 380 immutable original inputs remain
accepted and deterministic; on those original, unmigrated inputs the
current cascade matches 366 historical targets, with 14 mismatches.
That is a different population from the active 380 selected inputs, not
14 new failures or grounds to rewrite the archive. Both populations have zero final-output
deltas and zero deltas at every aligned physical stage, not just the end.
The internal annotation/lowering/decoding subtraces are also preserved.
Ordinary prominence adds no annotations on the selected corpus at SC040.
The final-overheavy sensitivity temporarily annotates harvest 2057,
lung 2114, shilling 2181 and thousand 2252, then decodes them; it does not
change their vowels or any selected prediction.

The selected evaluator, lexical and active-380 fingerprints remain
`35bbd32d…`, `0e938fac…` and `9fb5d393…`. The raw immutable table remains
byte-identical, SHA256 `d2120039…`; its historical projection
`fae65652…` is separate from that raw file checksum. Full hashes are recorded.
World, rainbow and soul are unchanged at every aligned checkpoint.
Production sources, canonical bins and build manifest were hashed before
and after the private execution and remained identical.

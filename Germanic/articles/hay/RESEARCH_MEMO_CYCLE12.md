# Research memorandum: the direct singular, its stem and its spelling

## Identity, question and scope

Cycle 12, `research/hay-article`, base `45e8e951`. Can the
early-apocope direct stem account for the earliest Anglian forms
without requiring protected-stem transfer? A securely established
incompatible nucleus or an independently dated, incompatible
outcome of final /e.i/ would weigh against regular survival.

Article-only comparison. The SC047 verdict, historical scope,
source, firing census and benchmark populations are unchanged.
Read the Germanic adjudication protocol/template, current state and
SC047 registry entry. The witnesses here are the inherited direct
input, protected-cell controls, and a requested comparison of two
already frozen orders; no new chronology edge is inferred from rule
identifiers, successful derivations or executable ordering alone.

## New checks: frozen traces and historical source

Extracted from Git object
`113101ac5f169b589e1a9647cdf24d32cdd4d919:Germanic/docs/models/sc047/captures/sc047-adoption-v1.json.gz`
(compressed SHA-256 `1355d125eb55f43f32fdb77c58cfa704825edca70847662a2c820b894212fc26`).
Use `.models.A` and `.models.B2`, the `corpus` row with
`row_id == "2061"`, and `diagnostic_trace`, not `canonical_trace`
(its late loss occurs at a different point). The five `paradigms`
entries with `lexeme == "hay"` supply two direct and three protected
controls. The `order` arrays establish where a non-firing stage
belongs. The core orders (one-based) are A: apocope 21, vocalization
22, gemination 23; B2: gemination 21, apocope 22, vocalization 23.
All protected traces are identical across the two models.

| Changed stage | A | B2 |
|---|---|---|
| Input expansion | `*x*á*w*j*ą` | `*x*á*w*j*ą` |
| Gemination before loss | — | `*x*á*w*w*j*ą` |
| Nasal apocope | `*x*á*w*j` | `*x*á*w*w*j` |
| Stranded-glide vocalization | `*x*á*w*i` | — |
| Gemination after loss | — | already applied |
| Resolution of geminated labial and palatal | — | `*x*áu*j` |
| Diphthong fronting and development | — | `*x*áeu*j`, then `*x*ēa*j` |
| Short *a* fronting | `*x*æ*w*i` | — |
| Initial fricative palatalization | `*ç*æ*w*i` | `*ç*ēa*j` |
| i-Umlaut | `*ç*e*w*i` | `*ç*īe*j` |
| Loss of *w* before unstressed *i* | `*ç*e*i` | — |
| Orthography, then removal of segment markers | `h*e*i`, `hei` | `h*īeġ`, `hīeġ` |

Normalization: write conventional Germanic initial `h` throughout,
while recording the model's `x > ç` separately; remove token separators
and stress marks; transcribe `áeu` as schematic fronted `aeu` without
claiming a phonetic triphthong. Display `hei` as `*he.i` where
syllabification matters (short stressed /e/ and syllabic unstressed
/i/); late `*īe` is long and final `ġ` stands for consonantal /j/.
The genitive *hawjas*, dative *hawjai* (early *-ē*) and direct plural
*hawjō* (early *-u*) retain a vowel after *j* at gemination and
yield *hīeġes*, *hīeġe*, *hīeġ* respectively. The genitive and
dative have an additional intervocalic palatal-strengthening stage;
don't put it in the direct singular. The model entry and source
ledger distinguish these predictions from selected attested targets.

Ringe & Taylor original PDF: printed pp. 53, 173, 246 on sheets
68, 188, 261 (printed page +15). P. 53 motivates reversal of
labial gemination before *j* (the distinction was not merged),
and p. 173 identifies OHG *hewi* as inherited direct and *houwi*
as reflecting oblique levelling. P. 246 supplies the English
substitution explicitly: direct *hawi > *hæwi*, protected
*[hawʲwʲ-] > *hauj- > *hēaj-*; then direct *hēaj* from that
protected stem, **before** mutation of *ēa*. West Saxon *hīeġ*,
Mercian and Northumbrian *hēġ* follow. The notation aligns the two
stem lines; it neither names a particular donor nor asserts that
*he.i* was the authors' final regular prediction. Hogg & Fulk
§2.23 compare early masculine oral loss *-az* with retention of
nasal *-ą* through gemination; that contrast grounds the later
order, not every detail of the labial sequence in the frozen model.

## New checks: bounded spelling search and ‘glee’

Checked the local catalogue and holdings before online lookup.
Literal ⟨hei⟩ in the `spelling` column of the 127-row morphological
inventory gives W01 only, the Worcester gloss. Cross-checked the
DOE handoff/crosswalk, principal concordance, Cooper's fourteen
document comparison, Bryan's Kentish spellings, and the local
Langlands, Wager and Wallenberg (1928) extracts for *hei/heiweg*.
The *híg/hég* and *hēah-weg* dictionary entries and Wright–Wülcker
glossary loci give no additional early exact spelling. Do not count
*heig*, other meanings of *hei*, an editorial spelling, or
the disputed *Hegforde* as exact matches. The source set was
bounded by the existing dossiers; it was not a new DOE query or
an exhaustive search for compounds. The MED public index confirms
the Worcester example (c.1225, s.v. *hei*, MED20239) and later
variants; the full entry returned HTTP 403. Worcester remains the
earliest secure simplex exact match in the checked material.
No new charter reading or manuscript collation is claimed.

Campbell §§120.2, 411, 579(4) treats *glīg/glīges* as a re-formation
beside *glīw/glīow*, made possible by existing *ī(g) : īw/īow*
alternations. This is not a report of a directly observed
*glī > glīg* or of copying *g* from the *w*-bearing genitive.
Brunner's printed p. 114 §130 n. 3 (sheet 126), read with §§173,
247 n. 1, retains *j* while the singleton *w* joins preceding
*i* to form *iu*, then umlaut gives *ie/ī*. A following ending
can allow gemination and preservation of *w*; *glīwes/glīowes*
have that shape, and *glēo* and related compounds exemplify
the competing vocalism. Brunner expressly allows secondary
extension in his discussion of *j*-forms. His mechanism is worth
testing at the level of inherited structure, but it does not
recover *j* after it has already become syllabic *i* in *hawi*.

## Reinterpretations and verdict for the article

- The charter edition yields an exact, early written counterpart
  to *hei* on the preferred ‘hay-road’ reading. This is a result
  independent of identifying the age, grammar or phonetics of
  the composition form. *Dei* supplies a route to spelling an
  existing glide; the long mid vowel of the protected analysis
  is not barred in Kentish (compare *ċēgan*, Ringe & Taylor p.
  246). This establishes a competing explanation, not a local
  long-vowel ⟨ei⟩ control.
- Hogg's *clēa*, Vespasian *sīem* and the *strēidæ/strēide*
  evidence have separate, complementary roles: the mechanism
  of losing syllabicity, the feasibility of front-vowel hiatus,
  and its persistence after *w*-loss. Together with ordinary
  ⟨g⟩ notation they support a historically motivated /ej/
  hypothesis without specifying a dated final front-vowel law.
  The independently attested contraction is more specific in
  vowel order but not in position; it also removes the potential
  source of the glide.
- Farman remains positive local evidence for length. No new
  quantitative calibration or experimental rule was run or
  warranted. The census remains 123 included/66 verified.
  Its inflected datives show an oblique function with an overt
  ending, not the age or direction of an earlier stem transfer.
- Under early loss, a regular hypothesis for Anglian is viable;
  no minimum analogy greater than zero is established by its
  earliest spellings. If contraction and a final /j/ are assumed,
  a consonantal repair suffices. West Saxon high vocalism
  requires a different account and gives positive evidence for
  the protected nucleus within the tested alternatives. This
  is not a new verdict for SC047, a new exception to a sound
  law, or a claim that the first member of *heiweg* was the
  inherited Kentish nominative–accusative singular.

Further evidence that could change the analysis: a dated
same-environment /e.i/ control; independently established quantity
in the earliest Anglian forms; a pre-levelling donor or direct
contrast; independent local spelling controls for long /eːj/,
or new evidence for the lexical identity of *heiweg*. The pending
Dal (1934), Wallenberg (1931) and Brooks & Kelly (2013) acquisitions
remain with the owner and were not searched for.

## Bidirectional publication audit

Read Sections 1.1–1.3 back against C01–03 (chronology, trace
normalization, and the verified substitution); Sections 2.1–2.3
against C04–07 (orthography and actual witness status); Sections
3.1–3.3 against C01, C06–07 (hiatus, desyllabification and quantity);
and Sections 4.1–4.4 against C02, C05, C08–09 (attested versus
predicted morphology and the scope of the comparanda). Sections 5–7
carry the conclusions from H1–H5 and C09 without making regular
survival a necessary premise or treating a reconstructed donor as
an observed transfer. In the reverse direction, all nine component
arguments have an explicit published locus: C01–03 in Section 1,
C04–05 in Sections 2.2–2.3 and 4.3, C06–07 in Section 3, C08 in
Section 4, and C09 in Sections 5–7. Appendix A retains the witness
checks and their limits. The formal prediction is spelled *hei* but
not treated as /hej/; the article uses *heiweg* as an orthographic
comparison rather than a grammatical counterexample.

The 16-page PDF was read in full as a standalone proof. All seven
tables fit, the three charter notes are individually complete on
page 4, and the appendix and bibliography are legible. Checks of the
source, generated TeX and PDF text confirmed greater-than notation,
italicized reconstructed forms, all three prose footnote anchors,
no unresolved references, and no internal file references in print.
The two frozen direct traces, shared protected traces, unchanged
census and 26 registered PDF/text hashes were checked independently.
No scientific input to the production book or runtime was changed;
the validation is a frozen-receipt and standalone publication
check, not a new production runtime certification.

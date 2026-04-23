# Skill: Be Lautgesetzlich

**Invocation:** "be Lautgesetzlich", "Lautgesetzlich check", or as a
reminder whenever designing a fix to a mismatch.

This pipeline models the regular sound-law development of PGmc → OE.
When we face a word that "doesn't come out right", the discipline is
to explain the attested OE form through **regular sound change** from
a **reconstructable proto-form**, not through ad-hoc rule tweaks or
morphology-hiding hacks. These are the habits that keep us honest.

## 1. Think hard about chronology

Almost every rule-bug in this pipeline is a chronology bug in disguise.
Before changing a rule body:

- Trace the failing word stage by stage with
  `python3 Germanic/tools/oe_full_trace_report.py`. (If the trace is
  stale or diverges from the main pipeline, fix that first — see
  `skills/sync-trace-report.md`.)
- Ask: at the stage this rule fires, what shape does the failing word
  have? What shape do *similar* words have that we *don't* want it to
  apply to?
- Ask: does the rule's ordering relative to apocope / vowel reduction /
  fronting correspond to what R/T, Campbell, Luick etc. say about the
  **relative chronology** of these changes? Relative chronology is the
  single most-cited structuring device in the Germanic literature;
  respect it.
- A rule body that does the wrong thing in the right stage is easier to
  fix than a correctly-written rule in the wrong stage. Check
  chronology before re-writing bodies.
- Document in DEV_NOTES the stage sequence you're assuming, with
  citations.

## 2. Check our local resources, exhaustively

The answer is almost always already in one of our sources. Do not
speculate until you have searched them. `docs/references/` holds a
large corpus; consult **at least the following** on any non-trivial
change:

### Grammars and handbooks (OE / NWGmc / PGmc)

- **Ringe & Taylor**, *Linguistic History of English* vol. 2 (NWGmc →
  OE): `ringe_taylor_linguistic_history_vol2.txt`
- **Ringe**, vol. 1 (PIE → PGmc): `ringe_vol1_pie_to_pgmc.txt`
- **Campbell**, *Old English Grammar*:
  `campbell_old_english_grammar.txt`
- **Hogg**, *Grammar of Old English* vol. 1: `hogg_vol1.txt`
- **Fulk**, *Comparative Grammar of the Early Germanic Languages*:
  `fulk_comparative_grammar_early_germanic.txt`
- **Luick**, *Historische Grammatik der englischen Sprache*:
  `luick_historische_grammatik.txt`
- **Brunner**, *Altenglische Grammatik* (1965):
  `brunner_1965_altenglische_grammatik.txt`
- **Bülbring**, *Altenglisches Elementarbuch*:
  `bulbring_altenglisches_elementarbuch.txt`
- **Kaluza**, *Historische Grammatik der englischen Sprache*:
  `kaluza_historische_grammatik_englisch.txt`
- **Streitberg**, *Urgermanische Grammatik*:
  `streitberg_urgermanische_grammatik.txt`
- **Noreen**, *Altisländische Grammatik* (cognate dialect):
  `noreen_altislaendisch.txt`

### Etymological dictionaries

- **Kroonen**, *Etymological Dictionary of Proto-Germanic*:
  `etymological_dictionary_of_proto_germanic_kroonen.txt`
- **Orel**, *Handbook of Germanic Etymology*:
  `orel_handbook_germanic_etymology.txt`
- **Seebold**, *Vergleichendes Wörterbuch der germanischen starken
  Verben*: `seebold_vergleichendes_woerterbuch.txt`
- **Kluge–Seebold**, *Etymologisches Wörterbuch der deutschen Sprache*:
  `kluge_seebold_etymologisches_woerterbuch.txt`
- **Lloyd/Springer**, *Etymologisches Wörterbuch des Althochdeutschen*
  (EWA) Band 1: `ewa_band1_lloyd_springer.txt`

### Specialist articles (consult when their topic is in play)

Stiles (on the four-part PWGmc series and a-umlaut of *u*), Howell &
Salmons (lowering of *i*), Cercignani (PGmc *i/*e, early umlaut),
Adamczyk (Sievers in OE), Pierce (Sievers / prosody), Kroonen (n-stems,
m/n stems), Bammesberger (herfest), Hamp (PIE bottom), van Helten
(numerals), Polomé, Lloyd (*a*-umlaut of *i*), Lühr, Vine, and the
Oxford chapter. Check `docs/references/` for the relevant `.txt` or
`.pdf` file.

### Readers / lexica (for attestations)

Sweet's primer, Bright's reader, Hall's concise dictionary, the Toller
Anglo-Saxon dictionary, Wright's primer. Use these to verify an OE
form is actually attested in the dialect/text you think it is — and
which cells of the paradigm survive.

### Search discipline

- Grep with several synonyms before concluding a change is not
  discussed (e.g. "tautosyll", "heterosyll", "coda nasal", "intervocalic
  nasal", "unstressed *a*", "nasali[sz]ed"; or in German sources,
  "Silbenende", "Silbengrenze", "in der Fuge", "tautosyllabisch",
  "Nasalvokal").
- Read the surrounding §§ in their entirety — these authors qualify
  their claims heavily in adjacent paragraphs.
- Record page numbers / section numbers in DEV_NOTES.
- When a source is in German, quote the German with a close English
  paraphrase; do not paraphrase silently.

### Opinio communis takes priority

If R/T, Campbell, Luick, and a modern handbook agree, that is what we
model. If they disagree, cite all, state which one we follow, and why.
Prefer the account that is:
- most phonologically explicit (rules, conditioning environments),
- most chronologically explicit (relative ordering),
- and most widely endorsed by later literature.

If no source addresses the change, say so in DEV_NOTES. Invent nothing.

## 3. Favour phonological solutions over analogical ones — until the
field itself says the form is analogical

Preference order when an OE form doesn't fall out cleanly:

1. **Wrong rule chronology** — re-order rules so the composition runs
   in the order the literature attests.
2. **Wrong rule conditioning** — tighten or loosen the rule's context
   to match the authors' conditioning (tautosyllabic vs heterosyllabic,
   stressed vs unstressed, before vowel vs before consonant, light vs
   heavy stem, etc.).
3. **Missing rule** — add a rule the authors describe but which we
   never implemented (e.g. secondary nasalisation, inter-stress
   raising, specific apocope sub-cases).
4. **Paradigm-cell PROTOFORM substitution** — **only once steps 1–3
   are exhausted, or once a source explicitly says the attested form
   is analogical / transferred / levelled.** See §4 below.

Don't rig phonology to produce an analogical outcome. If Campbell
§334 says `-en` in strong past participles is transferred from oblique
cells, we do not design a phonological rule to nasalise participles
into producing `-en`; we encode the oblique cell. Phonology that
produces an analogical form is worse than honest analogy, because it
misleads future debugging and tends to break adjacent forms.

## 4. Changing the PROTOFORM: paradigm-cell substitution

Sometimes the nom.sg. (or dictionary headword) is the output of
levelling, not sound change, and no regular derivation from the
reconstructable proto yields the attested form. In that case, change
the TSV PROTOFORM to a different paradigm cell in which:

- the attested OE form *is* the regular sound-law outcome,
- and the chosen cell is historically attested or reconstructable for
  that stem class in the relevant handbook.

### Established precedents in this repo

| Row | Lemma | Old PROTOFORM | New PROTOFORM | Cell | Note |
|-----|-------|---------------|---------------|------|------|
| 2119 | mann | `*mannăz` | `*mannas` | gen.sg. | avoids final-geminate simplification by keeping *nn medial |
| 1936 | bann | `*banną` | `*bannas` | gen.sg. | same mechanism |
| 2140 | span | `*spannō` | `*spannăi` | dat.sg. | uses unstressed *ai monophthongisation instead of ō-apocope |
| 2152 | ræste | `*rastiz` | `*rastōz` | gen.sg. | oblique cell with long *ō triggering right vowel |
| — | cow, fire | various | dat./loc. oblique | oblique | i-umlaut trigger present in oblique only |

### Conventions for paradigm-cell TSV rows

1. **Cite the cell explicitly in the commit message or note column.**
   "acc.sg.m.", "gen.sg.", "dat.sg.f." — never "paradigm form" without
   specifying.
2. **Write the cell-appropriate ending using the symbols already in
   the FST sigma.** If the cell's ending requires a new symbol, stop
   and justify adding it in DEV_NOTES before editing the TSV.
3. **Pick the cell that minimises downstream rule changes.** If two
   cells both yield the attested OE form by sound law, prefer the one
   that reuses existing apocope / reduction pathways over the one
   that requires a new rule branch.
4. **Cite the author whose account licenses the substitution.** A
   paradigm-cell change without textual support — ideally Campbell,
   Luick, R/T or Brunner saying "this form is analogical / levelled /
   transferred" — is indistinguishable from an ad-hoc fudge.
5. **Record the substitution in DEV_NOTES** under the per-word or
   per-case section, including which author says the nom.sg. is
   analogical and which cell preserves the regular outcome.

## 5. Don't carry two symbols for one sound

`*a` and `*ă` both stand for "unstressed short *a*". Using their
distinction to encode phonological information (e.g. whether a
following vowel survives long enough to keep a nasal in onset) is a
load-bearing hack; it will silently break the moment someone does a
principled normalisation.

If a rule needs to distinguish two phonological environments, condition
it on genuine phonological material — a segment, a boundary, or the
output of an earlier independently-motivated rule — not on notational
redundancy.

Exception: if the two symbols really do represent two historically
distinct segments (e.g. nasalised vs plain, long vs short, stressed
vs unstressed in a *prosodically distinctive* sense), they are
legitimate. But then the pipeline must make sure both symbols are
introduced by real rules, not just sprinkled in the TSV.

## 6. Red flags that you're leaving the Lautgesetzlich path

If you notice yourself doing any of these, stop and re-read sources:

- Writing a rule whose context is a specific morphological ending
  disguised as phonology (e.g. "applies before word-final *ą*" when
  what you really mean is "applies in the infinitive").
- Adding a TSV breve or acute that you can't match to a specific
  prosodic / morphological distinction attested in the sources.
- Finding yourself unable to explain a rule's conditioning to someone
  else without appealing to "it works for the mismatch count".
- Getting a regression on a form you *know* from R/T or Campbell
  should work, and suppressing it with an exception rather than
  re-examining the change.
- Inventing a proto-form that does not match either Kroonen, Orel,
  Seebold, or R/T.

## 7. Always commit DEV_NOTES first

When the reasoning is ready, commit DEV_NOTES **before** the rule or
TSV change. The notes are the thing we can re-read; the rules are the
thing we can re-derive from the notes. The commit history of DEV_NOTES
is this pipeline's intellectual audit trail — it is the artefact that
lets the next contributor (and your future self) understand *why* a
rule is written the way it is, and distinguish principled choices
from accumulated cruft.

— end of skill —

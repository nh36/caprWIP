### Lexeme report

#### Reconstruction and early-stage alternatives

This entry concerns row 2183 **shoulder / sċuldrum**, where the current project values are `PROTO = *skuldrō`, `PROTOFORM = *skúldramiz`, `COUNTERPART = sċuldrum`, and `DERIVATION_CLASS = late_analogy`. The first point to keep clear is that `PROTO` here functions as the project's cognate-set headword, not as the exact form fed into the Old English cascade. The comparative literature is not uniform: Kroonen reconstructs `*skuldra-` as a masculine a-stem, Orel gives `*skuldr(j)ō` as a feminine ō-/jō-stem, and Ringe and Taylor cite PWGmc `*skuldru` for the Old English branch [@Kroonen2013, p. 478; @Orel2003, p. 345; @RingeTaylor2014, p. 142]. The project therefore keeps `*skuldrō` as a lexeme-level label while treating the row itself as a paradigm-cell entry.

The row-specific input is `*skúldramiz`, not the earlier citation-form input `*skúldrō` and not the later-stage probe forms `*skúldrumiz` or `*skúldrum`. In the current analysis, `*skúldramiz` is a PGmc-proper datative/instrumental plural form with thematic `*-a-` plus `*-amiz`, chosen before NWGmc `a > u / _m`. That choice lets the report distinguish three different things cleanly: the lexeme-set proto label, the specific form used as FST input, and the attested Old English target. It also matches the usual derivation of OE nominal dative plural `-um` from the older instrumental/dative plural branch `*-omis / *-amiz` [@RingeTaylor2014, §6.8.1; @Campbell1959, §331.6; @Fulk2018, §5.5].

#### Chronological source dossier

The lexical record begins with the Old English dictionaries. Bosworth-Toller and Clark Hall both treat **sculdor** as the main Old English lemma, while Bosworth-Toller also preserves plural and oblique forms such as `sculdru`, `sculdra`, and `sculdrum` [@BosworthToller1898; @ClarkHall1960]. Toller's Supplement then adds a weak feminine **sculdra, an**, which explains why `sċuldra` entered the project's earlier row history even though it is not the safest inherited target for the present model [@BosworthToller1898].

The comparative dictionaries disagree about the earlier Germanic stem class, but they agree that the lexeme has a complicated morphological history across West Germanic. Kroonen's masculine `*skuldra-`, Orel's feminine `*skuldr(j)ō`, and Ringe and Taylor's PWGmc `*skuldru` are not interchangeable notations; they represent genuinely different views of which stage and stem class best explains the daughter forms [@Kroonen2013, p. 478; @Orel2003, p. 345; @RingeTaylor2014, p. 142].

The project's own shoulder work then moved through three stages. First, the older row tried to derive the weak-feminine `sċuldra` from `*skúldrō` and failed. Second, the shoulder dossiers treated `*skúldru -> sċuldor` as a serious plural-to-singular alternative. Third, the later paradigm survey and the current §17.41 material concluded that the attested dative plural `sċuldrum` is the only cell-consistent Old English form that the current cascade can reach lautgesetzlich. That third stage is the basis of the live row and of this draft.

#### Old English philology

The ordinary Old English headword is **sculdor**. Bosworth-Toller gives a strong masculine paradigm with forms including `sculdre`, `sculdru`, `sculdra`, and `sculdrum`, and Clark Hall likewise lemmatises `sculdor` as the main dictionary form [@BosworthToller1898; @ClarkHall1960]. The target used here, `sċuldrum`, is therefore not a reconstruction but an attested dative plural.

The form `sċuldra` is also real, but it belongs to a different part of the lexeme's history. In the current project reading it is a later weak-feminine doublet rather than the inherited form that the cascade should try to derive directly. Likewise, Brunner's late-West-Saxon `sceoldor` and i-mutated `scyldrum` show that secondary spellings and secondary analogical forms exist, but they do not displace conservative `sculdor / sculdrum` as the best base evidence for the inherited pathway [@SieversBrunner1965, §92.2.a].

For that reason, this report intentionally treats row 2183 as an **inflected-cell** entry rather than as a lemma entry. The lexeme's main citation form remains `sculdor`, but the row's chosen Old English target is the attested dative plural `sċuldrum`, because that is the paradigm cell where the inherited phonology and the attested evidence coincide most cleanly.

#### Project problem and solution

The project problem was not just that the older target had the wrong ending. A direct singular-oriented run from `*skúldrō` produced `sċoldor`, and the same root-vowel problem affected the other obvious singular cells. The former target `sċuldra` was worse still, because it represented a later analogical weak-feminine form rather than the conservative inherited outcome the row was supposed to model. The row therefore remains `late_analogy`: its special handling is driven by the lexeme's analogically disturbed singular history, even though the selected escape-hatch cell is itself regular.

The current solution is to use the masculine a-stem dative/instrumental plural cell `*skúldramiz`. This is the one cell in the surveyed paradigm where the relevant vowel conditioning works in the row's favor. Campbell states that unstressed `u` is "always well preserved" before `m`, especially in dative plural `-um` [@Campbell1959, §373]. Hogg and Brunner give the same conditioning in slightly different terms [@Hogg1992, §3.3.1.3; @SieversBrunner1965, §44 Anm. 7]. On that basis the project treats `*skúldramiz` as a defensible PGmc input: it passes through NWGmc `a > u / _m`, early loss of third-syllable `*i`, final `*z` deletion, and OE palatalization to yield `sċuldrum`.

This choice does not claim that the lemma `sculdor` itself is a direct reflex of `*skúldramiz`. Rather, the report treats `*skúldramiz -> sċuldrum` as the one attested paradigm-cell pairing that is both philologically defensible and computationally regular inside the current cascade. The superseded `*skúldru -> sċuldor` route remains worth remembering as a serious alternative considered by the project, but it crosses from a historically plural shape to a singular target and is therefore not the live row analysis.

#### Paradigm probe

The substantive probe work for this row already exists in the shoulder paradigm survey, even though there is not yet a reusable `oe_paradigm_probe.py` specification for shoulder. The current state of that probe can therefore be summarized quite directly.

First, the surveyed singular cells fail in the same way: forms such as `*skúldraz`, `*skúldrą`, `*skúldras`, and `*skúldrai` lower root `u` and produce `sċold-` outcomes, so they do not match the attested Old English forms of the same cells. Second, the post-shortening plural comparison form `*skúldru` yields `sċuldor`. That is a genuine and philologically serious alternative for explaining the singular lemma, but it is not cell-consistent with the present row.

Third, the dative/instrumental plural cell `*skúldramiz` is the winning form. It is the only surveyed input that both preserves root `u` and lands on an attested Old English target, namely `sċuldrum`. The current report therefore relies on an already completed conceptual paradigm probe rather than on a newly run automated one.

If this draft is later promoted, the reusable probe should still be formalized. At minimum it should include the singular control `*skúldraz`, the serious superseded alternative `*skúldru`, the winning dative plural `*skúldramiz`, and the analogical weak-feminine `sċuldra` as a non-winning control.

#### Drafting notes for model-entry review

- This draft deliberately treats 2183 as an **inflected-cell report**, not as a lemma report. That is probably the right model for other paradigm-cell `late_analogy` entries, but it is the first place where the distinction is stated this explicitly.
- The superseded `*skúldru -> sċuldor` path is kept in the prose because it was a serious project option, not because it remains the live solution. Review should decide whether this amount of superseded-history detail is the right norm for future model entries.
- No new automated paradigm-probe artifact was generated in this pass. If Nathan approves the prose model, the reusable shoulder probe can be added later as a separate tooling task rather than folded into the report itself.

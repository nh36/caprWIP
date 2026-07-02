# Introduction

## Sound laws as explicit derivations

This book is about a familiar historical-linguistic practice made explicit enough that it can be checked mechanically. Historical linguists have long described the history of languages through ordered sound laws, inherited morphological forms, lexical comparison, and exceptions that turn out to require other explanations [@OsthoffBrugmann1881]. A form is accepted as inherited when its phonological shape follows from the reconstruction and the relevant history of the branch. A form becomes suspicious when the expected development fails. The method is old; the difficulty is that its moving parts are numerous. Once a project contains hundreds of lexical items and dozens of ordered changes, even a careful scholar can lose track of what follows from what.

CAPR, computer-assisted phonological reconstruction, is one way to make this situation tractable. It supplements the comparative method by forcing a proposed historical phonology to take the form of explicit rules that can be applied to concrete reconstructed inputs. A rule either produces the expected output in a particular word or misses it. A rule can be moved earlier or later in an ordered sequence, and the lexical consequences of that movement can be inspected. A proposed input form can be compared with the Old English target it is meant to explain. When the formal system fails, the failure often becomes the most useful part of the inquiry, because it tells us where the regular history ends and where analogy, lexical replacement, borrowing, dialect mixture, uncertain attestation, or a mistaken reconstruction must be considered.

The present book applies that idea to the development from Proto-Germanic and early West Germanic forms into Old English. The empirical object is modest enough to be inspected and large enough to be useful. The implemented Germanic pipeline currently derives the overwhelming majority of the Old English comparison forms in its dataset. Its remaining failures are documented exceptions, so the present write-up explains a stabilized system and leaves further phonological patching aside. It asks which sound changes are being modeled, why they stand in the order they do, which lexical items support those choices, and which words require lexical or morphological explanation beyond the regular cascade.

The book has three parts. This introduction explains the method, the empirical scope, and the conventions used in the following sections. The first main part presents the sound-change sequence itself. It gives the historical discussion, the formal rule, and the chronological evidence for the modeled changes. The second main part turns from the rules to the words. It follows individual lexical items, especially those whose derivation is philologically or morphologically informative, and asks what must be true of the reconstruction, paradigm cell, attestation, or analogical history if the Old English form is to be understood.

The two main parts answer different questions. The sound-change part asks how a coherent chronological system is built. The lexical part asks how that system accounts for individual words. A reader should be able to move in both directions. When a rule chapter says that a particular ordering is supported by *learn*, *field*, *soul*, or *shoulder*, the lexical entries show what those words require. When a lexical entry says that a form is regular, analogical, a reconstructed Old English target, or a known unmodeled exception, the sound-change chapters show what the regular expectation would have been.

## What CAPR formalizes

The central claim behind CAPR is deliberately simple. A regular sound change can be treated as a relation between strings. A reconstructed form is given as an input string. An ordered sequence of sound changes maps that input to an output string. If the output matches the relevant Old English form, the derivation is successful at that level. If it fails, the failure has to be explained.

The string relation is literal. The formal background for treating phonological rules as finite-state relations is the regular-model approach to phonological rule systems developed by Kaplan and Kay [@KaplanKay1994]. In the implementation, a sound change is written as a finite-state transducer. A rule has a target, an output, and a conditioning environment. A series of rules is composed into a larger transducer. The resulting cascade represents a historical phonology. The details of the syntax matter for implementation, but the linguistic idea is the ordinary one. The formal rule is a way of making explicit what a historical grammar already says in prose.

A simple toy rule looks like this.

```foma
define ToyFinalZLoss [{*z} -> 0 || _ .#.];
```

This toy rule is only a compact illustration of the form of an explicit sound law. It says that starred \emph{*z} is deleted before the end of a word. It has a target, an output, and an environment. Real rules, written in the Foma finite-state toolkit, are often more complex [@Hulden2009]. They may refer to classes of vowels or consonants, stress, syllable weight, word boundaries, or previously defined transducers. The important point is that the prose statement and the formal statement remain accountable to one another.

A CAPR history has two kinds of structure. First, there is a phonological inventory and phonotactic definition for possible ancestral forms. The system must know what counts as a possible input. Without that restriction, backward reconstruction produces many formally possible but linguistically absurd ancestors. Second, there is an ordered list of changes. The order matters because many sound changes feed or bleed one another. If an early change creates the environment for a later change, the order is feeding. If an early change removes the environment for a later change, the order is bleeding. Both relations are central to historical explanation.

The original CAPR work was designed for Burmish and made this point through a web interface that combined cognate assignment, forward projection, backward projection, and visual marking of forms that had become regular or irregular after a change to the transducers. The same methodological lesson carries over to Germanic. A formal system is useful because it makes the consequences of a proposal immediate. A new rule can make a formerly irregular item regular. It can also break a word that used to work. Both outcomes are evidence. The researcher still decides what the evidence means.

For Old English, the input side of the problem differs from the situation in a young or poorly documented language family. The comparative and philological literature is deep. The grammar of Old English has been described repeatedly, and the earlier Germanic stages have been reconstructed with great sophistication by many scholars [@Campbell1959; @Hogg1992; @RingeTaylor2014; @Fulk2018]. That makes the formal implementation more demanding. The model must respect well-known handbooks and etymological dictionaries, and it must also explain its own deviations from citation forms when a particular paradigm cell is needed to reach the attested Old English comparison form [@Orel2003; @Kroonen2013].

## Scope of this book

This book gives a formal account of a particular historical path from Proto-Germanic and early West Germanic forms into Old English. The historical grammar comes from philology, comparative grammar, and the long tradition of work on Germanic and Old English [@Campbell1959; @Hogg1992; @RingeTaylor2014; @Fulk2018]. CAPR contributes a way of testing whether a large set of such claims can be made to cohere.

The lexical entries are selective accounts of the words that matter for the formal and historical argument. They do not attempt to give a full history of every English word, every Germanic cognate set, or every semantic development. Some entries are short because the derivation is ordinary. Some are longer because the comparison depends on a paradigm cell, an analogical form, a dialectal or attested variant, or an inherited form that differs from the dictionary citation form.

The model includes morphology where it is necessary to choose the relevant input. It includes orthography where the model must map phonological outputs to Old English surface forms. It remains a targeted derivational model with a narrower scope than a full parser of Old English, a full generator of paradigms, or a theory of all Old English variation.

The most important limitation is also one of the method's strengths. A deterministic sound-change model should keep irregularity visible. If a form is analogical, borrowed, dialectally mixed, or outside the regular path, it should remain visible as such. A model that explains too much by inventing small ad hoc sound laws has ceased to be useful. The aim is to show exactly which words are regular under a stated history, and what kind of explanation the others require.

## Why formalization helps historical linguists

The traditional comparative method already contains an implicit formal discipline [@OsthoffBrugmann1881; @SimsWilliams2018b]. When we say that Proto-Germanic \emph{*p} gives Old English \emph{f}, or that West Germanic \emph{*z} becomes \emph{r} in the relevant environment, we are describing a relation between earlier and later forms. When we say that a change must precede another change, we are making a claim about the ordering of operations. When we reject an etymology because it would produce the wrong vowel or consonant, we are using a mental derivation.

The problem is scale. A small derivation can be checked by hand. A single famous etymology can be discussed in a footnote. A network of hundreds of lexical items and many ordered sound changes is different. Sims-Williams's discussion of mechanising historical phonology makes this point directly, showing how explicit forward application of sound changes can uncover new cognates and sharpen relative chronology [@SimsWilliams2018a; @SimsWilliams2018b]. Errors can persist because each local step is familiar while the whole path is not inspected at once. A reconstruction may be plausible in isolation but fail after three later rules apply. A rule may work in the example for which it was introduced but damage other words. A relative chronology may seem harmless until a witness form forces a different order.

Formalization helps by turning these implicit derivations into inspectable objects. Judgment remains central, but it moves to explicit decisions about the input form, the source evidence, the interpretation of an Old English spelling, the status of a mismatch, and the historical reality of a narrow formal rule. The computer supplies consistency. It applies the rules as written, in the order given, to all relevant forms. It applies conditions uniformly, keeps every word in view, and preserves inconvenient consequences.

This is why CAPR is especially useful in the middle stage of historical work. At the beginning, one may not know enough to formalize much. At the end, one may imagine that the grammar is settled. In the middle, the investigator has many plausible sound changes, many reconstructed forms, and many lexical comparisons, but their interaction is unclear. A formal cascade creates pressure. It asks every part of the hypothesis to meet every other part.

## The Germanic and Old English case

The present Germanic model begins from Proto-Germanic and West Germanic reconstructions and derives Old English comparison forms through an ordered sequence of changes [@RingeTaylor2014; @Fulk2018]. The sequence includes large familiar developments such as West Germanic rhotacism, Anglo-Frisian brightening, breaking, i-umlaut, high-vowel apocope, and r-metathesis. It also includes smaller steps that matter because they fix particular derivations. Some changes are broad historical processes. Others are narrow formal notes whose value lies in a small group of witness forms.

The empirical dataset contains hundreds of Old English comparison forms. The current project state treats the research phase as complete. The major phonological system has moved out of debugging, and the remaining mismatches are documented as exceptions. This status matters for the prose. The book should read as an explanation of a stabilized model, with the residual problems presented honestly.

The Old English case also brings morphology to the foreground. A dictionary citation form sometimes differs from the form that should be fed to the sound-change cascade. The attested Old English comparison form may correspond to a dative plural, a genitive singular, a present-tense verbal form, or another paradigm cell. If the wrong cell is chosen, the formal derivation may fail for reasons that have little to do with phonology. The lexical entries therefore distinguish the citation reconstruction from the actual transducer input. This distinction is crucial for forms such as \emph{sċuldrum} 'shoulders, dative plural', where a plural case form gives the regular Old English target more directly than a singular citation form.

Old English spelling adds another layer. Some outputs are phonological forms. Some are orthographic normalizations. A form may be attested with a spelling that reflects dialect, manuscript practice, or later reshaping. The model must keep these questions separate. When the lexical section identifies an Old English target, it distinguishes attested forms, normalized forms, reconstructed Old English forms, and selected comparison forms. The formal derivation is strongest when the status of the target is clear.

The result is a model that is both stricter and more modest than a prose grammar. It is stricter because every rule must run. It is more modest because it has to say when an output is only a model output, when a lexical entry requires an analogical account, and when the evidence supports only an approximate placement in the sequence.

## Rules, forms, and accountability

The basic unit in the sound-change section is a rule. Each rule is presented with a historical discussion, a formal definition, and a prose explanation of what the definition does. The historical discussion explains why the change belongs in the grammar. The formal definition states the modeled operation. The chronology paragraph explains what happens if the rule is moved too early or too late, when such tests are informative.

The basic unit in the lexical section is a word or comparison form. Each entry begins with the relevant reconstruction, transducer input, Old English target, and derivation class. It then explains the comparative evidence, the Old English evidence, and the development from the selected input to the target. Complex entries may include paradigm comparison. Simple regular entries may not need one.

The relation between these two units is the main intellectual structure of the book. The rules are justified by the words. The words are explained by the rules. A sound law without lexical consequences is an empty formal gesture. A lexical derivation without an explicit rule sequence is too easy to adjust after the fact. CAPR brings the two kinds of claim into the same space.

This accountability is clearest when a rule is moved. Suppose a change currently stands before breaking. If it is delayed until after breaking, several words may produce the wrong outcome. Those words then become witnesses for a terminus ante quem. The change must have applied before breaking in the modeled sequence. If the same rule can be moved earlier with no effect on any checked form, the model has only a one-sided chronological constraint. The rule may still be historically real, and its placement may still be motivated by handbooks, branch history, or structural coherence. The checked forms by themselves fix only part of its position.

This distinction recurs throughout the sound-change section. Some rules have tight two-sided evidence. Some have a close relation on one side and a broad interval on the other. Some are placed chiefly because the sources treat a development as belonging to a historical cluster, even though the checked forms leave the nearest neighbor unresolved. The prose tries to preserve these differences. A formal model can make chronology look sharper than the evidence warrants. The book therefore separates what the forms prove, what the sources motivate, and what the implementation chooses in order to keep a coherent cascade.

## Relative chronology

Relative chronology is one of the main reasons to formalize sound change. A sound law is rarely just a statement that one segment becomes another. It is also part of a history in which earlier outputs become later inputs. The order of changes determines whether a form survives, feeds a later process, escapes a later process, or becomes opaque.

The sound-change section uses lexical consequences to explain order. The argument comes from the derivational effect of moving the rule; the number assigned to it is only a reference handle. If a delayed rhotacism produces the wrong form for \emph{learn}, then \emph{learn} is evidence about the relative order of rhotacism and the later change that it must precede. If moving an unstressed-vowel rule earlier makes no difference to any checked item, then the earlier side of the rule is not fixed by the current lexical tests.

This method is powerful because it makes negative space visible. Traditional prose often says that one change came before another because the result requires it. CAPR can show how broad that requirement is. A rule may need to precede some later development, but that later development may be far away in the sequence. Such a result is real evidence, although weaker than local adjacency. Conversely, a rule may need to follow an earlier change because the earlier change creates exactly the environment that the later rule consumes. That is a stronger local relation.

The book therefore avoids symbolic order notation in the main prose. It uses ordinary temporal language such as before, after, earlier, and later, then gives the lexical forms that break when the order is changed. This keeps the chronology tied to historical evidence. The formal model supplies the test; the prose explains the linguistic reason.

Some changes remain approximate. This is unavoidable. Handbooks may agree that a development belongs to an early West Germanic stage without fixing its position relative to every other early change. A small rule may be needed for a particular group of forms but lack enough witnesses to anchor both sides of its chronology. A technical stage may be useful in the implementation while lacking the status of an ordinary historical sound law. The draft says so where relevant. Formalization should clarify uncertain history, not convert it into false precision.

## The lexical entries

The lexical section answers a different kind of question. A sound-change chapter may say that a rule is supported by a set of witness forms, but a reader also needs to know what those forms are doing. Is the Proto-Germanic input a citation form or a particular inflectional cell? Is the Old English target a headword, a normalized spelling, an attested variant, or a reconstructed form? Do the handbooks agree on the reconstruction? Does the derivation depend on regular sound change, analogy, or a known unmodeled development?

The lexical entries make those distinctions explicit. Each entry begins with a small amount of metadata because the reader needs to know the selected input and target. The entry then turns to historical prose. The expected structure is simple. First, establish the transducer input and output. Then compare the reconstruction and the relevant source evidence. Then establish the Old English evidence. Then explain the development to Old English. If the argument depends on morphology, add a paradigm comparison.

The model entry for \emph{shoulder} shows why this structure is needed. The ordinary Old English headword is \emph{sculdor}, but the relevant comparison form for the successful derivation is the dative plural \emph{sċuldrum}. The sources differ in the reconstruction and stem-class implications of the Germanic word. A dative or instrumental plural input of the type \emph{*skúldramiz} aligns with the inherited plural ending and produces the Old English target. A singular-oriented input answers a different question. The lexical entry is where the model's choice of input becomes philologically accountable.

The derivation classes help keep the entries honest. A \emph{regular} entry is one in which the selected input and the deterministic rule path produce the Old English target. An `early_analogy` entry uses an input that reflects reshaping before the modeled Old English path. A `late_analogy` entry often depends on a paradigm cell whose form was later generalized or otherwise analogically important. An `attested_variant` entry reaches a real Old English form that may differ from the default dictionary headword. A `reconstructed_oe` entry uses a reconstructed target when that is the useful comparison. A `known_unmodelled` entry names an understood historical process that falls outside the deterministic FST. An `unexplained_unmodelled` entry preserves a real problem without inventing a solution.

These labels are working categories for accountability, deliberately narrower than a typology of all historical change. They tell the reader what kind of explanation the entry is offering. They also prevent the regular system from being quietly expanded to cover phenomena that should remain outside the sound-change cascade.

## The role of failure

A failed derivation is often more informative than a successful one. If the system derives \emph{dæg} from the selected input by the expected sequence, the entry may be straightforward. If it derives \emph{sċoldor} when the relevant Old English form is \emph{sċuldrum}, the mismatch forces a question. Was the wrong input chosen? Is the relevant Old English form a different paradigm cell? Is an analogical development involved? Is the target itself wrong? Is the sound-change rule missing a condition?

CAPR is useful because it makes these questions concrete. A failure has a shape. The output differs in a particular vowel, consonant, ending, or orthographic normalization. That difference points toward a type of problem. A wrong root vowel may indicate an ordering issue or a stem-class issue. A wrong ending may indicate the wrong paradigm cell. A plausible but non-attested output may point to analogy. A form that works only by suppressing a general rule may be a loan or a dialectal intrusion.

The original CAPR Burmish work made this point through the automatic detection of loanwords. If a rigorous model of regular sound change fails for a word while succeeding for the inherited vocabulary around it, the failure can reveal a non-inherited item. The Old English case is different in detail, but the logic is the same. A good regular model isolates irregularity and keeps it visible.

This is why the remaining mismatches in the Germanic model are treated as documented exceptions, which closes the route of adding more phonology for its own sake. A model with a few well-understood failures can be better than a model that achieves total coverage through artificial rules. The governing question is whether each success and each failure has the right kind of explanation.

## Formalization and philology

The formal model and the philological sources have different strengths. The model is good at consistency. The sources are good at historical interpretation, attestation, dialect, morphology, and comparison. The book depends on both.

The rule chapters cite the major handbooks and specialist sources where they are needed. Hogg, Campbell, Ringe and Taylor, Fulk, Luick, Brunner, Kroonen, Orel, and others provide the historical grammar and etymological framework within which the formalization makes sense [@Campbell1959; @Hogg1992; @RingeTaylor2014; @Fulk2018; @Luick1914; @SieversBrunner1965; @Orel2003; @Kroonen2013]. The FST operationalizes claims from these sources and asks what follows.

The lexical entries likewise begin from dictionaries, grammars, etymological works, and the Old English record. Attestation requires source support beyond appearance as a model target. A reconstruction requires historical support beyond a successful transducer output. When sources differ, the entry should identify the point of disagreement, such as stem class, gender, root vowel, suffix, branch stage, paradigm cell, or Old English attestation. Vague language about "source disagreement" is too weak.

This division of labor also matters for uncertainty. A source may support the historical reality of a change without fixing its exact position in the modeled sequence. A transducer may require a formal step whose historical scope is smaller than its code name suggests. A lexical entry may reach the target only by choosing a morphologically specific input. These facts should be visible. The book's prose therefore tries to write neither as code documentation nor as unformalized narrative. It is historical-linguistic prose under formal constraint.

## The formal sequence

The sound-change section begins with early West Germanic consonant and vowel changes and ends with Old English r-metathesis. The numbering follows the CAPR sound-change inventory. The numbers are useful because they keep the prose, the FST, and the chronology tests aligned. The argument itself lies in the historical discussion, the formal rule, and the lexical consequences.

Several internal numbers are technical or weight-marking stages, and the inventory also contains a numbering gap. This is normal in a formal system. Some implementation steps help the model run without corresponding to a historical sound law that deserves prose treatment. The introduction flags this so that the reader expects discontinuity in the internal labels.

The assembled sound-change section now covers the active manifest-backed sequence from the early West Germanic material through r-metathesis. Its chapters differ in scale. West Germanic rhotacism, Anglo-Frisian brightening, breaking, i-umlaut, apocope, and r-metathesis are large historical developments familiar from the literature. Other chapters treat narrower matters, including vowel adjustments, final-vowel behavior, cluster simplification, and special contexts needed to keep witness words regular. The book preserves this unevenness because the history itself is uneven.

A formal sound-change chapter normally has three obligations. It must identify the historical development, show the formal rule, and say how the modeled order is supported. If one of these obligations is weak, the prose should say so. A rule may be historically secure but chronologically loose. A rule may be chronologically useful but lexically narrow. A rule may be a formal convenience whose historical interpretation is cautious. Such cases are useful precisely because formalization clarifies the evidence.

## The word-by-word sequence

The lexical section gives a complementary view of the same system. It begins from a word and consults the sound laws through the derivation. For each word, the reader sees the selected Proto-Germanic or early input, the Old English comparison form, the derivation class, and the path through the modeled sound changes. Where a word needs further discussion, a lexeme report explains the sources and the reasoning.

This organization is especially important because many words are formally regular but historically interesting. A word may derive successfully only because the selected input is a particular inflected form. A word may be regular in the phonology but require a note about the Old English target. A word may have a straightforward output but a complex comparative background. Conversely, a word may be phonologically uninteresting and need no extended report.

The selective-report policy reflects this. Ordinary regular rows with no note can remain short. Rows with a note, a non-regular derivation class, or a manually supplied report need fuller discussion. The point is to spend attention where the historical argument needs it. A complete book should spare the reader identical descriptions of regular derivations while also explaining difficult words in prose.

The lexical section can therefore be read in two ways. It can be read as a derivation report, showing how the system maps inputs to outputs. It can also be read as a set of philological case studies. The second use is the more important for publication. A formal output is only as good as the input and target it connects. The lexical entries show why those inputs and targets were chosen.

## How to read the formal notation

The book uses several kinds of notation. Reconstructed forms are marked with an asterisk and usually appear in emphasis. Old English forms appear in emphasis in ordinary prose. FST rule names appear in the rule headings and in cross-references. Formal code appears in fenced `foma` blocks. The code blocks are the place where implementation details are visible. The surrounding prose explains the linguistic content.

The formal code should be read as a compact version of a historical claim. A line such as a vowel change before a particular class of following segments means that the model applies the change wherever the stated environment is met. If the rule is too broad, it will damage words. If it is too narrow, it will fail to derive words. If its order is wrong, it may feed or bleed later rules incorrectly.

The derivation tables in the lexical section divide the path into earlier Germanic developments and Old English developments. This division is sometimes approximate, but it helps the reader see the architecture of the model. Some words pass through many changes. Others pass through almost none. The absence of a change in a given word is as important as its presence, because it shows that the rule's environment was absent.

The book avoids treating formal labels as historical explanations by themselves. A label such as `OEIUmlaut` is a reference handle. The explanation lies in the surrounding prose, the code, and the witness forms. This is why the rule chapters give ordinary titles as well as FST names. The reader should be able to understand the linguistic development before inspecting the code.

## What counts as success

A successful derivation is one in which the selected input, passed through the ordered sound-change cascade, yields the target form. That statement needs unpacking. The input must be historically defensible. The target must be identified correctly. The rule path must be regular under the model. A success that depends on a bad input or an uncertain target has only formal value.

For this reason, the book treats success as layered. A purely formal success means that the transducer output matches the target string. A philological success means that the input and target are the right objects to compare. A historical success means that the derivation also makes sense in the broader evidence of Germanic and Old English. Many entries satisfy all three. Some satisfy only the formal condition and therefore need more explanation.

The reverse is also true. A formal failure can be historically informative. If the attested Old English form is analogical, a regular sound-change model should fail to derive it from the inherited input. If the target is a dialectal or later variant, the failure may reflect the limited scope of the modeled path. If a word is borrowed, the inherited cascade is the wrong explanation. Such cases are successful diagnoses when they are labeled correctly.

The derivation classes are therefore part of the argument. They keep different kinds of success and failure apart. A `known_unmodelled` item has a different status from an unexplained mismatch. A `late_analogy` item has a different status from a regular sound-change witness. A `reconstructed_oe` target has a different status from direct attestation. These distinctions make the book more cautious, but also more useful.

## Why a book is needed

CAPR is a database and a set of tools, but the present work also needs book prose. A database can tell us that an output matches or fails. It can store traces, classes, notes, and citations. Prose explains why a particular comparison matters, why a rule is historically plausible, and why an apparently small mismatch changes the analysis of a word.

The prose also lets the reader see the scale of the argument. In a table, a rule with one decisive witness and a rule with dozens of familiar examples may look similar. In a book, the difference can be stated. A narrow note can remain narrow. A broad historical change can be given fuller context. A rule whose placement is source-based can be marked as such. The written form prevents the formal system from projecting false symmetry.

The book format also makes the work contestable. A reader can disagree with a source interpretation, a selected input, a rule environment, or a derivation class. Because the claims are explicit, such disagreement has a place to attach. The ideal outcome is a set of decisions public enough to be corrected.

## Scope and limits of the present draft

The present draft reflects a stabilized phase of the Germanic-to-Old-English work. The main sound-change system is treated as fixed for publication purposes unless a serious error is found. The active work is writing the sound-change chronology, explaining lexical derivations, and making the relation between formal output and philological evidence clear.

The system remains open to future improvement. A future version may add more lexeme reports, improve bibliography, refine the treatment of morphology, or extend the model to dialectal variation. A future version may also separate some compact rule groupings or rewrite some chapters in fuller historical prose. The present book has a narrower goal. It offers a coherent account of the current model and the lexical evidence that matters most for understanding it.

The lexical write-up is also at a different stage from the sound-change write-up. The sound-change sequence has received sustained prose review. The lexical section contains a mixture of generated derivation views and manifest-backed production reports. This introduction is written to support the intended combined draft, which will contain an opening methodological section, a formal chronology section, and a word-by-word section. It should be revised after the combined PDF has been read as a whole.


## A small example of rule evidence

It may help to spell out the logic of a chronology test without making the introduction depend on any one rule. Imagine a rule that changes an inherited consonant before a later vowel development. If the consonant change applies first, the later vowel rule sees the right environment and the word reaches its Old English target. If the consonant change is postponed, the later vowel rule misses that environment, and the output has the wrong vowel. The word is then evidence that the consonant change must be earlier than the vowel rule.

The same reasoning also works in the other direction. If a rule creates a segment that a later rule would incorrectly alter, the rule must be placed after that later rule or else the derivation breaks. If a rule can be moved through a large stretch of the sequence without altering any checked form, the current lexical evidence leaves its position inside that stretch open. The rule may still belong there historically, but the book should report the limit of the order test.

This way of arguing is close to ordinary historical grammar. What CAPR adds is exhaustive application within the chosen dataset. A scholar can always test a rule against one or two examples by hand. The formal system tests it against the whole active set of comparison forms. The resulting evidence may confirm the expected history, expose a bad environment, or reveal that a traditional explanation is correct but less tightly ordered than the prose had suggested.

The recent revision of the sound-change chapters was largely an exercise in this kind of discipline. Earlier wording sometimes treated a broad interval as if it were a close local boundary. The revised prose says more carefully when the checked forms establish only a later relation, only an earlier relation, or a wide range within which source-based placement is still needed. This strengthens the argument by separating evidence from presentation.

## Morphology as part of the input

A sound-change model can only derive the form it is given. This fact is obvious in computation and easy to overlook in etymological prose. A dictionary headword is often a useful citation form, but a real Old English comparison may descend from a particular inflected form. Nouns have case and number. Verbs have tense, mood, person, and number. Stem classes and suffixes matter. If the input form has the wrong ending, the phonology may produce the wrong word for the right historical reason.

The Germanic model therefore distinguishes the citation reconstruction from the selected transducer input. The citation reconstruction identifies the lexical family. The input form identifies the form whose regular development is being tested. Sometimes these are the same. Sometimes they diverge. When they diverge, the lexical entry has to explain why the selected input is legitimate.

This distinction is especially important for analogical cases. A late analogical form may be phonologically regular from a particular paradigm cell while the citation form gives a different result. The entry must then show both sides of the argument. It must say what the ordinary citation comparison would produce, why that output misses the Old English target, and why the chosen cell or reshaped form is a plausible historical source for the attested form. A table of outputs can make the difference clear, while the historical interpretation belongs in prose.

The same point applies to early analogy. If a form was already reshaped before the modeled Old English sound changes, the model should begin from the reshaped input. This is legitimate when the reshaping is independently motivated and stated plainly. A silent adjustment of the input merely to make the output work would be illegitimate. The lexical entries expose the chosen input and ask whether it is historically defensible.

## Orthography and surface form

Old English orthography is another reason why derivational success has to be interpreted carefully. The model may produce a phonological output that then requires orthographic normalization. Some outputs contain symbols used internally by the model to represent phonetic or phonological values. Some Old English targets are normalized editorial forms. Some spellings are dialectal, manuscript-specific, or late. A visible spelling mismatch can be compatible with phonological success, and a visible spelling match may still need historical explanation.

The orthography-and-surface part of the derivation report records the final mapping from model output to Old English comparison form. In simple cases this is almost trivial. In others, it is where the reader sees that the regular phonology has produced a form that still needs editorial interpretation. The lexical entries then decide how much of that interpretation matters for the historical argument.

This matters because computational systems are exact about strings. A human reader may see immediately that two spellings are equivalent for the purpose at hand. The program needs that equivalence to be encoded. Exactness is useful when it catches real problems, but unhelpful when it mistakes notation for history. The book therefore treats orthographic normalization as a distinct layer. It is part of the pipeline and distinct from sound change.

## Loanwords, analogy, and the boundary of the regular

The Neogrammarian commitment to regular sound change is often misunderstood as a claim that every word must obey the same history [@OsthoffBrugmann1881]. In practice, the point is methodological. If sound change is regular, then departures from the regular path are meaningful. They may indicate borrowing, analogy, expressive reshaping, dialect mixture, textual variation, or error. The regular model is the instrument that lets us see those departures.

In the original Burmish CAPR setting, this logic made loanwords stand out. A word that resisted derivation by the inherited sound changes, while its neighbors succeeded, became a candidate for borrowing. In the Old English setting, analogy is more often the central issue. A word may be inherited, but the attested form may reflect leveling from another paradigm cell. A form may preserve a vowel because of a morphological environment that the simple citation form lacks. A verb may require a finite form as input because the infinitive citation form answers a different question.

The book therefore treats the boundary of the regular as a positive result. A known unmodeled item is resolved when the relevant process is named and supported. An unexplained unmodeled item remains a problem, but it is a contained problem. A lexeme retargeting is a substantive historical claim that the previous cognate or target assignment was inferior. These categories keep the non-regular material visible without letting it dissolve the regular grammar.

## Local decisions and global coherence

A historical grammar is often written locally. One chapter discusses breaking. Another discusses i-umlaut. A dictionary entry discusses a word. Each discussion may be correct in isolation. CAPR asks whether all of them can be true at once. This is the global question.

Global coherence allows rules with different status. A model can contain major rules, minor rules, technical stages, and lexical exceptions. The key requirement is that the interaction among them has been tested. A change that works only because an earlier rule has already removed a segment has a different status from a change that can float across twenty positions unnoticed. A word that supports a local order relation carries more chronological weight than a word that merely remains regular throughout a broad interval.

The introduction of explicit rules also encourages a useful kind of humility. It is easy to write prose that sounds settled. It is harder to write code that derives the forms. When the code fails, the prose must change. When the code succeeds too easily because a rule is overbroad, the prose must also change. The formal model is a check on the coherence of philological claims and remains subordinate to philology.

## Reproducibility and disagreement

One of the most important virtues of a formalized reconstruction is that it can be disagreed with precisely. A reader may think a rule is too broad. A different reader may accept the rule but reject its order. Another may object to the selected input for a particular lexical item. Another may think the Old English target has been normalized too aggressively. These are productive disagreements because each one points to an explicit part of the system.

Purely narrative accounts can leave more work implicit. If a grammar says that a development "regularly" gives a certain form, the reader may have to reconstruct the intermediate steps mentally. If an etymological note says that a word is analogical, the relevant paradigm comparison may remain implicit. CAPR aims to make those hidden steps public.

The model remains scholarly and inspectable. Every formalization reflects decisions about the inventory of symbols, the segmentation of forms, the selected reconstructions, the ordering of changes, the treatment of morphology, and the interpretation of Old English evidence. The point is that these decisions are recorded in a way that lets others inspect them. Reproducibility here means the reproducibility of consequences. Given these inputs and these rules in this order, the stated outputs follow.

## From tool to argument

The project began as a tool, but the book must become an argument. Its argument is that traditional rule-based reconstruction gains clarity when its derivations are made explicit. The Old English material is a historically rich case in which the strengths and limits of formalization can be seen.

The sound-change section argues that a large part of the Proto-Germanic to Old English path can be represented as an ordered sequence of explicit rules, with the relative chronology supported by identifiable lexical consequences. The lexical section argues that individual words can be made accountable to that sequence without erasing the philological complexity of reconstruction, attestation, and analogy. The introduction argues that these two forms of accountability belong together.

The book should be judged by both standards. If the formal system derives the words while the prose hides uncertainty, it fails as historical linguistics. If the prose is philologically subtle while the formal system fails to reproduce the derivations, it fails as a formal account. The goal is to hold both demands at once.

## How the parts fit together

The introduction gives the reader the method. The sound-change section gives the rule sequence. The lexical section gives the word evidence. None of the three is complete without the other two.

The method matters because formal derivations can look forbidding without an explanation of their purpose. The rule sequence matters because lexical entries can become arbitrary without an explicit sound-change history. The lexical entries matter because a rule sequence can become detached from evidence unless it is held against actual words.

A reader interested primarily in historical phonology should begin with the sound-change section, then follow the cross-references into the lexical entries. A reader interested in an individual Old English word should begin with the lexical entry and then consult the rule chapters for the changes mentioned in the derivation. A reader interested in computational method should read the whole book as an example of how a traditional historical grammar can be made operational without surrendering philological judgment.

The aspiration is practical. Historical linguistics already has a rich tradition of rigorous argument. CAPR gives that tradition a test bench. It lets us ask whether the rules we say we believe actually derive the words we claim they derive, in the order we claim they occurred. That question is simple. Answering it carefully is the work of the book.

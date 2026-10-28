#!/usr/bin/env python3
"""Private component/cascade experiments; never rebuild or install production."""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import platform
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import oe_pipeline
from anglo_frisian_experiments import compile_isolated
from capr_runtime import RuntimeLayout, check_build_manifest, layout
from cascade_baseline import build_baseline, legacy_subset, projection_sha256
from executable_facts import parse_defines
from sound_change_order_sensitivity import batch_apply_down

BASE = "3cb109c981c8868bf383172e2be06cdc88c00fb0"
EARLY = "PNWGmcULowering"
LINK = "OECompoundLinkingSyncope"
STRIP = "OEStripSecondaryStress"
RAISE = "OEInterStressRaising"
LATE = "OEMedUnstressedULowering"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def star(text):
    return "".join("*" + letter for letter in text)


def symbols(text):
    return " ".join("{*" + letter + "}" for letter in text)


EARLY_DEFINITIONS = """
define RSyllEarly Ctx([
    {*ù} -> {*ò} || _
        [EnglishStarConsonantNoJ - EnglishStarNasal]
        EnglishStarConsonantNoJ* EnglishStarNonHighVowel
]);
define RCompEarly Ctx([
    {*ù} -> {*ò} ||
        .#. EnglishStarConsonant* PGmcStarAcuteVowel
        [EnglishStarVocalic|EnglishStarConsonant]* _
        [EnglishStarConsonantNoJ - EnglishStarNasal]
        EnglishStarConsonantNoJ* EnglishStarNonHighVowel
]);
define RBroadEarly Ctx([
    {*u}->{*o} || _
        [EnglishStarConsonantNoJ - EnglishStarNasal]
        EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ù}->{*ò} || _
        [EnglishStarConsonantNoJ - EnglishStarNasal]
        EnglishStarConsonantNoJ* EnglishStarNonHighVowel
]);
define REarly [PNWGmcULowering .o. RSyllEarly];
define REarlyComp [PNWGmcULowering .o. RCompEarly];
define REarlyBroad [PNWGmcULowering .o. RBroadEarly];
define RCellTail [
    e:{*e} s:{*s} |
    a:{*a} s:{*s} a:{*a} |
    a:{*a} n:{*n} ō:{*ō} n:{*n} |
    ō:{*ō} n:{*n}
];
define RCellWord [
    pgrmStrongPlainHeavy RCellTail |
    pgrmCompoundFirst pgrmCompoundSep pgrmStrongPlainHeavy RCellTail
];
define RInput [[{ᵘ}:{*ᵘ}|{ᶜ}:{*ᶜ}|0] [pgrmWord|RCellWord]];
"""

# These are explicit experimental syllabification assumptions, not a new
# production phonotactics authority. A single-onset sensitivity control follows.
ONSETS = (
    "pr", "pl", "tr", "tw", "kr", "kl", "kw", "br", "bl", "dr", "dw",
    "gr", "gl", "gw", "fr", "fl", "θr", "θw", "xr", "xl", "xn", "xw",
    "sp", "st", "sk", "sm", "sn", "sl", "sw", "ʃr", "ʃw",
)
TRIPLES = ("spr", "spl", "str", "skr", "skw")


def foot_definitions():
    moves = []
    for cluster in sorted(TRIPLES + ONSETS, key=lambda x: (-len(x), x)):
        moves.append(
            f"[{symbols(cluster)} {{ᵇ}} -> {{ᵇ}} {symbols(cluster)} "
            "|| _ RV]"
        )
    single_move = "[" + ", ".join(
        f"{{*{consonant}}} {{ᵇ}} -> {{ᵇ}} {{*{consonant}}} || _ RV"
        for consonant in "bβdfgklmnprstwxzθðŋɡʧʤʝʃçʒjh"
    ) + "]"
    moves.append(single_move)
    mark = "[{*} -> {ᵇ*} || _ RVStart]"
    syllabify = " .o. ".join([mark, *moves])
    single = mark + " .o. " + single_move
    rewrites = []
    for plain, grave in zip("aeiou", "àèìòù"):
        rewrites.append(
            f"{{*{plain}}} -> {{*{grave}}} || "
            ".#. RPrefix RFirst RRest* {ᵇ} RC* _ RC+ {ᵇ}"
        )
    return f"""
define RC OEAnyConsonant;
define RV EnglishStarVocalic;
define RVStart [{"|".join("{" + ch + "}" for ch in "aeĕiouyȳæøāąãēęīōǭœūųɑɔəɛɜʉʊǣáéíóúḯḗàèìòù")}];
define RShort [EnglishStarShortVowel|EnglishStarShortDiphthong];
define RLong [RV - RShort];
define RPrefix [{{*ᶠ}} {{ᵇ}} RC* RShort|0];
define RL [{{ᵇ}} RC* RShort];
define RH [{{ᵇ}} RC* [RLong RC* | RShort RC+]];
define RS [RL|RH];
define RFirst [RH (RL) | RL RS];
define RRest [RH (RL) | RL];
define RSyll [{syllabify}];
define RSyllOne [{single}];
define RAccent [{", ".join(rewrites)}];
define RUnsyll [{{ᵇ}} -> 0];
define RFoot SentenceCtx([RSyll .o. RAccent .o. RUnsyll]);
define RFootOne SentenceCtx([RSyllOne .o. RAccent .o. RUnsyll]);
define RDecode Ctx([
    {{*à}}->{{*a}}, {{*è}}->{{*e}}, {{*ì}}->{{*i}},
    {{*ò}}->{{*o}}, {{*ù}}->{{*u}}
]);
define RLate [RFoot .o. OEMedUnstressedULowering .o. RDecode];
define RLateOne [RFootOne .o. OEMedUnstressedULowering .o. RDecode];
define RNoop [0];
"""


CANDIDATES = {
    "world": "*wír-àldiz",
    "rainbow": "*régna-bùgô",
    "soul": "*sáiwalō",
    "bow": "*búgô",
    "Buga-same-serialization-not-independent-reconstruction": "*búgô",
    "earthly-genitive-grave": "*érθa-kùnðas",
    "earthly-genitive-plain": "*érθa-kunðas",
    "earthly-genitive-final-a": "*érθa-kùnðasa",
    "earthly-genitive-neuter-es": "*érθa-kùnðes",
    "earthly-accusative-masculine": "*érθa-kùnðanōn",
    "earthly-nominative-masculine": "*érθa-kùnðaz",
    "earthly-neuter-nomacc": "*érθa-kùnðan",
    "earthly-feminine-accusative": "*érθa-kùnðōn",
    "earthly-feminine-genitive": "*érθa-kùnðaizōz",
    "earthly-voiceless-dental-diagnostic": "*érθa-kùndas",
    "godcund-nominative": "*gúða-kùnðaz",
    "godcund-genitive": "*gúða-kùnðas",
    "godcund-accusative": "*gúða-kùnðanōn",
    "which": "*xwí-līkaz",
    "onefold": "*án-fàldiz",
    "twofold": "*twí-fàldiz",
    "lung": "*lúnganjō",
    "gold": "*gúlθą",
    "hound": "*xúndaz",
    "wolf": "*wúlfaz",
    "full": "*fúllaz",
    "head": "*xáubudą",
    "heaven": "*xébun",
    "name": "*námô",
    "wound": "*wúndōdē",
}

COMPONENTS = {
    "early-bow-grave": star("régnabùgô"),
    "early-bow-independent": star("búgô"),
    "early-kund-grave": star("érθakùndaz"),
    "early-high-vowel-synthetic": star("bùgi"),
    "early-j-block-synthetic": star("bùgja"),
    "early-unstressed-synthetic": star("sátubagô"),
    "early-n-after-first-consonant-synthetic": star("sátùgna"),
    "late-dental-nasal": star("bérun"),
    "late-labial-nasal": star("bérum"),
    "late-world": star("wéruld"),
    "late-world-inflected": star("wéruldes"),
    "late-world-back-mutated": "*w*éo*r*u*l*d",
    "late-world-back-mutated-inflected": "*w*éo*r*u*l*d*e*s",
    "late-earthly": "*éo*r*θ*k*u*n*d*e*s",
    "late-earthly-pretonic-synthetic": "*ᶠ*g*e*éo*r*θ*k*u*n*d*e*s",
    "late-earthly-uninflected": "*éo*r*θ*k*u*n*d",
    "late-earthly-accusative": "*éo*r*θ*k*u*n*d*n*e",
    "late-godcund": star("gódkundes"),
    "late-rainbow": "*r*é*ʝ*n*b*o*g*a",
    "late-aetheling": star("áθeling"),
    "late-aetheling-inflected": star("áθelingas"),
    "late-cyning-inflected": star("kyningas"),
    "late-riding": "*r*ī*d*e*n*d*e",
    "late-being": star("wésende"),
    "late-head-inflected": "*x*éa*b*u*d*e",
    "late-sinfull-uninflected": star("synfull"),
    "late-sinfull-inflected": star("synfulle"),
    "late-hlafweard-transparent-root": "*x*l*ā*f*w*ea*r*d",
    "weak-LH-world": star("wérald"),
    "weak-LH-grave": star("wéràld"),
    "weak-LH-primary": star("wéráld"),
    "weak-LH-heavy-first": star("wértald"),
    "weak-LH-no-cluster": star("wéralu"),
    "weak-LH-initial-weak": star("werald"),
    "weak-LH-twofold": star("twífald"),
    "weak-LH-onefold": "*ā*n*f*a*l*d",
}


def orders(original):
    def replace(sequence, old, new):
        result = list(sequence)
        assert result.count(old) == 1
        result[result.index(old)] = new
        return result

    def insert(sequence, anchor, new):
        result = list(sequence)
        result.insert(result.index(anchor), new)
        return result

    models = {
        "identity": original,
        "A-secondary": replace(original, EARLY, "REarly"),
        "A-compound": replace(original, EARLY, "REarlyComp"),
        "A-negative": original,
        "A-overbroad-diagnostic": replace(original, EARLY, "REarlyBroad"),
        "B3-conditioned-lowering": replace(original, LATE, "RLate"),
        "B3-single-onset-sensitivity": replace(original, LATE, "RLateOne"),
        "G-parser-only": replace(original, "EnglishProtoInput", "RInput"),
    }
    # Decode immediately after the protected operation: representation cleanup,
    # not a second historical loss of stress.
    b2 = insert(original, LATE, "RFoot")
    b2.insert(b2.index(LATE) + 1, "RDecode")
    models["B2-foot-annotations"] = b2
    for name in (
        "B2-foot-annotations", "B3-conditioned-lowering",
        "B3-single-onset-sensitivity",
    ):
        models[name] = replace(models[name], "EnglishProtoInput", "RInput")
    models["joint"] = replace(models["B3-conditioned-lowering"], EARLY, "REarly")
    early_foot = insert(original, "OEMedUnstressedORaising", "RFoot")
    early_foot.insert(early_foot.index(LATE) + 1, "RDecode")
    models["joint-earlier-prosody-diagnostic"] = replace(
        replace(early_foot, EARLY, "REarly"), "EnglishProtoInput", "RInput")
    for early in (False, True):
        sequence = replace(original, EARLY, "REarly") if early else list(original)
        sequence.remove(STRIP)
        for label, anchor, after in (
            ("before-link", LINK, False),
            ("production", RAISE, False),
            ("after-raise", RAISE, True),
            ("after-late", LATE, True),
        ):
            moved = list(sequence)
            moved.insert(moved.index(anchor) + int(after), STRIP)
            models[f"strip-{label}-early-{int(early)}"] = moved
    return models


def apply_sets(binary, states):
    forms = sorted({form for outputs in states for form in outputs})
    values = batch_apply_down(binary, forms) if forms else []
    lookup = dict(zip(forms, values))
    return [
        sorted({out for form in outputs for out in lookup[form]})
        for outputs in states
    ]


def trace_model(sequence, bins, initial):
    states = [[value] for value in initial]
    trace = []
    for index, stage in enumerate(sequence, 1):
        previous = states
        states = apply_sets(bins["component:" + stage], states)
        ambiguous = [
            dict(input=initial[number], before=old, outputs=outputs)
            for number, (old, outputs) in enumerate(zip(previous, states))
            if len(outputs) > 1
        ]
        if ambiguous:
            raise RuntimeError(
                "Nonfunctional downward relation at " + stage + ": "
                + json.dumps(ambiguous, ensure_ascii=False))
        trace.append(dict(step=index, stage=stage, before=previous, after=states))
    return states, trace


def counts(rows, outputs):
    return dict(
        accepted=sum(bool(value) for value in outputs),
        rejected=sum(not value for value in outputs),
        ambiguous=sum(len(value) > 1 for value in outputs),
        matched=sum(row["counterpart"] in value for row, value in zip(rows, outputs)),
        mismatch_ids=[
            row["row_id"] for row, value in zip(rows, outputs)
            if row["counterpart"] not in value],
    )


def protected_files(runtime):
    paths = [
        *runtime.fsts_dir.rglob("*"),
        *runtime.data_dir.rglob("*"),
        *runtime.docs_dir.rglob("*"),
        *runtime.tools_dir.glob("*.py"),
        *runtime.bin_dir.glob("*.bin"),
        runtime.build_manifest, runtime.bin_dir / "oe_input_context.py",
    ]
    return {
        str(path.relative_to(runtime.germanic_dir)): digest(path)
        for path in sorted(set(paths)) if path.is_file()
    }


def check_functionality():
    runtime = layout()
    if not runtime.is_container or runtime.germanic_dir == Path("/usr/app"):
        raise RuntimeError("Run formal checks only in the private backend snapshot.")
    canonical = RuntimeLayout(Path("/usr/app"), Path("/usr/app"),
                              Path("/usr/app"), True)
    before = protected_files(canonical)
    definitions = EARLY_DEFINITIONS + foot_definitions()
    experimental_hash = hashlib.sha256(definitions.encode()).hexdigest()
    components = (
        "EnglishProtoInput", "RInput", EARLY, "RSyllEarly", "RCompEarly",
        "RBroadEarly", "REarly", "REarlyComp", "RSyll", "RSyllOne",
        "RFoot", "RFootOne", "RDecode", "RLate", "RLateOne",
    )
    # Close the input alphabet: Foma's identity test conservatively rejects
    # delayed UNKNOWN/IDENTITY arcs outside the serialized segment inventory.
    definitions += "\ndefine RFormalDomain [ContextSegments|{*ᶠ}|{*ᵘ}|{*ᶜ}]*;\n"
    tested = {}
    for index, name in enumerate(components):
        identifier = "RFunctional" + str(index)
        expression = name if name in ("EnglishProtoInput", "RInput") else (
            "RFormalDomain .o. " + name)
        definitions += f"\ndefine {identifier} [{expression}];\n"
        tested[name] = identifier
    recipe = dict(
        definitions=definitions, insert_after="", insert_rule="", replace={},
        component_checks=[dict(component=name) for name in tested.values()])
    checks = {}
    with tempfile.TemporaryDirectory(prefix="capr_secondary_functional_") as temporary:
        bins = compile_isolated(
            runtime.germanic_fst, recipe, [], Path(temporary), components_only=True)
        for name in components:
            binary = bins["component:" + tested[name]]
            result = subprocess.run(
                ["foma", "-q", "-e", "load stack " + binary.name,
                 "-e", "test functional", "-e", "quit"],
                cwd=binary.parent, capture_output=True, text=True, timeout=120,
                check=True)
            answer = re.findall(r"(?m)^([01]) \(1 = TRUE, 0 = FALSE\)$", result.stdout)
            if len(answer) != 1:
                raise RuntimeError("Unrecognized functionality test: " + result.stdout)
            checks[name] = dict(functional=answer == ["1"], stdout=result.stdout)
            ambiguous = subprocess.run(
                ["foma", "-q", "-e", "load stack " + binary.name,
                 "-e", "ambiguous upper", "-e", "test null", "-e", "quit"],
                cwd=binary.parent, capture_output=True, text=True, timeout=120,
                check=True)
            empty = re.findall(r"(?m)^([01]) \(1 = TRUE, 0 = FALSE\)$",
                               ambiguous.stdout)
            if len(empty) != 1:
                raise RuntimeError("Unrecognized ambiguity test: " + ambiguous.stdout)
            checks[name]["ambiguous_domain_empty"] = empty == ["1"]
            checks[name]["ambiguous_domain_stdout"] = ambiguous.stdout
            if name in ("EnglishProtoInput", "RInput"):
                checks[name]["biu_witness"] = batch_apply_down(binary, ["biu"])[0]
    after = protected_files(canonical)
    if before != after:
        raise RuntimeError("Production files changed during formal functionality checks.")
    return dict(
        base_commit=BASE, source_sha256=digest(runtime.germanic_fst),
        experimental_definitions_sha256=experimental_hash,
        definitions_sha256=hashlib.sha256(definitions.encode()).hexdigest(),
        command="foma -q -e 'load stack COMPONENT.bin' -e 'test functional' -e quit",
        domain="ContextSegments plus existing context markers, repeated",
        checks=checks, all_functional=all(row["functional"] for row in checks.values()),
        sound_operations_functional=all(checks[name]["functional"] for name in (
            EARLY, "RSyllEarly", "RCompEarly", "RBroadEarly", "REarly",
            "REarlyComp", "RFoot", "RDecode", "RLate", "RLateOne")),
        protected_before=before, protected_after=after)


def run():
    runtime = layout()
    canonical = RuntimeLayout(Path("/usr/app"), Path("/usr/app"),
                              Path("/usr/app"), True)
    if not runtime.is_container or runtime.germanic_dir == canonical.germanic_dir:
        raise RuntimeError("Stage the clean snapshot in a private backend directory.")
    for relative in (
        "fsts/germanic.txt", "fsts/old_english_sandbox.txt",
        "data/germanic-aligned-final.tsv", "data/entry_context_metadata.tsv",
        "oe_input_context.py",
    ):
        if digest(runtime.germanic_dir / relative) != digest(canonical.germanic_dir / relative):
            raise RuntimeError("Snapshot/canonical scientific source drift: " + relative)
    stages = oe_pipeline.stages()
    errors = check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], canonical)
    if errors:
        raise RuntimeError("; ".join(errors))
    before = protected_files(canonical)
    baseline = build_baseline(runtime.corpus_tsv, canonical.bin_dir / "old_english.bin")
    frozen_dir = runtime.docs_dir / "sound_changes/cascade_baseline"
    expected = json.loads((frozen_dir / "cascade_baseline_summary.json").read_text())
    if baseline["summary"] != expected:
        raise RuntimeError("Live production differs from frozen baseline.")
    original = [
        stage.foma_identifier if stage.kind == "named" else stage.inline_text
        for stage in stages]
    models = orders(original)
    rows = oe_pipeline.load_rows(runtime.corpus_tsv)
    inputs = [oe_pipeline.evaluation_input(row) for row in rows]
    with (frozen_dir / "cascade_baseline_outputs_legacy380.tsv").open() as handle:
        legacy = list(csv.DictReader(handle, delimiter="\t"))
    with (frozen_dir / "approved_input_migrations.tsv").open() as handle:
        migrations = list(csv.DictReader(handle, delimiter="\t"))
    selected_legacy = legacy_subset(baseline["records"], legacy, migrations)
    immutable_inputs = [oe_pipeline.evaluation_input(row) for row in legacy]
    candidate_offset = len(rows) + len(legacy)
    candidates = [
        oe_pipeline.evaluation_input({"proto_norm": oe_pipeline.normalize_proto(raw)})
        for raw in CANDIDATES.values()]
    all_inputs = inputs + immutable_inputs + candidates
    definitions = EARLY_DEFINITIONS + foot_definitions()
    components = sorted({
        item for sequence in models.values() for item in sequence
    } | {"RSyllEarly", "RCompEarly", "RBroadEarly", "OELHWeakRaising", "RSyll"})
    # Independent composed finals cross-check component evaluation, including
    # the composed metrical operation. No Python stress oracle changes strings.
    complete_models = (
        "identity", "A-secondary", "A-compound", "B2-foot-annotations",
        "B3-conditioned-lowering", "joint",
    )
    complete_names = {}
    for index, name in enumerate(complete_models):
        ident = f"RWhole{index}"
        complete_names[name] = ident
        definitions += "\ndefine " + ident + " " + " .o. ".join(models[name]) + ";\n"
        components.append(ident)
    recipe = dict(
        definitions=definitions, insert_after="", insert_rule="", replace={},
        component_checks=[dict(component=item) for item in components])
    production = batch_apply_down(canonical.bin_dir / "old_english.bin", inputs)
    results = {}
    with tempfile.TemporaryDirectory(prefix="capr_secondary_") as temporary:
        bins = compile_isolated(
            runtime.germanic_fst, recipe, [], Path(temporary), components_only=True)
        for name, sequence in models.items():
            print("model " + name, file=sys.stderr, flush=True)
            final, trace = trace_model(sequence, bins, all_inputs)
            corpus = final[:len(rows)]
            if name == "identity":
                if corpus != production:
                    raise RuntimeError("Isolated identity differs from production.")
                reference_trace = trace
                immutable_identity = final[len(rows):candidate_offset]
                for step, stage in zip(trace, stages):
                    actual = batch_apply_down(
                        canonical.bin_dir / stage.snapshot_bin, inputs)
                    if step["after"][:len(rows)] != actual:
                        raise RuntimeError("Identity snapshot disagreement: " + step["stage"])
            if name in complete_names:
                whole = batch_apply_down(
                    bins["component:" + complete_names[name]], all_inputs)
                if whole != final:
                    raise RuntimeError("Composed/component mismatch: " + name)
            delta = []
            for index, (row, old, new) in enumerate(zip(rows, production, corpus)):
                if old != new:
                    delta.append(dict(
                        **row, old=old, new=new,
                        trace=[dict(
                            step=step["step"], stage=step["stage"],
                            before=step["before"][index], after=step["after"][index])
                               for step in trace]))
            lexical = []
            for index, (label, raw) in enumerate(CANDIDATES.items(), candidate_offset):
                steps = [
                    dict(step=step["step"], stage=step["stage"],
                         before=step["before"][index], after=step["after"][index],
                         changed=step["before"][index] != step["after"][index])
                    for step in trace]
                rejection = next((step for step in steps if not step["after"]), None)
                replacements = {
                    "REarly": EARLY, "REarlyComp": EARLY, "REarlyBroad": EARLY,
                    "RInput": "EnglishProtoInput", "RLate": LATE, "RLateOne": LATE,
                }
                reference = {step["stage"]: step for step in reference_trace}
                divergence = next((
                    dict(stage=step["stage"], step=step["step"],
                         identity=reference[key]["after"][index],
                         experimental=step["after"][index])
                    for step in trace
                    if (key := replacements.get(step["stage"], step["stage"])) in reference
                    and step["after"][index] != reference[key]["after"][index]
                ), None)
                lexical.append(dict(
                    name=label, input=raw, evaluator_input=all_inputs[index],
                    parser_accepted=bool(steps[0]["after"]), rejection=rejection,
                    first_aligned_divergence=divergence,
                    final=final[index], steps=steps))
            transitions = []
            for step in trace:
                changes = [
                    dict(row_id=row["row_id"], concept=row["concept"],
                         before=old, after=new)
                    for row, old, new in zip(rows, step["before"], step["after"])
                    if old != new]
                transitions.append(dict(
                    step=step["step"], stage=step["stage"], changes=changes,
                    corpus_states=step["after"][:len(rows)],
                    immutable380_states=step["after"][len(rows):candidate_offset]))
            results[name] = dict(
                order=sequence, counts=counts(rows, corpus), final=corpus,
                final_deltas=delta, candidates=lexical, transitions=transitions,
                composed_crosscheck=name in complete_names)
            by_id = dict(zip((row["row_id"] for row in rows), corpus))
            projected = [
                dict(record, outputs="|".join(by_id[record["row_id"]]))
                for record in baseline["records"]]
            legacy_projection = "".join(
                record["proto_norm"] + "\x1f"
                + "|".join(by_id[record["row_id"]]) + "\x1e"
                for record in selected_legacy)
            immutable = final[len(rows):candidate_offset]
            results[name]["population_checks"] = dict(
                evaluator_sha256=projection_sha256(projected, "fst_input"),
                lexical_sha256=projection_sha256(projected, "proto_norm"),
                active380_sha256=hashlib.sha256(legacy_projection.encode()).hexdigest(),
                active380_count=len(selected_legacy),
                immutable380_outputs=immutable,
                immutable380_delta_ids=[
                    row["row_id"] for row, old, new in zip(
                        selected_legacy, immutable_identity, immutable)
                    if old != new],
                immutable380_rejected=sum(not value for value in immutable),
                immutable380_ambiguous=sum(len(value) > 1 for value in immutable))
        component_results = {
            ident: dict(zip(COMPONENTS, batch_apply_down(
                bins["component:" + ident], list(COMPONENTS.values()))))
            for ident in (
                EARLY, "RSyllEarly", "RCompEarly", "RBroadEarly",
                "RFoot", "RSyll", LATE, "RLate", "OELHWeakRaising")}
        for rule, controls in component_results.items():
            for name, outputs in controls.items():
                if len(outputs) > 1:
                    raise RuntimeError(
                        f"Nonfunctional component control: {rule}: {name}: {outputs}")
    after = protected_files(canonical)
    if before != after:
        changed = sorted(key for key in before.keys() | after.keys()
                         if before.get(key) != after.get(key))
        raise RuntimeError("Production files changed during experiment: " + repr(changed))
    early_step = next(step for step in reference_trace if step["stage"] == EARLY)
    grave_census = [
        dict(row_id=row["row_id"], concept=row["concept"],
             before=old, after=new)
        for row, old, new in zip(rows, early_step["before"], early_step["after"])
        if any("*ù" in value for value in old)]
    source = runtime.germanic_fst.read_text()
    facts = parse_defines(source)
    relevant = (
        EARLY, LINK, STRIP, "OELHWeakRaising", RAISE, "OESoulProxy",
        LATE, "OEStressFootContext", "EnglishProtoInput", "pgrmWord",
        "pgrmCompoundFirst", "pgrmCompoundSecond", "pgrmInputTailVowel")
    texts = {name: facts[name].body for name in relevant}
    for macro in ("FootCtx", "SentenceCtx", "Ctx"):
        match = re.search(
            r"(?m)^define " + macro + r"\(T\)([\s\S]*?);", source)
        texts[macro + "(T)"] = match.group(0)
    return dict(
        base_commit=BASE, source_sha256=digest(runtime.germanic_fst),
        corpus_sha256=digest(runtime.corpus_tsv), baseline=baseline,
        active_legacy380=selected_legacy,
        immutable_legacy380=legacy,
        immutable_legacy380_projection=projection_sha256(legacy, "proto_norm"),
        canonical_order=original, canonical_definition_text=texts,
        canonical_definition_sha256={
            name: hashlib.sha256(text.encode()).hexdigest() for name, text in texts.items()},
        definitions=definitions, candidates=CANDIDATES,
        component_inputs=COMPONENTS, components=component_results,
        grave_u_early_census=grave_census, rows=rows, models=results,
        runtime=dict(
            python=platform.python_version(),
            foma=subprocess.run(["foma", "-v"], capture_output=True, text=True).stdout.strip(),
            flookup=subprocess.run(["flookup", "-v"], capture_output=True, text=True).stdout.strip()),
        protected_before=before, protected_after=after,
        production_unchanged=True, identity_equal=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--functionality-only", action="store_true")
    args = parser.parse_args()
    report = check_functionality() if args.functionality_only else run()
    with args.output.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as compressed:
            compressed.write(json.dumps(
                report, ensure_ascii=False, sort_keys=True,
                separators=(",", ":")).encode())

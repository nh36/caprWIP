"""Current precedence diagnostics and commit-pinned superseded experiments."""
import json
from pathlib import Path
import subprocess
import sys
from dataclasses import replace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import executable_facts
import generate_registry_views as registry
import oe_pipeline
from capr_runtime import layout, run_in_runner
from sound_change_order_sensitivity import build_variant_appendix


ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT_COMMIT = "515b0f4b"


@pytest.mark.parametrize("relation,basis,direction,status", [
    ("one_sided_chronology", "stage_entailed", "later_boundary", "consistent"),
    ("one_sided_chronology", "independently_demonstrated", "earlier_boundary", "contradiction"),
    ("technical_computational", "technical", "earlier_boundary", "contradiction"),
    ("technical_computational", "boundary_observation", "earlier_boundary", "nonordering_observation"),
    ("superseded_experiment", "archived_experiment", "earlier_boundary", "superseded_experiment"),
    ("nonordering_observation", "boundary_observation", "earlier_boundary", "nonordering_observation"),
    ("one_sided_chronology", "stage_entailed", "", "invalid_direction"),
])
def test_direction_and_evidence_classes_are_not_conflated(relation, basis, direction, status):
    reg = [{"sc_id": "SC001", "fst_identifier": "A"},
           {"sc_id": "SC002", "fst_identifier": "B"}]
    stages = [oe_pipeline.Stage(1, "A", "Prelude", "named"),
              oe_pipeline.Stage(2, "B", "Rules", "named", cascade_position=1)]
    edge = dict(source_change_id="SC001", target_change_id="SC002",
                relation_type=relation, evidence_basis=basis, direction_basis=direction)
    observation = registry.chronology_order_observations(reg, [edge], stages=stages)[0]
    assert observation == dict(source_exec_index="1", target_exec_index="2", order_check=status)


def test_unavailable_and_ambiguous_endpoints_are_explicit():
    edge = dict(source_change_id="Unnumbered", target_change_id="Missing",
                relation_type="one_sided_chronology", evidence_basis="stage_entailed",
                direction_basis="later_boundary")
    stage = oe_pipeline.Stage(1, "Unnumbered", "Prelude", "named")
    assert registry.chronology_order_observations([], [edge], stages=[stage])[0][
        "order_check"] == "unavailable_endpoint"
    edge["target_change_id"] = "Unnumbered"
    assert registry.chronology_order_observations(
        [], [edge], stages=[stage, replace(stage, exec_index=2)])[0][
            "order_check"] == "ambiguous_endpoint"


def test_normal_registry_validation_rejects_an_inverted_current_claim():
    reg = registry.read_tsv(registry.SC_REGISTRY)
    edges = registry.read_tsv(registry.EDGE_REGISTRY)
    edge = next(e for e in edges if e["source_change_id"] == "SC072"
                and e["target_change_id"] == "SC040")
    edge["direction_basis"] = "earlier_boundary"
    errors = registry.validate_registry(reg, edges)
    assert any("SC072->SC040 contradiction" in error and "exec_index" in error
               and "Campbell" in error for error in errors)


def test_current_source_distinguishes_old_experiments_from_adopted_relations():
    edges = registry.read_tsv(registry.EDGE_REGISTRY)
    archived = [e for e in edges if e["relation_type"] == "superseded_experiment"]
    assert len(archived) == 4
    assert all(e["evidence_basis"] == "archived_experiment" for e in archived)
    assert not registry.validate_registry(registry.read_tsv(registry.SC_REGISTRY), edges)
    for e in edges:
        if {e["source_change_id"], e["target_change_id"]} == {"SC026", "SC027"}:
            assert e["relation_type"] == "technical_computational"
            assert e["evidence_basis"] == "technical"


@pytest.fixture(scope="module")
def chronology_replay(tmp_path_factory):
    """Only disposable container-local paths receive compiled assay networks."""
    old = subprocess.check_output(
        ["git", "show", f"{EXPERIMENT_COMMIT}:Germanic/fsts/germanic.txt"],
        cwd=ROOT, text=True)
    old_path = tmp_path_factory.mktemp("chronology_source") / "germanic.txt"
    old_path.write_text(old)
    order = oe_pipeline.composition_members_of("EnglishProtoToOE", old_path)
    after_shortening = list(order)
    after_shortening.remove("OEMedUnstressedULowering")
    after_shortening.insert(
        after_shortening.index("OEUnstressedLongVowelShortening") + 1,
        "OEMedUnstressedULowering")
    after_lowering = list(order)
    after_lowering.remove("OEWsPalatalGlide")
    after_lowering.insert(after_lowering.index("NWGmcULowering") + 1, "OEWsPalatalGlide")
    variants = {"old_identity": order, "old_delayed_lowering": after_shortening,
                "old_delayed_glide": after_lowering}
    appendix = ""
    for i, (name, sequence) in enumerate(variants.items()):
        appendix += build_variant_appendix(sequence, old_path).replace(
            "Variant", f"V{i}").replace("old_english_variant.bin", f"{name}.bin")
    repaired = [name for name in after_shortening if name != "OEWsPalatalGlide"]
    appendix += "\n" + executable_facts.definition_raw("OEWsPalatalGlide") + "\n"
    appendix += build_variant_appendix(repaired, old_path).replace(
        "Variant", "V3").replace(
            "old_english_variant.bin", "repaired_glide.bin").replace(
                ".o. OEGlideUToEO", ".o. OEWsPalatalGlide")

    stages = oe_pipeline.stages()
    current_variants = {"current_identity": stages}
    earlier = [s for s in stages if s.foma_identifier != "OEMedUnstressedULowering"]
    lowering = next(s for s in stages if s.foma_identifier == "OEMedUnstressedULowering")
    destination = next(i for i, s in enumerate(earlier)
                       if s.foma_identifier == "OEUnstressedLongVowelShortening")
    earlier.insert(destination, lowering)
    current_variants["current_earlier_lowering"] = earlier
    current_variants["current_without_glide"] = [
        s for s in stages if s.foma_identifier != "OEWsPalatalGlide"]
    before_umlaut = [s for s in stages if s.foma_identifier != "OEMedUnstressedULowering"]
    destination = next(i for i, s in enumerate(before_umlaut)
                       if s.foma_identifier == "OEWICombinativeUUmlaut")
    before_umlaut.insert(destination, lowering)
    current_variants["current_before_umlaut"] = before_umlaut
    delayed_umlaut = [s for s in stages if s.foma_identifier != "OEWICombinativeUUmlaut"]
    umlaut = next(s for s in stages if s.foma_identifier == "OEWICombinativeUUmlaut")
    destination = next(i for i, s in enumerate(delayed_umlaut)
                       if s.foma_identifier == "OEMedUnstressedULowering")
    delayed_umlaut.insert(destination + 1, umlaut)
    current_variants["current_delayed_umlaut"] = delayed_umlaut
    current_appendix = ""
    for i, (name, sequence) in enumerate(current_variants.items()):
        members = [s.foma_identifier if s.kind == "named" else s.inline_text
                   for s in sequence]
        current_appendix += (
            f"\ndefine A{i} " + " .o. ".join(members) +
            f";\nclear stack\nregex A{i};\nsave stack {name}.bin\n")
    rows = [r for r in oe_pipeline.load_rows(layout().corpus_tsv)
            if r["concept"] in {"yoke", "youth", "widow", "world"}]
    payload = {"old": old + appendix, "current_appendix": current_appendix,
               "old_names": list(variants) + ["repaired_glide"],
               "current_names": list(current_variants), "rows": rows}
    script = """
import json, subprocess, tempfile
from pathlib import Path
import sys
sys.path.insert(0, '/usr/app/tools')
from oe_pipeline import apply_down, evaluation_input
payload = PAYLOAD
result = {}
with tempfile.TemporaryDirectory(prefix='capr_chronology_') as temporary:
    root = Path(temporary)
    for model in ('old', 'current'):
        source = (payload['old'] if model == 'old' else
                  Path('/usr/app/fsts/germanic.txt').read_text() +
                  payload['current_appendix'])
        path = root / (model + '.foma')
        path.write_text(source)
        proc = subprocess.run(['foma', '-q', '-f', str(path), '-e', 'quit'],
                              cwd=root, text=True, capture_output=True,
                              timeout=1800)
        if proc.returncode:
            raise RuntimeError(model + ': foma failed\\n' + proc.stdout[-6000:] + proc.stderr)
        for name in payload[model + '_names']:
            binary = root / (name + '.bin')
            if not binary.is_file() or binary.stat().st_size < 1000:
                raise RuntimeError(name + ': compilation failed\\n' + proc.stdout + proc.stderr)
            result[name] = {
                row['concept']: apply_down(binary, row['proto_norm'] if model == 'old'
                                            else evaluation_input(row))
                for row in payload['rows']}
print(json.dumps(result, ensure_ascii=False))
""".replace("PAYLOAD", repr(payload))
    proc = run_in_runner("python3 -", input=script, text=True, capture_output=True,
                         check=True, timeout=3900)
    (old_path.parent / "replay.json").write_text(proc.stdout)
    return json.loads(proc.stdout)


@pytest.mark.runtime
def test_original_displacement_is_contingent_on_the_retired_early_glide(chronology_replay):
    result = chronology_replay
    assert result["old_identity"]["yoke"] == ["ġeoc"]
    assert result["old_delayed_glide"]["yoke"] == ["ġoc"]
    assert result["old_identity"]["youth"] == ["ġeoguþ"]
    assert result["old_delayed_lowering"]["youth"] == ["ġeogoþ"]
    assert result["repaired_glide"]["youth"] == ["ġeoguþ"]
    assert result["repaired_glide"]["yoke"] == ["ġeoc"]


@pytest.mark.runtime
def test_current_lowering_displacement_and_written_surface_controls(chronology_replay):
    result = chronology_replay
    for name in ("current_identity", "current_earlier_lowering"):
        for concept, output in {"yoke": "ġeoc", "youth": "ġeoguþ",
                                "widow": "wuduwe", "world": "weorold"}.items():
            assert result[name][concept] == [output], (name, concept, result[name])
    assert result["current_without_glide"]["yoke"] == ["ġoc"]
    assert result["current_without_glide"]["youth"] == ["ġuguþ"]
    for concept in ("widow", "world"):
        assert result["current_without_glide"][concept] == result["current_identity"][concept]
    assert result["current_before_umlaut"]["widow"] == ["wuduwe"]
    assert result["current_before_umlaut"]["world"] == ["weorald"]
    assert result["current_delayed_umlaut"]["widow"] == ["wudowe"]
    assert result["current_delayed_umlaut"]["world"] == ["weorold"]

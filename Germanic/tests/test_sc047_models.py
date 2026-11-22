import gzip
import json
from pathlib import Path

import pytest

import sc047_models as models
from oe_pipeline import stages


def test_active_models_share_one_inventory_and_differ_only_in_nasal_loss_order():
    plan = json.loads(models.PLAN.read_text(encoding="utf-8"))
    orders = models.model_orders([stage.foma_identifier for stage in stages()], plan)
    assert set(orders) == {"A", "B2"}
    for order in orders.values():
        shared = [models.LOWER, models.LENGTHEN, models.RAISE, models.Z_LOSS, models.ORAL, models.GEM]
        assert [order.index(stage) for stage in shared] == sorted(order.index(stage) for stage in shared)
    assert orders["A"].index(models.NASAL) < orders["A"].index(models.GEM)
    assert orders["B2"].index(models.NASAL) > orders["B2"].index(models.GEM)
    assert [stage for stage in orders["A"] if stage not in (models.NASAL, "FNG")] == [
        stage for stage in orders["B2"] if stage not in (models.NASAL, "FNG")]


def test_only_attested_cells_overlay_the_same_394_diagnostic_rows():
    with gzip.open(models.FROZEN, "rt", encoding="utf-8") as stream:
        rows = json.load(stream)["corpus"]
    cells = models.read_cells()
    a = {key: value for key, value in models.selections(rows, cells, "A").items() if value}
    b2 = {key: value for key, value in models.selections(rows, cells, "B2").items() if value}
    assert set(a) == {"2069", "2138", "2152", "2332"}
    assert set(b2) == {*a, "2061"}
    assert a["2138"]["selected_cell"] == "dat.sg" and a["2138"]["selected_target"] == "nette"
    assert a["2332"]["selected_cell"] == "gen.sg" and a["2332"]["selected_target"] == "hīewes"
    assert b2["2138"]["selected_cell"] == "acc.sg" and b2["2138"]["selected_target"] == "nett"
    assert b2["2332"]["selected_target"] == "hīew"
    assert all(a[row_id] == b2[row_id] for row_id in ("2069", "2152"))
    with pytest.raises(ValueError, match="duplicate"):
        models.selections(rows, cells + [next(cell for cell in cells if cell["selected_in"] == "A")], "A")


def test_recorded_active_build_preserves_controls_and_separates_inherited_and_selected_cells():
    capture = models.CELLS.parent / "captures" / f"{models.VERSION}.json.gz"
    with gzip.open(capture, "rt", encoding="utf-8") as stream:
        observations = json.load(stream)
    assert observations["runner_sha256"] == models.sha(Path(models.__file__))
    assert observations["cells_sha256"] == models.sha(models.CELLS)
    assert set(observations["models"]) == {"A", "B2"}
    inherited_mismatches = {"1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"}
    expected_diagnostics = {
        "A": {"2061": ["hei"], "2069": ["heġe"], "2138": ["nete"], "2332": ["hī"]},
        "B2": {"2069": ["heġe"]},
    }
    for model, result in observations["models"].items():
        rows = {row["row_id"]: row for row in result["corpus"]}
        assert len(rows) == len(result["corpus"]) == 394
        assert {key: row["diagnostic_outputs"] for key, row in rows.items()
                if row["diagnostic_outputs"] != row["canonical_outputs"]} == expected_diagnostics[model]
        assert {key for key, row in rows.items() if row["selected_target"] not in
                row["selected_outputs"]} == inherited_mismatches | ({"2061"} if model == "A" else set())
        assert rows["2138"]["selected_outputs"] == (["nette"] if model == "A" else ["nett"])
        assert rows["2332"]["selected_outputs"] == (["hīewes"] if model == "A" else ["hīew"])

        def firing_set(trace):
            return {key for key, row in rows.items() if models.LOWER in dict(row[trace])}

        assert len(firing_set("canonical_trace")) == 40
        assert firing_set("diagnostic_trace") == firing_set("canonical_trace")
        before_lengthening = set(result["order"][:result["order"].index(models.LENGTHEN)])
        door = [outputs for stage, outputs in rows["1992"]["diagnostic_trace"]
                if stage in before_lengthening]
        assert door[-1] == ["*d*ó*r*ą"]
        for key, outputs in {"1992": ["dor"], "2333": ["þǣr"], "2334": ["hwǣr"]}.items():
            assert rows[key]["diagnostic_outputs"] == outputs
            assert (models.LENGTHEN in dict(rows[key]["diagnostic_trace"])) == (key != "1992")

        probes = {(cell["lexeme"], cell["cell"]): cell for cell in result["paradigms"]}
        for lexeme, expected in {"rest": ("ræste", "rasta"), "gift": ("ġiefe", "ġiefa"),
                                 "wool": ("wolle", "wolla"), "love": ("lofe", "lofa")}.items():
            gen = probes[lexeme, "gen.sg.bimoric"]
            dat = probes[lexeme, "dat.sg"]
            assert gen["outputs"] == dat["outputs"] == [expected[0]]
            assert models.RAISE not in dict(gen["trace"])
            assert models.DAT_MONO in dict(dat["trace"])
            assert probes[lexeme, "gen.sg.trimoric"]["outputs"] == [expected[1]]
            assert probes[lexeme, "inst.pl"]["outputs"]
        assert [models.DAT_MONO in dict(probe["trace"]) for probe in result["queries"]] == [True, False]

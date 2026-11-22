import gzip
import json

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

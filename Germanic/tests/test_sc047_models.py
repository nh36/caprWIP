import csv
import gzip
import json
from pathlib import Path
import runpy

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
    assert observations["runner_sha256"] == (
        "09a23d65b4c3f87e86c8dc67d1384b6e21a9523fda572e9768fa2f1457a7a201")
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


def test_light_neuter_paradigms_distinguish_loss_gemination_and_simplification():
    capture = models.CELLS.parent / "captures" / f"{models.VERSION}.json.gz"
    with gzip.open(capture, "rt", encoding="utf-8") as stream:
        results = json.load(stream)["models"]

    for model, result in results.items():
        probes = {(cell["lexeme"], cell["cell"]): cell for cell in result["paradigms"]}
        for lexeme, stem, consonant, a, b2, dat, gen in (
            ("net", "*n*á*t", "t", "nete", "nett", "nette", "nettes"),
            ("bed", "*b*á*d", "d", "bede", "bedd", "bedde", "beddes"),
            ("pledge", "*w*á*d", "d", "wede", "wedd", "wedde", "weddes"),
            ("kin", "*k*ú*n", "n", "cyne", "cyn", "cynne", "cynnes"),
        ):
            doubled = f"{stem}*{consonant}*j"
            for label in ("nom.sg", "acc.sg"):
                probe = probes[lexeme, label]
                trace = probe["trace"]
                assert probe["outputs"] == [a if model == "A" else b2]
                if model == "A":
                    assert trace[1:3] == [[models.NASAL, [f"{stem}*j"]],
                                          ["FNG", [f"{stem}*i"]]]
                    assert models.GEM not in dict(trace)
                else:
                    assert trace[1:3] == [[models.GEM, [f"{doubled}*ą"]],
                                          [models.NASAL, [doubled]]]
            for label, output, ending in (("dat.sg", dat, "*ē"), ("gen.sg", gen, "*a*s")):
                probe = probes[lexeme, label]
                assert probe["outputs"] == [output]
                assert dict(probe["trace"])[models.GEM] == [doubled + ending]

        kin = dict(probes["kin", "nom.sg"]["trace"])
        if model == "B2":
            assert kin["OEHighVowelApocope"] == ["*k*y*n*n"]
            assert kin["OEFinalGeminateSimplification"] == ["*k*y*n"]
        else:
            assert "OEFinalGeminateSimplification" not in kin

        for lexeme, output in (("retainer", "seġe"), ("end", "ende")):
            probe = probes[lexeme, "nom.sg"]
            trace = dict(probe["trace"])
            assert probe["outputs"] == [output]
            assert models.ORAL in trace and models.GEM not in trace
        assert dict(probes["retainer", "gen.sg"]["trace"])[models.GEM] == ["*s*á*g*g*j*a*s"]
        assert probes["searu", "direct"]["outputs"] == ["saru"]
        assert probes["searu", "gen.sg"]["outputs"] == ["searwes"]


def test_supplemental_capture_preserves_the_benchmark_and_records_new_probes():
    captures = models.CELLS.parent / "captures"
    with gzip.open(captures / f"{models.VERSION}.json.gz", "rt", encoding="utf-8") as stream:
        baseline = json.load(stream)
    with gzip.open(captures / "sc047-lexical-expansion-v1.json.gz", "rt", encoding="utf-8") as stream:
        expanded = json.load(stream)
    assert {k: v for k, v in expanded.items() if k != "models"} == {
        k: v for k, v in baseline.items() if k != "models"}
    assert expanded["models"].keys() == baseline["models"].keys()
    for model, result in expanded["models"].items():
        previous = baseline["models"][model]
        for key in ("order", "corpus", "paradigms"):
            assert result[key] == previous[key]
        assert result["queries"][:2] == previous["queries"]
        probes = {probe["input"]: probe for probe in result["queries"][2:]}
        assert probes["bádjamiz"]["outputs"] == ["beddum"]
        assert probes["bázjas"]["outputs"] == ["berġes"]
        assert models.GEM not in dict(probes["bázjas"]["trace"])
        assert probes["fánją"]["outputs"] == (["fene"] if model == "A" else ["fen"])
        assert probes["fánjai"]["outputs"] == ["fenne"]
        direct = probes["wígją"]
        trace = dict(direct["trace"])
        if model == "A":
            assert direct["outputs"] == ["wiġe"]
            assert models.GEM not in trace
            assert trace["OEVelarPalatalization"] == ["*w*í*ʝ*i"]
        else:
            assert direct["outputs"] == ["wiġġ"]
            assert trace[models.GEM] == ["*w*í*g*g*j*ą"]
            assert trace["OEVelarPalatalization"] == ["*w*í*ʤ*ʤ*i"]
        protected = dict(probes["wígjai"]["trace"])
        assert protected[models.GEM] == ["*w*í*g*g*j*ē"]
        assert protected["OEVelarPalatalization"] == ["*w*í*ʤ*ʤ*j*ē"]
        assert probes["wígjô"]["outputs"] == ["wiġġa"]


def test_publisher_keeps_expansion_proposals_outside_scored_catalogues(tmp_path):
    source = models.CELLS.parent
    with gzip.open(source / "captures" / f"{models.VERSION}.json.gz", "rt", encoding="utf-8") as stream:
        result = json.load(stream)
    runpy.run_path(str(source / "publish.py"))["publish"](result, tmp_path)
    for model, expected in {
        "A": [("sc047-bed", "dat.sg", "bedde"), ("sc047-kin", "gen.sg", "cynnes")],
        "B2": [("sc047-bed", "acc.sg", "bedd"), ("sc047-kin", "nom.sg", "cyn")],
    }.items():
        with (tmp_path / f"{model}-expansions.tsv").open(encoding="utf-8") as stream:
            assert [(r["id"], r["cell"], r["target"])
                    for r in csv.DictReader(stream, delimiter="\t")] == expected
    summary = json.loads((tmp_path / "summary.json").read_text(encoding="utf-8"))
    assert [(summary[m]["matches"], summary[m]["selected_slots"]) for m in ("A", "B2")] == [
        (385, 393), (386, 394)]


def test_active_corpus_uses_source_supported_common_cells():
    from oe_pipeline import load_rows

    rows = load_rows(models.ROOT / "data/germanic-aligned-final.tsv")
    by_id = {row["row_id"]: row for row in rows}
    assert len(rows) == len(by_id) == 396
    assert {row_id: (by_id[row_id]["fst_input"], by_id[row_id]["counterpart"])
            for row_id in ("1988", "2061", "2069", "2138", "2152", "2332", "2340", "2341")} == {
        "1988": ("déuzô", "dēora"), "2061": ("xáwją", "hīeġ"),
        "2069": ("xágjō", "heġġ"), "2138": ("nátjai", "nette"),
        "2152": ("rástǭ", "ræste"), "2332": ("xíwjas", "hīewes"),
        "2340": ("bádjai", "bedde"), "2341": ("kúnjas", "cynnes"),
    }
    assert {"pledge", "fen", "wicg"}.isdisjoint(row["concept"] for row in rows)


def test_adoption_capture_is_bound_to_active_source_and_preserves_historical_controls():
    from oe_pipeline import load_rows

    active_source = models.ROOT / "data/germanic-aligned-final.tsv"
    capture_dir = models.CELLS.parent / "captures"
    with gzip.open(capture_dir / "sc047-adoption-v1.json.gz", "rt", encoding="utf-8") as stream:
        result = json.load(stream)
    with gzip.open(capture_dir / "sc047-lexical-expansion-v1.json.gz", "rt", encoding="utf-8") as stream:
        reference = json.load(stream)
    assert result["runner_sha256"] == models.sha(Path(models.__file__))
    assert result["corpus_sha256"] == models.sha(active_source)
    assert result["fst_sha256"] == models.sha(models.ROOT / "fsts/germanic.txt")
    source = {row["row_id"]: row for row in load_rows(active_source)}
    shared = {"2069", "2138", "2152", "2332", "2340", "2341"}
    inherited = {"1973", "2013", "2030", "2162", "2224", "2240", "2298", "2300"}
    for model, value in result["models"].items():
        historical = reference["models"][model]
        for key in ("order", "paradigms", "queries"):
            assert value[key] == historical[key]
        assert {row["row_id"]: row for row in value["corpus"]} == {
            row["row_id"]: row for row in historical["corpus"]}
        active = {row["row_id"]: row for row in value["active_corpus"]}
        assert len(value["active_corpus"]) == len(active) == len(source)
        assert active.keys() == source.keys()
        assert {key for key, row in active.items() if row["counterpart"] not in row["outputs"]} == (
            inherited | ({"2061"} if model == "A" else set()))
        for key, row in source.items():
            assert all(active[key][field] == expected for field, expected in row.items())
        assert all(active[key]["outputs"] == [active[key]["counterpart"]] for key in shared)


def test_shared_book_indexes_admitted_entries_and_comparative_evidence():
    docs = models.ROOT / "docs"
    with (docs / "assembly/manifest_all_by_class.tsv").open(encoding="utf-8") as stream:
        manifest = list(csv.DictReader(stream, delimiter="\t"))
    book = (docs / "assembly/capr_book_draft_alpha_01.md").read_text(encoding="utf-8")
    for key, headword, target in (("2340", "bedd", "bedde"), ("2341", "cynn", "cynnes")):
        row, = [entry for entry in manifest if entry["row_id"] == key]
        assert row["counterpart"] == target
        dossier = models.ROOT.parent / row["model_entry_path"]
        assert dossier.with_name(dossier.name.replace(".model.md", ".source_ledger.md")).is_file()
        label = f"{row['lexical_item']} — OE"
        chapter, = [section for section in book.split("\n## ") if section.startswith(label)]
        assert headword in chapter.splitlines()[0]
        assert f"@\\iventry{{{target}}}" in chapter
    with (docs / "book/index_verborum_print_main.tsv").open(encoding="utf-8") as stream:
        entries = {(row["language"], row["form"], row["form_role"])
                   for row in csv.DictReader(stream, delimiter="\t")}
    assert {("oe", "bedde", "target_form"), ("oe", "cynnes", "target_form"),
            ("oe", "nette", "target_form"), ("oe", "hīewes", "target_form"),
            ("oe", "hīeġ", "target_form"), ("oe", "heġġ", "target_form"),
            ("oe", "ræste", "target_form"), ("oe", "hiewes", "comparison_form"),
            ("oe", "hege", "comparison_form"), ("pwgmc", "rástē", "comparison_form"),
            ("pgmc", "rástōz", "comparison_form"),
            ("oe", "bedd", "comparison_form"), ("oe", "cyn", "comparison_form"),
            ("ohg", "peti", "comparison_form"), ("os", "feni", "comparison_form"),
            ("ofris", "fennem", "comparison_form"),
            ("oe", "wicg", "comparison_form")} <= entries

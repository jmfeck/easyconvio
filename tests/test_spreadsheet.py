import os

import pytest

from easyconvio.spreadsheet import SpreadsheetFile

from .conftest import needs_openpyxl, needs_odfpy, needs_libreoffice


# --- CSV / TSV (stdlib only) ---


def test_read_csv(csv_sheet_path):
    sh = SpreadsheetFile(csv_sheet_path)
    assert sh.sheet_count == 1
    assert sh.sheet_names == ["Sheet1"]
    assert sh.row_count() == 3
    rows = sh.rows()
    assert rows[0] == ["a", "b", "c"]
    assert rows[1] == ["1", "2", "3"]


def test_read_tsv(tsv_path):
    sh = SpreadsheetFile(tsv_path)
    assert sh.row_count() == 3
    assert sh.rows()[0] == ["a", "b", "c"]


def test_csv_to_tsv(csv_sheet_path, tmp_path):
    sh = SpreadsheetFile(csv_sheet_path)
    out = str(tmp_path / "out.tsv")
    sh.to_tsv(out)
    text = open(out, encoding="utf-8").read()
    assert "a\tb\tc" in text
    assert "1\t2\t3" in text


def test_tsv_to_csv(tsv_path, tmp_path):
    sh = SpreadsheetFile(tsv_path)
    out = str(tmp_path / "out.csv")
    sh.to_csv(out)
    assert "a,b,c" in open(out, encoding="utf-8").read()


# --- XLSX (openpyxl) ---


@needs_openpyxl
def test_read_xlsx(xlsx_path):
    sh = SpreadsheetFile(xlsx_path)
    assert sh.sheet_count == 2
    assert "Sheet1" in sh.sheet_names
    assert "Summary" in sh.sheet_names
    assert sh.rows("Sheet1")[0] == ("a", "b", "c") or sh.rows("Sheet1")[0] == ["a", "b", "c"]


@needs_openpyxl
def test_xlsx_to_csv(xlsx_path, tmp_path):
    sh = SpreadsheetFile(xlsx_path)
    out = str(tmp_path / "out.csv")
    sh.to_csv(out)
    text = open(out, encoding="utf-8").read()
    assert "a,b,c" in text


@needs_openpyxl
def test_xlsx_round_trip(xlsx_path, tmp_path):
    sh = SpreadsheetFile(xlsx_path)
    out = str(tmp_path / "rt.xlsx")
    sh.to_xlsx(out)
    sh2 = SpreadsheetFile(out)
    assert sh2.sheet_names == sh.sheet_names


@needs_openpyxl
def test_csv_to_xlsx(csv_sheet_path, tmp_path):
    sh = SpreadsheetFile(csv_sheet_path)
    out = str(tmp_path / "out.xlsx")
    sh.to_xlsx(out)
    assert os.path.exists(out)
    sh2 = SpreadsheetFile(out)
    assert sh2.row_count() == 3


# --- ODS (odfpy) ---


@needs_odfpy
def test_read_ods(ods_path):
    sh = SpreadsheetFile(ods_path)
    assert "Data" in sh.sheet_names
    assert sh.row_count("Data") == 3


@needs_odfpy
def test_ods_to_csv(ods_path, tmp_path):
    sh = SpreadsheetFile(ods_path)
    out = str(tmp_path / "out.csv")
    sh.to_csv(out)
    text = open(out, encoding="utf-8").read()
    assert "a,b" in text


@needs_odfpy
def test_csv_to_ods(csv_sheet_path, tmp_path):
    sh = SpreadsheetFile(csv_sheet_path)
    out = str(tmp_path / "out.ods")
    sh.to_ods(out)
    sh2 = SpreadsheetFile(out)
    assert sh2.sheet_count >= 1


# --- XLS (LibreOffice writer) ---


@needs_openpyxl
@needs_libreoffice
def test_xlsx_to_xls(xlsx_path, tmp_path):
    sh = SpreadsheetFile(xlsx_path)
    out = str(tmp_path / "out.xls")
    sh.to_xls(out)
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


# --- sheet manipulation ---


@needs_openpyxl
def test_add_remove_rename_sheet(xlsx_path):
    sh = SpreadsheetFile(xlsx_path)
    sh.add_sheet("Extra", [["x"], ["y"]])
    assert "Extra" in sh.sheet_names
    sh.rename_sheet("Extra", "X")
    assert "X" in sh.sheet_names
    assert "Extra" not in sh.sheet_names
    sh.remove_sheet("X")
    assert "X" not in sh.sheet_names


def test_iter_rows(csv_sheet_path):
    sh = SpreadsheetFile(csv_sheet_path)
    rows = list(sh.iter_rows())
    assert len(rows) == 3
    assert rows[0] == ["a", "b", "c"]


def test_unsupported_format_raises(tmp_path):
    p = tmp_path / "data.unknown"
    p.write_text("x")
    with pytest.raises(ValueError, match="Unsupported"):
        SpreadsheetFile(str(p))


def test_to_generic(csv_sheet_path, tmp_path):
    sh = SpreadsheetFile(csv_sheet_path)
    out = str(tmp_path / "g.tsv")
    sh.to("tsv", out)
    assert os.path.exists(out)

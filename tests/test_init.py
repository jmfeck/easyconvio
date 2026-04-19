"""Test that the lazy reader functions return the right class for every claimed format."""
import pytest

import easyconvio as ec
from easyconvio.archive import ArchiveFile
from easyconvio.document import DocumentFile
from easyconvio.ebook import EbookFile


# --- readers that touch real files we can build cheaply with stdlib alone ---


def test_read_jpg(jpg_path):
    f = ec.read_jpg(jpg_path)
    assert f.format == "jpg"


def test_read_png(png_path):
    f = ec.read_png(png_path)
    assert f.format == "png"


def test_read_zip(zip_path):
    f = ec.read_zip(zip_path)
    assert isinstance(f, ArchiveFile)
    assert f.file_count == 3


def test_read_jar(zip_path, tmp_path):
    """JAR uses the zip codec — rename a zip to .jar and read it."""
    import shutil
    jar = tmp_path / "lib.jar"
    shutil.copy(zip_path, jar)
    f = ec.read_jar(str(jar))
    assert isinstance(f, ArchiveFile)
    assert f.file_count == 3


def test_read_csv_routes_to_spreadsheet(csv_sheet_path):
    from easyconvio.spreadsheet import SpreadsheetFile
    f = ec.read_csv(csv_sheet_path)
    assert isinstance(f, SpreadsheetFile)


def test_read_md_routes_to_document(md_path):
    f = ec.read_md(md_path)
    assert isinstance(f, DocumentFile)
    assert f.format == "md"


# --- public surface ---


def test_all_readers_listed_are_callable():
    for name in ec.__all__:
        if name.startswith("read_"):
            attr = getattr(ec, name)
            assert callable(attr), f"{name} is not callable"


def test_dropped_formats_are_gone():
    """Formats we explicitly dropped should not be in the public API."""
    for dropped in ("read_ai", "read_cdr", "read_lrf", "read_pdb", "read_snb"):
        assert not hasattr(ec, dropped), f"{dropped} should have been removed"


def test_unknown_attribute_raises():
    with pytest.raises(AttributeError):
        ec.read_nonsense


# --- new format readers exist ---


@pytest.mark.parametrize(
    "name",
    [
        "read_heic", "read_heif",  # images
        "read_xlsx", "read_xls", "read_ods", "read_csv", "read_tsv",  # spreadsheets
        "read_jar",  # archives
        "read_pps", "read_ppsx",  # presentations
    ],
)
def test_new_readers_exposed(name):
    assert callable(getattr(ec, name))


def test_classes_lazy_loaded():
    """All file classes should be importable through the package root."""
    for cls_name in (
        "ImageFile", "AudioFile", "VideoFile", "DocumentFile", "EbookFile",
        "ArchiveFile", "PresentationFile", "SpreadsheetFile",
        "VectorFile", "FontFile", "CADFile",
    ):
        assert isinstance(getattr(ec, cls_name), type)

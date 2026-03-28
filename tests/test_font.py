import pytest
from unittest.mock import patch, MagicMock

from easyconvio.font import FontFile


@pytest.fixture
def font_file():
    mock_font = MagicMock()
    name_record_1 = MagicMock()
    name_record_1.nameID = 1
    name_record_1.toUnicode.return_value = "Roboto"
    name_record_2 = MagicMock()
    name_record_2.nameID = 2
    name_record_2.toUnicode.return_value = "Regular"

    mock_font.__getitem__ = MagicMock()
    mock_font["name"].names = [name_record_1, name_record_2]
    mock_font.getGlyphOrder.return_value = ["a"] * 100
    mock_font["head"].unitsPerEm = 1000

    with patch.object(FontFile, "_load"):
        f = FontFile("font.ttf")
        f._font = mock_font
    return f


def test_family_name(font_file):
    assert font_file.family_name == "Roboto"


def test_style(font_file):
    assert font_file.style == "Regular"


def test_glyph_count(font_file):
    assert font_file.glyph_count == 100


def test_units_per_em(font_file):
    assert font_file.units_per_em == 1000


def test_info(font_file):
    info = font_file.info()
    assert info["family_name"] == "Roboto"
    assert info["style"] == "Regular"
    assert info["glyph_count"] == 100
    assert info["units_per_em"] == 1000


def test_to_ttf(font_file, tmp_path):
    out = str(tmp_path / "out.ttf")
    result = font_file.to_ttf(out)
    assert result == out
    font_file._font.save.assert_called_once_with(out)


def test_to_woff2(font_file, tmp_path):
    out = str(tmp_path / "out.woff2")
    result = font_file.to_woff2(out)
    assert result == out
    assert font_file._font.flavor == "woff2"


def test_import_error():
    with patch.dict("sys.modules", {"fontTools": None, "fontTools.ttLib": None}):
        with pytest.raises(ImportError, match="fonttools"):
            FontFile("font.ttf")

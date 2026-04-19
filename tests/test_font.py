import os

import pytest

from easyconvio.font import FontFile

from .conftest import needs_fonttools

pytestmark = needs_fonttools


@pytest.fixture
def font_file(ttf_path):
    return FontFile(ttf_path)


def test_family_and_style(font_file):
    assert font_file.family_name == "Tiny"
    assert font_file.style == "Regular"


def test_glyph_count(font_file):
    assert font_file.glyph_count >= 3  # .notdef + A + B


def test_units_per_em(font_file):
    assert font_file.units_per_em == 1024


def test_info(font_file):
    info = font_file.info()
    assert info == {
        "family_name": "Tiny",
        "style": "Regular",
        "glyph_count": font_file.glyph_count,
        "units_per_em": 1024,
    }


def test_subset(font_file):
    font_file.subset("A")
    # subsetting should not raise; glyph count should be reduced
    assert font_file.glyph_count >= 1


@pytest.mark.parametrize(
    "method, ext, expected_flavor",
    [
        ("to_ttf", "ttf", None),
        ("to_otf", "otf", None),
        ("to_woff", "woff", "woff"),
        ("to_woff2", "woff2", "woff2"),
    ],
)
def test_export_format(font_file, tmp_path, method, ext, expected_flavor):
    out = str(tmp_path / f"out.{ext}")
    result = getattr(font_file, method)(out)
    assert result == out
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0
    # Re-open to confirm it's a valid font
    from fontTools.ttLib import TTFont
    TTFont(out)


def test_to_generic(font_file, tmp_path):
    out = str(tmp_path / "g.woff2")
    font_file.to("woff2", out)
    assert os.path.exists(out)

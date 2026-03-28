import os
import pytest
from unittest.mock import patch, MagicMock

from easyconvio.vector import VectorFile


@pytest.fixture
def svg_file(tmp_path):
    svg_path = tmp_path / "logo.svg"
    svg_path.write_text('<svg width="100" height="50"></svg>')
    return VectorFile(str(svg_path))


@pytest.fixture
def eps_file():
    with patch.object(VectorFile, "_load"):
        f = VectorFile("logo.eps")
        f._is_svg = False
    return f


def test_is_svg(svg_file):
    assert svg_file.is_svg is True


def test_non_svg(eps_file):
    assert eps_file.is_svg is False


def test_scale(svg_file):
    result = svg_file.scale(2.0)
    assert result is svg_file
    with open(svg_file.path) as f:
        content = f.read()
    assert 'width="200.0' in content
    assert 'height="100.0' in content


def test_scale_non_svg(eps_file):
    with pytest.raises(NotImplementedError, match="SVG"):
        eps_file.scale(2.0)


@patch("easyconvio.vector.VectorFile._cairosvg_convert")
def test_to_png_svg(mock_cairo, svg_file, tmp_path):
    out = str(tmp_path / "logo.png")
    mock_cairo.return_value = out
    result = svg_file.to_png(out)
    assert result == out
    mock_cairo.assert_called_once_with("svg2png", out)


@patch("easyconvio.vector.VectorFile._cairosvg_convert")
def test_to_pdf_svg(mock_cairo, svg_file, tmp_path):
    out = str(tmp_path / "logo.pdf")
    mock_cairo.return_value = out
    result = svg_file.to_pdf(out)
    assert result == out


def test_to_svg_copy(svg_file, tmp_path):
    out = str(tmp_path / "copy.svg")
    result = svg_file.to_svg(out)
    assert result == out
    assert os.path.exists(out)

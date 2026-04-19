import os

import pytest

from easyconvio.vector import VectorFile

from .conftest import needs_cairosvg, needs_inkscape


@pytest.fixture
def svg_file(svg_path):
    return VectorFile(svg_path)


def test_is_svg(svg_file):
    assert svg_file.is_svg is True
    assert svg_file.format == "svg"


def test_scale(svg_file):
    svg_file.scale(2.0)
    content = open(svg_file.path).read()
    assert 'width="200.0' in content
    assert 'height="100.0' in content


def test_to_svg_copy(svg_file, tmp_path):
    out = str(tmp_path / "copy.svg")
    result = svg_file.to_svg(out)
    assert result == out
    assert os.path.exists(out)
    assert "<svg" in open(out).read()


@needs_cairosvg
@pytest.mark.parametrize(
    "method, ext",
    [("to_png", "png"), ("to_pdf", "pdf"), ("to_eps", "eps")],
)
def test_cairosvg_export(svg_file, tmp_path, method, ext):
    out = str(tmp_path / f"out.{ext}")
    result = getattr(svg_file, method)(out)
    assert result == out
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


@needs_inkscape
@pytest.mark.parametrize(
    "method, ext",
    [("to_emf", "emf"), ("to_wmf", "wmf"), ("to_dxf", "dxf")],
)
def test_inkscape_export(svg_file, tmp_path, method, ext):
    out = str(tmp_path / f"out.{ext}")
    result = getattr(svg_file, method)(out)
    assert result == out
    assert os.path.exists(out)


def test_scale_only_for_svg(tmp_path):
    """Non-SVG files reject scale()."""
    eps_path = tmp_path / "fake.eps"
    eps_path.write_text("%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: 0 0 100 100\nshowpage\n")
    f = VectorFile(str(eps_path))
    assert not f.is_svg
    with pytest.raises(NotImplementedError):
        f.scale(2.0)

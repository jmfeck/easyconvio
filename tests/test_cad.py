import os

import pytest

from easyconvio.cad import CADFile

from .conftest import needs_ezdxf

pytestmark = needs_ezdxf


@pytest.fixture
def cad_file(dxf_path):
    return CADFile(dxf_path)


def test_layers(cad_file):
    layers = cad_file.layers
    assert "0" in layers
    assert "Walls" in layers


def test_list_layers(cad_file):
    assert cad_file.list_layers() == cad_file.layers


def test_entity_count(cad_file):
    assert cad_file.entity_count == 2  # one line, one circle


def test_to_dxf(cad_file, tmp_path):
    out = str(tmp_path / "out.dxf")
    result = cad_file.to_dxf(out)
    assert result == out
    assert os.path.exists(out)
    # round-trip
    again = CADFile(out)
    assert again.entity_count == 2


def _has_matplotlib():
    try:
        import matplotlib  # noqa: F401
        return True
    except ImportError:
        return False


needs_matplotlib = pytest.mark.skipif(
    not _has_matplotlib(), reason="matplotlib not installed"
)


@needs_matplotlib
@pytest.mark.parametrize(
    "method, ext",
    [("to_png", "png"), ("to_svg", "svg"), ("to_pdf", "pdf")],
)
def test_render_export(cad_file, tmp_path, method, ext):
    out = str(tmp_path / f"out.{ext}")
    result = getattr(cad_file, method)(out)
    assert result == out
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0

import os

import pytest

from easyconvio.presentation import PresentationFile

from .conftest import needs_python_pptx, needs_libreoffice

pytestmark = needs_python_pptx


@pytest.fixture
def pres_file(pptx_path):
    return PresentationFile(pptx_path)


def test_slide_count(pres_file):
    assert pres_file.slide_count == 2


def test_slide_dimensions(pres_file):
    assert pres_file.slide_width > 0
    assert pres_file.slide_height > 0


def test_extract_text(pres_file):
    texts = pres_file.extract_text()
    assert len(texts) == 2
    assert "Slide 1" in texts[0]


def test_extract_images_empty(pres_file, tmp_path):
    """Our fixture has no images — extraction returns empty list, not crash."""
    paths = pres_file.extract_images(str(tmp_path / "imgs"))
    assert paths == []


def test_remove_slide(pres_file, tmp_path):
    pres_file.remove_slide(0)
    assert pres_file.slide_count == 1


def test_to_pptx(pres_file, tmp_path):
    out = str(tmp_path / "out.pptx")
    pres_file.to_pptx(out)
    assert os.path.exists(out)
    PresentationFile(out)  # round-trip


def test_to_ppsx(pres_file, tmp_path):
    out = str(tmp_path / "out.ppsx")
    pres_file.to_ppsx(out)
    assert os.path.exists(out)
    # PPSX uses the same container as PPTX, so we can re-open it
    PresentationFile(out)


# --- LibreOffice-driven conversions ---


@needs_libreoffice
@pytest.mark.parametrize(
    "method, ext",
    [
        ("to_pdf", "pdf"),
        ("to_odp", "odp"),
        ("to_ppt", "ppt"),
        ("to_html", "html"),
        ("to_pps", "pps"),
    ],
)
def test_libreoffice_export(pres_file, tmp_path, method, ext):
    out = str(tmp_path / f"out.{ext}")
    result = getattr(pres_file, method)(out)
    assert result == out
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


@needs_libreoffice
def test_read_odp_via_libreoffice(pres_file, tmp_path):
    """Convert pptx → odp, then read it back through PresentationFile."""
    odp = str(tmp_path / "via.odp")
    pres_file.to_odp(odp)
    odp_pres = PresentationFile(odp)
    assert odp_pres.slide_count >= 1
    odp_pres.close()

import pytest
from unittest.mock import patch, MagicMock

from easyconvio.presentation import PresentationFile


@pytest.fixture
def pres_file():
    mock_prs = MagicMock()
    mock_prs.slides = [MagicMock(), MagicMock()]
    mock_prs.slide_width = 9144000
    mock_prs.slide_height = 6858000

    with patch("easyconvio.presentation.PresentationFile._load") as mock_load:
        f = PresentationFile("slides.pptx")
        f._prs = mock_prs
    return f


def test_slide_count(pres_file):
    assert pres_file.slide_count == 2


def test_slide_width(pres_file):
    assert pres_file.slide_width == 9144000


def test_slide_height(pres_file):
    assert pres_file.slide_height == 6858000


def test_extract_text(pres_file):
    shape = MagicMock()
    shape.has_text_frame = True
    paragraph = MagicMock()
    paragraph.text = "Hello"
    shape.text_frame.paragraphs = [paragraph]

    pres_file._prs.slides = [MagicMock()]
    pres_file._prs.slides[0].shapes = [shape]

    texts = pres_file.extract_text()
    assert texts == ["Hello"]


def test_to_pptx(pres_file, tmp_path):
    out = str(tmp_path / "out.pptx")
    result = pres_file.to_pptx(out)
    assert result == out
    pres_file._prs.save.assert_called_once_with(out)


def test_import_error():
    with patch.dict("sys.modules", {"pptx": None}):
        with patch("builtins.__import__", side_effect=ImportError):
            with pytest.raises(ImportError, match="python-pptx"):
                PresentationFile("slides.pptx")

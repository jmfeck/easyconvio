import os
import pytest
from unittest.mock import patch

from easyconvio.base import BaseFile


class ConcreteFile(BaseFile):
    def _load(self):
        pass


@patch.object(ConcreteFile, "_load")
def test_init_sets_path_and_format(mock_load):
    f = ConcreteFile("some/dir/file.TXT")
    assert f.path == os.path.abspath("some/dir/file.TXT")
    assert f.format == "txt"
    mock_load.assert_called_once()


@patch.object(ConcreteFile, "_load")
def test_output_path_default(mock_load):
    f = ConcreteFile("photo.jpg")
    result = f._output_path("png")
    expected = os.path.splitext(os.path.abspath("photo.jpg"))[0] + ".png"
    assert result == expected


@patch.object(ConcreteFile, "_load")
def test_output_path_explicit(mock_load):
    f = ConcreteFile("photo.jpg")
    result = f._output_path("png", "custom/output.png")
    assert result == "custom/output.png"


@patch.object(ConcreteFile, "_load")
def test_repr(mock_load):
    f = ConcreteFile("some/dir/report.docx")
    assert repr(f) == "<ConcreteFile 'report.docx' (docx)>"


@patch.object(ConcreteFile, "_load")
def test_to_delegates_to_method(mock_load):
    f = ConcreteFile("file.txt")
    f.to_pdf = lambda output_path=None: f"converted to {output_path}"
    result = f.to("pdf", "out.pdf")
    assert result == "converted to out.pdf"


@patch.object(ConcreteFile, "_load")
def test_to_unsupported_format(mock_load):
    f = ConcreteFile("file.txt")
    with pytest.raises(ValueError, match="Unsupported format"):
        f.to("xyz123")

import pytest
from unittest.mock import patch, MagicMock

from easyconvio.cad import CADFile


@pytest.fixture
def cad_file():
    mock_doc = MagicMock()
    layer1 = MagicMock()
    layer1.dxf.name = "0"
    layer2 = MagicMock()
    layer2.dxf.name = "Walls"
    mock_doc.layers = [layer1, layer2]
    mock_doc.modelspace.return_value = [MagicMock()] * 50

    with patch.object(CADFile, "_load"):
        f = CADFile("drawing.dxf")
        f._doc = mock_doc
    return f


def test_layers(cad_file):
    assert cad_file.layers == ["0", "Walls"]


def test_list_layers(cad_file):
    assert cad_file.list_layers() == ["0", "Walls"]


def test_entity_count(cad_file):
    assert cad_file.entity_count == 50


def test_to_dxf(cad_file, tmp_path):
    out = str(tmp_path / "out.dxf")
    result = cad_file.to_dxf(out)
    assert result == out
    cad_file._doc.saveas.assert_called_once_with(out)


@patch("easyconvio.cad.CADFile._load")
def test_import_error(mock_load):
    with patch.dict("sys.modules", {"ezdxf": None}):
        with pytest.raises(ImportError, match="ezdxf"):
            mock_load.side_effect = ImportError(
                "CADFile requires ezdxf. Install with: pip install easyconvio[cad]"
            )
            CADFile("drawing.dxf")

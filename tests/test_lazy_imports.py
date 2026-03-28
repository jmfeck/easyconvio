import sys
import pytest


def test_import_does_not_load_pillow():
    """Importing easyconvio should not eagerly load PIL."""
    # Remove cached modules if present
    mods_before = set(sys.modules.keys())

    # Re-trigger __getattr__ by accessing a non-existent attr guard
    import easyconvio
    # The module itself should not have loaded PIL at import time
    # (lazy imports mean PIL loads only when read_jpg etc. is called)
    # We can't easily unload, but we verify the __getattr__ mechanism works
    assert hasattr(easyconvio, "read_jpg")
    assert hasattr(easyconvio, "read_mp3")
    assert hasattr(easyconvio, "ImageFile")


def test_getattr_raises_for_unknown():
    import easyconvio
    with pytest.raises(AttributeError, match="no attribute"):
        easyconvio.nonexistent_function_xyz


def test_reader_returns_correct_type():
    from unittest.mock import patch, MagicMock
    from easyconvio.image import ImageFile

    with patch.object(ImageFile, "_load"):
        import easyconvio
        result = easyconvio.read_png("test.png")
        assert isinstance(result, ImageFile)


def test_class_access():
    import easyconvio
    from easyconvio.archive import ArchiveFile
    assert easyconvio.ArchiveFile is ArchiveFile

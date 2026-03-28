import os
import pytest
from unittest.mock import patch, MagicMock, PropertyMock
from PIL import Image

from easyconvio.image import ImageFile


@pytest.fixture
def img_file(tmp_path):
    path = tmp_path / "test.jpg"
    Image.new("RGB", (100, 50), color="red").save(str(path))
    return ImageFile(str(path))


def test_properties(img_file):
    assert img_file.size == (100, 50)
    assert img_file.width == 100
    assert img_file.height == 50
    assert img_file.mode == "RGB"


def test_resize(img_file):
    result = img_file.resize(200, 100)
    assert result is img_file
    assert img_file.size == (200, 100)


def test_crop(img_file):
    result = img_file.crop(10, 10, 50, 40)
    assert result is img_file
    assert img_file.size == (40, 30)


def test_rotate(img_file):
    result = img_file.rotate(90)
    assert result is img_file
    assert img_file.width == 50
    assert img_file.height == 100


def test_flip_horizontal(img_file):
    result = img_file.flip_horizontal()
    assert result is img_file
    assert img_file.size == (100, 50)


def test_flip_vertical(img_file):
    result = img_file.flip_vertical()
    assert result is img_file
    assert img_file.size == (100, 50)


def test_thumbnail(img_file):
    result = img_file.thumbnail(30, 30)
    assert result is img_file
    assert img_file.width <= 30
    assert img_file.height <= 30


def test_grayscale(img_file):
    result = img_file.grayscale()
    assert result is img_file
    assert img_file.mode == "L"


def test_brightness(img_file):
    result = img_file.brightness(1.5)
    assert result is img_file


def test_contrast(img_file):
    result = img_file.contrast(1.5)
    assert result is img_file


def test_sharpness(img_file):
    result = img_file.sharpness(2.0)
    assert result is img_file


def test_saturation(img_file):
    result = img_file.saturation(0.5)
    assert result is img_file


def test_invert(img_file):
    result = img_file.invert()
    assert result is img_file


def test_auto_contrast(img_file):
    result = img_file.auto_contrast()
    assert result is img_file


def test_equalize(img_file):
    result = img_file.equalize()
    assert result is img_file


def test_sepia(img_file):
    result = img_file.sepia()
    assert result is img_file
    assert img_file.mode == "RGB"


def test_opacity(img_file):
    result = img_file.opacity(0.5)
    assert result is img_file
    assert img_file.mode == "RGBA"


def test_blur(img_file):
    result = img_file.blur(radius=3)
    assert result is img_file


def test_add_border(img_file):
    result = img_file.add_border(10, color="blue")
    assert result is img_file
    assert img_file.width == 120
    assert img_file.height == 70


def test_paste(img_file, tmp_path):
    overlay_path = tmp_path / "overlay.png"
    Image.new("RGB", (20, 20), color="blue").save(str(overlay_path))
    result = img_file.paste(str(overlay_path), 5, 5)
    assert result is img_file


def test_to_png(img_file, tmp_path):
    out = str(tmp_path / "out.png")
    result = img_file.to_png(out)
    assert result == out
    assert os.path.exists(out)


def test_to_webp(img_file, tmp_path):
    out = str(tmp_path / "out.webp")
    result = img_file.to_webp(out)
    assert result == out
    assert os.path.exists(out)


def test_to_bmp(img_file, tmp_path):
    out = str(tmp_path / "out.bmp")
    result = img_file.to_bmp(out)
    assert result == out
    assert os.path.exists(out)


def test_to_generic(img_file, tmp_path):
    out = str(tmp_path / "out.tiff")
    result = img_file.to("tiff", out)
    assert result == out
    assert os.path.exists(out)


def test_save(img_file, tmp_path):
    out = str(tmp_path / "saved.jpg")
    result = img_file.save(out)
    assert result == out
    assert os.path.exists(out)


def test_chaining(img_file, tmp_path):
    out = str(tmp_path / "chained.png")
    result = img_file.resize(50, 25).grayscale().blur().to_png(out)
    assert os.path.exists(out)
    reopened = Image.open(out)
    assert reopened.size == (50, 25)

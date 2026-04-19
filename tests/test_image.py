import os

import pytest
from PIL import Image

from easyconvio.image import ImageFile

from .conftest import needs_pillow_heif


@pytest.fixture
def img_file(jpg_path):
    return ImageFile(jpg_path)


# --- properties / transforms (already covered, keep tight) ---


def test_properties(img_file):
    assert img_file.size == (120, 80)
    assert img_file.width == 120
    assert img_file.height == 80
    assert img_file.mode == "RGB"


def test_resize_crop_rotate(img_file):
    img_file.resize(60, 40)
    assert img_file.size == (60, 40)
    img_file.crop(0, 0, 30, 20)
    assert img_file.size == (30, 20)
    img_file.rotate(90)
    assert img_file.size == (20, 30)


def test_flip_thumbnail(img_file):
    img_file.flip_horizontal()
    img_file.flip_vertical()
    img_file.thumbnail(20, 20)
    assert img_file.width <= 20 and img_file.height <= 20


def test_color_ops(img_file):
    img_file.brightness(1.2).contrast(1.1).sharpness(1.5).saturation(0.8)
    img_file.auto_contrast().equalize().sepia()
    assert img_file.mode == "RGB"


def test_grayscale_invert(img_file):
    img_file.grayscale()
    assert img_file.mode == "L"
    img_file2 = ImageFile(img_file.path)
    img_file2.invert()


def test_opacity_makes_rgba(img_file):
    img_file.opacity(0.5)
    assert img_file.mode == "RGBA"


def test_blur_border_paste(img_file, tmp_path):
    overlay = tmp_path / "ov.png"
    Image.new("RGB", (10, 10), color="blue").save(overlay)
    img_file.blur(2).add_border(5, color="black").paste(str(overlay), 2, 2)


# --- exports — REAL files for every claimed format ---


@pytest.mark.parametrize(
    "method, ext",
    [
        ("to_jpg", "jpg"),
        ("to_png", "png"),
        ("to_gif", "gif"),
        ("to_bmp", "bmp"),
        ("to_tiff", "tiff"),
        ("to_webp", "webp"),
        ("to_ico", "ico"),
        ("to_tga", "tga"),
        ("to_ppm", "ppm"),
        ("to_pcx", "pcx"),
        ("to_dds", "dds"),
    ],
)
def test_export_format(img_file, tmp_path, method, ext):
    out = str(tmp_path / f"out.{ext}")
    result = getattr(img_file, method)(out)
    assert result == out
    assert os.path.exists(out)
    # Re-open to confirm the file is a valid image PIL can read
    Image.open(out).verify()


def test_to_generic(img_file, tmp_path):
    out = str(tmp_path / "out.tiff")
    result = img_file.to("tiff", out)
    assert result == out
    assert os.path.exists(out)


def test_save_default_path(img_file, tmp_path):
    out = str(tmp_path / "saved.jpg")
    img_file.save(out)
    assert os.path.exists(out)


def test_chaining(img_file, tmp_path):
    out = str(tmp_path / "chained.png")
    img_file.resize(50, 25).grayscale().blur().to_png(out)
    assert Image.open(out).size == (50, 25)


# --- HEIC/HEIF round-trip via pillow-heif ---


@needs_pillow_heif
def test_read_heic(heic_path):
    img = ImageFile(heic_path)
    assert img.size == (40, 30)
    assert img.format == "heic"


@needs_pillow_heif
def test_to_heic_to_heif(jpg_path, tmp_path):
    img = ImageFile(jpg_path)
    out_heic = str(tmp_path / "out.heic")
    out_heif = str(tmp_path / "out.heif")
    img.to_heic(out_heic)
    img.to_heif(out_heif)
    assert os.path.exists(out_heic)
    assert os.path.exists(out_heif)
    # Open back as ImageFile to confirm round-trip
    back = ImageFile(out_heic)
    assert back.size == (120, 80)


@needs_pillow_heif
def test_heic_chain_to_png(heic_path, tmp_path):
    out = str(tmp_path / "from_heic.png")
    ImageFile(heic_path).resize(20, 15).to_png(out)
    assert Image.open(out).size == (20, 15)

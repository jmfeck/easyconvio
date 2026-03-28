import os
import pytest
from PIL import Image
from pydub import AudioSegment

from easyconvio.image import ImageFile
from easyconvio.audio import AudioFile


def test_image_context_manager(tmp_path):
    path = tmp_path / "test.jpg"
    Image.new("RGB", (100, 50), color="red").save(str(path))

    with ImageFile(str(path)) as img:
        assert img.size == (100, 50)
        out = img.to_png(str(tmp_path / "out.png"))
    assert os.path.exists(out)


def test_audio_context_manager(tmp_path):
    path = tmp_path / "test.wav"
    AudioSegment.silent(duration=1000).export(str(path), format="wav")

    with AudioFile(str(path)) as audio:
        assert audio.duration == pytest.approx(1.0, abs=0.1)
        out = audio.to_wav(str(tmp_path / "out.wav"))
    assert os.path.exists(out)

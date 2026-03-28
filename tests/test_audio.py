import os
import pytest
from pydub import AudioSegment

from easyconvio.audio import AudioFile


@pytest.fixture
def audio_file(tmp_path):
    path = tmp_path / "test.wav"
    silence = AudioSegment.silent(duration=3000, frame_rate=44100)
    silence.export(str(path), format="wav")
    return AudioFile(str(path))


def test_properties(audio_file):
    assert audio_file.duration == pytest.approx(3.0, abs=0.1)
    assert audio_file.channels >= 1
    assert audio_file.sample_rate == 44100


def test_trim(audio_file):
    result = audio_file.trim(start=0.5, end=2.0)
    assert result is audio_file
    assert audio_file.duration == pytest.approx(1.5, abs=0.1)


def test_append(audio_file, tmp_path):
    other = tmp_path / "other.wav"
    AudioSegment.silent(duration=1000).export(str(other), format="wav")
    result = audio_file.append(str(other))
    assert result is audio_file
    assert audio_file.duration == pytest.approx(4.0, abs=0.1)


def test_overlay(audio_file, tmp_path):
    other = tmp_path / "other.wav"
    AudioSegment.silent(duration=1000).export(str(other), format="wav")
    result = audio_file.overlay(str(other), position=0.5)
    assert result is audio_file


def test_repeat(audio_file):
    result = audio_file.repeat(2)
    assert result is audio_file
    assert audio_file.duration == pytest.approx(6.0, abs=0.1)


def test_reverse(audio_file):
    result = audio_file.reverse()
    assert result is audio_file
    assert audio_file.duration == pytest.approx(3.0, abs=0.1)


def test_silence(audio_file):
    result = audio_file.silence(2)
    assert result is audio_file
    assert audio_file.duration == pytest.approx(5.0, abs=0.1)


def test_volume(audio_file):
    result = audio_file.volume(3)
    assert result is audio_file


def test_normalize(audio_file):
    result = audio_file.normalize()
    assert result is audio_file


def test_fade_in(audio_file):
    result = audio_file.fade_in(1)
    assert result is audio_file


def test_fade_out(audio_file):
    result = audio_file.fade_out(1)
    assert result is audio_file


def test_low_pass_filter(audio_file):
    result = audio_file.low_pass_filter(3000)
    assert result is audio_file


def test_high_pass_filter(audio_file):
    result = audio_file.high_pass_filter(200)
    assert result is audio_file


def test_set_channels(audio_file):
    result = audio_file.set_channels(1)
    assert result is audio_file
    assert audio_file.channels == 1


def test_set_frame_rate(audio_file):
    result = audio_file.set_frame_rate(22050)
    assert result is audio_file
    assert audio_file.sample_rate == 22050


def test_speed(audio_file):
    result = audio_file.speed(2.0)
    assert result is audio_file
    assert audio_file.duration == pytest.approx(1.5, abs=0.2)


def test_to_wav(audio_file, tmp_path):
    out = str(tmp_path / "out.wav")
    result = audio_file.to_wav(out)
    assert result == out
    assert os.path.exists(out)


def test_to_flac(audio_file, tmp_path):
    out = str(tmp_path / "out.flac")
    result = audio_file.to_flac(out)
    assert result == out
    assert os.path.exists(out)


def test_to_generic(audio_file, tmp_path):
    out = str(tmp_path / "out.wav")
    result = audio_file.to("wav", out)
    assert result == out
    assert os.path.exists(out)

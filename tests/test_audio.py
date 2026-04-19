import os

import pytest

from easyconvio.audio import AudioFile

from .conftest import needs_ffmpeg, needs_amr_encoder


@pytest.fixture
def audio_file(wav_path):
    return AudioFile(wav_path)


# --- properties ---


def test_properties(audio_file):
    assert audio_file.duration == pytest.approx(0.5, abs=0.1)
    assert audio_file.channels == 1
    assert audio_file.sample_rate == 16000


# --- editing ---


def test_trim(audio_file):
    audio_file.trim(start=0.1, end=0.4)
    assert audio_file.duration == pytest.approx(0.3, abs=0.05)


def test_append_overlay(audio_file, wav_path):
    audio_file.append(wav_path)
    assert audio_file.duration == pytest.approx(1.0, abs=0.1)
    audio_file.overlay(wav_path, position=0.1)


def test_repeat_reverse_silence(audio_file):
    base = audio_file.duration
    audio_file.repeat(2)
    assert audio_file.duration == pytest.approx(base * 2, abs=0.1)
    audio_file.reverse()
    audio_file.silence(0.2)


def test_volume_normalize_fade(audio_file):
    audio_file.volume(3).normalize().fade_in(0.1).fade_out(0.1)


def test_filters(audio_file):
    audio_file.low_pass_filter(3000).high_pass_filter(200)


def test_format_settings(audio_file):
    audio_file.set_channels(1).set_frame_rate(22050).set_sample_width(2)
    assert audio_file.sample_rate == 22050


def test_speed(audio_file):
    base = audio_file.duration
    audio_file.speed(2.0)
    assert audio_file.duration == pytest.approx(base / 2, abs=0.2)


# --- exports — REAL files for every claimed format ---


@pytest.mark.parametrize(
    "method, ext",
    [
        ("to_wav", "wav"),
        pytest.param("to_mp3", "mp3", marks=needs_ffmpeg),
        pytest.param("to_ogg", "ogg", marks=needs_ffmpeg),
        pytest.param("to_flac", "flac", marks=needs_ffmpeg),
        pytest.param("to_aac", "aac", marks=needs_ffmpeg),
        pytest.param("to_m4a", "m4a", marks=needs_ffmpeg),
        pytest.param("to_aiff", "aiff", marks=needs_ffmpeg),
        pytest.param("to_ac3", "ac3", marks=needs_ffmpeg),
        pytest.param("to_opus", "opus", marks=needs_ffmpeg),
        pytest.param("to_amr", "amr", marks=[needs_ffmpeg, needs_amr_encoder]),
        pytest.param("to_au", "au", marks=needs_ffmpeg),
        pytest.param("to_wma", "wma", marks=needs_ffmpeg),
    ],
)
def test_export_format(audio_file, tmp_path, method, ext):
    out = str(tmp_path / f"out.{ext}")
    result = getattr(audio_file, method)(out)
    assert result == out
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


def test_to_generic(audio_file, tmp_path):
    out = str(tmp_path / "out.wav")
    result = audio_file.to("wav", out)
    assert result == out
    assert os.path.exists(out)

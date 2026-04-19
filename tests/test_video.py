import os

import pytest

from easyconvio.video import VideoFile

from .conftest import needs_ffmpeg

pytestmark = needs_ffmpeg


@pytest.fixture
def video_file(mp4_path):
    f = VideoFile(mp4_path)
    yield f
    f.close()


# --- properties ---


def test_properties(video_file):
    assert video_file.duration == pytest.approx(1.0, abs=0.2)
    assert tuple(video_file.size) == (64, 48)
    assert video_file.width == 64
    assert video_file.height == 48
    assert video_file.fps == 10.0


def test_resize_returns_tuple(video_file):
    video_file.resize(32, 24)
    assert tuple(video_file.size) == (32, 24)


# --- editing ---


def test_clip(video_file):
    video_file.clip(0, 0.5)
    assert video_file.duration == pytest.approx(0.5, abs=0.2)


def test_resize(video_file):
    video_file.resize(32, 24)
    assert tuple(video_file.size) == (32, 24)


def test_crop(video_file):
    video_file.crop(0, 0, 32, 24)
    assert tuple(video_file.size) == (32, 24)


def test_speed_reverse_fps(video_file):
    video_file.speed(2.0)
    video_file.set_fps(5)
    assert video_file.fps == 5


def test_visual_effects(video_file):
    video_file.flip_horizontal().flip_vertical().grayscale().brightness(1.2)
    video_file.fade_in(0.1).fade_out(0.1)


def test_rotate(video_file):
    video_file.rotate(90)


def test_mute(video_file):
    video_file.mute()


# --- exports — REAL files ---


@pytest.mark.parametrize(
    "method, ext",
    [
        ("to_mp4", "mp4"),
        ("to_webm", "webm"),
        ("to_mov", "mov"),
        ("to_mkv", "mkv"),
        ("to_avi", "avi"),
        ("to_flv", "flv"),
        ("to_ogv", "ogv"),
        ("to_wmv", "wmv"),
        ("to_3gp", "3gp"),
        ("to_ts", "ts"),
        ("to_mpeg", "mpeg"),
        ("to_mpg", "mpg"),
    ],
)
def test_export_format(video_file, tmp_path, method, ext):
    out = str(tmp_path / f"out.{ext}")
    result = getattr(video_file, method)(out, logger=None)
    assert result == out
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


def test_to_generic(video_file, tmp_path):
    out = str(tmp_path / "g.mp4")
    video_file.to("mp4", out, logger=None)
    assert os.path.exists(out)


# --- extract / snapshot ---


def test_snapshot(video_file, tmp_path):
    out = str(tmp_path / "frame.png")
    video_file.snapshot(0.0, out)
    assert os.path.exists(out)
    from PIL import Image
    Image.open(out).verify()


def test_extract_audio_when_present(mp4_path, tmp_path):
    """Build a video WITH audio and extract it."""
    try:
        from moviepy import ColorClip, AudioArrayClip
    except ImportError:
        pytest.skip("moviepy variant without AudioArrayClip")
    import numpy as np
    rate = 16000
    samples = (0.3 * np.sin(2 * np.pi * 440 * np.arange(rate) / rate)).astype("float32")
    audio = AudioArrayClip(samples.reshape(-1, 1), fps=rate)
    audio.duration = 1.0
    clip = ColorClip(size=(32, 24), color=(0, 0, 255), duration=1.0).with_fps(10)
    clip = clip.with_audio(audio)
    src = str(tmp_path / "withaudio.mp4")
    clip.write_videofile(src, codec="libx264", audio_codec="aac", logger=None)
    clip.close()

    f = VideoFile(src)
    out = str(tmp_path / "audio.mp3")
    f.extract_audio(out)
    f.close()
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


def test_concatenate_loop(video_file, mp4_path):
    base = video_file.duration
    video_file.concatenate(mp4_path)
    assert video_file.duration == pytest.approx(base * 2, abs=0.3)


def test_context_manager(mp4_path):
    with VideoFile(mp4_path) as v:
        assert v.duration > 0

import pytest
from unittest.mock import patch, MagicMock

from easyconvio.video import VideoFile


@pytest.fixture
def video_file():
    mock_clip = MagicMock()
    mock_clip.duration = 120.0
    mock_clip.size = (1920, 1080)
    mock_clip.fps = 30.0

    with patch("easyconvio.video._require_ffmpeg"), \
         patch("easyconvio.video.VideoFileClip", return_value=mock_clip):
        f = VideoFile("clip.mp4")
    return f


def test_properties(video_file):
    assert video_file.duration == 120.0
    assert video_file.size == (1920, 1080)
    assert video_file.width == 1920
    assert video_file.height == 1080
    assert video_file.fps == 30.0


def test_clip(video_file):
    result = video_file.clip(0, 30)
    assert result is video_file


def test_resize(video_file):
    result = video_file.resize(1280, 720)
    assert result is video_file


def test_crop(video_file):
    result = video_file.crop(0, 0, 640, 360)
    assert result is video_file


def test_speed(video_file):
    result = video_file.speed(2.0)
    assert result is video_file


def test_reverse(video_file):
    result = video_file.reverse()
    assert result is video_file


def test_set_fps(video_file):
    result = video_file.set_fps(24)
    assert result is video_file


def test_rotate(video_file):
    result = video_file.rotate(90)
    assert result is video_file


def test_flip_horizontal(video_file):
    result = video_file.flip_horizontal()
    assert result is video_file


def test_flip_vertical(video_file):
    result = video_file.flip_vertical()
    assert result is video_file


def test_grayscale(video_file):
    result = video_file.grayscale()
    assert result is video_file


def test_brightness(video_file):
    result = video_file.brightness(1.3)
    assert result is video_file


def test_fade_in(video_file):
    result = video_file.fade_in(2)
    assert result is video_file


def test_fade_out(video_file):
    result = video_file.fade_out(2)
    assert result is video_file


def test_mute(video_file):
    result = video_file.mute()
    assert result is video_file


def test_volume(video_file):
    result = video_file.volume(0.5)
    assert result is video_file


@patch("easyconvio.video.AudioFileClip")
def test_add_audio(mock_audio_cls, video_file):
    result = video_file.add_audio("music.mp3")
    assert result is video_file
    mock_audio_cls.assert_called_once_with("music.mp3")


def test_close(video_file):
    video_file.close()
    video_file._clip.close.assert_called_once()


def test_context_manager(video_file):
    with video_file as v:
        assert v is video_file
    video_file._clip.close.assert_called_once()


@patch("easyconvio.video.concatenate_videoclips")
@patch("easyconvio.video.VideoFileClip")
def test_concatenate(mock_vfc, mock_concat, video_file):
    result = video_file.concatenate("clip2.mp4")
    assert result is video_file


@patch("easyconvio.video.concatenate_videoclips")
def test_loop(mock_concat, video_file):
    result = video_file.loop(3)
    assert result is video_file

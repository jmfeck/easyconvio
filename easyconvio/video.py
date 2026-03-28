from __future__ import annotations

import shutil
from typing import Optional, Any, Tuple

from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, vfx, afx

from .base import BaseFile


def _require_ffmpeg() -> None:
    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "ffmpeg not found. Install it from https://ffmpeg.org/download.html "
            "and make sure it is on your PATH."
        )


CODEC_MAP = {
    "mp4": "libx264",
    "avi": "png",
    "mov": "libx264",
    "mkv": "libx264",
    "webm": "libvpx",
    "flv": "flv",
    "ogv": "libtheora",
    "wmv": "wmv2",
    "3gp": "libx264",
    "ts": "mpeg2video",
    "mpeg": "mpeg2video",
    "mpg": "mpeg2video",
}


class VideoFile(BaseFile):
    """Video file with conversion and manipulation methods."""

    def _load(self) -> None:
        _require_ffmpeg()
        self._clip = VideoFileClip(self.path)

    def close(self) -> None:
        """Release the video clip resources."""
        self._clip.close()

    # --- Properties ---

    @property
    def duration(self) -> float:
        """Duration in seconds."""
        return self._clip.duration

    @property
    def size(self) -> Tuple[int, int]:
        """Width and height in pixels."""
        return self._clip.size

    @property
    def width(self) -> int:
        """Width in pixels."""
        return self._clip.size[0]

    @property
    def height(self) -> int:
        """Height in pixels."""
        return self._clip.size[1]

    @property
    def fps(self) -> float:
        """Frames per second."""
        return self._clip.fps

    # --- Editing ---

    def clip(self, start: float = 0, end: Optional[float] = None) -> VideoFile:
        """Trim to the given time range (in seconds)."""
        self._clip = self._clip.subclipped(start, end)
        return self

    def resize(self, width: int, height: int) -> VideoFile:
        """Resize to exact dimensions."""
        self._clip = self._clip.resized((width, height))
        return self

    def crop(self, x1: int, y1: int, x2: int, y2: int) -> VideoFile:
        """Crop to the given bounding box."""
        self._clip = self._clip.cropped(x1=x1, y1=y1, x2=x2, y2=y2)
        return self

    def concatenate(self, other_path: str) -> VideoFile:
        """Append another video file to the end."""
        other = VideoFileClip(other_path)
        self._clip = concatenate_videoclips([self._clip, other])
        return self

    def loop(self, n: int) -> VideoFile:
        """Loop the video n times."""
        self._clip = concatenate_videoclips([self._clip] * n)
        return self

    # --- Speed and time ---

    def speed(self, factor: float) -> VideoFile:
        """Change playback speed. >1 faster, <1 slower."""
        self._clip = self._clip.with_effects([vfx.MultiplySpeed(factor)])
        return self

    def reverse(self) -> VideoFile:
        """Reverse the video."""
        self._clip = self._clip.with_effects([vfx.TimeMirror()])
        return self

    def set_fps(self, fps: float) -> VideoFile:
        """Set the frames per second."""
        self._clip = self._clip.with_fps(fps)
        return self

    # --- Visual effects ---

    def rotate(self, degrees: float) -> VideoFile:
        """Rotate by the given degrees."""
        self._clip = self._clip.with_effects([vfx.Rotate(degrees)])
        return self

    def flip_horizontal(self) -> VideoFile:
        """Mirror horizontally."""
        self._clip = self._clip.with_effects([vfx.MirrorX()])
        return self

    def flip_vertical(self) -> VideoFile:
        """Mirror vertically."""
        self._clip = self._clip.with_effects([vfx.MirrorY()])
        return self

    def grayscale(self) -> VideoFile:
        """Convert to grayscale."""
        self._clip = self._clip.with_effects([vfx.BlackAndWhite()])
        return self

    def brightness(self, factor: float) -> VideoFile:
        """Adjust brightness. 1.0 = original."""
        self._clip = self._clip.with_effects([vfx.MultiplyColor(factor)])
        return self

    def fade_in(self, duration: float) -> VideoFile:
        """Apply a fade-in effect (duration in seconds)."""
        self._clip = self._clip.with_effects([vfx.FadeIn(duration)])
        return self

    def fade_out(self, duration: float) -> VideoFile:
        """Apply a fade-out effect (duration in seconds)."""
        self._clip = self._clip.with_effects([vfx.FadeOut(duration)])
        return self

    # --- Audio ---

    def mute(self) -> VideoFile:
        """Remove the audio track."""
        self._clip = self._clip.without_audio()
        return self

    def volume(self, factor: float) -> VideoFile:
        """Adjust audio volume. 1.0 = original."""
        self._clip = self._clip.with_effects([afx.MultiplyVolume(factor)])
        return self

    def add_audio(self, audio_path: str) -> VideoFile:
        """Replace the audio track with the given audio file."""
        audio = AudioFileClip(audio_path)
        self._clip = self._clip.with_audio(audio)
        return self

    def extract_audio(self, output_path: str) -> str:
        """Extract the audio track to a file."""
        self._clip.audio.write_audiofile(output_path)
        return output_path

    # --- Frame extraction ---

    def snapshot(self, time: float, output_path: str) -> str:
        """Save a single frame at the given time (in seconds) as an image."""
        self._clip.save_frame(output_path, t=time)
        return output_path

    # --- Export ---

    def _write_as(self, fmt: str, output_path: Optional[str] = None, **kwargs: Any) -> str:
        output_path = self._output_path(fmt, output_path)
        codec = kwargs.pop("codec", CODEC_MAP.get(fmt))
        if not codec:
            raise ValueError(f"Unsupported video format: {fmt}")
        self._clip.write_videofile(output_path, codec=codec, **kwargs)
        return output_path

    def to_mp4(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as MP4."""
        return self._write_as("mp4", output_path, **kwargs)

    def to_avi(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as AVI."""
        return self._write_as("avi", output_path, **kwargs)

    def to_mov(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as MOV."""
        return self._write_as("mov", output_path, **kwargs)

    def to_mkv(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as MKV."""
        return self._write_as("mkv", output_path, **kwargs)

    def to_webm(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as WebM."""
        return self._write_as("webm", output_path, **kwargs)

    def to_flv(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as FLV."""
        return self._write_as("flv", output_path, **kwargs)

    def to_ogv(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as OGV."""
        return self._write_as("ogv", output_path, **kwargs)

    def to_wmv(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as WMV."""
        return self._write_as("wmv", output_path, **kwargs)

    def to_3gp(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as 3GP."""
        return self._write_as("3gp", output_path, **kwargs)

    def to_ts(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as TS."""
        return self._write_as("ts", output_path, **kwargs)

    def to_mpeg(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as MPEG."""
        return self._write_as("mpeg", output_path, **kwargs)

    def to_mpg(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as MPG."""
        return self._write_as("mpg", output_path, **kwargs)

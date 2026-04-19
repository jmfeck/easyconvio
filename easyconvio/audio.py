from __future__ import annotations

from typing import Optional, Any

from pydub import AudioSegment
from pydub.effects import normalize as pydub_normalize

from .base import BaseFile


# pydub passes `format` straight through to ffmpeg's `-f` (muxer) flag.
# Some extensions don't match a muxer name and need an explicit codec too.
# The value is either a muxer string or a (muxer, codec) tuple.
PYDUB_FORMAT_MAP = {
    "mp3": "mp3",
    "wav": "wav",
    "ogg": "ogg",
    "flac": "flac",
    "aac": ("adts", "aac"),       # raw AAC stream
    "wma": ("asf", "wmav2"),      # WMA is asf-container with wmav2 codec
    "m4a": ("ipod", "aac"),       # m4a needs ipod muxer for proper container
    "aiff": "aiff",
    "ac3": "ac3",
    "opus": ("opus", "libopus"),
    "amr": ("amr", "libopencore_amrnb"),  # requires ffmpeg built with opencore
    "au": "au",
}


class AudioFile(BaseFile):
    """Audio file with conversion and manipulation methods."""

    def _load(self) -> None:
        self._audio = AudioSegment.from_file(self.path)

    # --- Properties ---

    @property
    def duration(self) -> float:
        """Duration in seconds."""
        return len(self._audio) / 1000.0

    @property
    def channels(self) -> int:
        """Number of audio channels."""
        return self._audio.channels

    @property
    def sample_rate(self) -> int:
        """Sample rate in Hz."""
        return self._audio.frame_rate

    @property
    def sample_width(self) -> int:
        """Sample width in bytes."""
        return self._audio.sample_width

    # --- Editing ---

    def trim(self, start: float = 0, end: Optional[float] = None) -> AudioFile:
        """Trim to the given time range (in seconds)."""
        start_ms = int(start * 1000)
        end_ms = int(end * 1000) if end else len(self._audio)
        self._audio = self._audio[start_ms:end_ms]
        return self

    def append(self, other_path: str) -> AudioFile:
        """Append another audio file to the end."""
        other = AudioSegment.from_file(other_path)
        self._audio = self._audio + other
        return self

    def overlay(self, other_path: str, position: float = 0) -> AudioFile:
        """Overlay another audio file at the given position (in seconds)."""
        other = AudioSegment.from_file(other_path)
        self._audio = self._audio.overlay(other, position=int(position * 1000))
        return self

    def repeat(self, n: int) -> AudioFile:
        """Repeat the audio n times."""
        self._audio = self._audio * n
        return self

    def reverse(self) -> AudioFile:
        """Reverse the audio."""
        self._audio = self._audio.reverse()
        return self

    def silence(self, duration: float) -> AudioFile:
        """Append silence of the given duration (in seconds)."""
        self._audio = self._audio + AudioSegment.silent(duration=int(duration * 1000))
        return self

    # --- Volume and effects ---

    def volume(self, db: float) -> AudioFile:
        """Adjust volume by the given amount in dB."""
        self._audio = self._audio + db
        return self

    def normalize(self) -> AudioFile:
        """Normalize volume to maximum without clipping."""
        self._audio = pydub_normalize(self._audio)
        return self

    def fade_in(self, duration: float) -> AudioFile:
        """Apply a fade-in effect (duration in seconds)."""
        self._audio = self._audio.fade_in(int(duration * 1000))
        return self

    def fade_out(self, duration: float) -> AudioFile:
        """Apply a fade-out effect (duration in seconds)."""
        self._audio = self._audio.fade_out(int(duration * 1000))
        return self

    def low_pass_filter(self, cutoff: int) -> AudioFile:
        """Apply a low-pass filter at the given cutoff frequency (Hz)."""
        self._audio = self._audio.low_pass_filter(cutoff)
        return self

    def high_pass_filter(self, cutoff: int) -> AudioFile:
        """Apply a high-pass filter at the given cutoff frequency (Hz)."""
        self._audio = self._audio.high_pass_filter(cutoff)
        return self

    # --- Format settings ---

    def set_channels(self, n: int) -> AudioFile:
        """Set the number of channels (1 = mono, 2 = stereo)."""
        self._audio = self._audio.set_channels(n)
        return self

    def set_frame_rate(self, rate: int) -> AudioFile:
        """Set the sample rate in Hz."""
        self._audio = self._audio.set_frame_rate(rate)
        return self

    def set_sample_width(self, width: int) -> AudioFile:
        """Set the sample width in bytes."""
        self._audio = self._audio.set_sample_width(width)
        return self

    def speed(self, factor: float) -> AudioFile:
        """Change playback speed. >1 faster, <1 slower."""
        new_rate = int(self._audio.frame_rate * factor)
        self._audio = self._audio._spawn(
            self._audio.raw_data,
            overrides={"frame_rate": new_rate},
        ).set_frame_rate(self._audio.frame_rate)
        return self

    # --- Export ---

    def _export_as(self, fmt: str, output_path: Optional[str] = None, **kwargs: Any) -> str:
        output_path = self._output_path(fmt, output_path)
        spec = PYDUB_FORMAT_MAP.get(fmt, fmt)
        # AMR requires narrowband: 8 kHz mono. Coerce in a temp segment so we
        # don't mutate the user's AudioFile.
        audio = self._audio
        if fmt == "amr":
            audio = audio.set_frame_rate(8000).set_channels(1)
        if isinstance(spec, tuple):
            muxer, codec = spec
            kwargs.setdefault("codec", codec)
            audio.export(output_path, format=muxer, **kwargs)
        else:
            audio.export(output_path, format=spec, **kwargs)
        return output_path

    def to_mp3(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as MP3."""
        return self._export_as("mp3", output_path, **kwargs)

    def to_wav(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as WAV."""
        return self._export_as("wav", output_path, **kwargs)

    def to_ogg(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as OGG."""
        return self._export_as("ogg", output_path, **kwargs)

    def to_flac(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as FLAC."""
        return self._export_as("flac", output_path, **kwargs)

    def to_aac(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as AAC."""
        return self._export_as("aac", output_path, **kwargs)

    def to_wma(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as WMA."""
        return self._export_as("wma", output_path, **kwargs)

    def to_m4a(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as M4A."""
        return self._export_as("m4a", output_path, **kwargs)

    def to_aiff(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as AIFF."""
        return self._export_as("aiff", output_path, **kwargs)

    def to_ac3(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as AC3."""
        return self._export_as("ac3", output_path, **kwargs)

    def to_opus(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as Opus."""
        return self._export_as("opus", output_path, **kwargs)

    def to_amr(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as AMR."""
        return self._export_as("amr", output_path, **kwargs)

    def to_au(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as AU."""
        return self._export_as("au", output_path, **kwargs)

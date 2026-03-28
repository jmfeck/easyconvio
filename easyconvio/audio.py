from pydub import AudioSegment
from pydub.effects import normalize as pydub_normalize

from .base import BaseFile


PYDUB_FORMAT_MAP = {
    "mp3": "mp3",
    "wav": "wav",
    "ogg": "ogg",
    "flac": "flac",
    "aac": "aac",
    "wma": "wma",
    "m4a": "mp4",
    "aiff": "aiff",
    "ac3": "ac3",
    "opus": "opus",
    "amr": "amr",
    "au": "au",
}


class AudioFile(BaseFile):
    """Audio file with conversion and manipulation methods."""

    def _load(self):
        self._audio = AudioSegment.from_file(self.path)

    # --- Properties ---

    @property
    def duration(self):
        """Duration in seconds."""
        return len(self._audio) / 1000.0

    @property
    def channels(self):
        return self._audio.channels

    @property
    def sample_rate(self):
        return self._audio.frame_rate

    @property
    def sample_width(self):
        return self._audio.sample_width

    # --- Editing ---

    def trim(self, start=0, end=None):
        start_ms = int(start * 1000)
        end_ms = int(end * 1000) if end else len(self._audio)
        self._audio = self._audio[start_ms:end_ms]
        return self

    def append(self, other_path):
        other = AudioSegment.from_file(other_path)
        self._audio = self._audio + other
        return self

    def overlay(self, other_path, position=0):
        other = AudioSegment.from_file(other_path)
        self._audio = self._audio.overlay(other, position=int(position * 1000))
        return self

    def repeat(self, n):
        self._audio = self._audio * n
        return self

    def reverse(self):
        self._audio = self._audio.reverse()
        return self

    def silence(self, duration):
        self._audio = self._audio + AudioSegment.silent(duration=int(duration * 1000))
        return self

    # --- Volume and effects ---

    def volume(self, db):
        self._audio = self._audio + db
        return self

    def normalize(self):
        self._audio = pydub_normalize(self._audio)
        return self

    def fade_in(self, duration):
        self._audio = self._audio.fade_in(int(duration * 1000))
        return self

    def fade_out(self, duration):
        self._audio = self._audio.fade_out(int(duration * 1000))
        return self

    def low_pass_filter(self, cutoff):
        self._audio = self._audio.low_pass_filter(cutoff)
        return self

    def high_pass_filter(self, cutoff):
        self._audio = self._audio.high_pass_filter(cutoff)
        return self

    # --- Format settings ---

    def set_channels(self, n):
        self._audio = self._audio.set_channels(n)
        return self

    def set_frame_rate(self, rate):
        self._audio = self._audio.set_frame_rate(rate)
        return self

    def set_sample_width(self, width):
        self._audio = self._audio.set_sample_width(width)
        return self

    def speed(self, factor):
        new_rate = int(self._audio.frame_rate * factor)
        self._audio = self._audio._spawn(
            self._audio.raw_data,
            overrides={"frame_rate": new_rate},
        ).set_frame_rate(self._audio.frame_rate)
        return self

    # --- Export ---

    def _export_as(self, fmt, output_path=None, **kwargs):
        output_path = self._output_path(fmt, output_path)
        pydub_fmt = PYDUB_FORMAT_MAP.get(fmt, fmt)
        self._audio.export(output_path, format=pydub_fmt, **kwargs)
        return output_path

    def to_mp3(self, output_path=None, **kwargs):
        return self._export_as("mp3", output_path, **kwargs)

    def to_wav(self, output_path=None, **kwargs):
        return self._export_as("wav", output_path, **kwargs)

    def to_ogg(self, output_path=None, **kwargs):
        return self._export_as("ogg", output_path, **kwargs)

    def to_flac(self, output_path=None, **kwargs):
        return self._export_as("flac", output_path, **kwargs)

    def to_aac(self, output_path=None, **kwargs):
        return self._export_as("aac", output_path, **kwargs)

    def to_wma(self, output_path=None, **kwargs):
        return self._export_as("wma", output_path, **kwargs)

    def to_m4a(self, output_path=None, **kwargs):
        return self._export_as("m4a", output_path, **kwargs)

    def to_aiff(self, output_path=None, **kwargs):
        return self._export_as("aiff", output_path, **kwargs)

    def to_ac3(self, output_path=None, **kwargs):
        return self._export_as("ac3", output_path, **kwargs)

    def to_opus(self, output_path=None, **kwargs):
        return self._export_as("opus", output_path, **kwargs)

    def to_amr(self, output_path=None, **kwargs):
        return self._export_as("amr", output_path, **kwargs)

    def to_au(self, output_path=None, **kwargs):
        return self._export_as("au", output_path, **kwargs)

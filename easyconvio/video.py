from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, afx

from .base import BaseFile


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

    def _load(self):
        self._clip = VideoFileClip(self.path)

    # --- Properties ---

    @property
    def duration(self):
        """Duration in seconds."""
        return self._clip.duration

    @property
    def size(self):
        return self._clip.size

    @property
    def width(self):
        return self._clip.size[0]

    @property
    def height(self):
        return self._clip.size[1]

    @property
    def fps(self):
        return self._clip.fps

    # --- Editing ---

    def clip(self, start=0, end=None):
        self._clip = self._clip.subclip(start, end)
        return self

    def resize(self, width, height):
        self._clip = self._clip.resize((width, height))
        return self

    def crop(self, x1, y1, x2, y2):
        self._clip = self._clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
        return self

    def concatenate(self, other_path):
        other = VideoFileClip(other_path)
        self._clip = concatenate_videoclips([self._clip, other])
        return self

    def loop(self, n):
        self._clip = concatenate_videoclips([self._clip] * n)
        return self

    # --- Speed and time ---

    def speed(self, factor):
        self._clip = self._clip.fx(vfx.speedx, factor)
        return self

    def reverse(self):
        self._clip = self._clip.fx(vfx.time_mirror)
        return self

    def set_fps(self, fps):
        self._clip = self._clip.set_fps(fps)
        return self

    # --- Visual effects ---

    def rotate(self, degrees):
        self._clip = self._clip.fx(vfx.rotate, degrees)
        return self

    def flip_horizontal(self):
        self._clip = self._clip.fx(vfx.mirror_x)
        return self

    def flip_vertical(self):
        self._clip = self._clip.fx(vfx.mirror_y)
        return self

    def grayscale(self):
        self._clip = self._clip.fx(vfx.blackwhite)
        return self

    def brightness(self, factor):
        self._clip = self._clip.fx(vfx.colorx, factor)
        return self

    def fade_in(self, duration):
        self._clip = self._clip.fx(vfx.fadein, duration)
        return self

    def fade_out(self, duration):
        self._clip = self._clip.fx(vfx.fadeout, duration)
        return self

    # --- Audio ---

    def mute(self):
        self._clip = self._clip.without_audio()
        return self

    def volume(self, factor):
        self._clip = self._clip.fx(afx.volumex, factor)
        return self

    def add_audio(self, audio_path):
        from moviepy.editor import AudioFileClip
        audio = AudioFileClip(audio_path)
        self._clip = self._clip.set_audio(audio)
        return self

    def extract_audio(self, output_path):
        self._clip.audio.write_audiofile(output_path)
        self._clip.close()
        return output_path

    # --- Frame extraction ---

    def snapshot(self, time, output_path):
        self._clip.save_frame(output_path, t=time)
        self._clip.close()
        return output_path

    # --- Export ---

    def _write_as(self, fmt, output_path=None, **kwargs):
        output_path = self._output_path(fmt, output_path)
        codec = kwargs.pop("codec", CODEC_MAP.get(fmt))
        if not codec:
            raise ValueError(f"Unsupported video format: {fmt}")
        self._clip.write_videofile(output_path, codec=codec, **kwargs)
        self._clip.close()
        return output_path

    def to_mp4(self, output_path=None, **kwargs):
        return self._write_as("mp4", output_path, **kwargs)

    def to_avi(self, output_path=None, **kwargs):
        return self._write_as("avi", output_path, **kwargs)

    def to_mov(self, output_path=None, **kwargs):
        return self._write_as("mov", output_path, **kwargs)

    def to_mkv(self, output_path=None, **kwargs):
        return self._write_as("mkv", output_path, **kwargs)

    def to_webm(self, output_path=None, **kwargs):
        return self._write_as("webm", output_path, **kwargs)

    def to_flv(self, output_path=None, **kwargs):
        return self._write_as("flv", output_path, **kwargs)

    def to_ogv(self, output_path=None, **kwargs):
        return self._write_as("ogv", output_path, **kwargs)

    def to_wmv(self, output_path=None, **kwargs):
        return self._write_as("wmv", output_path, **kwargs)

    def to_3gp(self, output_path=None, **kwargs):
        return self._write_as("3gp", output_path, **kwargs)

    def to_ts(self, output_path=None, **kwargs):
        return self._write_as("ts", output_path, **kwargs)

    def to_mpeg(self, output_path=None, **kwargs):
        return self._write_as("mpeg", output_path, **kwargs)

    def to_mpg(self, output_path=None, **kwargs):
        return self._write_as("mpg", output_path, **kwargs)

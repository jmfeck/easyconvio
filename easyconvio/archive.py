import os
import shutil
import tempfile
import zipfile
import tarfile

from .base import BaseFile


class ArchiveFile(BaseFile):
    """Archive file with extraction, listing, and conversion methods."""

    def _load(self):
        self._file_list = None

    # --- Properties ---

    @property
    def file_list(self):
        if self._file_list is None:
            self._file_list = self._get_file_list()
        return self._file_list

    @property
    def file_count(self):
        return len(self.file_list)

    def _get_file_list(self):
        fmt = self.format
        if fmt == "zip":
            with zipfile.ZipFile(self.path, "r") as zf:
                return zf.namelist()
        elif fmt in ("tar", "gz", "tgz", "bz2", "tbz2", "xz"):
            with tarfile.open(self.path, "r:*") as tf:
                return tf.getnames()
        elif fmt == "7z":
            import py7zr
            with py7zr.SevenZipFile(self.path, "r") as sz:
                return sz.getnames()
        elif fmt == "rar":
            import rarfile
            with rarfile.RarFile(self.path, "r") as rf:
                return rf.namelist()
        return []

    # --- Operations ---

    def list_files(self):
        return self.file_list

    def extract(self, output_dir="."):
        fmt = self.format
        os.makedirs(output_dir, exist_ok=True)
        if fmt == "zip":
            with zipfile.ZipFile(self.path, "r") as zf:
                zf.extractall(output_dir)
        elif fmt in ("tar", "gz", "tgz", "bz2", "tbz2", "xz"):
            with tarfile.open(self.path, "r:*") as tf:
                tf.extractall(output_dir)
        elif fmt == "7z":
            import py7zr
            with py7zr.SevenZipFile(self.path, "r") as sz:
                sz.extractall(output_dir)
        elif fmt == "rar":
            import rarfile
            with rarfile.RarFile(self.path, "r") as rf:
                rf.extractall(output_dir)
        return output_dir

    def extract_file(self, name, output_dir="."):
        fmt = self.format
        os.makedirs(output_dir, exist_ok=True)
        if fmt == "zip":
            with zipfile.ZipFile(self.path, "r") as zf:
                zf.extract(name, output_dir)
        elif fmt in ("tar", "gz", "tgz", "bz2", "tbz2", "xz"):
            with tarfile.open(self.path, "r:*") as tf:
                tf.extract(name, output_dir)
        elif fmt == "7z":
            import py7zr
            with py7zr.SevenZipFile(self.path, "r") as sz:
                sz.extract(output_dir, [name])
        elif fmt == "rar":
            import rarfile
            with rarfile.RarFile(self.path, "r") as rf:
                rf.extract(name, output_dir)
        return os.path.join(output_dir, name)

    def _extract_to_temp(self):
        tmp = tempfile.mkdtemp()
        self.extract(tmp)
        return tmp

    def _pack_from_dir(self, source_dir, fmt, output_path):
        if fmt == "zip":
            with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for root, _, files in os.walk(source_dir):
                    for f in files:
                        full = os.path.join(root, f)
                        arcname = os.path.relpath(full, source_dir)
                        zf.write(full, arcname)
        elif fmt == "tar":
            with tarfile.open(output_path, "w") as tf:
                for root, _, files in os.walk(source_dir):
                    for f in files:
                        full = os.path.join(root, f)
                        arcname = os.path.relpath(full, source_dir)
                        tf.add(full, arcname)
        elif fmt in ("gz", "tgz"):
            with tarfile.open(output_path, "w:gz") as tf:
                for root, _, files in os.walk(source_dir):
                    for f in files:
                        full = os.path.join(root, f)
                        arcname = os.path.relpath(full, source_dir)
                        tf.add(full, arcname)
        elif fmt in ("bz2", "tbz2"):
            with tarfile.open(output_path, "w:bz2") as tf:
                for root, _, files in os.walk(source_dir):
                    for f in files:
                        full = os.path.join(root, f)
                        arcname = os.path.relpath(full, source_dir)
                        tf.add(full, arcname)
        elif fmt == "xz":
            with tarfile.open(output_path, "w:xz") as tf:
                for root, _, files in os.walk(source_dir):
                    for f in files:
                        full = os.path.join(root, f)
                        arcname = os.path.relpath(full, source_dir)
                        tf.add(full, arcname)
        elif fmt == "7z":
            import py7zr
            with py7zr.SevenZipFile(output_path, "w") as sz:
                for root, _, files in os.walk(source_dir):
                    for f in files:
                        full = os.path.join(root, f)
                        arcname = os.path.relpath(full, source_dir)
                        sz.write(full, arcname)

    def _convert_to(self, fmt, output_path=None):
        output_path = self._output_path(fmt, output_path)
        tmp = self._extract_to_temp()
        try:
            self._pack_from_dir(tmp, fmt, output_path)
        finally:
            shutil.rmtree(tmp)
        return output_path

    # --- Export ---

    def to_zip(self, output_path=None):
        return self._convert_to("zip", output_path)

    def to_tar(self, output_path=None):
        return self._convert_to("tar", output_path)

    def to_gz(self, output_path=None):
        return self._convert_to("gz", output_path)

    def to_tgz(self, output_path=None):
        return self._convert_to("tgz", output_path)

    def to_bz2(self, output_path=None):
        return self._convert_to("bz2", output_path)

    def to_xz(self, output_path=None):
        return self._convert_to("xz", output_path)

    def to_7z(self, output_path=None):
        return self._convert_to("7z", output_path)

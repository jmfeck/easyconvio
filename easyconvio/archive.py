from __future__ import annotations

import os
import shutil
import tempfile
import zipfile
import tarfile
from typing import Optional, List

from .base import BaseFile


class ArchiveFile(BaseFile):
    """Archive file with extraction, listing, and conversion methods."""

    def _load(self) -> None:
        self._file_list: Optional[List[str]] = None

    # --- Properties ---

    @property
    def file_list(self) -> List[str]:
        """List of file names in the archive."""
        if self._file_list is None:
            self._file_list = self._get_file_list()
        return self._file_list

    @property
    def file_count(self) -> int:
        """Number of files in the archive."""
        return len(self.file_list)

    def _get_file_list(self) -> List[str]:
        fmt = self.format
        if fmt in ("zip", "jar"):
            with zipfile.ZipFile(self.path, "r") as zf:
                return zf.namelist()
        elif fmt in ("tar", "gz", "tgz", "bz2", "tbz2", "xz"):
            with tarfile.open(self.path, "r:*") as tf:
                return tf.getnames()
        elif fmt == "7z":
            try:
                import py7zr
            except ImportError:
                raise ImportError(
                    "7z support requires py7zr. "
                    "Install with: pip install easyconvio[archives]"
                )
            with py7zr.SevenZipFile(self.path, "r") as sz:
                return sz.getnames()
        elif fmt == "rar":
            try:
                import rarfile
            except ImportError:
                raise ImportError(
                    "RAR support requires rarfile. "
                    "Install with: pip install easyconvio[archives]"
                )
            with rarfile.RarFile(self.path, "r") as rf:
                return rf.namelist()
        return []

    # --- Operations ---

    def list_files(self) -> List[str]:
        """Return a list of file names in the archive."""
        return self.file_list

    def extract(self, output_dir: str = ".") -> str:
        """Extract all files to the given directory."""
        fmt = self.format
        os.makedirs(output_dir, exist_ok=True)
        if fmt in ("zip", "jar"):
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

    def extract_file(self, name: str, output_dir: str = ".") -> str:
        """Extract a single file by name to the given directory."""
        fmt = self.format
        os.makedirs(output_dir, exist_ok=True)
        if fmt in ("zip", "jar"):
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

    def _extract_to_temp(self) -> str:
        tmp = tempfile.mkdtemp()
        self.extract(tmp)
        return tmp

    def _pack_from_dir(self, source_dir: str, fmt: str, output_path: str) -> None:
        if fmt in ("zip", "jar"):
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

    def _convert_to(self, fmt: str, output_path: Optional[str] = None) -> str:
        output_path = self._output_path(fmt, output_path)
        tmp = self._extract_to_temp()
        try:
            self._pack_from_dir(tmp, fmt, output_path)
        finally:
            shutil.rmtree(tmp)
        return output_path

    # --- Export ---

    def to_zip(self, output_path: Optional[str] = None) -> str:
        """Export as ZIP."""
        return self._convert_to("zip", output_path)

    def to_jar(self, output_path: Optional[str] = None) -> str:
        """Export as JAR (zip-format Java archive)."""
        return self._convert_to("jar", output_path)

    def to_tar(self, output_path: Optional[str] = None) -> str:
        """Export as TAR."""
        return self._convert_to("tar", output_path)

    def to_gz(self, output_path: Optional[str] = None) -> str:
        """Export as gzipped TAR."""
        return self._convert_to("gz", output_path)

    def to_tgz(self, output_path: Optional[str] = None) -> str:
        """Export as .tgz (gzipped TAR)."""
        return self._convert_to("tgz", output_path)

    def to_bz2(self, output_path: Optional[str] = None) -> str:
        """Export as bzip2-compressed TAR."""
        return self._convert_to("bz2", output_path)

    def to_xz(self, output_path: Optional[str] = None) -> str:
        """Export as xz-compressed TAR."""
        return self._convert_to("xz", output_path)

    def to_7z(self, output_path: Optional[str] = None) -> str:
        """Export as 7z."""
        return self._convert_to("7z", output_path)

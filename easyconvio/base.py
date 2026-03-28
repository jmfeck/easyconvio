from __future__ import annotations

import os
from typing import Any, Optional


class BaseFile:
    """Base class for all file types in easyconvio."""

    def __init__(self, path: str) -> None:
        self.path: str = os.path.abspath(path)
        self.format: str = os.path.splitext(path)[1].lower().lstrip(".")
        self._load()

    def _load(self) -> None:
        raise NotImplementedError("Subclasses must implement _load()")

    def _output_path(self, target_format: str, output_path: Optional[str] = None) -> str:
        """Build output file path, using the source path as base if not provided."""
        if output_path:
            return output_path
        base = os.path.splitext(self.path)[0]
        return f"{base}.{target_format.lower().lstrip('.')}"

    def to(self, fmt: str, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Convert to the given format using the matching to_<fmt> method."""
        fmt = fmt.lower().lstrip(".")
        method = getattr(self, f"to_{fmt}", None)
        if not method:
            raise ValueError(f"Unsupported format: {fmt}")
        return method(output_path, **kwargs)

    def close(self) -> None:
        """Release resources. Override in subclasses that hold open handles."""
        pass

    def __enter__(self) -> BaseFile:
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} '{os.path.basename(self.path)}' ({self.format})>"

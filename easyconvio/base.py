import os


class BaseFile:
    """Base class for all file types in easyconvio."""

    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.format = os.path.splitext(path)[1].lower().lstrip(".")
        self._load()

    def _load(self):
        raise NotImplementedError("Subclasses must implement _load()")

    def _output_path(self, target_format, output_path=None):
        if output_path:
            return output_path
        base = os.path.splitext(self.path)[0]
        return f"{base}.{target_format.lower().lstrip('.')}"

    def to(self, fmt, output_path=None, **kwargs):
        fmt = fmt.lower().lstrip(".")
        method = getattr(self, f"to_{fmt}", None)
        if not method:
            raise ValueError(f"Unsupported format: {fmt}")
        return method(output_path, **kwargs)

    def __repr__(self):
        return f"<{self.__class__.__name__} '{os.path.basename(self.path)}' ({self.format})>"

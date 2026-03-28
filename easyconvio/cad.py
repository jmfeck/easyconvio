from __future__ import annotations

from typing import Optional, List, Any

from .base import BaseFile


class CADFile(BaseFile):
    """CAD file (DXF) with inspection and conversion methods."""

    def _load(self) -> None:
        try:
            import ezdxf
        except ImportError:
            raise ImportError(
                "CADFile requires ezdxf. "
                "Install with: pip install easyconvio[cad]"
            )
        self._doc = ezdxf.readfile(self.path)

    # --- Properties ---

    @property
    def layers(self) -> List[str]:
        """List of layer names in the drawing."""
        return [layer.dxf.name for layer in self._doc.layers]

    @property
    def entity_count(self) -> int:
        """Number of entities in the model space."""
        msp = self._doc.modelspace()
        return len(list(msp))

    # --- Operations ---

    def list_layers(self) -> List[str]:
        """Return a list of layer names."""
        return self.layers

    # --- Export ---

    def to_dxf(self, output_path: Optional[str] = None) -> str:
        """Export as DXF."""
        output_path = self._output_path("dxf", output_path)
        self._doc.saveas(output_path)
        return output_path

    def to_png(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as PNG (requires matplotlib)."""
        output_path = self._output_path("png", output_path)
        try:
            from ezdxf.addons.drawing import matplotlib as draw_mpl
        except ImportError:
            raise ImportError(
                "CAD rendering requires matplotlib. "
                "Install with: pip install easyconvio[cad]"
            )
        fig = draw_mpl.qfigure(self._doc.modelspace())
        fig.savefig(output_path, dpi=kwargs.get("dpi", 300))
        import matplotlib.pyplot as plt
        plt.close(fig)
        return output_path

    def to_svg(self, output_path: Optional[str] = None) -> str:
        """Export as SVG (requires matplotlib)."""
        output_path = self._output_path("svg", output_path)
        try:
            from ezdxf.addons.drawing import matplotlib as draw_mpl
        except ImportError:
            raise ImportError(
                "CAD rendering requires matplotlib. "
                "Install with: pip install easyconvio[cad]"
            )
        fig = draw_mpl.qfigure(self._doc.modelspace())
        fig.savefig(output_path, format="svg")
        import matplotlib.pyplot as plt
        plt.close(fig)
        return output_path

    def to_pdf(self, output_path: Optional[str] = None) -> str:
        """Export as PDF (requires matplotlib)."""
        output_path = self._output_path("pdf", output_path)
        try:
            from ezdxf.addons.drawing import matplotlib as draw_mpl
        except ImportError:
            raise ImportError(
                "CAD rendering requires matplotlib. "
                "Install with: pip install easyconvio[cad]"
            )
        fig = draw_mpl.qfigure(self._doc.modelspace())
        fig.savefig(output_path, format="pdf")
        import matplotlib.pyplot as plt
        plt.close(fig)
        return output_path

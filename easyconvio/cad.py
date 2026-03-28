import os

from .base import BaseFile


class CADFile(BaseFile):
    """CAD file (DXF) with inspection and conversion methods."""

    def _load(self):
        try:
            import ezdxf
        except ImportError:
            raise ImportError(
                "CADFile requires ezdxf. "
                "Install with: pip install ezdxf"
            )
        self._doc = ezdxf.readfile(self.path)

    # --- Properties ---

    @property
    def layers(self):
        return [layer.dxf.name for layer in self._doc.layers]

    @property
    def entity_count(self):
        msp = self._doc.modelspace()
        return len(list(msp))

    # --- Operations ---

    def list_layers(self):
        return self.layers

    # --- Export ---

    def to_dxf(self, output_path=None):
        output_path = self._output_path("dxf", output_path)
        self._doc.saveas(output_path)
        return output_path

    def to_png(self, output_path=None, **kwargs):
        output_path = self._output_path("png", output_path)
        import ezdxf
        from ezdxf.addons.drawing import matplotlib as draw_mpl
        fig = draw_mpl.qfigure(self._doc.modelspace())
        fig.savefig(output_path, dpi=kwargs.get("dpi", 300))
        import matplotlib.pyplot as plt
        plt.close(fig)
        return output_path

    def to_svg(self, output_path=None):
        output_path = self._output_path("svg", output_path)
        import ezdxf
        from ezdxf.addons.drawing import matplotlib as draw_mpl
        fig = draw_mpl.qfigure(self._doc.modelspace())
        fig.savefig(output_path, format="svg")
        import matplotlib.pyplot as plt
        plt.close(fig)
        return output_path

    def to_pdf(self, output_path=None):
        output_path = self._output_path("pdf", output_path)
        import ezdxf
        from ezdxf.addons.drawing import matplotlib as draw_mpl
        fig = draw_mpl.qfigure(self._doc.modelspace())
        fig.savefig(output_path, format="pdf")
        import matplotlib.pyplot as plt
        plt.close(fig)
        return output_path

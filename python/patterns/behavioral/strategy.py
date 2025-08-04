from __future__ import annotations
import abc


# ---------------------------------------------------------------------------- #
#                                Abstract Class                                #
# ---------------------------------------------------------------------------- #
class ExportStrategy(abc.ABC):
    @abc.abstractmethod
    def export(self, canvas: ImageCanvas, filepath: str):
        pass

# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #

# ------------------------------ Strategy Class ------------------------------ #
class PngExportStrategy(ExportStrategy):
    def export(self, canvas: ImageCanvas, filepath: str):
        print(f"Exporting to PNG: '{filepath}'")
        print(f"  - Wrote {len(canvas.shapes)} shapes to raster image.")
        print("Done.")

class JpegExportStrategy(ExportStrategy):
    def export(self, canvas: ImageCanvas, filepath: str):
        print(f"Exporting to JPEG: '{filepath}'")
        print(f"  - Wrote {len(canvas.shapes)} shapes to raster image.")
        print("Done.")

class SvgExportStrategy(ExportStrategy):
    def export(self, canvas: ImageCanvas, filepath: str):
        print(f"Exporting to SVG: '{filepath}'")
        print("Done.")

# -------------------------------- Data Class -------------------------------- #
class ImageCanvas:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape_data):
        self.shapes.append(shape_data)
        print(f"Added '{shape_data}' to canvas.")

# ------------------------------- Context Class ------------------------------ #
class ImageExporter:
    def __init__(self, strategy: ExportStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ExportStrategy):
        self._strategy = strategy

    def do_export(self, canvas: ImageCanvas, filepath: str):
        self._strategy.export(canvas, filepath)


# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    my_canvas = ImageCanvas()
    my_canvas.add_shape("circle")
    my_canvas.add_shape("square")
    print("-" * 25)

    exporter = ImageExporter(PngExportStrategy())
    exporter.do_export(my_canvas, "my_drawing.png")
    print("-" * 25)

    exporter.set_strategy(JpegExportStrategy())
    exporter.do_export(my_canvas, "my_drawing.jpg")
    print("-" * 25)

    exporter.set_strategy(SvgExportStrategy())
    exporter.do_export(my_canvas, "my_drawing.svg")
    print("-" * 25)

    # **THE BIG ADVANTAGE**: A new developer is asked to add PDF export.
    # They can do so without touching ANY of the existing code.
    class PdfExportStrategy(ExportStrategy):
        def export(self, canvas: ImageCanvas, filepath: str):
            print(f"Exporting to PDF: '{filepath}'")
            print(f"  - Embedding {len(canvas.shapes)} shapes into PDF document structure.")
            print("Done.")

    print("New functionality added!")
    exporter.set_strategy(PdfExportStrategy())
    exporter.do_export(my_canvas, "my_drawing.pdf")


# ---------------------------------- Output ---------------------------------- #
# Added 'circle' to canvas.
# Added 'square' to canvas.
# -------------------------
# Exporting to PNG: 'my_drawing.png'
#   - Wrote 2 shapes to raster image.
# Done.
# -------------------------
# Exporting to JPEG: 'my_drawing.jpg'
#   - Wrote 2 shapes to raster image.
# Done.
# -------------------------
# Exporting to SVG: 'my_drawing.svg'
# Done.
# -------------------------
# New functionality added!
# Exporting to PDF: 'my_drawing.pdf'
#   - Embedding 2 shapes into PDF document structure.
# Done.
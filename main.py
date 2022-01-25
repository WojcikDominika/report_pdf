# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import string

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table


def random_char(y):
    return "".join(random.choice(string.ascii_letters) for x in range(y))


def random_table(cols, rows):
    data = []
    first = True
    for row in range(rows):
        r = []
        for col in range(cols):
            if first:
                r.append(random_char(5))
            else:
                r.append(random.choice(string.ascii_letters))
        data += [r]
        first = False
    t = Table(data)
    t.setStyle(
        [
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("GRID", (0, 0), (-1, -1), 1, "black"),
        ]
    )
    return t


class FooterCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_canvas()
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self):
        t = Table([["Report"]], LETTER[0])
        t.setStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#cccccc")),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
        t.wrapOn(self, 0, 0)
        t.drawOn(self, 0, 0)



class HeaderCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_canvas()
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self):
        HEADER_HEIGHT= LETTER[1] * 0.15
        t = Table([["Report Title"]], LETTER[0], HEADER_HEIGHT)
        t.setStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#7DA9E6")),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
        t.wrapOn(self, 0, LETTER[1] - HEADER_HEIGHT)
        t.drawOn(self, 0, LETTER[1] - HEADER_HEIGHT)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    styles = getSampleStyleSheet()
    spacer = Spacer(0, 10)
    elements = [
        random_table(4, 5),
        spacer,
        random_table(3, 6),
        spacer,
        random_table(7, 4),
        spacer,
        random_table(4, 5),
        spacer,
        random_table(2, 10),
        spacer,
        random_table(3, 6),
        spacer,
        random_table(7, 4),
        spacer,
        random_table(8, 5),
        spacer,
        random_table(4, 8),
    ]

    doc = SimpleDocTemplate("my_file.pdf", pagesize=LETTER)
    doc.handle_pageBegin()
    doc.multiBuild(elements, canvasmaker=HeaderCanvas)

#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def drawSquare(self, x, y, x1, y1, color, percent, fillColor):
        # vertical lines
        graphics.DrawLine(self.canvas, x, y, x, y1, color)
        graphics.DrawLine(self.canvas, x1, y, x1, y1, color)

        # horizontal lines
        graphics.DrawLine(self.canvas, x, y, x1, y, color)
        graphics.DrawLine(self.canvas, x, y1, x1, y1, color)

        fill = int(30 * percent)
        for i in range(fill):
            graphics.DrawLine(self.canvas, (x + 1) + i, y + 1, x + 1 + i, y1 - 1, fillColor)


    def run(self):
        self.canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("fonts/4x6.bdf")

        red = graphics.Color(100, 0, 0)
        green = graphics.Color(0, 100, 0)
        self.drawSquare(0, 8, 31, 15, red, 1, green)

        # green = graphics.Color(0, 255, 0)
        # graphics.Drawe(canvas, 15, 15, 10, green)

        # blue = graphics.Color(0, 0, 255)
        # green = graphics.Color(0, 255, 0)
        # graphics.DrawText(canvas, font, 0, 5, blue, "one two")
        # graphics.DrawText(canvas, font, 0, 12, green, "three four")

        while True:
            time.sleep(10)   # show display for 10 seconds before exit


# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()

#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class FixedText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(FixedText, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("animation/fonts/4x6.bdf")

        blue = graphics.Color(0, 0, 255)
        green = graphics.Color(0, 255, 0)
        graphics.DrawText(canvas, font, 0, 5, blue, "one two")
        graphics.DrawText(canvas, font, 0, 12, green, "three four")

        while True:
            time.sleep(2)   


# Main function
if __name__ == "__main__":
    fixed_text = FixedText()
    if (not fixed_text.process()):
        fixed_text.print_help()

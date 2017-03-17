#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import random


class FixedText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(FixedText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to display. Format <line 1>::<line 2>", default="Line 1: Line 2")

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("animation/fonts/5x7.bdf")

        line1_color = []
        line2_color = []
        for i in range(3):
            line1_color.append(random.randint(0, 255))
            line2_color.append(random.randint(0, 255))

        l1_color = graphics.Color(*tuple(line1_color))
        l2_color = graphics.Color(*tuple(line2_color))
        line1, line2 = self.args.text.strip().split('::')
        graphics.DrawText(canvas, font, 0, 7, l1_color, line1)
        graphics.DrawText(canvas, font, 0, 14, l2_color, line2)

        while True:
            time.sleep(2)   


# Main function
if __name__ == "__main__":
    fixed_text = FixedText()
    if (not fixed_text.process()):
        fixed_text.print_help()

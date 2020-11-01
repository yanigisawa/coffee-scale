#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import random


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def load_text(self):
        with open("marquee_text.txt", "r") as f:
            self.all_lines = f.readlines()

    def getColor(self):
        rgb = []
        for i in range(3):
            rgb.append(random.randint(0, 255))

        return tuple(rgb)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        self.load_text()
        font = graphics.Font()
        font.LoadFont("fonts/7x13.bdf")
        # font.LoadFont("fonts/10x20.bdf")
        color = graphics.Color(*self.getColor())
        pos = offscreen_canvas.width
        my_text = self.args.text
        y_coords = [0, 10, 30]
        y_opt = 1
        line = 0

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, y_coords[y_opt], color, self.all_lines[line].strip())
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width
                y_opt *= -1
                line += 1
                color = graphics.Color(*self.getColor())
                if line > self.all_lines:
                    line = 0

            time.sleep(0.03)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()

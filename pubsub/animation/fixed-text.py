#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import random

class FixedText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(FixedText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to display. Format <line 1>::<line 2>", default="Line 1: Line 2")
        self.parser.add_argument("-u", "--united", action="store", help="United Way Completion Percent", default=0, type=float)


    def drawPercentComplete(self, x, y, x1, y1, color, percent, fillColor):
        # vertical lines
        graphics.DrawLine(self.matrix, x, y, x, y1, color)
        graphics.DrawLine(self.matrix, x1, y, x1, y1, color)

        # horizontal lines
        graphics.DrawLine(self.matrix, x, y, x1, y, color)
        graphics.DrawLine(self.matrix, x, y1, x1, y1, color)

        # fill = int(30 * percent)
        # for i in range(fill):
        #     graphics.DrawLine(self.matrix, (x + 1) + i, y + 1, x + 1 + i, y1 - 1, fillColor)

    def clearProgress(self, canvas):
        for i in range(1, 31):
            for j in range (9, 15):
                canvas.SetPixel(i, j, 0, 0, 0)

    def getProgressColor(self, percent):
        red = [255, 0, 0]
        green = [0, 155, 50]
        yellow = [155, 155, 0]
        blue = [0, 0, 255]

        if percent <= 0.34:
            return red
        elif percent > 0.34 and percent <= 0.67:
            return yellow
        # elif percent > 0.5 and percent <= 0.75:
        #     return blue
        else:
            return green

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("/home/pi/src/coffee-scale/pubsub/animation/fonts/5x7.bdf")

        line1_color = []
        line2_color = []
        square_color = []
        fill_color = []
        for i in range(3):
            line1_color.append(random.randint(0, 255))
            line2_color.append(random.randint(0, 255))
            square_color.append(random.randint(0, 255))
            fill_color.append(random.randint(0, 255))

        l1_color = graphics.Color(*tuple([155, 155, 155]))
        l2_color = graphics.Color(*tuple(line2_color))
        line1, line2 = self.args.text.strip().split('::')
        graphics.DrawText(canvas, font, 0, 7, l1_color, line1)

        uw_percent = 0
        if self.args.united > 0:
            s = l1_color # graphics.Color(*tuple(square_color))
            f = graphics.Color(*tuple(fill_color))
            uw_percent = self.args.united
            self.drawPercentComplete(0, 8, 31, 15, s, uw_percent, f)
        else:
            graphics.DrawText(canvas, font, 0, 14, l2_color, line2)

        i, j = 1, 8
        rotateCount = 0
        while True:
            if self.args.united == 0:
                time.sleep(2)
                continue

            fill = int(30 * uw_percent)
            if i > fill:
                if rotateCount > 2:
                    continue
                i = 1
                rotateCount += 1
                self.clearProgress(canvas)

            progress_color = self.getProgressColor(float(i) / 30)
            for j in range(9, 15):
                canvas.SetPixel(i, j, *tuple(progress_color))

            i += 1
            delay = 1.2 / fill
            time.sleep(delay)   


# Main function
if __name__ == "__main__":
    fixed_text = FixedText()
    if (not fixed_text.process()):
        fixed_text.print_help()




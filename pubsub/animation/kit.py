#!/usr/bin/env python
from samplebase import SampleBase


class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        print("{0} / {1}".format(offset_canvas.width, offset_canvas.height))
        print("{0} / {1}".format(self.matrix.width, self.matrix.height))
        x, y = 0, 7
        start, end, direction = 0, offset_canvas.width, 1
        while True:
            self.usleep(50000)

            for j in range(0, offset_canvas.width):
                if j == x + direction * 4:
                    offset_canvas.SetPixel(j, y, 255, 0, 0)
                    offset_canvas.SetPixel(j, y - 1, 255, 0, 0)
                    offset_canvas.SetPixel(j, y + 1, 255, 0, 0)
                elif j == x + direction * 5:
                    offset_canvas.SetPixel(j, y, 255, 0, 0)
                    offset_canvas.SetPixel(j, y - 1, 255, 0, 0)
                    offset_canvas.SetPixel(j, y + 1, 255, 0, 0)
                if j == x + direction * 2:
                    offset_canvas.SetPixel(j, y, 175, 0, 0)
                    offset_canvas.SetPixel(j, y - 1, 175, 0, 0)
                    offset_canvas.SetPixel(j, y + 1, 175, 0, 0)
                elif j == x + direction * 3:
                    offset_canvas.SetPixel(j, y, 155, 0, 0)
                    offset_canvas.SetPixel(j, y - 1, 155, 0, 0)
                    offset_canvas.SetPixel(j, y + 1, 155, 0, 0)
                elif j == x + direction:
                    offset_canvas.SetPixel(j, y, 55, 0, 0)
                    offset_canvas.SetPixel(j, y - 1, 55, 0, 0)
                    offset_canvas.SetPixel(j, y + 1, 55, 0, 0)
                elif j == x: 
                    offset_canvas.SetPixel(j, y, 25, 0, 0)
                    offset_canvas.SetPixel(j, y - 1, 25, 0, 0)
                    offset_canvas.SetPixel(j, y + 1, 25, 0, 0)
                else:
                    offset_canvas.SetPixel(j, y, 0, 0, 0)
                    offset_canvas.SetPixel(j, y - 1, 0, 0, 0)
                    offset_canvas.SetPixel(j, y + 1, 0, 0, 0)

            x = x + direction
            if x > end or x < start:
                direction = -direction


            # for x in range(0, self.matrix.width):
            #     offset_canvas.SetPixel(x, x, 255, 255, 255)
            #     offset_canvas.SetPixel(offset_canvas.height - 1 - x, x, 255, 0, 255)
            # for x in range(0, offset_canvas.width):
            #     offset_canvas.SetPixel(x * 2, x, 255, 255, 255)
            #     offset_canvas.SetPixel((offset_canvas.height - 1 - x) * 2, x, 255, 0, 255)

            # for x in range(0, offset_canvas.width):
            #     offset_canvas.SetPixel(x, 0, 255, 0, 0)
            #     offset_canvas.SetPixel(x, offset_canvas.height - 1, 255, 255, 0)

            # for y in range(0, offset_canvas.height):
            #     offset_canvas.SetPixel(0, y, 0, 0, 255)
            #     offset_canvas.SetPixel(offset_canvas.width - 1, y, 0, 255, 0)
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)


# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()

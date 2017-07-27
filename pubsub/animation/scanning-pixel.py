#!/usr/bin/env python
from samplebase import SampleBase


class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        print("{0} / {1}".format(offset_canvas.width, offset_canvas.height))
        print("{0} / {1}".format(self.matrix.width, self.matrix.height))
        x, y = 0, 0
        min_x, max_x = 0, 32
        min_y, max_y = 0, 16
        direction = 1
        while True:
            self.usleep(50000)
            for i in range(0, max_x):
                for j in range(0, max_y):
                    if i == x and j == y:
                        offset_canvas.SetPixel(i, j, 150, 50, 0)
                    else:
                        offset_canvas.SetPixel(i, j, 0, 0, 0)


            x = x + 1 * direction
            if x > max_x or x < min_x:
                direction = direction * -1

                y = y + 1
                if y > max_y:
                    y = 0


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

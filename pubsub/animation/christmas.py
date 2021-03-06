#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
from time import sleep
import random

class Pixel():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class Christmas(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Christmas, self).__init__(*args, **kwargs)

    def get_random_pixels(self, count_of_pixels):
        red = (255, 0, 0)
        green = (0, 255, 0)
        pixels = []
        for i in range(count_of_pixels):
            pixels.append(
                    Pixel(random.randint(0, self.canvas.width),
                        random.randint(0, self.canvas.height),
                        red if i % 2 == 0 else green
                    )
                    )
        return pixels


    def clear_screen(self):
        for i in range(self.canvas.width):
            for j in range(self.canvas.height):
                self.canvas.SetPixel(i, j, 0, 0, 0)

    def random_pixels(self):
        print("{0} / {1}".format(self.canvas.width, self.canvas.height))
        x, y = 0, 7
        start, end, direction = 0, self.canvas.width, 1
        count_of_pixels = random.randint(10, 300)
        while True:
            pixels = self.get_random_pixels(count_of_pixels)
            for p in pixels:
                self.canvas.SetPixel(p.x, p.y, *p.color)

            self.canvas = self.matrix.SwapOnVSync(self.canvas)
            sleep(2)
            self.clear_screen()

    def tree(self):
        green = graphics.Color(0, 255, 0)
        yellow = graphics.Color(255, 255, 0)
        height = self.matrix.height - 1
        x = self.matrix.width / 2
        while True:
            # trunk
            graphics.DrawLine(self.matrix, x, 5, x, height, green)
            graphics.DrawLine(self.matrix, x - 1, 5, x - 1, height, green)
            graphics.DrawLine(self.matrix, x + 1, 5, x + 1, height, green)

            # topper
            graphics.DrawCircle(self.matrix, x, 2, 3, yellow)
            for i in range(x - 2, x + 3):
                graphics.DrawLine(self.matrix, i, 0, i, 5, yellow)

            # top triangle
            graphics.DrawLine(self.matrix, x - 2, 5, x / 2, height / 2, green)
            graphics.DrawLine(self.matrix, x + 2, 5, x + (x / 2), height / 2, green)
            graphics.DrawLine(self.matrix, x / 2, height / 2, x + (x / 2), height / 2, green)

            # middle triangle
            graphics.DrawLine(self.matrix, x / 2 + 4, height / 2, x / 4, (height / 2) * 2, green)
            graphics.DrawLine(
                self.matrix, x + (x / 2) - 4, height / 2, 
                self.matrix.width * .875, (height / 2) * 2, 
                green)
            graphics.DrawLine(
                self.matrix, 
                self.matrix.width * .875, height / 2 * 2,
                x / 4, height / 2 * 2, 
                green)

            graphics.DrawLine(self.matrix, x / 4, height, self.matrix.width * .875, height, green)

            # bottom triangle
            # graphics.DrawLine(self.matrix, x / 4 + 4, height / 3 * 2, 0, height, green)
            # graphics.DrawLine(self.matrix, self.matrix.width * .875 - 4, height / 3 * 2, x * 2, height, green)
            # graphics.DrawLine(self.matrix, 0, height, x * 2, height, green)

            sleep(2)


    def run(self):
        self.canvas = self.matrix.CreateFrameCanvas()
        # self.random_pixels()
        self.tree()


# Main function
if __name__ == "__main__":
    christmas = Christmas()
    if (not christmas.process()):
        christmas.print_help()

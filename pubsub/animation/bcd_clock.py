#!/usr/bin/env python
from samplebase import SampleBase
from datetime import datetime
import time

class Pixel():
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]
        self.red = args[2]
        self.green = args[3]
        self.blue = args[4]

    def __repr__(self):
        return '[{0}, {1}]'.format(self.x, self.y)

class BcdClock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(BcdClock, self).__init__(*args, **kwargs)

    def get_bcd_time(self):
        now = datetime.now()
        bcd = []
        for part in [now.hour, now.minute, now.second]:
            p = '{0:02}'.format(part)
            for c in p:
                bcd.append('{0:04b}'.format(int(c)))

        return bcd
        

    def get_bcd_digit_pixels(self, n, x, y):
        offset = 0
        pixels = []
        for bit in n:
            if bit == "1":
                pixels.append(Pixel(x + offset, y, 255, 0, 0))
                pixels.append(Pixel(x + 1 + offset, y, 255, 0, 0))
                pixels.append(Pixel(x + offset, y + 1, 255, 0, 0))
                pixels.append(Pixel(x + 1 + offset, y + 1, 255, 0, 0))

            offset += 4

        return pixels

    def clearScreen(self, x = 0):
        minx = max(x - 4, 0)
        maxX = min(x + 16, 32)
        for i in range(minx, maxX):
            for j in range(0, 16):
                self.canvas.SetPixel(i, j, 0, 0, 0)

    def run(self):
        print('bcd: {0}'.format(self.get_bcd_time()))
        print('pixels: {0}'.format(self.get_bcd_digit_pixels(self.get_bcd_time()[1], 0, 7)))
        self.canvas = self.matrix.CreateFrameCanvas()
        x, y = 0, 0
        start, end, direction = 0, 32, 1
        while True:
            self.clearScreen(x)
            bcd_time = self.get_bcd_time()
            pixels = []
            y_offset = 0
            for d in bcd_time:
                pixels.extend(self.get_bcd_digit_pixels(d, x, y + y_offset))
                y_offset += 4

            for p in pixels:
                self.canvas.SetPixel(p.x, p.y, p.red, p.green, p.blue)

            canvas = self.matrix.SwapOnVSync(self.canvas)
            time.sleep(1)


# Main function
if __name__ == "__main__":
    bcdClock = BcdClock()
    if (not bcdClock.process()):
        bcdClock.print_help()

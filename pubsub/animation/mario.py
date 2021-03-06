#!/usr/bin/env python
from samplebase import SampleBase
import time
import logging

log = logging.getLogger()

class Pixel():
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]
        self.red = args[2]
        self.green = args[3]
        self.blue = args[4]

class Mario(SampleBase):
    red = (155, 0, 0)
    yellow = (25, 25, 0)
    flesh = (155, 155, 0)
    brown = (32, 5, 0)
    blue = (0, 0, 155)
    _halt = None

    def __init__(self, *args, **kwargs):
        super(Mario, self).__init__(*args, **kwargs)

    def clearScreen(self, x = 0):
        minx = max(x - 4, 0)
        maxX = min(x + 16, 64)
        for i in range(minx, maxX):
            for j in range(0, 16):
                self.canvas.SetPixel(i, j, 0, 0, 0)

    def run(self):
        x, y, step = 10, 0, 1
        count = 0
        self.canvas = self.matrix.CreateFrameCanvas()
        inverse = False
        while True:
            if self._halt and self._halt.isSet():
                log.info('Halting Mario')
                break

            self.clearScreen(x)
            count += 1
            if count == 6:
                count = 2

            if count == 1:
                self.draw(self.getRun1(x, y, inverse))
            elif count == 2:
                self.draw(self.getRun2(x, y, inverse))
            elif count == 3:
                self.draw(self.getRun3(x, y, inverse))
            elif count == 4:
                self.draw(self.getRun4(x, y, inverse))
            elif count == 5:
                self.draw(self.getRun5(x, y, inverse))
            else:
                count = 0
                

            # if count % 2 == 0:
            #     self.draw(self.getStanding(x, y, inverse))
            # else:
            #     # self.draw(self.getStanding(x, y, inverse))
                self.draw(self.getJumping(x, y, inverse))

            time.sleep(0.2)
            x += step
            if x > 65 or x < -14:
                step *= -1
                inverse = not inverse

            self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def draw(self, pixels):
        for p in pixels:
            self.canvas.SetPixel(p.x, p.y, p.red, p.green, p.blue)

    def getRun1(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 4,  y + 0, *self.red))
        pixels.append(Pixel(x + 5,  y + 0, *self.red))
        pixels.append(Pixel(x + 6,  y + 0, *self.red))
        pixels.append(Pixel(x + 7,  y + 0, *self.red))
        pixels.append(Pixel(x + 8,  y + 0, *self.red))

        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))
        pixels.append(Pixel(x + 7,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))
        pixels.append(Pixel(x + 9,  y + 1, *self.red))
        pixels.append(Pixel(x + 10, y + 1, *self.red))
        pixels.append(Pixel(x + 11, y + 1, *self.red))

        # Head / Hair)
        pixels.append(Pixel(x + 3,  y + 2, *self.brown))
        pixels.append(Pixel(x + 4,  y + 2, *self.brown))
        pixels.append(Pixel(x + 5,  y + 2, *self.brown))
        # Skin)
        pixels.append(Pixel(x + 6,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 2, *self.brown))
        pixels.append(Pixel(x + 9,  y + 2, *self.flesh))

        pixels.append(Pixel(x + 2,  y + 3, *self.brown))
        pixels.append(Pixel(x + 3,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 3, *self.brown))
        pixels.append(Pixel(x + 5,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 6,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 3, *self.brown))
        pixels.append(Pixel(x + 9,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 10, y +  3, *self.flesh))
        pixels.append(Pixel(x + 11, y +  3,*self.flesh))

        pixels.append(Pixel(x + 2,  y + 4, *self.brown))
        pixels.append(Pixel(x + 3,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 4, *self.brown))
        pixels.append(Pixel(x + 5,  y + 4, *self.brown))
        pixels.append(Pixel(x + 6,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 9,  y + 4, *self.brown))
        pixels.append(Pixel(x + 10, y +  4, *self.flesh))
        pixels.append(Pixel(x + 11, y +  4, *self.flesh))
        pixels.append(Pixel(x + 12, y +  4, *self.flesh))

        pixels.append(Pixel(x + 2,  y + 5, *self.brown))
        pixels.append(Pixel(x + 3,  y + 5, *self.brown))
        pixels.append(Pixel(x + 4,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 5,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 6,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 5, *self.brown))
        pixels.append(Pixel(x + 9,  y + 5, *self.brown))
        pixels.append(Pixel(x + 10, y +  5, *self.brown))
        pixels.append(Pixel(x + 11, y +  5, *self.brown))

        pixels.append(Pixel(x + 3, y + 6, *self.flesh))
        pixels.append(Pixel(x + 4, y + 6, *self.flesh))
        pixels.append(Pixel(x + 5, y + 6, *self.flesh))
        pixels.append(Pixel(x + 6, y + 6, *self.flesh))
        pixels.append(Pixel(x + 7, y + 6, *self.flesh))
        pixels.append(Pixel(x + 8, y + 6, *self.flesh))
        pixels.append(Pixel(x + 9, y + 6, *self.flesh))


        # Body)
        pixels.append(Pixel(x + 2, y + 7, *self.red))
        pixels.append(Pixel(x + 3, y + 7, *self.red))
        pixels.append(Pixel(x + 4, y + 7, *self.red))
        pixels.append(Pixel(x + 5, y + 7, *self.blue))
        pixels.append(Pixel(x + 6, y + 7, *self.red))
        pixels.append(Pixel(x + 7, y + 7, *self.red))


        pixels.append(Pixel(x + 1, y + 8, *self.red))
        pixels.append(Pixel(x + 2, y + 8, *self.red))
        pixels.append(Pixel(x + 3, y + 8, *self.red))
        pixels.append(Pixel(x + 4, y + 8, *self.red))
        pixels.append(Pixel(x + 5, y + 8, *self.blue))
        pixels.append(Pixel(x + 6, y + 8, *self.blue))
        pixels.append(Pixel(x + 7, y + 8, *self.red))
        pixels.append(Pixel(x + 8, y + 8, *self.red))


        pixels.append(Pixel(x + 1, y + 9, *self.red))
        pixels.append(Pixel(x + 2, y + 9, *self.red))
        pixels.append(Pixel(x + 3, y + 9, *self.red))
        pixels.append(Pixel(x + 4, y + 9, *self.blue))
        pixels.append(Pixel(x + 5, y + 9, *self.blue))
        pixels.append(Pixel(x + 6, y + 9, *self.yellow))
        pixels.append(Pixel(x + 7, y + 9, *self.blue))
        pixels.append(Pixel(x + 8, y + 9, *self.blue))


        pixels.append(Pixel(x + 1, y + 10, *self.red))
        pixels.append(Pixel(x + 2, y + 10, *self.red))
        pixels.append(Pixel(x + 3, y + 10, *self.red))
        pixels.append(Pixel(x + 4, y + 10, *self.red))
        pixels.append(Pixel(x + 5, y + 10, *self.blue))
        pixels.append(Pixel(x + 6, y + 10, *self.blue))
        pixels.append(Pixel(x + 7, y + 10, *self.blue))
        pixels.append(Pixel(x + 8, y + 10, *self.blue))


        pixels.append(Pixel(x + 1, y + 11, *self.blue))
        pixels.append(Pixel(x + 2, y + 11, *self.red))
        pixels.append(Pixel(x + 3, y + 11, *self.red))
        pixels.append(Pixel(x + 4, y + 11, *self.flesh))
        pixels.append(Pixel(x + 5, y + 11, *self.flesh))
        pixels.append(Pixel(x + 6, y + 11, *self.red))
        pixels.append(Pixel(x + 7, y + 11, *self.red))
        pixels.append(Pixel(x + 8, y + 11, *self.red))


        pixels.append(Pixel(x + 2, y + 12, *self.blue))
        pixels.append(Pixel(x + 3, y + 12, *self.red))
        pixels.append(Pixel(x + 4, y + 12, *self.flesh))
        pixels.append(Pixel(x + 5, y + 12, *self.flesh))
        pixels.append(Pixel(x + 6, y + 12, *self.blue))
        pixels.append(Pixel(x + 7, y + 12, *self.blue))


        pixels.append(Pixel(x + 3, y + 13, *self.blue))
        pixels.append(Pixel(x + 4, y + 13, *self.blue))
        pixels.append(Pixel(x + 5, y + 13, *self.blue))
        pixels.append(Pixel(x + 6, y + 13, *self.brown))
        pixels.append(Pixel(x + 7, y + 13, *self.brown))
        pixels.append(Pixel(x + 8, y + 13, *self.brown))


        # Feet
        pixels.append(Pixel(x + 3,  y + 14, *self.brown))
        pixels.append(Pixel(x + 4,  y + 14, *self.brown))
        pixels.append(Pixel(x + 5,  y + 14, *self.brown))
        pixels.append(Pixel(x + 6,  y + 14, *self.brown))



        # Standing Mario is 12 pixels wide. With 6 as the mid-point
        # flip all pixels around the 6 pixel mark to turn him around
        if inverse:
            left = x 
            right = left + 12
            mid = left + 6
            for p in pixels:
                if p.x < mid:
                    distance = mid - p.x
                    p.x = p.x + distance * 2
                elif p.x > mid:
                    distance = p.x - mid
                    p.x = p.x - distance * 2

        return pixels

    def getRun2(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 4,  y + 0, *self.red))
        pixels.append(Pixel(x + 5,  y + 0, *self.red))
        pixels.append(Pixel(x + 6,  y + 0, *self.red))
        pixels.append(Pixel(x + 7,  y + 0, *self.red))
        pixels.append(Pixel(x + 8,  y + 0, *self.red))

        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))
        pixels.append(Pixel(x + 7,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))
        pixels.append(Pixel(x + 9,  y + 1, *self.red))
        pixels.append(Pixel(x + 10, y + 1, *self.red))
        pixels.append(Pixel(x + 11, y + 1, *self.red))

        # Head / Hair)
        pixels.append(Pixel(x + 3,  y + 2, *self.brown))
        pixels.append(Pixel(x + 4,  y + 2, *self.brown))
        pixels.append(Pixel(x + 5,  y + 2, *self.brown))
        # Skin)
        pixels.append(Pixel(x + 6,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 2, *self.brown))
        pixels.append(Pixel(x + 9,  y + 2, *self.flesh))

        pixels.append(Pixel(x + 2,  y + 3, *self.brown))
        pixels.append(Pixel(x + 3,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 3, *self.brown))
        pixels.append(Pixel(x + 5,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 6,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 3, *self.brown))
        pixels.append(Pixel(x + 9,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 10, y +  3, *self.flesh))
        pixels.append(Pixel(x + 11, y +  3,*self.flesh))


        pixels.append(Pixel(x + 2,  y + 4, *self.brown))
        pixels.append(Pixel(x + 3,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 4, *self.brown))
        pixels.append(Pixel(x + 5,  y + 4, *self.brown))
        pixels.append(Pixel(x + 6,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 9,  y + 4, *self.brown))
        pixels.append(Pixel(x + 10, y +  4, *self.flesh))
        pixels.append(Pixel(x + 11, y +  4, *self.flesh))
        pixels.append(Pixel(x + 12, y +  4, *self.flesh))


        pixels.append(Pixel(x + 2,  y + 5, *self.brown))
        pixels.append(Pixel(x + 3,  y + 5, *self.brown))
        pixels.append(Pixel(x + 4,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 5,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 6,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 5, *self.brown))
        pixels.append(Pixel(x + 9,  y + 5, *self.brown))
        pixels.append(Pixel(x + 10, y +  5, *self.brown))
        pixels.append(Pixel(x + 11, y +  5, *self.brown))


        pixels.append(Pixel(x + 3, y + 6, *self.flesh))
        pixels.append(Pixel(x + 4, y + 6, *self.flesh))
        pixels.append(Pixel(x + 5, y + 6, *self.flesh))
        pixels.append(Pixel(x + 6, y + 6, *self.flesh))
        pixels.append(Pixel(x + 7, y + 6, *self.flesh))
        pixels.append(Pixel(x + 8, y + 6, *self.flesh))
        pixels.append(Pixel(x + 9, y + 6, *self.flesh))


        # Body
        pixels.append(Pixel(x + 4, y + 7, *self.red))
        pixels.append(Pixel(x + 5, y + 7, *self.red))
        pixels.append(Pixel(x + 6, y + 7, *self.blue))
        pixels.append(Pixel(x + 7, y + 7, *self.blue))
        pixels.append(Pixel(x + 8, y + 7, *self.red))


        pixels.append(Pixel(x + 3, y + 8, *self.red))
        pixels.append(Pixel(x + 4, y + 8, *self.red))
        pixels.append(Pixel(x + 5, y + 8, *self.red))
        pixels.append(Pixel(x + 6, y + 8, *self.red))
        pixels.append(Pixel(x + 7, y + 8, *self.blue))
        pixels.append(Pixel(x + 8, y + 8, *self.red))
        pixels.append(Pixel(x + 9, y + 8, *self.flesh))
        pixels.append(Pixel(x + 10, y + 8, *self.flesh))


        pixels.append(Pixel(x + 1, y + 9, *self.flesh))
        pixels.append(Pixel(x + 2, y + 9, *self.flesh))
        pixels.append(Pixel(x + 3, y + 9, *self.red))
        pixels.append(Pixel(x + 4, y + 9, *self.red))
        pixels.append(Pixel(x + 5, y + 9, *self.red))
        pixels.append(Pixel(x + 6, y + 9, *self.red))
        pixels.append(Pixel(x + 7, y + 9, *self.red))
        pixels.append(Pixel(x + 8, y + 9, *self.red))
        pixels.append(Pixel(x + 9, y + 9, *self.flesh))
        pixels.append(Pixel(x + 10, y + 9, *self.flesh))
        pixels.append(Pixel(x + 11, y + 9, *self.flesh))



        pixels.append(Pixel(x + 0, y + 10, *self.flesh))
        pixels.append(Pixel(x + 1, y + 10, *self.flesh))
        pixels.append(Pixel(x + 2, y + 10, *self.flesh))
        pixels.append(Pixel(x + 3, y + 10, *self.blue))
        pixels.append(Pixel(x + 4, y + 10, *self.red))
        pixels.append(Pixel(x + 5, y + 10, *self.red))
        pixels.append(Pixel(x + 6, y + 10, *self.red))
        pixels.append(Pixel(x + 7, y + 10, *self.red))
        pixels.append(Pixel(x + 8, y + 10, *self.red))
        pixels.append(Pixel(x + 9, y + 10, *self.flesh))
        pixels.append(Pixel(x + 10, y + 10, *self.flesh))


        pixels.append(Pixel(x + 1, y + 11, *self.brown))
        pixels.append(Pixel(x + 2, y + 11, *self.brown))
        pixels.append(Pixel(x + 3, y + 11, *self.blue))
        pixels.append(Pixel(x + 4, y + 11, *self.blue))
        pixels.append(Pixel(x + 5, y + 11, *self.blue))
        pixels.append(Pixel(x + 6, y + 11, *self.blue))
        pixels.append(Pixel(x + 7, y + 11, *self.blue))
        pixels.append(Pixel(x + 8, y + 11, *self.blue))
        pixels.append(Pixel(x + 9, y + 11, *self.blue))


        pixels.append(Pixel(x + 1, y + 12, *self.brown))
        pixels.append(Pixel(x + 2, y + 12, *self.blue))
        pixels.append(Pixel(x + 3, y + 12, *self.blue))
        pixels.append(Pixel(x + 4, y + 12, *self.blue))
        pixels.append(Pixel(x + 5, y + 12, *self.blue))
        pixels.append(Pixel(x + 6, y + 12, *self.blue))
        pixels.append(Pixel(x + 7, y + 12, *self.blue))
        pixels.append(Pixel(x + 8, y + 12, *self.blue))
        pixels.append(Pixel(x + 9, y + 12, *self.blue))


        pixels.append(Pixel(x + 0, y + 13, *self.brown))
        pixels.append(Pixel(x + 1, y + 13, *self.brown))
        pixels.append(Pixel(x + 2, y + 13, *self.blue))
        pixels.append(Pixel(x + 3, y + 13, *self.blue))
        pixels.append(Pixel(x + 6, y + 13, *self.blue))
        pixels.append(Pixel(x + 7, y + 13, *self.blue))
        pixels.append(Pixel(x + 8, y + 13, *self.blue))


        # Feet)
        pixels.append(Pixel(x + 0,  y + 14, *self.brown))
        pixels.append(Pixel(x + 6,  y + 14, *self.brown))
        pixels.append(Pixel(x + 7,  y + 14, *self.brown))
        pixels.append(Pixel(x + 8,  y + 14, *self.brown))


        pixels.append(Pixel(x + 7,  y + 15, *self.brown))
        pixels.append(Pixel(x + 8,  y + 15, *self.brown))
        pixels.append(Pixel(x + 9,  y + 15, *self.brown))

        # Standing Mario is 12 pixels wide. With 6 as the mid-point
        # flip all pixels around the 6 pixel mark to turn him around
        if inverse:
            left = x 
            right = left + 12
            mid = left + 6
            for p in pixels:
                if p.x < mid:
                    distance = mid - p.x
                    p.x = p.x + distance * 2
                elif p.x > mid:
                    distance = p.x - mid
                    p.x = p.x - distance * 2

        return pixels

    def getRun3(self, x, y, inverse = False):
        return self.getRun1(x, y, inverse)

    def getRun4(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 4,  y + 0, *self.red))
        pixels.append(Pixel(x + 5,  y + 0, *self.red))
        pixels.append(Pixel(x + 6,  y + 0, *self.red))
        pixels.append(Pixel(x + 7,  y + 0, *self.red))
        pixels.append(Pixel(x + 8,  y + 0, *self.red))

        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))
        pixels.append(Pixel(x + 7,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))
        pixels.append(Pixel(x + 9,  y + 1, *self.red))
        pixels.append(Pixel(x + 10, y + 1, *self.red))
        pixels.append(Pixel(x + 11, y + 1, *self.red))

        # Head / Hair)
        pixels.append(Pixel(x + 3,  y + 2, *self.brown))
        pixels.append(Pixel(x + 4,  y + 2, *self.brown))
        pixels.append(Pixel(x + 5,  y + 2, *self.brown))
        # Skin)
        pixels.append(Pixel(x + 6,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 2, *self.brown))
        pixels.append(Pixel(x + 9,  y + 2, *self.flesh))

        pixels.append(Pixel(x + 2,  y + 3, *self.brown))
        pixels.append(Pixel(x + 3,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 3, *self.brown))
        pixels.append(Pixel(x + 5,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 6,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 3, *self.brown))
        pixels.append(Pixel(x + 9,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 10, y +  3, *self.flesh))
        pixels.append(Pixel(x + 11, y +  3,*self.flesh))


        pixels.append(Pixel(x + 2,  y + 4, *self.brown))
        pixels.append(Pixel(x + 3,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 4, *self.brown))
        pixels.append(Pixel(x + 5,  y + 4, *self.brown))
        pixels.append(Pixel(x + 6,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 9,  y + 4, *self.brown))
        pixels.append(Pixel(x + 10, y +  4, *self.flesh))
        pixels.append(Pixel(x + 11, y +  4, *self.flesh))
        pixels.append(Pixel(x + 12, y +  4, *self.flesh))


        pixels.append(Pixel(x + 2,  y + 5, *self.brown))
        pixels.append(Pixel(x + 3,  y + 5, *self.brown))
        pixels.append(Pixel(x + 4,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 5,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 6,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 5, *self.brown))
        pixels.append(Pixel(x + 9,  y + 5, *self.brown))
        pixels.append(Pixel(x + 10, y +  5, *self.brown))
        pixels.append(Pixel(x + 11, y +  5, *self.brown))


        pixels.append(Pixel(x + 3, y + 6, *self.flesh))
        pixels.append(Pixel(x + 4, y + 6, *self.flesh))
        pixels.append(Pixel(x + 5, y + 6, *self.flesh))
        pixels.append(Pixel(x + 6, y + 6, *self.flesh))
        pixels.append(Pixel(x + 7, y + 6, *self.flesh))
        pixels.append(Pixel(x + 8, y + 6, *self.flesh))
        pixels.append(Pixel(x + 9, y + 6, *self.flesh))


        # Body)
        pixels.append(Pixel(x + 1, y + 7, *self.red))
        pixels.append(Pixel(x + 2, y + 7, *self.red))
        pixels.append(Pixel(x + 3, y + 7, *self.red))
        pixels.append(Pixel(x + 4, y + 7, *self.red))
        pixels.append(Pixel(x + 5, y + 7, *self.blue))
        pixels.append(Pixel(x + 6, y + 7, *self.red))
        pixels.append(Pixel(x + 7, y + 7, *self.red))
        pixels.append(Pixel(x + 8, y + 7, *self.red))
        pixels.append(Pixel(x + 9, y + 7, *self.blue))


        pixels.append(Pixel(x - 1, y + 8, *self.flesh))
        pixels.append(Pixel(x + 0, y + 8, *self.flesh))
        pixels.append(Pixel(x + 1, y + 8, *self.red))
        pixels.append(Pixel(x + 2, y + 8, *self.red))
        pixels.append(Pixel(x + 3, y + 8, *self.red))
        pixels.append(Pixel(x + 4, y + 8, *self.red))
        pixels.append(Pixel(x + 5, y + 8, *self.blue))
        pixels.append(Pixel(x + 6, y + 8, *self.blue))
        pixels.append(Pixel(x + 7, y + 8, *self.red))
        pixels.append(Pixel(x + 8, y + 8, *self.red))
        pixels.append(Pixel(x + 9, y + 8, *self.red))
        pixels.append(Pixel(x + 10, y + 8, *self.blue))
        pixels.append(Pixel(x + 11, y + 8, *self.red))
        pixels.append(Pixel(x + 12, y + 8, *self.flesh))
        pixels.append(Pixel(x + 13, y + 8, *self.flesh))
        pixels.append(Pixel(x + 14, y + 8, *self.flesh))


        pixels.append(Pixel(x - 1, y + 9, *self.flesh))
        pixels.append(Pixel(x - 0, y + 9, *self.flesh))
        pixels.append(Pixel(x + 1, y + 9, *self.flesh))
        pixels.append(Pixel(x + 3, y + 9, *self.red))
        pixels.append(Pixel(x + 4, y + 9, *self.red))
        pixels.append(Pixel(x + 5, y + 9, *self.blue))
        pixels.append(Pixel(x + 6, y + 9, *self.blue))
        pixels.append(Pixel(x + 7, y + 9, *self.blue))
        pixels.append(Pixel(x + 8, y + 9, *self.blue))
        pixels.append(Pixel(x + 9, y + 9, *self.blue))
        pixels.append(Pixel(x + 10, y + 9, *self.blue))
        pixels.append(Pixel(x + 11, y + 9, *self.red))
        pixels.append(Pixel(x + 12, y + 9, *self.red))
        pixels.append(Pixel(x + 13, y + 9, *self.flesh))
        pixels.append(Pixel(x + 14, y + 9, *self.flesh))


        pixels.append(Pixel(x - 1, y + 10, *self.flesh))
        pixels.append(Pixel(x + 0, y + 10, *self.flesh))
        pixels.append(Pixel(x + 3, y + 10, *self.blue))
        pixels.append(Pixel(x + 4, y + 10, *self.blue))
        pixels.append(Pixel(x + 5, y + 10, *self.blue))
        pixels.append(Pixel(x + 6, y + 10, *self.yellow))
        pixels.append(Pixel(x + 7, y + 10, *self.blue))
        pixels.append(Pixel(x + 8, y + 10, *self.blue))
        pixels.append(Pixel(x + 9, y + 10, *self.blue))
        pixels.append(Pixel(x + 10, y + 10, *self.yellow))
        pixels.append(Pixel(x + 13, y + 10, *self.brown))


        pixels.append(Pixel(x + 2, y + 11, *self.blue))
        pixels.append(Pixel(x + 3, y + 11, *self.blue))
        pixels.append(Pixel(x + 4, y + 11, *self.blue))
        pixels.append(Pixel(x + 5, y + 11, *self.blue))
        pixels.append(Pixel(x + 6, y + 11, *self.blue))
        pixels.append(Pixel(x + 7, y + 11, *self.blue))
        pixels.append(Pixel(x + 8, y + 11, *self.blue))
        pixels.append(Pixel(x + 9, y + 11, *self.blue))
        pixels.append(Pixel(x + 10, y + 11, *self.blue))
        pixels.append(Pixel(x + 11, y + 11, *self.blue))
        pixels.append(Pixel(x + 12, y + 11, *self.brown))
        pixels.append(Pixel(x + 13, y + 11, *self.brown))


        pixels.append(Pixel(x + 1, y + 12, *self.blue))
        pixels.append(Pixel(x + 2, y + 12, *self.blue))
        pixels.append(Pixel(x + 3, y + 12, *self.blue))
        pixels.append(Pixel(x + 4, y + 12, *self.blue))
        pixels.append(Pixel(x + 5, y + 12, *self.blue))
        pixels.append(Pixel(x + 6, y + 12, *self.blue))
        pixels.append(Pixel(x + 7, y + 12, *self.blue))
        pixels.append(Pixel(x + 8, y + 12, *self.blue))
        pixels.append(Pixel(x + 9, y + 12, *self.blue))
        pixels.append(Pixel(x + 10, y + 12, *self.blue))
        pixels.append(Pixel(x + 11, y + 12, *self.blue))
        pixels.append(Pixel(x + 12, y + 12, *self.brown))
        pixels.append(Pixel(x + 13, y + 12, *self.brown))


        pixels.append(Pixel(x + 0, y + 13, *self.brown))
        pixels.append(Pixel(x + 1, y + 13, *self.brown))
        pixels.append(Pixel(x + 2, y + 13, *self.blue))
        pixels.append(Pixel(x + 3, y + 13, *self.blue))
        pixels.append(Pixel(x + 4, y + 13, *self.blue))
        pixels.append(Pixel(x + 9, y + 13, *self.blue))
        pixels.append(Pixel(x + 9, y + 13, *self.blue))
        pixels.append(Pixel(x + 10, y + 13, *self.blue))
        pixels.append(Pixel(x + 11, y + 13, *self.blue))
        pixels.append(Pixel(x + 12, y + 13, *self.brown))
        pixels.append(Pixel(x + 13, y + 13, *self.brown))


        # Feet)
        pixels.append(Pixel(x + 0,  y + 14, *self.brown))
        pixels.append(Pixel(x + 1,  y + 14, *self.brown))
        pixels.append(Pixel(x + 2,  y + 14, *self.brown))


        pixels.append(Pixel(x + 1,  y + 15, *self.brown))
        pixels.append(Pixel(x + 2,  y + 15, *self.brown))
        pixels.append(Pixel(x + 3,  y + 15, *self.brown))

        # Standing Mario is 12 pixels wide. With 6 as the mid-point
        # flip all pixels around the 6 pixel mark to turn him around
        if inverse:
            left = x 
            right = left + 12
            mid = left + 6
            for p in pixels:
                if p.x < mid:
                    distance = mid - p.x
                    p.x = p.x + distance * 2
                elif p.x > mid:
                    distance = p.x - mid
                    p.x = p.x - distance * 2

        return pixels

    def getRun5(self, x, y, inverse = False):
        return self.getRun1(x, y, inverse)

    def getJumping(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 4,  y + 0, *self.red))
        pixels.append(Pixel(x + 5,  y + 0, *self.red))
        pixels.append(Pixel(x + 6,  y + 0, *self.red))
        pixels.append(Pixel(x + 7,  y + 0, *self.red))
        pixels.append(Pixel(x + 8,  y + 0, *self.red))
        pixels.append(Pixel(x + 11,  y + 0, *self.flesh) )
        pixels.append(Pixel(x + 12,  y + 0, *self.flesh) )
        pixels.append(Pixel(x + 13,  y + 0, *self.flesh) )

        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))
        pixels.append(Pixel(x + 7,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))
        pixels.append(Pixel(x + 9,  y + 1, *self.red))
        pixels.append(Pixel(x + 10, y + 1, *self.red))
        pixels.append(Pixel(x + 11, y + 1, *self.red))
        pixels.append(Pixel(x + 12,  y + 1, *self.flesh) )
        pixels.append(Pixel(x + 13,  y + 1, *self.flesh) )

        # Head / Hair)
        pixels.append(Pixel(x + 3,  y + 2, *self.brown))
        pixels.append(Pixel(x + 4,  y + 2, *self.brown))
        pixels.append(Pixel(x + 5,  y + 2, *self.brown))
        # Skin)
        pixels.append(Pixel(x + 6,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 2, *self.brown))
        pixels.append(Pixel(x + 9,  y + 2, *self.flesh))
        pixels.append(Pixel(x + 11, y + 2, *self.red))
        pixels.append(Pixel(x + 12, y + 2, *self.red))
        pixels.append(Pixel(x + 13, y + 2, *self.red))

        pixels.append(Pixel(x + 2,  y + 3, *self.brown))
        pixels.append(Pixel(x + 3,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 3, *self.brown))
        pixels.append(Pixel(x + 5,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 6,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 3, *self.brown))
        pixels.append(Pixel(x + 9,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 10, y + 3, *self.flesh))
        pixels.append(Pixel(x + 11, y + 3,*self.flesh))
        pixels.append(Pixel(x + 12, y + 3, *self.red))
        pixels.append(Pixel(x + 13, y + 3, *self.red))



        pixels.append(Pixel(x + 2,  y + 4, *self.brown))
        pixels.append(Pixel(x + 3,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 4, *self.brown))
        pixels.append(Pixel(x + 5,  y + 4, *self.brown))
        pixels.append(Pixel(x + 6,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 9,  y + 4, *self.brown))
        pixels.append(Pixel(x + 10, y + 4, *self.flesh))
        pixels.append(Pixel(x + 11, y + 4, *self.flesh))
        pixels.append(Pixel(x + 12, y + 4, *self.flesh))
        pixels.append(Pixel(x + 13, y + 4, *self.red))


        pixels.append(Pixel(x + 2,  y + 5, *self.brown))
        pixels.append(Pixel(x + 3,  y + 5, *self.brown))
        pixels.append(Pixel(x + 4,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 5,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 6,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 5, *self.brown))
        pixels.append(Pixel(x + 9,  y + 5, *self.brown))
        pixels.append(Pixel(x + 10, y +  5, *self.brown))
        pixels.append(Pixel(x + 11, y +  5, *self.brown))
        pixels.append(Pixel(x + 12, y + 5, *self.red))


        pixels.append(Pixel(x + 3, y + 6, *self.flesh))
        pixels.append(Pixel(x + 4, y + 6, *self.flesh))
        pixels.append(Pixel(x + 5, y + 6, *self.flesh))
        pixels.append(Pixel(x + 6, y + 6, *self.flesh))
        pixels.append(Pixel(x + 7, y + 6, *self.flesh))
        pixels.append(Pixel(x + 8, y + 6, *self.flesh))
        pixels.append(Pixel(x + 9, y + 6, *self.flesh))
        pixels.append(Pixel(x + 10, y + 6, *self.red))
        pixels.append(Pixel(x + 11, y + 6, *self.red))


        # Body)
        pixels.append(Pixel(x - 2, y + 7, *self.flesh))
        pixels.append(Pixel(x - 1, y + 7, *self.flesh))
        pixels.append(Pixel(x + 0, y + 7, *self.flesh))
        pixels.append(Pixel(x + 1, y + 7, *self.red))
        pixels.append(Pixel(x + 2, y + 7, *self.red))
        pixels.append(Pixel(x + 3, y + 7, *self.red))
        pixels.append(Pixel(x + 4, y + 7, *self.red))
        pixels.append(Pixel(x + 5, y + 7, *self.blue))
        pixels.append(Pixel(x + 6, y + 7, *self.red))
        pixels.append(Pixel(x + 7, y + 7, *self.red))
        pixels.append(Pixel(x + 8, y + 7, *self.red))
        pixels.append(Pixel(x + 9, y + 7, *self.blue))
        pixels.append(Pixel(x + 10, y + 7, *self.red))
        pixels.append(Pixel(x + 11, y + 7, *self.red))
        pixels.append(Pixel(x + 14, y + 7, *self.brown))


        pixels.append(Pixel(x - 2, y + 8, *self.flesh))
        pixels.append(Pixel(x - 1, y + 8, *self.flesh))
        pixels.append(Pixel(x + 0, y + 8, *self.flesh))
        pixels.append(Pixel(x + 1, y + 8, *self.red))
        pixels.append(Pixel(x + 2, y + 8, *self.red))
        pixels.append(Pixel(x + 3, y + 8, *self.red))
        pixels.append(Pixel(x + 4, y + 8, *self.red))
        pixels.append(Pixel(x + 5, y + 8, *self.red))
        pixels.append(Pixel(x + 6, y + 8, *self.blue))
        pixels.append(Pixel(x + 7, y + 8, *self.red))
        pixels.append(Pixel(x + 8, y + 8, *self.red))
        pixels.append(Pixel(x + 9, y + 8, *self.red))
        pixels.append(Pixel(x + 10, y + 8, *self.blue))
        pixels.append(Pixel(x + 13, y + 8, *self.brown))
        pixels.append(Pixel(x + 14, y + 8, *self.brown))


        pixels.append(Pixel(x - 1, y + 9, *self.flesh))
        pixels.append(Pixel(x + 3, y + 9, *self.red))
        pixels.append(Pixel(x + 4, y + 9, *self.red))
        pixels.append(Pixel(x + 5, y + 9, *self.red))
        pixels.append(Pixel(x + 6, y + 9, *self.blue))
        pixels.append(Pixel(x + 7, y + 9, *self.blue))
        pixels.append(Pixel(x + 8, y + 9, *self.blue))
        pixels.append(Pixel(x + 9, y + 9, *self.blue))
        pixels.append(Pixel(x + 10, y + 9, *self.yellow))
        pixels.append(Pixel(x + 11, y + 9, *self.blue))
        pixels.append(Pixel(x + 12, y + 9, *self.blue))
        pixels.append(Pixel(x + 13, y + 9, *self.brown))
        pixels.append(Pixel(x + 14, y + 9, *self.brown))


        pixels.append(Pixel(x + 4, y + 10, *self.blue))
        pixels.append(Pixel(x + 5, y + 10, *self.blue))
        pixels.append(Pixel(x + 6, y + 10, *self.blue))
        pixels.append(Pixel(x + 7, y + 10, *self.yellow))
        pixels.append(Pixel(x + 8, y + 10, *self.blue))
        pixels.append(Pixel(x + 9, y + 10, *self.blue))
        pixels.append(Pixel(x + 10, y + 10, *self.blue))
        pixels.append(Pixel(x + 11, y + 10, *self.blue))
        pixels.append(Pixel(x + 12, y + 10, *self.blue))
        pixels.append(Pixel(x + 13, y + 10, *self.brown))
        pixels.append(Pixel(x + 14, y + 10, *self.brown))


        pixels.append(Pixel(x + 2, y + 11, *self.brown))
        pixels.append(Pixel(x + 3, y + 11, *self.brown))
        pixels.append(Pixel(x + 4, y + 11, *self.blue))
        pixels.append(Pixel(x + 5, y + 11, *self.blue))
        pixels.append(Pixel(x + 6, y + 11, *self.blue))
        pixels.append(Pixel(x + 7, y + 11, *self.blue))
        pixels.append(Pixel(x + 8, y + 11, *self.blue))
        pixels.append(Pixel(x + 9, y + 11, *self.blue))
        pixels.append(Pixel(x + 10, y + 11, *self.blue))
        pixels.append(Pixel(x + 11, y + 11, *self.blue))
        pixels.append(Pixel(x + 12, y + 11, *self.blue))
        pixels.append(Pixel(x + 13, y + 11, *self.brown))
        pixels.append(Pixel(x + 14, y + 11, *self.brown))


        pixels.append(Pixel(x + 1, y + 12, *self.brown))
        pixels.append(Pixel(x + 2, y + 12, *self.brown))
        pixels.append(Pixel(x + 3, y + 12, *self.brown))
        pixels.append(Pixel(x + 3, y + 12, *self.blue))
        pixels.append(Pixel(x + 4, y + 12, *self.blue))
        pixels.append(Pixel(x + 5, y + 12, *self.blue))
        pixels.append(Pixel(x + 6, y + 12, *self.blue))
        pixels.append(Pixel(x + 7, y + 12, *self.blue))
        pixels.append(Pixel(x + 8, y + 12, *self.blue))

        pixels.append(Pixel(x + 1, y + 13, *self.brown))
        pixels.append(Pixel(x + 2, y + 13, *self.brown))

        # Jumping Mario is 17 pixels wide. With 8 as the mid-point
        # flip all pixels around the 8 pixel mark to turn him around
        if inverse:
            left = x - 2
            right = left + 17
            mid = left + 8
            for p in pixels:
                if p.x < mid:
                    distance = mid - p.x
                    p.x = p.x + distance * 2
                elif p.x > mid:
                    distance = p.x - mid
                    p.x = p.x - distance * 2

        return pixels

    def getStanding(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 4,  y + 0, *self.red))
        pixels.append(Pixel(x + 5,  y + 0, *self.red))
        pixels.append(Pixel(x + 6,  y + 0, *self.red))
        pixels.append(Pixel(x + 7,  y + 0, *self.red))
        pixels.append(Pixel(x + 8,  y + 0, *self.red))

        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))
        pixels.append(Pixel(x + 7,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))
        pixels.append(Pixel(x + 9,  y + 1, *self.red))
        pixels.append(Pixel(x + 10, y + 1, *self.red))
        pixels.append(Pixel(x + 11, y + 1, *self.red))

        # Head / Hair)
        pixels.append(Pixel(x + 3,  y + 2, *self.brown))
        pixels.append(Pixel(x + 4,  y + 2, *self.brown))
        pixels.append(Pixel(x + 5,  y + 2, *self.brown))
        # Skin)
        pixels.append(Pixel(x + 6,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 2, *self.brown))
        pixels.append(Pixel(x + 9,  y + 2, *self.flesh))

        pixels.append(Pixel(x + 2,  y + 3, *self.brown))
        pixels.append(Pixel(x + 3,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 3, *self.brown))
        pixels.append(Pixel(x + 5,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 6,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 3, *self.brown))
        pixels.append(Pixel(x + 9,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 10, y +  3, *self.flesh))
        pixels.append(Pixel(x + 11, y +  3,*self.flesh))


        pixels.append(Pixel(x + 2,  y + 4, *self.brown))
        pixels.append(Pixel(x + 3,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 4, *self.brown))
        pixels.append(Pixel(x + 5,  y + 4, *self.brown))
        pixels.append(Pixel(x + 6,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 9,  y + 4, *self.brown))
        pixels.append(Pixel(x + 10, y +  4, *self.flesh))
        pixels.append(Pixel(x + 11, y +  4, *self.flesh))
        pixels.append(Pixel(x + 12, y +  4, *self.flesh))


        pixels.append(Pixel(x + 2,  y + 5, *self.brown))
        pixels.append(Pixel(x + 3,  y + 5, *self.brown))
        pixels.append(Pixel(x + 4,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 5,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 6,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 5, *self.brown))
        pixels.append(Pixel(x + 9,  y + 5, *self.brown))
        pixels.append(Pixel(x + 10, y +  5, *self.brown))
        pixels.append(Pixel(x + 11, y +  5, *self.brown))


        pixels.append(Pixel(x + 3, y + 6, *self.flesh))
        pixels.append(Pixel(x + 4, y + 6, *self.flesh))
        pixels.append(Pixel(x + 5, y + 6, *self.flesh))
        pixels.append(Pixel(x + 6, y + 6, *self.flesh))
        pixels.append(Pixel(x + 7, y + 6, *self.flesh))
        pixels.append(Pixel(x + 8, y + 6, *self.flesh))
        pixels.append(Pixel(x + 9, y + 6, *self.flesh))


        # Body)
        pixels.append(Pixel(x + 2, y + 7, *self.red))
        pixels.append(Pixel(x + 3, y + 7, *self.red))
        pixels.append(Pixel(x + 4, y + 7, *self.blue))
        pixels.append(Pixel(x + 5, y + 7, *self.red))
        pixels.append(Pixel(x + 6, y + 7, *self.red))
        pixels.append(Pixel(x + 7, y + 7, *self.red))
        pixels.append(Pixel(x + 8, y + 7, *self.red))


        pixels.append(Pixel(x + 1, y + 8, *self.red))
        pixels.append(Pixel(x + 2, y + 8, *self.red))
        pixels.append(Pixel(x + 3, y + 8, *self.red))
        pixels.append(Pixel(x + 4, y + 8, *self.blue))
        pixels.append(Pixel(x + 5, y + 8, *self.red))
        pixels.append(Pixel(x + 6, y + 8, *self.red))
        pixels.append(Pixel(x + 7, y + 8, *self.blue))
        pixels.append(Pixel(x + 8, y + 8, *self.red))
        pixels.append(Pixel(x + 9, y + 8, *self.red))
        pixels.append(Pixel(x + 10, y + 8, *self.red))


        pixels.append(Pixel(x + 0, y + 9, *self.red))
        pixels.append(Pixel(x + 1, y + 9, *self.red))
        pixels.append(Pixel(x + 2, y + 9, *self.red))
        pixels.append(Pixel(x + 3, y + 9, *self.red))
        pixels.append(Pixel(x + 4, y + 9, *self.blue))
        pixels.append(Pixel(x + 5, y + 9, *self.blue))
        pixels.append(Pixel(x + 6, y + 9, *self.blue))
        pixels.append(Pixel(x + 7, y + 9, *self.blue))
        pixels.append(Pixel(x + 8, y + 9, *self.red))
        pixels.append(Pixel(x + 9, y + 9, *self.red))
        pixels.append(Pixel(x + 10, y + 9, *self.red))
        pixels.append(Pixel(x + 11, y + 9, *self.red))


        pixels.append(Pixel(x + 0, y + 10, *self.flesh))
        pixels.append(Pixel(x + 1, y + 10, *self.flesh))
        pixels.append(Pixel(x + 2, y + 10, *self.red))
        pixels.append(Pixel(x + 3, y + 10, *self.blue))
        pixels.append(Pixel(x + 4, y + 10, *self.yellow))
        pixels.append(Pixel(x + 5, y + 10, *self.blue))
        pixels.append(Pixel(x + 6, y + 10, *self.blue))
        pixels.append(Pixel(x + 7, y + 10, *self.yellow))
        pixels.append(Pixel(x + 8, y + 10, *self.blue))
        pixels.append(Pixel(x + 9, y + 10, *self.red))
        pixels.append(Pixel(x + 10, y + 10, *self.flesh))
        pixels.append(Pixel(x + 11, y + 10, *self.flesh))


        pixels.append(Pixel(x + 0, y + 11, *self.flesh))
        pixels.append(Pixel(x + 1, y + 11, *self.flesh))
        pixels.append(Pixel(x + 2, y + 11, *self.flesh))
        pixels.append(Pixel(x + 3, y + 11, *self.blue))
        pixels.append(Pixel(x + 4, y + 11, *self.blue))
        pixels.append(Pixel(x + 5, y + 11, *self.blue))
        pixels.append(Pixel(x + 6, y + 11, *self.blue))
        pixels.append(Pixel(x + 7, y + 11, *self.blue))
        pixels.append(Pixel(x + 8, y + 11, *self.blue))
        pixels.append(Pixel(x + 9, y + 11, *self.flesh))
        pixels.append(Pixel(x + 10, y + 11, *self.flesh))
        pixels.append(Pixel(x + 11, y + 11, *self.flesh))


        pixels.append(Pixel(x + 0, y + 12, *self.flesh))
        pixels.append(Pixel(x + 1, y + 12, *self.flesh))
        pixels.append(Pixel(x + 2, y + 12, *self.blue))
        pixels.append(Pixel(x + 3, y + 12, *self.blue))
        pixels.append(Pixel(x + 4, y + 12, *self.blue))
        pixels.append(Pixel(x + 5, y + 12, *self.blue))
        pixels.append(Pixel(x + 6, y + 12, *self.blue))
        pixels.append(Pixel(x + 7, y + 12, *self.blue))
        pixels.append(Pixel(x + 8, y + 12, *self.blue))
        pixels.append(Pixel(x + 9, y + 12, *self.blue))
        pixels.append(Pixel(x + 10, y + 12, *self.flesh))
        pixels.append(Pixel(x + 11, y + 12, *self.flesh))


        pixels.append(Pixel(x + 2, y + 13, *self.blue))
        pixels.append(Pixel(x + 3, y + 13, *self.blue))
        pixels.append(Pixel(x + 4, y + 13, *self.blue))
        pixels.append(Pixel(x + 7, y + 13, *self.blue))
        pixels.append(Pixel(x + 8, y + 13, *self.blue))
        pixels.append(Pixel(x + 9, y + 13, *self.blue))


        # Feet)
        pixels.append(Pixel(x + 1,  y + 14, *self.brown))
        pixels.append(Pixel(x + 2,  y + 14, *self.brown))
        pixels.append(Pixel(x + 3,  y + 14, *self.brown))
        pixels.append(Pixel(x + 8,  y + 14, *self.brown))
        pixels.append(Pixel(x + 9,  y + 14, *self.brown))
        pixels.append(Pixel(x + 10,  y + 14, *self.brown))


        pixels.append(Pixel(x + 0,  y + 15, *self.brown))
        pixels.append(Pixel(x + 1,  y + 15, *self.brown))
        pixels.append(Pixel(x + 2,  y + 15, *self.brown))
        pixels.append(Pixel(x + 3,  y + 15, *self.brown))
        pixels.append(Pixel(x + 8,  y + 15, *self.brown))
        pixels.append(Pixel(x + 9,  y + 15, *self.brown))
        pixels.append(Pixel(x + 10,  y + 15, *self.brown))
        pixels.append(Pixel(x + 11,  y + 15, *self.brown))

        # Standing Mario is 12 pixels wide. With 6 as the mid-point
        # flip all pixels around the 6 pixel mark to turn him around
        if inverse:
            left = x 
            right = left + 12
            mid = left + 6
            for p in pixels:
                if p.x < mid:
                    distance = mid - p.x
                    p.x = p.x + distance * 2
                elif p.x > mid:
                    distance = p.x - mid
                    p.x = p.x - distance * 2

        return pixels
            


# Main function
if __name__ == "__main__":
    mario = Mario()
    if (not mario.process()):
        mario.print_help()

#!/usr/bin/env python
from samplebase import SampleBase
import time
import logging
import random

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
        minx = 0
        maxX = 64
        for i in range(minx, maxX):
            for j in range(0, 32):
                self.canvas.SetPixel(i, j, 0, 0, 0)

    def run(self):
        x, y, step = -3, 0, 1
        count = 0
        width = 10
        self.canvas = self.matrix.CreateFrameCanvas()
        inverse = False
        while True:
            if self._halt and self._halt.isSet():
                log.info('Halting Mario')
                break

            possible_params = [
                (x + 5, y, inverse),
                (x + 5, y + 16, not inverse),
                (x + 23, y, inverse),
                (x + 23, y + 16, not inverse)
            ]
            self.clearScreen(x)

            self.draw_hat(width, y)

            methods = [
                self.getRun1,
                self.getRun2,
                self.getRun3,
                self.getRun4,
                self.getRun5,
                self.getJumping,
                self.getStanding
            ]
            mario_count = random.randint(1,4)
            inverse = random.choice([True, False])
            for i in range(mario_count):
                args = random.choice(possible_params)
                possible_params.remove(args)
                m = random.choice(methods)
                self.draw(m(*args))


            # self.draw(self.getStanding(x + 32, y, inverse))

            # self.draw(self.getJumping(x + 32, y + 16, inverse))

            # self.draw(self.getJumping(x + 50, y, not inverse))

            # self.draw(self.getStanding(x + 50, y + 16, not inverse))



            time.sleep(0.5)
            # time.sleep(0.6009999983238451)
            # x += step
            # if x > 65 or x < -14:
            #     step *= -1
            inverse = not inverse

            self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def draw_hat(self, width, y):
        x = 50
        for i in range(x, width + x):
            self.canvas.SetPixel(i, y, 255, 0, 0)
            self.canvas.SetPixel(i, y + 1, 255, 0, 0)
            self.canvas.SetPixel(i, y + 2, 255, 0, 0)

            self.canvas.SetPixel(i, y + 3, 255, 255, 255)
            self.canvas.SetPixel(i, y + 4, 255, 255, 255)
            self.canvas.SetPixel(i, y + 5, 255, 255, 255)

            self.canvas.SetPixel(i, y + 6, 255, 0, 0)
            self.canvas.SetPixel(i, y + 7, 255, 0, 0)
            self.canvas.SetPixel(i, y + 8, 255, 0, 0)

            self.canvas.SetPixel(i, y + 9, 255, 255, 255)
            self.canvas.SetPixel(i, y + 10, 255, 255, 255)
            self.canvas.SetPixel(i, y + 11, 255, 255, 255)

            self.canvas.SetPixel(i, y + 12, 255, 0, 0)
            self.canvas.SetPixel(i, y + 13, 255, 0, 0)
            self.canvas.SetPixel(i, y + 14, 255, 0, 0)

        for i in range(x - 2, x + 2 + width):
            self.canvas.SetPixel(i, y + 15, 255, 255, 255)

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

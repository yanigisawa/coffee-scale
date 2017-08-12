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

class Invader(SampleBase):
    red = (155, 0, 0)
    yellow = (25, 25, 0)
    flesh = (155, 155, 0)
    brown = (32, 5, 0)
    blue = (0, 0, 155)
    green = (0, 255, 0)
    _halt = None

    def __init__(self, *args, **kwargs):
        super(Invader, self).__init__(*args, **kwargs)

    def clearScreen(self, x = 0):
        minx = 0 # max(x - 4, 0)
        maxX = 32 # min(x + 16, 32)
        for i in range(minx, maxX):
            for j in range(0, 16):
                self.canvas.SetPixel(i, j, 0, 0, 0)

    def run(self):
        playerX, x, y, step, playerStep = 32, -30, 0, 1, -1
        self.canvas = self.matrix.CreateFrameCanvas()
        inverse = False
        while True:
            time.sleep(0.5)
            if self._halt and self._halt.isSet():
                log.info('Halting Invader')
                break

            self.clearScreen(0)
            if x % 2 == 0:
                self.draw(self.getSmallInvaderPosition1(x, y, inverse))
                self.draw(self.getMediumInvaderPosition1(x + 10, y, inverse))
                self.draw(self.getLargeInvaderPosition1(x + 23, y, inverse))
                self.draw(self.getPlayerShip(playerX, y + 10, inverse))
            else:
                self.draw(self.getSmallInvaderPosition2(x, y + 1, inverse))
                self.draw(self.getMediumInvaderPosition2(x + 10, y + 1, inverse))
                self.draw(self.getLargeInvaderPosition2(x + 23, y + 1, inverse))
                self.draw(self.getPlayerShip(playerX, y + 10, inverse))

            x += step
            if x > 32:
                x = -30

            playerX += playerStep
            if playerX < -15:
                playerX = 33


            self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def draw(self, pixels):
        for p in pixels:
            self.canvas.SetPixel(p.x, p.y, p.red, p.green, p.blue)

    def getPlayerShip(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 8,  y + 0, *self.green))

        pixels.append(Pixel(x + 7,  y + 1, *self.green))
        pixels.append(Pixel(x + 8,  y + 1, *self.green))
        pixels.append(Pixel(x + 9,  y + 1, *self.green))

        pixels.append(Pixel(x + 7,  y + 2, *self.green))
        pixels.append(Pixel(x + 8,  y + 2, *self.green))
        pixels.append(Pixel(x + 9,  y + 2, *self.green))

        pixels.append(Pixel(x + 2,  y + 3, *self.green))
        pixels.append(Pixel(x + 3,  y + 3, *self.green))
        pixels.append(Pixel(x + 4,  y + 3, *self.green))
        pixels.append(Pixel(x + 5,  y + 3, *self.green))
        pixels.append(Pixel(x + 6,  y + 3, *self.green))
        pixels.append(Pixel(x + 7,  y + 3, *self.green))
        pixels.append(Pixel(x + 8,  y + 3, *self.green))
        pixels.append(Pixel(x + 9,  y + 3, *self.green))
        pixels.append(Pixel(x + 10,  y + 3, *self.green))
        pixels.append(Pixel(x + 11,  y + 3, *self.green))
        pixels.append(Pixel(x + 12,  y + 3, *self.green))
        pixels.append(Pixel(x + 13,  y + 3, *self.green))
        pixels.append(Pixel(x + 14,  y + 3, *self.green))

        pixels.append(Pixel(x + 1,  y + 4, *self.green))
        pixels.append(Pixel(x + 2,  y + 4, *self.green))
        pixels.append(Pixel(x + 3,  y + 4, *self.green))
        pixels.append(Pixel(x + 4,  y + 4, *self.green))
        pixels.append(Pixel(x + 5,  y + 4, *self.green))
        pixels.append(Pixel(x + 6,  y + 4, *self.green))
        pixels.append(Pixel(x + 7,  y + 4, *self.green))
        pixels.append(Pixel(x + 8,  y + 4, *self.green))
        pixels.append(Pixel(x + 9,  y + 4, *self.green))
        pixels.append(Pixel(x + 10,  y + 4, *self.green))
        pixels.append(Pixel(x + 11,  y + 4, *self.green))
        pixels.append(Pixel(x + 12,  y + 4, *self.green))
        pixels.append(Pixel(x + 13,  y + 4, *self.green))
        pixels.append(Pixel(x + 14,  y + 4, *self.green))
        pixels.append(Pixel(x + 15,  y + 4, *self.green))

        pixels.append(Pixel(x + 1,  y + 5, *self.green))
        pixels.append(Pixel(x + 2,  y + 5, *self.green))
        pixels.append(Pixel(x + 3,  y + 5, *self.green))
        pixels.append(Pixel(x + 4,  y + 5, *self.green))
        pixels.append(Pixel(x + 5,  y + 5, *self.green))
        pixels.append(Pixel(x + 6,  y + 5, *self.green))
        pixels.append(Pixel(x + 7,  y + 5, *self.green))
        pixels.append(Pixel(x + 8,  y + 5, *self.green))
        pixels.append(Pixel(x + 9,  y + 5, *self.green))
        pixels.append(Pixel(x + 10,  y + 5, *self.green))
        pixels.append(Pixel(x + 11,  y + 5, *self.green))
        pixels.append(Pixel(x + 12,  y + 5, *self.green))
        pixels.append(Pixel(x + 13,  y + 5, *self.green))
        pixels.append(Pixel(x + 14,  y + 5, *self.green))
        pixels.append(Pixel(x + 15,  y + 5, *self.green))

        return pixels

    def getLargeInvaderPosition2(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 5,  y + 0, *self.red))
        pixels.append(Pixel(x + 6,  y + 0, *self.red))
        pixels.append(Pixel(x + 7,  y + 0, *self.red))
        pixels.append(Pixel(x + 8,  y + 0, *self.red))

        pixels.append(Pixel(x + 2,  y + 1, *self.red))
        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))
        pixels.append(Pixel(x + 7,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))
        pixels.append(Pixel(x + 9,  y + 1, *self.red))
        pixels.append(Pixel(x + 10,  y + 1, *self.red))
        pixels.append(Pixel(x + 11,  y + 1, *self.red))

        pixels.append(Pixel(x + 1,  y + 2, *self.red))
        pixels.append(Pixel(x + 2,  y + 2, *self.red))
        pixels.append(Pixel(x + 3,  y + 2, *self.red))
        pixels.append(Pixel(x + 4,  y + 2, *self.red))
        pixels.append(Pixel(x + 5,  y + 2, *self.red))
        pixels.append(Pixel(x + 6,  y + 2, *self.red))
        pixels.append(Pixel(x + 7,  y + 2, *self.red))
        pixels.append(Pixel(x + 8,  y + 2, *self.red))
        pixels.append(Pixel(x + 9,  y + 2, *self.red))
        pixels.append(Pixel(x + 10,  y + 2, *self.red))
        pixels.append(Pixel(x + 11,  y + 2, *self.red))
        pixels.append(Pixel(x + 12,  y + 2, *self.red))

        pixels.append(Pixel(x + 1,  y + 3, *self.red))
        pixels.append(Pixel(x + 2,  y + 3, *self.red))
        pixels.append(Pixel(x + 3,  y + 3, *self.red))
        pixels.append(Pixel(x + 6,  y + 3, *self.red))
        pixels.append(Pixel(x + 7,  y + 3, *self.red))
        pixels.append(Pixel(x + 10,  y + 3, *self.red))
        pixels.append(Pixel(x + 11,  y + 3, *self.red))
        pixels.append(Pixel(x + 12,  y + 3, *self.red))
        
        pixels.append(Pixel(x + 1,  y + 4, *self.red))
        pixels.append(Pixel(x + 2,  y + 4, *self.red))
        pixels.append(Pixel(x + 3,  y + 4, *self.red))
        pixels.append(Pixel(x + 4,  y + 4, *self.red))
        pixels.append(Pixel(x + 5,  y + 4, *self.red))
        pixels.append(Pixel(x + 6,  y + 4, *self.red))
        pixels.append(Pixel(x + 7,  y + 4, *self.red))
        pixels.append(Pixel(x + 8,  y + 4, *self.red))
        pixels.append(Pixel(x + 9,  y + 4, *self.red))
        pixels.append(Pixel(x + 10,  y + 4, *self.red))
        pixels.append(Pixel(x + 11,  y + 4, *self.red))
        pixels.append(Pixel(x + 12,  y + 4, *self.red))

        pixels.append(Pixel(x + 3,  y + 5, *self.red))
        pixels.append(Pixel(x + 4,  y + 5, *self.red))
        pixels.append(Pixel(x + 5,  y + 5, *self.red))
        pixels.append(Pixel(x + 8,  y + 5, *self.red))
        pixels.append(Pixel(x + 9,  y + 5, *self.red))
        pixels.append(Pixel(x + 10,  y + 5, *self.red))

        pixels.append(Pixel(x + 2,  y + 6, *self.red))
        pixels.append(Pixel(x + 3,  y + 6, *self.red))
        pixels.append(Pixel(x + 6,  y + 6, *self.red))
        pixels.append(Pixel(x + 7,  y + 6, *self.red))
        pixels.append(Pixel(x + 10,  y + 6, *self.red))
        pixels.append(Pixel(x + 11,  y + 6, *self.red))

        pixels.append(Pixel(x + 3,  y + 7, *self.red))
        pixels.append(Pixel(x + 4,  y + 7, *self.red))
        pixels.append(Pixel(x + 9,  y + 7, *self.red))
        pixels.append(Pixel(x + 10,  y + 7, *self.red))

        return pixels

    def getLargeInvaderPosition1(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 5,  y + 0, *self.red))
        pixels.append(Pixel(x + 6,  y + 0, *self.red))
        pixels.append(Pixel(x + 7,  y + 0, *self.red))
        pixels.append(Pixel(x + 8,  y + 0, *self.red))

        pixels.append(Pixel(x + 2,  y + 1, *self.red))
        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))
        pixels.append(Pixel(x + 7,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))
        pixels.append(Pixel(x + 9,  y + 1, *self.red))
        pixels.append(Pixel(x + 10,  y + 1, *self.red))
        pixels.append(Pixel(x + 11,  y + 1, *self.red))

        pixels.append(Pixel(x + 1,  y + 2, *self.red))
        pixels.append(Pixel(x + 2,  y + 2, *self.red))
        pixels.append(Pixel(x + 3,  y + 2, *self.red))
        pixels.append(Pixel(x + 4,  y + 2, *self.red))
        pixels.append(Pixel(x + 5,  y + 2, *self.red))
        pixels.append(Pixel(x + 6,  y + 2, *self.red))
        pixels.append(Pixel(x + 7,  y + 2, *self.red))
        pixels.append(Pixel(x + 8,  y + 2, *self.red))
        pixels.append(Pixel(x + 9,  y + 2, *self.red))
        pixels.append(Pixel(x + 10,  y + 2, *self.red))
        pixels.append(Pixel(x + 11,  y + 2, *self.red))
        pixels.append(Pixel(x + 12,  y + 2, *self.red))

        pixels.append(Pixel(x + 1,  y + 3, *self.red))
        pixels.append(Pixel(x + 2,  y + 3, *self.red))
        pixels.append(Pixel(x + 3,  y + 3, *self.red))
        pixels.append(Pixel(x + 6,  y + 3, *self.red))
        pixels.append(Pixel(x + 7,  y + 3, *self.red))
        pixels.append(Pixel(x + 10,  y + 3, *self.red))
        pixels.append(Pixel(x + 11,  y + 3, *self.red))
        pixels.append(Pixel(x + 12,  y + 3, *self.red))
        
        pixels.append(Pixel(x + 1,  y + 4, *self.red))
        pixels.append(Pixel(x + 2,  y + 4, *self.red))
        pixels.append(Pixel(x + 3,  y + 4, *self.red))
        pixels.append(Pixel(x + 4,  y + 4, *self.red))
        pixels.append(Pixel(x + 5,  y + 4, *self.red))
        pixels.append(Pixel(x + 6,  y + 4, *self.red))
        pixels.append(Pixel(x + 7,  y + 4, *self.red))
        pixels.append(Pixel(x + 8,  y + 4, *self.red))
        pixels.append(Pixel(x + 9,  y + 4, *self.red))
        pixels.append(Pixel(x + 10,  y + 4, *self.red))
        pixels.append(Pixel(x + 11,  y + 4, *self.red))
        pixels.append(Pixel(x + 12,  y + 4, *self.red))

        pixels.append(Pixel(x + 4,  y + 5, *self.red))
        pixels.append(Pixel(x + 5,  y + 5, *self.red))
        pixels.append(Pixel(x + 8,  y + 5, *self.red))
        pixels.append(Pixel(x + 9,  y + 5, *self.red))

        pixels.append(Pixel(x + 3,  y + 6, *self.red))
        pixels.append(Pixel(x + 4,  y + 6, *self.red))
        pixels.append(Pixel(x + 6,  y + 6, *self.red))
        pixels.append(Pixel(x + 7,  y + 6, *self.red))
        pixels.append(Pixel(x + 9,  y + 6, *self.red))
        pixels.append(Pixel(x + 10,  y + 6, *self.red))

        pixels.append(Pixel(x + 1,  y + 7, *self.red))
        pixels.append(Pixel(x + 2,  y + 7, *self.red))
        pixels.append(Pixel(x + 11,  y + 7, *self.red))
        pixels.append(Pixel(x + 12,  y + 7, *self.red))

        return pixels

    def getMediumInvaderPosition2(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 3,  y + 0, *self.red))
        pixels.append(Pixel(x + 9,  y + 0, *self.red))

        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))

        pixels.append(Pixel(x + 3,  y + 2, *self.red))
        pixels.append(Pixel(x + 4,  y + 2, *self.red))
        pixels.append(Pixel(x + 5,  y + 2, *self.red))
        pixels.append(Pixel(x + 6,  y + 2, *self.red))
        pixels.append(Pixel(x + 7,  y + 2, *self.red))
        pixels.append(Pixel(x + 8,  y + 2, *self.red))
        pixels.append(Pixel(x + 9,  y + 2, *self.red))

        # Eyes
        pixels.append(Pixel(x + 2,  y + 3, *self.red))
        pixels.append(Pixel(x + 3,  y + 3, *self.red))
        pixels.append(Pixel(x + 5,  y + 3, *self.red))
        pixels.append(Pixel(x + 6,  y + 3, *self.red))
        pixels.append(Pixel(x + 7,  y + 3, *self.red))
        pixels.append(Pixel(x + 9,  y + 3, *self.red))
        pixels.append(Pixel(x + 10,  y + 3, *self.red))

        pixels.append(Pixel(x + 1,  y + 4, *self.red))
        pixels.append(Pixel(x + 2,  y + 4, *self.red))
        pixels.append(Pixel(x + 3,  y + 4, *self.red))
        pixels.append(Pixel(x + 4,  y + 4, *self.red))
        pixels.append(Pixel(x + 5,  y + 4, *self.red))
        pixels.append(Pixel(x + 6,  y + 4, *self.red))
        pixels.append(Pixel(x + 7,  y + 4, *self.red))
        pixels.append(Pixel(x + 8,  y + 4, *self.red))
        pixels.append(Pixel(x + 9,  y + 4, *self.red))
        pixels.append(Pixel(x + 10,  y + 4, *self.red))
        pixels.append(Pixel(x + 11,  y + 4, *self.red))

        pixels.append(Pixel(x + 1,  y + 5, *self.red))
        pixels.append(Pixel(x + 3,  y + 5, *self.red))
        pixels.append(Pixel(x + 4,  y + 5, *self.red))
        pixels.append(Pixel(x + 5,  y + 5, *self.red))
        pixels.append(Pixel(x + 6,  y + 5, *self.red))
        pixels.append(Pixel(x + 7,  y + 5, *self.red))
        pixels.append(Pixel(x + 8,  y + 5, *self.red))
        pixels.append(Pixel(x + 9,  y + 5, *self.red))
        pixels.append(Pixel(x + 11,  y + 5, *self.red))

        pixels.append(Pixel(x + 1,  y + 6, *self.red))
        pixels.append(Pixel(x + 3,  y + 6, *self.red))
        pixels.append(Pixel(x + 9,  y + 6, *self.red))
        pixels.append(Pixel(x + 11,  y + 6, *self.red))

        pixels.append(Pixel(x + 4,  y + 7, *self.red))
        pixels.append(Pixel(x + 5,  y + 7, *self.red))
        pixels.append(Pixel(x + 7,  y + 7, *self.red))
        pixels.append(Pixel(x + 8,  y + 7, *self.red))

        return pixels

    def getMediumInvaderPosition1(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 3,  y + 0, *self.red))
        pixels.append(Pixel(x + 9,  y + 0, *self.red))

        pixels.append(Pixel(x + 1,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))
        pixels.append(Pixel(x + 11,  y + 1, *self.red))

        pixels.append(Pixel(x + 1,  y + 2, *self.red))
        pixels.append(Pixel(x + 3,  y + 2, *self.red))
        pixels.append(Pixel(x + 4,  y + 2, *self.red))
        pixels.append(Pixel(x + 5,  y + 2, *self.red))
        pixels.append(Pixel(x + 6,  y + 2, *self.red))
        pixels.append(Pixel(x + 7,  y + 2, *self.red))
        pixels.append(Pixel(x + 8,  y + 2, *self.red))
        pixels.append(Pixel(x + 9,  y + 2, *self.red))
        pixels.append(Pixel(x + 11,  y + 2, *self.red))

        # Eyes
        pixels.append(Pixel(x + 1,  y + 3, *self.red))
        pixels.append(Pixel(x + 2,  y + 3, *self.red))
        pixels.append(Pixel(x + 3,  y + 3, *self.red))
        pixels.append(Pixel(x + 5,  y + 3, *self.red))
        pixels.append(Pixel(x + 6,  y + 3, *self.red))
        pixels.append(Pixel(x + 7,  y + 3, *self.red))
        pixels.append(Pixel(x + 9,  y + 3, *self.red))
        pixels.append(Pixel(x + 10,  y + 3, *self.red))
        pixels.append(Pixel(x + 11,  y + 3, *self.red))

        pixels.append(Pixel(x + 1,  y + 4, *self.red))
        pixels.append(Pixel(x + 2,  y + 4, *self.red))
        pixels.append(Pixel(x + 3,  y + 4, *self.red))
        pixels.append(Pixel(x + 4,  y + 4, *self.red))
        pixels.append(Pixel(x + 5,  y + 4, *self.red))
        pixels.append(Pixel(x + 6,  y + 4, *self.red))
        pixels.append(Pixel(x + 7,  y + 4, *self.red))
        pixels.append(Pixel(x + 8,  y + 4, *self.red))
        pixels.append(Pixel(x + 9,  y + 4, *self.red))
        pixels.append(Pixel(x + 10,  y + 4, *self.red))
        pixels.append(Pixel(x + 11,  y + 4, *self.red))

        pixels.append(Pixel(x + 2,  y + 5, *self.red))
        pixels.append(Pixel(x + 3,  y + 5, *self.red))
        pixels.append(Pixel(x + 4,  y + 5, *self.red))
        pixels.append(Pixel(x + 5,  y + 5, *self.red))
        pixels.append(Pixel(x + 6,  y + 5, *self.red))
        pixels.append(Pixel(x + 7,  y + 5, *self.red))
        pixels.append(Pixel(x + 8,  y + 5, *self.red))
        pixels.append(Pixel(x + 9,  y + 5, *self.red))
        pixels.append(Pixel(x + 10,  y + 5, *self.red))

        pixels.append(Pixel(x + 3,  y + 6, *self.red))
        pixels.append(Pixel(x + 9,  y + 6, *self.red))

        pixels.append(Pixel(x + 2,  y + 7, *self.red))
        pixels.append(Pixel(x + 10,  y + 7, *self.red))

        return pixels

    def getSmallInvaderPosition2(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 4,  y + 0, *self.red))
        pixels.append(Pixel(x + 5,  y + 0, *self.red))

        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))

        pixels.append(Pixel(x + 2,  y + 2, *self.red))
        pixels.append(Pixel(x + 3,  y + 2, *self.red))
        pixels.append(Pixel(x + 4,  y + 2, *self.red))
        pixels.append(Pixel(x + 5,  y + 2, *self.red))
        pixels.append(Pixel(x + 6,  y + 2, *self.red))
        pixels.append(Pixel(x + 7,  y + 2, *self.red))

        # Eyes
        pixels.append(Pixel(x + 1,  y + 3, *self.red))
        pixels.append(Pixel(x + 2,  y + 3, *self.red))
        pixels.append(Pixel(x + 4,  y + 3, *self.red))
        pixels.append(Pixel(x + 5,  y + 3, *self.red))
        pixels.append(Pixel(x + 7,  y + 3, *self.red))
        pixels.append(Pixel(x + 8,  y + 3, *self.red))

        pixels.append(Pixel(x + 1,  y + 4, *self.red))
        pixels.append(Pixel(x + 2,  y + 4, *self.red))
        pixels.append(Pixel(x + 3,  y + 4, *self.red))
        pixels.append(Pixel(x + 4,  y + 4, *self.red))
        pixels.append(Pixel(x + 5,  y + 4, *self.red))
        pixels.append(Pixel(x + 6,  y + 4, *self.red))
        pixels.append(Pixel(x + 7,  y + 4, *self.red))
        pixels.append(Pixel(x + 8,  y + 4, *self.red))

        pixels.append(Pixel(x + 2,  y + 5, *self.red))
        pixels.append(Pixel(x + 4,  y + 5, *self.red))
        pixels.append(Pixel(x + 5,  y + 5, *self.red))
        pixels.append(Pixel(x + 7,  y + 5, *self.red))

        pixels.append(Pixel(x + 1,  y + 6, *self.red))
        pixels.append(Pixel(x + 8,  y + 6, *self.red))

        pixels.append(Pixel(x + 2,  y + 7, *self.red))
        pixels.append(Pixel(x + 7,  y + 7, *self.red))

        return pixels

    def getSmallInvaderPosition1(self, x, y, inverse = False):
        pixels = []
        pixels.append(Pixel(x + 4,  y + 0, *self.red))
        pixels.append(Pixel(x + 5,  y + 0, *self.red))

        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))

        pixels.append(Pixel(x + 2,  y + 2, *self.red))
        pixels.append(Pixel(x + 3,  y + 2, *self.red))
        pixels.append(Pixel(x + 4,  y + 2, *self.red))
        pixels.append(Pixel(x + 5,  y + 2, *self.red))
        pixels.append(Pixel(x + 6,  y + 2, *self.red))
        pixels.append(Pixel(x + 7,  y + 2, *self.red))

        # Eyes
        pixels.append(Pixel(x + 1,  y + 3, *self.red))
        pixels.append(Pixel(x + 2,  y + 3, *self.red))
        pixels.append(Pixel(x + 4,  y + 3, *self.red))
        pixels.append(Pixel(x + 5,  y + 3, *self.red))
        pixels.append(Pixel(x + 7,  y + 3, *self.red))
        pixels.append(Pixel(x + 8,  y + 3, *self.red))

        pixels.append(Pixel(x + 1,  y + 4, *self.red))
        pixels.append(Pixel(x + 2,  y + 4, *self.red))
        pixels.append(Pixel(x + 3,  y + 4, *self.red))
        pixels.append(Pixel(x + 4,  y + 4, *self.red))
        pixels.append(Pixel(x + 5,  y + 4, *self.red))
        pixels.append(Pixel(x + 6,  y + 4, *self.red))
        pixels.append(Pixel(x + 7,  y + 4, *self.red))
        pixels.append(Pixel(x + 8,  y + 4, *self.red))

        pixels.append(Pixel(x + 3,  y + 5, *self.red))
        pixels.append(Pixel(x + 6,  y + 5, *self.red))

        pixels.append(Pixel(x + 2,  y + 6, *self.red))
        pixels.append(Pixel(x + 4,  y + 6, *self.red))
        pixels.append(Pixel(x + 5,  y + 6, *self.red))
        pixels.append(Pixel(x + 7,  y + 6, *self.red))

        pixels.append(Pixel(x + 1,  y + 7, *self.red))
        pixels.append(Pixel(x + 3,  y + 7, *self.red))
        pixels.append(Pixel(x + 6,  y + 7, *self.red))
        pixels.append(Pixel(x + 8,  y + 7, *self.red))


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
    invader = Invader()
    if (not invader.process()):
        invader.print_help()

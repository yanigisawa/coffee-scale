#!/usr/bin/env python
import curses
import random
import os
from samplebase import SampleBase
from threading import Thread, Lock

COLUMNS = 'qwertyuiopasdfgh'


class KeyboardInput(SampleBase):
    """
        Class expects to wait for keyboard input to begin rendering pixels.
        Once a key is pressed, this class will start running methods of the name
        "__X__()" where X is an incrementing integer from 0. If no method is found,
        the counter resets to 0, and the class will begin drawing over.
        The screen is cleared between each method call.
    """
    red = (255, 0, 0)
    yellow = (125, 125, 0)
    flesh = (155, 155, 0)
    brown = (32, 5, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)

    def __init__(self, *args, **kwargs):
        super(KeyboardInput, self).__init__(*args, **kwargs)
        self.animate = False
        self.configure_args()
        self.canvas = self.matrix.CreateFrameCanvas()
        self.win = None
        self.current = 0

    def __0__(self):
        column = 4
        for row in range(10, 12):
            color = self.get_color()
            self.canvas.SetPixel(column, row, *self.red)
            self.canvas.SetPixel(column+1, row, *self.red)

    def __1__(self):
        column = 4
        for row in range(10, 12):
            self.canvas.SetPixel(column, row, *self.yellow)
            self.canvas.SetPixel(column+1, row, *self.yellow)

    def __2__(self):
        column = 8
        for row in range(10, 12):
            self.canvas.SetPixel(column, row, *self.blue)
            self.canvas.SetPixel(column+1, row, *self.blue)

    def __3__(self):
        column = 10
        for row in range(10, 12):
            self.canvas.SetPixel(column, row, *self.white)
            self.canvas.SetPixel(column+1, row, *self.white)

    def __4__(self):
        column = 12
        for row in range(10, 12):
            self.canvas.SetPixel(column, row, *self.white)
            self.canvas.SetPixel(column+1, row, *self.white)


    def __5__(self):
        column = 4
        for row in range(10, 12):
            color = self.get_color()
            self.canvas.SetPixel(column, row, *self.red)
            self.canvas.SetPixel(column+1, row, *self.red)

    def __6__(self):
        column = 4
        for row in range(10, 12):
            self.canvas.SetPixel(column, row, *self.yellow)
            self.canvas.SetPixel(column+1, row, *self.yellow)

    def __7__(self):
        column = 12
        for row in range(10, 12):
            self.canvas.SetPixel(column, row, *self.blue)
            self.canvas.SetPixel(column+1, row, *self.blue)

    def __8__(self):
        column = 10
        for row in range(10, 12):
            self.canvas.SetPixel(column, row, *self.white)
            self.canvas.SetPixel(column+1, row, *self.white)

    def __9__(self):
        column = 12
        for row in range(10, 12):
            self.canvas.SetPixel(column, row, *self.white)
            self.canvas.SetPixel(column+1, row, *self.white)

    def __10__(self):
        column = 12
        for row in range(10, 12):
            self.canvas.SetPixel(column, row, *self.white)
            self.canvas.SetPixel(column+1, row, *self.white)

    def __11__(self):
        pass

    def __22__(self):
        for row in range(16, 32):
            for column in range(32, 64):
                self.canvas.SetPixel(column, row, *self.white)


    def __33__(self):
        for row in range(16, 32):
            for column in range(32):
                self.canvas.SetPixel(column, row, *self.white)


    def __44__(self):
        for row in range(32):
            for column in range(32, 48):
                self.canvas.SetPixel(column, row, *self.white)


    def __55__(self):
        for row in range(32):
            for column in range(16):
                self.canvas.SetPixel(column, row, *self.white)




    def stop(self):
        self.clear_screen()

    def clear_screen(self):
        self.win.addstr("\nClear: {0} - {1}".format(self.canvas.width, self.canvas.height))
        for i in range(self.canvas.width):
            for j in range(self.canvas.height):
                self.canvas.SetPixel(i, j, 0, 0, 0)

        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def get_color(self):
        rgb = []
        for i in range(3):
            rgb.append(random.randint(0, 255))

        return tuple(rgb)

    def drawNext(self):
        """
            Configure a list of methods within this class to call
            to draw the pixels to the screen.
            The list will be initialized during the __init__ method.
            A counter will be set to 0, and drawNext here will
            iterate over the methods calling each in sequence.
        """
        self.win.addstr("\n Called Draw Next - {0}".format(self.current))

        m = "__{0}__".format(self.current)
        if not hasattr(self, m):
            self.current = 0
            m = "__{0}__".format(self.current)


        self.win.addstr("\n Later Called Draw Next - {0}".format(self.current))

        self.win.addstr("\n Called Draw Next - {0}".format(m))
        self.win.addstr("\nCall Method: {0}".format(m))

        self.current += 1
        getattr(self, m)()

    def run(self, key=""):
        self.clear_screen()
        self.canvas = self.matrix.SwapOnVSync(self.canvas)

        self.win.addstr("Called Run")
        self.drawNext()
        self.canvas = self.matrix.SwapOnVSync(self.canvas)


    def main(self, win):
        self.animate = True
        win.nodelay(True)
        self.win = win
        prev_key, key="", ""
        win.clear()
        win.addstr("Detected key:")
        iterations = 0
        while True:
            try:
                key = win.getkey()
                win.clear()
                win.addstr(str(key))
                if key == os.linesep:
                    self.stop()
                    break
                key = str(key)
                self.win.addstr("Before checking KEY - run")
                if key:
                    self.win.addstr("\nIterations: {0}".format(iterations))
                    iterations += 1
                    self.run()

            except Exception as e:
                # No input
                pass


# Main function
if __name__ == "__main__":
    keyboard_input = KeyboardInput()
    curses.wrapper(keyboard_input.main)

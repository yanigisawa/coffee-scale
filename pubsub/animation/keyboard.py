#!/usr/bin/env python
import curses
import random
import os
from samplebase import SampleBase
from threading import Thread, Lock
from golbase import GameOfLifeBase, Cell

COLUMNS = 'qwertyuiopasdfgh'


class KeyboardInput(GameOfLifeBase):
    def __init__(self, *args, **kwargs):
        super(KeyboardInput, self).__init__(*args, **kwargs)
        self.animate = False
        self.lock = Lock()
        self.configure_args()
        # self.canvas = self.matrix.CreateFrameCanvas()
        self.canvas = self.matrix.SwapOnVSync(self.canvas)


    def stop(self):
        self.animate = False
        if self.animate_thread is not None:
            self.animate_thread.join()
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

    def run_rows(self, key="k"):
        self.win.addstr("{0} / {1} - {2}".format(self.canvas.width, self.canvas.height, key))
        if key not in COLUMNS:
            return

        self.clear_screen()
        row = COLUMNS.find(key) * 2
        for column in range(self.canvas.width):
            color = self.get_color()
            self.canvas.SetPixel(column, row, *self.get_color())
            self.canvas.SetPixel(column, row + 1, *self.get_color())

        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def run_both(self, key="k"):
        self.win.addstr("{0} / {1} - {2}".format(self.canvas.width, self.canvas.height, key))
        if key not in COLUMNS:
            return

        self.clear_screen()
        row = COLUMNS[::-1].find(key) * 2
        for column in range(32):
            color = self.get_color()
            self.canvas.SetPixel(column, row, *self.get_color())
            self.canvas.SetPixel(column, row + 1, *self.get_color())

        column = 32 + (COLUMNS.find(key) * 2)
        for row in range(32):
            color = self.get_color()
            self.canvas.SetPixel(column, row, *self.get_color())
            self.canvas.SetPixel(column + 1, row, *self.get_color())

        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def run(self, key=""):
        self.win.addstr("Called Run")
        self.drawCells()
        self.evolve()
        self.canvas = self.matrix.SwapOnVSync(self.canvas)





    def main(self, win):
        self.animate = True
        win.nodelay(True)
        self.win = win
        prev_key, key="", ""
        win.clear()
        win.addstr("Detected key:")
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
                    self.win.addstr("Calling run")
                    self.run()
                    # with self.lock:
                    #     if self.animate:
                    #         self.stop()
                    #     self.animate = True
                    # self.animate_thread = Thread(target=self.run, args=(key))
                    # self.animate_thread.start()
                    # prev_key = key
            except Exception as e:
                # No input
                pass


# Main function
if __name__ == "__main__":
    keyboard_input = KeyboardInput()
    curses.wrapper(keyboard_input.main)

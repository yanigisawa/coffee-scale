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
        self.canvas = self.matrix.CreateFrameCanvas()
        self.initializeCells()
        self.win = None
        self.animate_thread = None
        # self.block_switch()
        self.gosper_gun()
        # self.drawCells()

    def block_switch(self):
        x = 8
        y = 15
        self.cells[x + 11][y + 6].alive = True
        self.cells[x + 13][y + 6].alive = True
        self.cells[x + 13][y + 5].alive = True
        self.cells[x + 15][y + 4].alive = True
        self.cells[x + 15][y + 3].alive = True
        self.cells[x + 15][y + 2].alive = True
        self.cells[x + 17][y + 3].alive = True
        self.cells[x + 17][y + 2].alive = True
        self.cells[x + 17][y + 1].alive = True
        self.cells[x + 18][y + 2].alive = True

    def gosper_gun(self):
        x, y = 20, 7
        self.cells[x][y + 5].alive = True
        self.cells[x + 1][y + 5].alive = True
        self.cells[x][y + 6].alive = True
        self.cells[x + 1][y + 6].alive = True

        self.cells[x + 10][y + 5].alive = True
        self.cells[x + 10][y + 6].alive = True
        self.cells[x + 10][y + 7].alive = True
        self.cells[x + 11][y + 4].alive = True
        self.cells[x + 11][y + 8].alive = True
        self.cells[x + 12][y + 3].alive = True
        self.cells[x + 12][y + 9].alive = True
        self.cells[x + 13][y + 3].alive = True
        self.cells[x + 13][y + 9].alive = True
        self.cells[x + 14][y + 6].alive = True

        self.cells[x + 15][y + 4].alive = True
        self.cells[x + 15][y + 8].alive = True
        self.cells[x + 16][y + 5].alive = True
        self.cells[x + 16][y + 6].alive = True
        self.cells[x + 16][y + 7].alive = True
        self.cells[x + 17][y + 6].alive = True
        self.cells[x + 20][y + 5].alive = True
        self.cells[x + 20][y + 4].alive = True
        self.cells[x + 20][y + 3].alive = True
        self.cells[x + 21][y + 5].alive = True
        self.cells[x + 21][y + 4].alive = True
        self.cells[x + 21][y + 3].alive = True
        self.cells[x + 22][y + 2].alive = True
        self.cells[x + 22][y + 6].alive = True
        self.cells[x + 24][y + 2].alive = True
        self.cells[x + 24][y + 1].alive = True
        self.cells[x + 24][y + 6].alive = True
        self.cells[x + 24][y + 7].alive = True

        self.cells[x + 34][y + 4].alive = True
        self.cells[x + 34][y + 5].alive = True
        self.cells[x + 35][y + 4].alive = True
        self.cells[x + 35][y + 5].alive = True


    def makeGlider(self, x, y):
        self.cells[x + 0][y + 2].alive = True
        self.cells[x + 1][y + 2].alive = True
        self.cells[x + 2][y + 2].alive = True
        self.cells[x + 2][y + 1].alive = True
        self.cells[x + 1][y + 0].alive = True

    def red_glider(self):
        for i in range(0, 60, 5):
            for j in range(0, 27, 5):
                self.makeGlider(i, j)

    def acorn(self):
        x = 29
        self.cells[x][16].alive = True
        self.cells[x + 1][16].alive = True
        self.cells[x + 1][14].alive = True
        self.cells[x + 3][15].alive = True
        self.cells[x + 3][16].alive = True
        self.cells[x + 4][16].alive = True
        self.cells[x + 5][16].alive = True

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


    def run(self, key=""):
        self.drawCells()
        self.canvas = self.matrix.SwapOnVSync(self.canvas)
        self.evolve()


    def main(self, win):
        self.animate = True
        win.nodelay(True)
        self.win = win
        prev_key, key="", ""
        iterations = 0
        # for _ in range(75):
        #     self.evolve()
        # self.drawCells()
        # self.canvas = self.matrix.SwapOnVSync(self.canvas)
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
                if key:
                    # with self.lock:
                    #     if self.animate:
                    #         self.stop()
                    #     self.animate = True
                    win.addstr("\nIterations: {0}".format(iterations))
                    self.run()
                    iterations += 1
            except Exception as e:
                # No input
                pass


# Main function
if __name__ == "__main__":
    keyboard_input = KeyboardInput()
    curses.wrapper(keyboard_input.main)

#!/usr/bin/env python
from golbase import GameOfLifeBase, Cell
import random
import time


class GameOfLifeGlider(GameOfLifeBase):
    def __init__(self, *args, **kwargs):
        super(GameOfLifeGlider, self).__init__(*args, **kwargs)

    def makeGlider(self, x, y):
        self.cells[x + 0][y + 2].alive = True
        self.cells[x + 1][y + 2].alive = True
        self.cells[x + 2][y + 2].alive = True
        self.cells[x + 2][y + 1].alive = True
        self.cells[x + 1][y + 0].alive = True

    def run(self):
        self.initializeCells()
            
        self.makeGlider(0, 0)
        self.makeGlider(5, 0)
        self.makeGlider(10, 0)
        self.makeGlider(16, 0)
        self.makeGlider(21, 0)
        self.makeGlider(26, 0)
        self.makeGlider(0, 6)
        self.makeGlider(5, 6)
        self.makeGlider(10, 6)
        self.makeGlider(16, 6)
        self.makeGlider(21, 6)
        self.makeGlider(26, 6)

        self.makeGlider(0, 11)
        self.makeGlider(5, 11)
        self.makeGlider(10, 11)
        self.makeGlider(16, 11)
        self.makeGlider(21, 11)
        self.makeGlider(26, 11)

        while True:

            self.drawCells()
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

            time.sleep(0.2)
            self.evolve()


# Main function
if __name__ == "__main__":
    gol = GameOfLifeGlider()
    if (not gol.process()):
        gol.print_help()

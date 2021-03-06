#!/usr/bin/env python
from golbase import GameOfLifeBase, Cell
import random
import time


# Pentadecathlon
class GameOfLifePent(GameOfLifeBase):
    def __init__(self, *args, **kwargs):
        super(GameOfLifePent, self).__init__(*args, **kwargs)

    def run(self):
        self.initializeCells()
            
        x, y = 15, 3
        self.cells[x + 3][y + 4].alive = True
        self.cells[x + 3][y + 5].alive = True
        self.cells[x + 3][y + 6].alive = True
        self.cells[x + 4][y + 5].alive = True
        self.cells[x + 5][y + 5].alive = True
        self.cells[x + 6][y + 4].alive = True
        self.cells[x + 6][y + 5].alive = True
        self.cells[x + 6][y + 6].alive = True
        self.cells[x + 8][y + 4].alive = True
        self.cells[x + 8][y + 5].alive = True
        self.cells[x + 8][y + 6].alive = True
        self.cells[x + 9][y + 4].alive = True
        self.cells[x + 9][y + 5].alive = True
        self.cells[x + 9][y + 6].alive = True
        self.cells[x + 11][y +4].alive = True
        self.cells[x + 11][y + 5].alive = True
        self.cells[x + 11][y + 6].alive = True
        self.cells[x + 12][y + 5].alive = True
        self.cells[x + 13][y + 5].alive = True
        self.cells[x + 14][y + 4].alive = True
        self.cells[x + 14][y + 5].alive = True
        self.cells[x + 14][y + 6].alive = True

        while True:

            self.drawCells()
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

            time.sleep(0.5)
            self.evolve()


# Main function
if __name__ == "__main__":
    gol = GameOfLifePent()
    if (not gol.process()):
        gol.print_help()

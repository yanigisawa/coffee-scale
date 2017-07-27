#!/usr/bin/env python
from golbase import GameOfLifeBase, Cell
import random
import time


class GameOfLifeGosper(GameOfLifeBase):
    def __init__(self, *args, **kwargs):
        super(GameOfLifeGosper, self).__init__(*args, **kwargs)

    def run(self):
        self.initializeCells()
            
        x, y = 0, 0
        self.cells[x + 1][y + 5].alive = True
        self.cells[x + 2][y + 5].alive = True
        self.cells[x + 1][y + 6].alive = True
        self.cells[x + 2][y + 6].alive = True
        self.cells[x + 11][y + 6].alive = True
        self.cells[x + 11][y + 7].alive = True
        self.cells[x + 11][y + 8].alive = True
        self.cells[x + 12][y + 5].alive = True
        self.cells[x + 12][y + 9].alive = True
        self.cells[x + 13][y + 4].alive = True
        self.cells[x + 13][y + 10].alive = True
        self.cells[x + 13][y + 4].alive = True
        self.cells[x + 13][y + 10].alive = True
        self.cells[x + 14][y + 7].alive = True
        self.cells[x + 15][y + 5].alive = True
        self.cells[x + 15][y + 9].alive = True
        self.cells[x + 16][y + 6].alive = True
        self.cells[x + 16][y + 7].alive = True
        self.cells[x + 16][y + 8].alive = True
        self.cells[x + 17][y + 7].alive = True
        self.cells[x + 20][y + 6].alive = True
        self.cells[x + 20][y + 5].alive = True
        self.cells[x + 20][y + 4].alive = True
        self.cells[x + 21][y + 6].alive = True
        self.cells[x + 21][y + 5].alive = True
        self.cells[x + 21][y + 4].alive = True
        self.cells[x + 22][y + 3].alive = True
        self.cells[x + 22][y + 7].alive = True
        self.cells[x + 24][y + 3].alive = True
        self.cells[x + 24][y + 2].alive = True
        self.cells[x + 24][y + 7].alive = True
        self.cells[x + 24][y + 8].alive = True

        while True:

            self.drawCells()
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

            time.sleep(0.2)
            self.evolve()


# Main function
if __name__ == "__main__":
    gol = GameOfLifeGosper()
    if (not gol.process()):
        gol.print_help()

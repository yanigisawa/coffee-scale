#!/usr/bin/env python
from golbase import GameOfLifeBase, Cell
import random
import time


class GameOfLifeAtom(GameOfLifeBase):
    def __init__(self, *args, **kwargs):
        super(GameOfLifeAtom, self).__init__(*args, **kwargs)
        # self.toroidal = False


    def run(self):
        self.initializeCells()

        x, y  = 28, 13
        self.cells[x][y + 2].alive = True
        self.cells[x + 1][y + 2].alive = True
        self.cells[x + 1][y].alive = True
        self.cells[x + 3][y + 1].alive = True
        self.cells[x + 3][y + 2].alive = True
        self.cells[x + 4][y + 2].alive = True
        self.cells[x + 5][y + 2].alive = True

        # self.cells[11][8].alive = True
        # self.cells[12][8].alive = True
        # self.cells[12][6].alive = True
        # self.cells[14][7].alive = True
        # self.cells[14][8].alive = True
        # self.cells[15][8].alive = True
        # self.cells[16][8].alive = True

        while True:

            self.drawCells()
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

            time.sleep(0.1) # 3643529415130615)
            self.evolve()


# Main function
if __name__ == "__main__":
    gol = GameOfLifeAtom()
    if (not gol.process()):
        gol.print_help()

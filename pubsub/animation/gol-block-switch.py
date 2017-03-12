#!/usr/bin/env python
from golbase import GameOfLifeBase, Cell
import random
import time


class GameOfLifeBlockSwitch(GameOfLifeBase):
    def __init__(self, *args, **kwargs):
        super(GameOfLifeBlockSwitch, self).__init__(*args, **kwargs)
        self.toroidal = True

        
    def run(self):
        self.initializeCells()
            
        y = 0
        self.cells[11][y + 6].alive = True
        self.cells[13][y + 6].alive = True
        self.cells[13][y + 5].alive = True
        self.cells[15][y + 4].alive = True
        self.cells[15][y + 3].alive = True
        self.cells[15][y + 2].alive = True
        self.cells[17][y + 3].alive = True
        self.cells[17][y + 2].alive = True
        self.cells[17][y + 1].alive = True
        self.cells[18][y + 2].alive = True

        while True:

            self.drawCells()
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

            time.sleep(0.2)
            self.evolve()


# Main function
if __name__ == "__main__":
    gol = GameOfLifeBlockSwitch()
    if (not gol.process()):
        gol.print_help()

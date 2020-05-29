#!/usr/bin/env python
from golbase import GameOfLifeBase, Cell
import random
import time
import logging

class GameOfLifeBlockSwitch(GameOfLifeBase):
    def __init__(self, *args, **kwargs):
        super(GameOfLifeBlockSwitch, self).__init__(*args, **kwargs)
        self.toroidal = True

        
    def run(self):
        self.initializeCells()
            
        y = 15 
        x = 8
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

        ms_delay = 0.5313076904003437
        print("delay = {0}".format(ms_delay))
        while True:

            self.drawCells()
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

            time.sleep(ms_delay)
            self.evolve()


# Main function
if __name__ == "__main__":
    gol = GameOfLifeBlockSwitch()
    if (not gol.process()):
        gol.print_help()

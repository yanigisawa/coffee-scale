#!/usr/bin/env python
from golbase import GameOfLifeBase, Cell
import random
import time
import logging

class GameOfLifeRandom(GameOfLifeBase):
    def __init__(self, *args, **kwargs):
        super(GameOfLifeRandom, self).__init__(*args, **kwargs)
        self.toroidal = True

    def reset(self):
        self.initializeCells()
        self._evolutionQueue = []
        self.get_random_config()

    def get_random_config(self):
        active_cells = random.randint(10, self.matrix.width * self.matrix.height)
        for _ in range(active_cells):
            x = random.randint(0, self.matrix.width -1)
            y = random.randint(0, self.matrix.height - 1)
            self.cells[x][y].alive = True


    def run(self):
        self.initializeCells()

        self.get_random_config()

        ms_delay = 0.1
        print("delay = {0}".format(ms_delay))
        while True:

            self.drawCells()
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

            time.sleep(ms_delay)
            self.evolve()


# Main function
if __name__ == "__main__":
    gol = GameOfLifeRandom()
    if (not gol.process()):
        gol.print_help()

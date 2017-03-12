#!/usr/bin/env python
"""
This is an example script that is already setup to run the Game of Life
The only part you need to modify starts in the run() method below, under
the "Set Initial Cell State Here" comment (~ line 20)
"""

from golbase import GameOfLifeBase, Cell
import random
import time


class GameOfLifeSkeleton(GameOfLifeBase):
    def __init__(self, *args, **kwargs):
        super(GameOfLifeSkeleton, self).__init__(*args, **kwargs)
        
    def run(self):
        self.initializeCells()
            
        # Set Initial Cell State here
        # self.cells[0][0].alive = True
        # self.cells[1][1].alive = True
        # self.cells[2][2].alive = True
        # self.cells[3][3].alive = True

        while True:

            self.drawCells()
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

            time.sleep(0.2)
            self.evolve()


# Main function
if __name__ == "__main__":
    gol = GameOfLifeSkeleton()
    if (not gol.process()):
        gol.print_help()

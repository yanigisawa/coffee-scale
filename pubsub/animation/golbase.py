#!/usr/bin/env python
from samplebase import SampleBase
import random
import time


class Cell(object):
    x = 0
    y = 0
    alive = False
    neighborCount = 0

    def __init__(self, x = 0, y = 0, alive = False):
        self.x = x
        self.y = y
        self.alive = alive

    def getColor(self):
        if not self.alive: 
            return (0, 0, 0)

        rgb = []
        for i in range(3):
            rgb.append(random.randint(0, 255))

        return tuple(rgb)

class GameOfLifeBase(SampleBase):
    # Stitch edges together for 'infinite' cell array
    toroidal = True

    def __init__(self, *args, **kwargs):
        super(GameOfLifeBase, self).__init__(*args, **kwargs)


    def initializeCells(self):
        self.canvas = self.matrix.CreateFrameCanvas()
        self.cells = []
        for i in range(self.canvas.width):
            row = []
            for j in range(self.canvas.height):
                row.append(Cell(i, j, False))
            self.cells.append(row)

    def drawCells(self):
        for row in self.cells:
            for c in row:
                self.canvas.SetPixel(c.x, c.y, *c.getColor())

    def countNeighbors(self, c, cells):
        coords = [-1, 0, 1]
        xcomp, ycomp = 0, 0
        neighborCount = 0

        for x in coords:
            for y in coords:
                xcomp = c.x + x

                if not self.toroidal:
                    if xcomp < 0 or xcomp >= len(cells):
                        continue

                if xcomp < 0:
                    xcomp = len(cells) - 1
                elif xcomp >= len(cells):
                    xcomp = 0

                ycomp = c.y + y

                if not self.toroidal:
                    if ycomp < 0 or ycomp >= len(cells[0]):
                        continue

                if ycomp < 0:
                    ycomp = len(cells[0]) - 1
                elif ycomp >= len(cells[0]):
                    ycomp = 0

                if xcomp == c.x and ycomp == c.y:
                    continue

                if cells[xcomp][ycomp].alive:
                    neighborCount += 1

        return neighborCount

    def evolve(self):
        """
        Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
        Any live cell with two or three live neighbours lives on to the next generation.
        Any live cell with more than three live neighbours dies, as if by overpopulation.
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        # for each cell, count # of neighbors
        # if less than 2 or more than 3, cell dies
        # if dead and has 3 neighbors, cell becomes alive

        for row in self.cells:
            for c in row:
                c.neighborCount = self.countNeighbors(c, self.cells)

        for row in self.cells:
            for c in row:
                if c.neighborCount < 2 or c.neighborCount > 3:
                    c.alive = False
                elif c.neighborCount == 3:
                    c.alive = True
        return self.cells

        

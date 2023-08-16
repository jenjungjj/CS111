#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *

def alive_neighbors(posnr, posnc, grid):
    """ returns the number of alive neighbors of a cell at position [posnr, posnc]
    """
    alive_count = 0
    for r in range(posnr-1, posnr+2):
        for c in range(posnc-1, posnc+2):
            if grid[r][c] == 1:
                alive_count += 1
                if r == posnr and c == posnc:
                    alive_count -= 1
    return alive_count


def next_gen(grid):
    """ returns a new 2D list representing the next generation of cells 
        using the Game of Life rules 
    """
    new_grid = copy(grid)
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[0])-1):
            count = alive_neighbors(r,c,grid)
            if count < 2 or count > 3:
                new_grid[r][c] = 0
            elif count == 3:
                new_grid[r][c] = 1
    return new_grid
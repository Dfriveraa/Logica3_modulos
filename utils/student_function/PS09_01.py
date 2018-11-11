import numpy as np
def find_target(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j]=="T"):
                target=(i,j)
    
    return target
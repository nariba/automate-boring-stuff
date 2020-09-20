#!/usr/bin/python3

grid = \
    [['.', '.', '.', '.', '.', '.'],
    ['.', 'o', 'o', '.', '.', '.'],
    ['o', 'o', 'o', 'o', '.', '.'],
    ['o', 'o', 'o', 'o', 'o', '.'],
    ['.', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', '.'],
    ['o', 'o', 'o', 'o', '.', '.'],
    ['.', 'o', 'o', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']]

def transpose(grid, newgrid):
    y = len(grid)
    x = len(grid[0])
    pivot_x = 0
    pivot_y = 0
    for i in range(x-1):
        newgrid.append([])
    
    for i in grid:
        for j in i:
            newgrid[pivot_x].append(j)
            pivot_x = (pivot_x + 1) % x
        pivot_y = (pivot_y + 1) % y

if __name__ == "__main__":
    newgrid = [[]]
    transpose(grid, newgrid)
    for i in grid:
        print(i)
    for i in newgrid:
        print(i)


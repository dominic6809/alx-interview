#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Params:
        grid (list of list of int):
        A grid where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract 2 for each horizontal adjacency
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Subtract 2 for each vertical adjacency
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter

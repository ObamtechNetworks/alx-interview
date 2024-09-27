#!/usr/bin/python3
"""The Island Perimeter"""


def island_perimeter(grid) -> int:
    """Function that returns the perimeter of the
    island described in grid.

    Args:
        grid (List of lists): A 2D list representing the grid.

    Returns:
        int: perimeter of the island in the grid.
    """
    # edge cases
    if not grid or not isinstance(grid, list) \
            or len(grid) == 0 or len(grid[0]) == 0:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Iterate through the grid using index values
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Each land cell contributes 4 to the perimeter initially
                perimeter += 4

                # Check up if the neighboring cell is land
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge

                # Check left if the neighboring cell is land
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge

    return perimeter

"""
You are given an n X m grid where each cell
contains one character A, B, C or D.
For each cell, you must change the character to
A, B, C or D. The new character must be different from the old one.
Your task is to change the characters in every cell
such that no two adjacent cells have the same character.
Input
The first line has two integers n and m: the number of rows and columns.
The next n lines each have m characters: the description of the grid.
Output
Print n lines each with m characters: the description of the final grid.
You may print any valid solution.
If no solution exists, just print IMPOSSIBLE.
Constraints

1 <= n, m <= 500

Example
Input:
3 4
AAAA
BBBB
CCDD

Output:
CDCD
DCDC
ABAB


CDCD
ACAC
BABA

For every cell gather its valid neighbors but
we should think that the cells towards right and
down are not filled and we will not use the initial
values of the colors stored in those cell
(row-1, col)
(row, col-1)
(row, col)
Pick a color which does not belong to the
above colors set and place it in current
cell

Go on doing this for every other cell
The original color set is {A,B,C,D}
So we need to do set difference to get
the next uncolored node.

If we get this difference as empty we stop
"""


def print_helper(grid):
    for row in grid:
        for element in row:
            print(element, end="")
        print()


def is_valid_cell(cell, n, m):
    row, col = cell
    return row >= 0 and col >= 0 and row < n and col < m


def solve():
    n, m = list(map(int, input().split(' ')))
    grid = []
    for _ in range(n):
        row = input()
        grid.append(list(row))

    directions = [(-1, 0), (0, -1)]
    valid_colors = ['A', 'B', 'C', 'D']

    for row in range(n):
        for col in range(m):
            current_cell = grid[row][col]
            colored_set = set()
            colored_set.add(current_cell)
            for direction in directions:
                # Fill the colors of neighbors that we have visited
                new_cell = (row + direction[0], col + direction[1])
                if is_valid_cell(new_cell, n, m):
                    new_cell_value = grid[new_cell[0]][new_cell[1]]
                    colored_set.add(new_cell_value)

            next_color = ''
            for color in valid_colors:
                # Iterate from A to D to fill available color
                if color not in colored_set:
                    next_color = color
                    break
            else:
                print("IMPOSSIBLE")
                return
            # Fill the next color in current cell
            grid[row][col] = next_color

    print_helper(grid)


if __name__ == "__main__":
    solve()

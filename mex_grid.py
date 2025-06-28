"""
Your task is to construct an n X n grid where each square
has the smallest nonnegative integer that does not appear to
the left on the same row or above on the same column.
Input
The only line has an integer n.
Output
Print the grid according to the example.
Constraints

1 <= n <= 100

Example
Input:
5

Output:
0 1 2 3 4
1 0 3 2 5
2 3 0 1 6
3 2 1 0 7
4 5 6 7 0


Idea: Just run the simulation to place a smallest non-negative
number in the cell by checking it does not exist to left or up

Smallest Non-Negative Number while loop from 0 till we find valid candidate
Number not existing in up and left elements, use a set to determine
in O(1) time if it exists
"""


def print_helper(grid):
    for row in grid:
        for element in row:
            print(element, end=" ")
        print()


def solve():
    n = int(input())
    grid = [[0] * n for _ in range(n)]

    for row in range(0, n):
        elements_used = set()
        for col in range(0, n):
            if row == 0 and col == 0:
                elements_used.add(0)
                continue

            candidate = 0
            left = set([grid[row][pcol] for pcol in range(0, col)]) if col > 0 else set()
            up = set([grid[prow][col] for prow in range(0, row)]) if row > 0 else set()
            while (candidate in elements_used or
                   candidate in left or
                   candidate in up):
                candidate += 1

            grid[row][col] = candidate
            elements_used.add(candidate)

    print_helper(grid)


if __name__ == "__main__":
    solve()

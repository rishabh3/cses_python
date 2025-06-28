"""
Idea: Graph pattern

If a knight is in cell (x, y)
the cells it can move to are
(x+1, y+2)
(x+2, y+1)
(x-1, y-2)
(x-2, y-1)
(x-1, y+2)
(x+2, y-1)
(x+1, y-2)
(x-2, y+1)

Now starting with cell (0, 0) with moves as 0
we can use BFS traversal to find minimum moves
to each cell
"""


from collections import deque


def is_valid_cell(cell, n):
    row, col = cell
    return row >= 0 and col >= 0 and row < n and col < n


def yet_to_visit(grid, cell):
    row, col = cell
    return grid[row][col] == -1


def mark_visited(grid, cell, moves):
    row, col = cell
    grid[row][col] = moves


def print_helper(grid):
    for row in grid:
        for element in row:
            print(element, end=" ")
        print()


def solve():
    n = int(input())

    grid = [[-1] * n for _ in range(n)]

    queue = deque([((0, 0), 0)])
    movement_direction = [(1, 2), (2, 1), (-1, -2), (-2, -1),
                          (-1, 2), (2, -1), (1, -2), (-2, 1)]
    mark_visited(grid, (0, 0), 0)

    while queue:
        cell, moves = queue.popleft()

        # Insert the valid and not visited cells
        for direction in movement_direction:
            row, col = cell
            new_cell = (row + direction[0], col + direction[1])
            if is_valid_cell(new_cell, n) and yet_to_visit(grid, new_cell):
                # Cell is valid and it is yet to be visited
                queue.append((new_cell, moves + 1))
                mark_visited(grid, new_cell, moves + 1)

    print_helper(grid)


if __name__ == "__main__":
    solve()

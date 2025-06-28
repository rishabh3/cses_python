def solve():
    n = 8
    board = []
    for _ in range(n):
        board.append(input())

    col_set, diag1, diag2 = set(), set(), set()
    path = [0]

    def queen_placement(index, positions):
        nonlocal path
        if index >= n:
            if len(positions) == n:
                path[0] += 1
            return

        for idx in range(n):
            current_cell = (index, idx)
            diag1_comp = index - idx
            diag2_comp = index + idx

            if idx in col_set or board[index][idx] == '*' or diag1_comp in diag1 or diag2_comp in diag2:
                continue

            col_set.add(idx)
            diag1.add(diag1_comp)
            diag2.add(diag2_comp)
            positions.append(current_cell)
            queen_placement(index + 1, positions)
            positions.pop()
            diag1.remove(diag1_comp)
            diag2.remove(diag2_comp)
            col_set.remove(idx)

    queen_placement(0, [])
    print(path[0])


if __name__ == "__main__":
    solve()

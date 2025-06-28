def solve():
    test = int(input())
    for _ in range(test):
        row, col = list(map(int, input().split(' ')))
        if row > col:
            ans = (row-1)*(row-1)

            if row%2 != 0:
                add = col
            else:
                add = 2*row - col

            print(ans + add)
        else:
            ans = (col-1)*(col-1)

            if col%2 == 0:
                add = row
            else:
                add = 2*col - row

            print(ans + add)


if __name__ == "__main__":
    solve()

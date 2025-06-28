def solve():
    test_case = int(input())
    res = [test_case]

    while res[-1] != 1:
        if res[-1] %2 == 0:
            res.append(res[-1] // 2)
        else:
            res.append(res[-1]*3 + 1)

    for element in res:
        print(element, end=" ")



if __name__ == "__main__":
    solve()

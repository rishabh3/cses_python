def solve():
    number = int(input())
    for i in range(1, number+1):
        result = (i**2)*(i**2 - 1) // 2 - 4*(i-1)*(i-2)
        if result < 0:
            result = 0
        print(result)


if __name__ == "__main__":
    solve()

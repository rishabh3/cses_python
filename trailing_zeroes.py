import math


def solve():
    n = int(input())
    highest_power = math.floor(math.log(n, 5))

    count = 0
    while highest_power > 0:
        count += math.floor(n/(5**highest_power))
        highest_power -= 1
    print(count)


if __name__ == "__main__":
    solve()

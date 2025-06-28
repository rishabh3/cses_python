def solve():
    n = int(input())
    numbers = set(map(int, input().split(' ')))
    number_lookup = list(range(1, n+1))

    for number in number_lookup:
        if number not in numbers:
            print(number)
            break


if __name__ == "__main__":
    solve()

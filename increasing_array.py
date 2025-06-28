def solve():
    arr_size = int(input())
    arr = list(map(int, input().split(' ')))

    num_increase = 0
    start = arr[0]
    for idx in range(1, arr_size):
        if arr[idx] < start:
            diff = abs(start - arr[idx])
            num_increase += diff
            arr[idx] += diff
        start = arr[idx]

    print(num_increase)


if __name__ == "__main__":
    solve()

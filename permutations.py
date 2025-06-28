from collections import deque


def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    if n <= 3:
        print("NO SOLUTION")
        return
    if n == 4:
        print("2 4 1 3")
        return
    ans = deque([4, 2, 5, 3, 1])
    for num in range(6, n+1):
        if num % 2 == 0:
            ans.appendleft(num)
        else:
            ans.append(num)

    for num in ans:
        print(num, end=" ")


if __name__ == "__main__":
    solve()

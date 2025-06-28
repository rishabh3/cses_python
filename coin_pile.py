def solve():
    test = int(input())
    for _ in range(test):
        a, b = list(map(int, input().split(' ')))
        if (a == 0 or b == 0) and (a+b != 0):
            print("NO")
        elif max(a,b) > 2*min(a,b):
            print("NO")
        elif (a+b)%3 == 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()

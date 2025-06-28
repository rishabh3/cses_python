def solve():
    n = int(input())
    for num in range((1 << n)):
        gray = num ^ (num >> 1)
        code = ""
        for idx in range(n-1, -1, -1):
            code += "1" if (gray & (1 << idx)) else "0"
        print(code)


if __name__ == "__main__":
    solve()

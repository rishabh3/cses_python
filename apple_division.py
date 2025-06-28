def solve():
    n = int(input())
    weights = list(map(int, input().split(' ')))
    
    def divide(index, sum1, sum2):
        if index == n:
            return abs(sum1 - sum2)

        take = divide(index + 1, sum1 + weights[index], sum2)
        not_take = divide(index + 1, sum1, sum2 + weights[index])

        return min(take, not_take)

    print(divide(0, 0, 0))



if __name__ == "__main__":
    solve()

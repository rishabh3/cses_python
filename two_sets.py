def solve():
    n = int(input())
    total_sum = n*(n+1) // 2
    if total_sum % 2 != 0:
        print("NO")
        return

    sum_set1 = 0
    set1 = []
    sum_set2 = 0
    set2 = []
    for num in range(n, 0, -1):
        if sum_set1 <= sum_set2:
            set1.append(num)
            sum_set1 += num
        else:
            set2.append(num)
            sum_set2 += num

    print("YES")
    print(len(set1))
    for element in set1:
        print(element, end=" ")
    print()
    print(len(set2))
    for element in set2:
        print(element, end=" ")


if __name__ == "__main__":
    solve()

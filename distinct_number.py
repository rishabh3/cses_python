"""
You are given a list of n integers, and your task is to calculate the number of distinct values in the list.
Input
The first input line has an integer n: the number of values.
The second line has n integers x_1,x_2,......,x_n.
Output
Print one integers: the number of distinct values.
Constraints

1 <= n <= 2 . 10^5
1 <= x_i <= 10^9

Example
Input:
5
2 3 2 2 3

Output:
2


Idea is to sort and pick count distinct numbers
"""


def solve():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    arr.sort()

    unique_counter = 0

    prev_seen = 0
    for num in arr:
        if num != prev_seen:
            unique_counter += 1
            prev_seen = num
    
    print(unique_counter)


if __name__ == "__main__":
    solve()

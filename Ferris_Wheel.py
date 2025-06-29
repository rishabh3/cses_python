"""
There are n children who want to go to a Ferris wheel, and your task is to find a gondola for each child.
Each gondola may have one or two children in it, and in addition, the total weight in a gondola may not exceed x. You know the weight of every child.
What is the minimum number of gondolas needed for the children?
Input
The first input line contains two integers n and x: the number of children and the maximum allowed weight.
The next line contains n integers p_1,p_2,....,p_n: the weight of each child.
Output
Print one integer: the minimum number of gondolas.
Constraints

1 <= n <= 2 . 10^5
1 <= x <= 10^9
1 <= p_i <= x

Example
Input:
4 10
7 2 3 9

Output:
3


Sort the weights array
Keep two pointer one on left and other on right
If sum is <= x add one gondola
else add one gondola and move the larger pointer (pointing largest element)

2 3 7 9

2 + 9 = 11 > 10 hence move right pointer back and add one gondola
2 + 7 = 9 < 10 hence move left and right pointer and add one gondola
3 < 10 hence move left and right and add one gondola
Stop as right < left
"""


def solve():
    n, weight = list(map(int, input().split(' ')))
    weights = list(map(int, input().split(' ')))
    weights.sort()

    left = 0
    right = n - 1
    gondola_count = 0

    while left <= right:
        if left != right:
            total_weight = weights[left] + weights[right]
        else:
            total_weight = weights[left]
        if total_weight > weight:
            right -= 1
        else:
            left += 1
            right -= 1
        gondola_count += 1

    print(gondola_count)


if __name__ == "__main__":
    solve()


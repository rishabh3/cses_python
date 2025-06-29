"""
There are n concert tickets available, each with a certain price. Then, m customers arrive, one after another.
Each customer announces the maximum price they are willing to pay for a ticket, and after this, they will get a ticket with the nearest possible price such that it does not exceed the maximum price.
Input
The first input line contains integers n and m: the number of tickets and the number of customers.
The next line contains n integers h_1,h_2,....,h_n: the price of each ticket.
The last line contains m integers t_1,t_2,....,t_m: the maximum price for each customer in the order they arrive.
Output
Print, for each customer, the price that they will pay for their ticket. After this, the ticket cannot be purchased again.
If a customer cannot get any ticket, print -1.
Constraints

1 <= n, m <= 2 . 10^5
1 <= h_i, t_i <= 10^9

Example
Input:
5 3
5 3 7 8 5
4 8 3

Output:
3
8
-1



Sort the ticket prices and use binary search to find 
where we can place customers price (index - 1) is our ticket
price which customer will get for

"""
import sys
import math
from collections import Counter
import bisect


class FenwickTree:

    def __init__(self, length):
        self.n = length + 1
        self.tree = [0] * (length + 1)

    def update(self, idx, delta):
        while idx < self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)
    
    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s
    
    def find(self, k):
        left, right = 1, k
        res = -1
        prev_ans = -1
        while left <= right:
            mid = (left + right) // 2
            ans = self.query(mid)
            if ans > 0 and ans != prev_ans:
                res = mid
                prev_ans = ans
                left = mid + 1
            else:
                right = mid - 1
        return res
            


def bin_search(arr, target):
    """
        Returns the index where the element can be inserted
        @params:
        arr: Array (sorted)
        target: Find index for this target in sorted array
        @returns:
        Index at which the target can be inserted
    """
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def solve():
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    n, m = data[0], data[1]
    tickets = data[2:2+n]
    customer = data[2+n:]

    maxPrice = sorted(tickets)
    ans = [0 for j in range(len(customer))]

    for i in range(len(customer)):
        temp = customer[i]

        itr = bisect.bisect(maxPrice, temp)

        if itr == 0:
            ans[i] = -1
        else:
            itr -= 1
            ans[i] = maxPrice[itr]
            maxPrice.remove(ans[i])
    
    output = list(map(str, ans))
    sys.stdout.write('\n'.join(output))
    


if __name__ == "__main__":
    solve()

"""
$lastCommand = Get-History | Select-Object -Last 1
$executionTime = $lastCommand.EndExecutionTime - $lastCommand.StartExecutionTime
Write-Host "The last command took $($executionTime.TotalSeconds) seconds to execute."
"""
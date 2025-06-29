"""
You are given the arrival and leaving times of n customers in a restaurant.
What was the maximum number of customers in the restaurant at any time?
Input
The first input line has an integer n: the number of customers.
After this, there are n lines that describe the customers. Each line has two integers a and b: the arrival and leaving times of a customer.
You may assume that all arrival and leaving times are distinct.
Output
Print one integer: the maximum number of customers.
Constraints

1 <= n <= 2 . 10^5
1 <= a < b <= 10^9

Example
Input:
3
5 8
2 4
3 9

Output:
2

2|3|5
4|9|8


[(5, 8), (2, 4), (3, 9)]
[(2,4), (3,9), (5,8)]
Max 2

When we input the arrival and departure time we add the following tuple in customer list
(arrival_time, 1) and (departure_time, -1)

Now sort this array and process each element one by one
Just add the second element of the tuple to customer = 0 (initially)
When we process departure time we store the current customer count in max variable
and add the departure second element

Go on doing this until all elements are processed
"""


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    customers = []

    idx = 1
    for _ in range(n):
        arrival = int(data[idx])
        departure = int(data[idx + 1])
        customers.append((arrival, 1))
        customers.append((departure, -1))
        idx += 2

    # Sort events: earlier time first, arrivals before departures at same time
    customers.sort()

    customer_cnt = 0
    max_customer = 0
    for _, change in customers:
        customer_cnt += change
        max_customer = max(max_customer, customer_cnt)

    sys.stdout.write("{}\n".format(max_customer))


if __name__ == "__main__":
    solve()
    

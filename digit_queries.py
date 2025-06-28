"""
Consider an infinite string that consists of all positive integers in
increasing order:
12345678910111213141516171819202122232425...
Your task is to process q queries of the form: what is the digit at position k
in the string?
Input
The first input line has an integer q: the number of queries.
After this, there are q lines that describe the queries. Each line has an
integer k: a 1-indexed position in the string.
Output
For each query, print the corresponding digit.
Constraints

1 <= q <= 1000
1 <= k <= 10^{18}

Example
Input:
3
7
19
12

Output:
7
4
1

Idea:
The queries here can be made O(1) if we can just preprocess and store the
string of digits before hand.
We know the constraint on k is till 10^18 which means that we can find the
upperlimit of the number

there are 9 1 digits  9
there are 90 2 digits 180
there are 900 3 digits 2700
there are 9000 4 digits number 36000
go on like this

9 + 180 + 2700 + 36000 + 450000 + 5400000 + 63000000 + ...

We cant generate whole string before hand as that will be costly instead we can
generate a substring and add more to it based on the query asked


1234567891011
k = 12 -> 1
For k = 12 we find out which number the digit belongs to
9 189
digit = 2
(12 - 9) % 2 = 1
(12 - 9) // 2 = 1

10 + 1 = 11

str(11)[1-1] = 1

123456789101112131415
"""
import bisect


def generate_prefix_str_length():
    prefix = [0]*18

    prefix[0] = 9
    itr = 2

    while itr < 19:
        multipler = 10 ** (itr-1)
        prefix[itr-1] = prefix[itr-2] + 9 * multipler * itr
        itr += 1

    return prefix


def solve():
    queries = int(input())
    prefix = generate_prefix_str_length()
    for _ in range(queries):
        k = int(input())
        # Find the position where k exists
        digit_length = 1
        count = 9
        start = 1

        while k > digit_length * count:
            k -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
        num = start + (k - 1) // digit_length
        index = (k - 1) % digit_length
        ans = str(num)[index]
        print(ans)


if __name__ == "__main__":
    solve()

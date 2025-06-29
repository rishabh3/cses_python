"""
There are n applicants and m free apartments. Your task is to distribute the apartments so that as many applicants as possible will get an apartment.
Each applicant has a desired apartment size, and they will accept any apartment whose size is close enough to the desired size.
Input
The first input line has three integers n, m, and k: the number of applicants, the number of apartments, and the maximum allowed difference.
The next line contains n integers a_1, a_2, ...., a_n: the desired apartment size of each applicant. If the desired size of an applicant is x, they will accept any apartment whose size is between x-k and x+k.
The last line contains m integers b_1, b_2, ...., b_m: the size of each apartment.
Output
Print one integer: the number of applicants who will get an apartment.
Constraints

1 <= n, m <= 2 . 10^5
0 <= k <= 10^9
1 <= a_i, b_i <= 10^9

Example
Input:
4 3 5
60 45 80 60
30 60 75

Output:
2


Sort both the array applicants size requirement and apartment sizes.
Now start processing with two pointers
Compare every pair and move the pointer which has a smallest element
when a mismatch. On a match move both and increment the counter
Stop when we finish one of the array
"""


def solve():
    n, m, k = list(map(int, input().split(' ')))
    applicants = list(map(int, input().split(' ')))
    apartments = list(map(int, input().split(' ')))

    applicants.sort()
    apartments.sort()

    apartment_itr = 0
    applicant_itr = 0

    unique_counter = 0

    while apartment_itr < m and applicant_itr < n:
        if abs(applicants[applicant_itr] - apartments[apartment_itr]) <= k:
            unique_counter += 1
            apartment_itr += 1
            applicant_itr += 1
        else:
            if applicants[applicant_itr] > apartments[apartment_itr]:
                apartment_itr += 1
            else:
                applicant_itr += 1
    
    print(unique_counter)


if __name__ == "__main__":
    solve()
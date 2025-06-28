"""
Your task is to reorder the characters of a string so that no two adjacent characters are the same. What is the lexicographically minimal such string?
Input
The only line has a string of length n consisting of characters A-Z.
Output
Print the lexicographically minimal reordered string where no two adjacent characters are the same. If it is not possible to create such a string, print -1.
Constraints

1 <= n <= 10^6

Example
Input:
HATTIVATTI

Output:
AHATITITVT

The idea is to first check if the max_frequency of any character
if it exceeds half the string length then we cannot reorder 
Now we iterate from 0th to n-1 index and we check every 
character from A to Z.
Since we are checking all characters from A to Z we guarantee 
we pick the minimal lex string
Before picking any valid character we first check if the character
is feasible by checking the same thing if max is greater than half 
the total remaining letters
This way we pick minimally feasible characters, if it is not feasible
we backtrack by increment the count of the frequency for the character and
moving to next character.
"""
import heapq
from collections import Counter


def solve():
    word = input()
    counter = Counter(word)
    max_freq = max(counter.values())
    if max_freq > (len(word) + 1) // 2:
        print(-1)
        return
    
    result = []
    total_left = len(word)
    prev_char = ''
    options = sorted(counter.keys())
    for _ in range(0, len(word)):
        for char in options:
            if counter[char] == 0 or char == prev_char:
                continue
            counter[char] -= 1 # Choose tenatively
            total_left -= 1

            if max_freq == counter[char] + 1:
                if counter[char] <= max(counter.values(), default=0):
                    max_freq = max(counter.values())

            if max_freq <= (total_left + 1) // 2:
                result.append(char)
                prev_char = char
                break
            else:
                counter[char] += 1
                total_left += 1
        else:
            print(-1)
            return
    
    print(''.join(result))

    


if __name__ == "__main__":
    solve()
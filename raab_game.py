"""
Observations:
    - If numbers picked are equal 0 point
    - If someone has greater number then 1 point
    - It is range of number 1,2....n (Maybe Binary search)

Input:
    Number of cards (n)
    Score for player 1 and player 2 at the end of the game.

Output:
    Valid sequence if possible with YES else NO

Maintain two sets for visited numbers for each players
Now perform binary search to pick two numbers to make the
score equal to end score.
Keep doing this until we get our final answer or we exhaust
the numbers and still cant get final score

If sum of score is greater than n then not possible
"""


def process(n, a, b):
    if a + b > n:
        return False, []

    limit = a + b
    A_cards = list(range(1, limit + 1))
    B_cards = list(range(1, limit + 1))
    A_used = set()
    B_used = set()
    sequence = []

    reverse = False
    if b < a:
        reverse = True
        a, b = b, a
        A_cards, B_cards = B_cards, A_cards

    while a > 0:
        for a_card in reversed(A_cards):
            if a_card in A_used:
                continue
            for b_card in B_cards:
                if b_card in B_used:
                    continue
                if a_card > b_card:
                    sequence.append([a_card, b_card])
                    A_used.add(a_card)
                    B_used.add(b_card)
                    a -= 1
                    break
            if a == 0:
                break
        else:
            return False, []

    while b > 0:
        for b_card in reversed(B_cards):
            if b_card in B_used:
                continue
            for a_card in reversed(A_cards):
                if a_card in A_used:
                    continue
                if a_card < b_card:
                    sequence.append([a_card, b_card])
                    A_used.add(a_card)
                    B_used.add(b_card)
                    b -= 1
                    break
            if b == 0:
                break
        else:
            return False, []

    number = limit + 1
    for num in range(number, n+1):
        sequence.append([num, num])

    if reverse:
        for element in sequence:
            element[0], element[1] = element[1], element[0]

    return True, sequence


def solve():
    test = int(input())
    for _ in range(test):
        n, a, b = list(map(int, input().split(' ')))
        possible, sequence = process(n, a, b)
        if possible:
            print("YES")
            for first, _ in sequence:
                print(first, end=" ")
            print()
            for _, second in sequence:
                print(second, end=" ")
            print()
        else:
            print("NO")


if __name__ == "__main__":
    solve()

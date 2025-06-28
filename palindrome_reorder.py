from collections import defaultdict, deque


def solve():
    word = input()
    freq = defaultdict(int)
    for char in word:
        freq[char] += 1

    freq_list = []
    for key in freq:
        freq_list.append((freq[key], key))

    freq_list.sort()

    count_odd = 0
    odd_char = ''
    odd_char_count = 0
    for count, char in freq_list:
        if count%2 != 0:
            count_odd += 1
            odd_char = char
            odd_char_count = count

    if count_odd > 1:
        print("NO SOLUTION")
        return

    if odd_char_count > 0:
        start_str = odd_char*odd_char_count
        container = deque([start_str])
    else:
        container = deque([])

    for count, char in freq_list:
        if char != odd_char:
            while count > 0:
                container.appendleft(char)
                container.append(char)
                count -= 2

    result = "".join(container)
    print(result)


if __name__ == "__main__":
    solve()

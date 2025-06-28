def solve():
    dna_sequence = input()
    start_pos = 0
    end_pos = 0

    count = 0
    max_count = 0
    while end_pos < len(dna_sequence):
        if dna_sequence[start_pos] == dna_sequence[end_pos]:
            end_pos += 1
            count += 1
        else:
            start_pos = end_pos
            max_count = max(count, max_count)
            count = 0
    max_count = max(max_count, count)

    print(max_count)



if __name__=="__main__":
    solve()

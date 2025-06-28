def move_disk(num, moves, source, dest, middle):
    if num == 1:
        moves.append([str(source), str(dest)])
        return

    move_disk(num-1, moves, source, middle, dest)
    moves.append([str(source), str(dest)])
    move_disk(num-1, moves, middle, dest, source)


def tower_of_hanoi(num):
    moves = []
    source, target, middle = 1, 3, 2
    move_disk(num, moves, source, target, middle)
    print(len(moves))
    for move in moves:
        print(" ".join(move))


def solve():
    num_towers = int(input())
    tower_of_hanoi(num_towers)


if __name__ == "__main__":
    solve()

def solve():
    s = input()

    result = set()

    def recur_generate(index, data):
        if index == len(data):
            result.add("".join(data))
            return

        for idx in range(index, len(data)):
            data[index], data[idx] = data[idx], data[index]
            recur_generate(index+1, data)
            data[index], data[idx] = data[idx], data[index]

    recur_generate(0, list(s))

    print(len(result))
    result = list(result)
    result.sort()
    for ans in result:
        print(ans)


if __name__ == "__main__":
    solve()

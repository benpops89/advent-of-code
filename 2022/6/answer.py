def parse():
    with open("2022/6/input.txt", "r") as f:
        data = list(map(lambda x: x.strip("\n"), f.readlines()))

    return data


def find_pattern(message, repeat):
    seen = []
    start = 0
    while len(seen) < repeat:
        for x in message[start:]:
            if len(seen) == repeat:
                break

            if x not in seen:
                seen.append(x)
            else:
                del seen[:]
                start += 1
                break

    return start + repeat


if __name__ == "__main__":
    data = parse()[0]

    answer1 = find_pattern(data, 4)
    print(answer1)

    answer2 = find_pattern(data, 14)
    print(answer2)

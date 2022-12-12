def parse():
    with open("2022/6/input.txt", "r") as f:
        data = list(map(lambda x: x.strip("\n"), f.readlines()))

    return data


if __name__ == "__main__":
    data = parse()[0]

    seen = []
    start = 0
    while len(seen) < 4:
        for x in data[start:]:
            if len(seen) == 4:
                break

            if x not in seen:
                seen.append(x)
            else:
                del seen[:]
                start += 1
                break

    answer1 = start + 4
    print(answer1)

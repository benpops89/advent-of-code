import string
from itertools import tee


def parse():
    with open("2022/3/input.txt", "r") as f:
        data = list(map(str.strip, f.readlines()))

    return data


if __name__ == "__main__":
    data = parse()

    scores = {
        k: v
        for k, v in zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53))
    }

    # Part 1
    rucksacks = [(x[: (len(x) // 2)], x[(len(x) // 2) :]) for x in data]
    overlap = [list(set(x) & set(y))[0] for x, y in rucksacks]
    answer1 = sum([scores[x] for x in overlap])
    print(answer1)

    # Part 2
    rucksacks = [data[i : i + 3] for i in range(0, len(data), 3)]
    badges = [list(set(x) & set(y) & set(z))[0] for x, y, z in rucksacks]
    answer2 = sum([scores[x] for x in badges])
    print(answer2)

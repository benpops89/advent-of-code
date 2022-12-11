import re


def parse():
    with open("2022/4/input.txt", "r") as f:
        data = list(map(str.strip, f.readlines()))

    return data


if __name__ == "__main__":
    data = parse()

    bounds = [list(map(int, re.findall(r"(\d+)", x))) for x in data]
    within = [[set(range(x[0], x[1] + 1)), set(range(x[2], x[3] + 1))] for x in bounds]
    contains = [x <= y or x >= y for x, y in within]
    answer1 = sum(contains)
    print(answer1)

    overlap = [len(x & y) > 0 for x, y in within]
    answer2 = sum(overlap)
    print(answer2)

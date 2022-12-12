import re
from collections import defaultdict


def parse():
    with open("2022/5/input.txt", "r") as f:
        data = list(map(lambda x: x.rstrip("\n"), f.readlines()))

    return data


if __name__ == "__main__":
    data = parse()

    index = data.index("")
    stacks = data[:index]
    keys = sorted(list(map(int, stacks[-1].strip().split("   "))))

    crates = []
    for row in stacks[:-1]:
        crates.append(
            [row[i : i + 3].replace("   ", "[ ]")[1] for i in range(0, len(row), 4)]
        )

    cargo = {}
    for crate in crates:
        for k, v in zip(keys, crate):
            if v != " ":
                cargo.setdefault(k, []).insert(0, v)

    original = {**cargo}
    instructions = [list(map(int, re.findall(r"(\d+)", x))) for x in data[index + 1 :]]
    for quantity, src, dst in instructions:
        containers = original[src][-quantity:][::-1]
        original[src] = original[src][:-quantity]
        original[dst] = original[dst] + containers

    letter_ordered = sorted(
        [(k, v[-1]) for k, v in original.items()], key=lambda x: x[0]
    )
    answer1 = "".join([x[1] for x in letter_ordered])
    print(answer1)

    for quantity, src, dst in instructions:
        containers = cargo[src][-quantity:]
        cargo[src] = cargo[src][:-quantity]
        cargo[dst] = cargo[dst] + containers

    letter_ordered = sorted([(k, v[-1]) for k, v in cargo.items()], key=lambda x: x[0])

    answer2 = "".join([x[1] for x in letter_ordered])
    print(answer2)

# Part 1 - 1834060
# Part 2 -

from collections import Counter


class Solution:
    PART1: int = 31
    PART2: int = 24

    def __init__(self):
        # Read the input data from this folder
        self.input_data: str = "data"

    def part1(self):
        result = 31

        return result

    def part2(self):
        result = 24

        return result


def solve():
    pass


if __name__ == "__main__":
    with open("2024/01/input.txt") as f:
        data = [x.strip().split() for x in f.readlines()]

    left = [int(x[0]) for x in data]
    right = [int(x[1]) for x in data]

    sum = 0
    for x, y in zip(sorted(left), sorted(right)):
        sum += abs(x - y)

    print(sum)

    sum = 0
    counts = Counter(right)
    for x in left:
        sum += x * counts.get(x, 0)

    print(sum)

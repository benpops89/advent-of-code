# Part 1 - 4814
# Part 2 - 5448

from itertools import combinations
from functools import cmp_to_key


class Solution:
    PART1: int = 143
    PART2: int = 123

    def __init__(self, data):
        self.data = "\n".join(data).split("\n\n")

        self.rules = {
            tuple(map(int, x.strip().split("|"))): True
            for x in self.data[0].split("\n")
        }

    def is_valid(self, numbers):
        for x in list(combinations(numbers, 2)):
            if not self.rules.get(x, False):
                return False
        return True

    def cmp(self, a, b):
        if self.rules.get((a, b), False):
            return -1
        else:
            return 1

    def part1(self):
        total = 0
        for row in self.data[1].split("\n"):
            order = list(map(int, row.split(",")))
            if self.is_valid(order):
                total += order[len(order) // 2]

        return total

    def part2(self):
        total = 0
        for row in self.data[1].split("\n"):
            order = list(map(int, row.split(",")))
            if self.is_valid(order):
                continue

            order.sort(key=cmp_to_key(self.cmp))
            total += order[len(order) // 2]

        return total

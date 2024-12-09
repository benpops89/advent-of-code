# Part 1 - 167090022
# Part 2 - 89823704

import re


class Solution:
    PART1: int = 161
    PART2: int = 48

    def __init__(self, data):
        self.data = data

    @staticmethod
    def multiple(row, enabled=True) -> int:
        if not enabled:
            return 0

        re_mul = re.compile(r"mul\((\d{1,3},\d{1,3})\)")
        sum = 0
        for m in re_mul.findall(row):
            digits = list(map(int, m.split(",")))
            sum += digits[0] * digits[1]

        return sum

    def part1(self):
        return self.multiple("".join(self.data))

    def part2(self):
        data = re.split(r"(don't\(\)|do\(\))", "".join(self.data))
        sum = 0
        enabled = True
        for row in data:
            if row == "don't()":
                enabled = False
            elif row == "do()":
                enabled = True
            else:
                sum += self.multiple(row, enabled)

        return sum

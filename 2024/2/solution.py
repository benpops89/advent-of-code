# Part 1 - 242
# Part 2 - 311


class Solution:
    PART1: int = 2
    PART2: int = 4

    def __init__(self, data):
        self.data = list(map(str.split, data))

    @staticmethod
    def is_safe(row) -> bool:
        differences = [int(b) - int(a) for a, b in zip(row, row[1:])]
        first_diff = differences[0]
        return all(0 < abs(d) <= 3 and (d > 0) == (first_diff > 0) for d in differences)

    def part1(self) -> int:
        return sum(self.is_safe(row) for row in self.data)

    def part2(self) -> int:
        count = 0
        for row in self.data:
            permutations = [row[:i] + row[i + 1 :] for i in range(len(row))]
            if any(self.is_safe(p) for p in permutations):
                count += 1

        return count

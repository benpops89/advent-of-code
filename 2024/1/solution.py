# Part 1 - 1834060
# Part 2 - 21607792

from collections import Counter

class Solution:
    PART1: int = 11
    PART2: int = 31

    def __init__(self, data):
        self.data = list(map(str.split, data))

    def part1(self):
        left = [int(x[0]) for x in self.data]
        right = [int(x[1]) for x in self.data]

        result = 0
        for x, y in zip(sorted(left), sorted(right)):
            result += abs(x - y)

        return result

    def part2(self):
        left = [int(x[0]) for x in self.data]
        right = [int(x[1]) for x in self.data]
        
        result = 0
        counts = Counter(right)
        for x in left:
            result += x * counts.get(x, 0)

        return result

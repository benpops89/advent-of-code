# Part 1 - 2644
# Part 2 - ?


class Solution:
    PART1: int = 18
    PART2: int = 0

    def __init__(self, data):
        self.data = {
            (i, j): letter for i, row in enumerate(data) for j, letter in enumerate(row)
        }

    def search(self, point) -> int:
        points = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (-1, -1),
            (-1, 1),
            (1, 0),
            (1, -1),
            (1, 1),
        ]
        words = []
        for i, j in points:
            word = "X"
            for k in range(1, 4):
                w = self.data.get((i * k + point[0], j * k + point[1]), None)
                if w is None:
                    break
                word += w
            words.append(word)

        return words.count("XMAS")

    def part1(self) -> int:
        count = 0
        for point, letter in self.data.items():
            if letter != "X":
                continue

            count += self.search(point)

        return count

    def part2(self):
        pass

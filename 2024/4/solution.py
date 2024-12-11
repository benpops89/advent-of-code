# Part 1 - 2644
# Part 2 - 1952


class Solution:
    PART1: int = 18
    PART2: int = 9

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
        count = 0
        for point, letter in self.data.items():
            if letter != "A":
                continue

            letters = []
            for i, j in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
                w = self.data.get((i + point[0], j + point[1]), None)
                if w in ["M", "S"]:
                    letters.append(w)

            if len(letters) == 4:
                left = letters[:2]
                right = letters[2:]

                if left[0] != left[1] and right[0] != right[1]:
                    count += 1

        return count

# Part 1 - ?
# Part 2 - ?


class Solution:
    PART1: int = 4814
    PART2: int = 0

    def __init__(self, data):
        self.data = data

    def part1(self):
        data = "\n".join(self.data).split("\n\n")

        before = {}
        after = {}
        for k, v in map(lambda x: x.split("|"), data[0].split("\n")):
            before.setdefault(k, []).append(v)
            after.setdefault(v, []).append(k)

        count = 0
        for page in data[1].split("\n"):
            order = page.split(",")
            valid = True
            for i, x in enumerate(order):
                if i == 0:
                    if len(set(order[1:]) & set(before[x])) != len(order[1:]):
                        valid = False
                elif i + 1 == len(order):
                    if len(set(order[:-1]) & set(after[x])) != len(order[:-1]):
                        valid = False
                else:
                    if not before.get(x, []) or not after.get(x, []):
                        valid = False
                        break

                    if (
                        len(set(order[i + 1 :]) & set(before[x])) != len(order[i + 1 :])
                    ) or (
                        len(set(order[: i - 1]) & set(after[x])) != len(order[: i - 1])
                    ):
                        valid = False

            if valid:
                count += int(order[len(order) // 2])

        return count

    def part2(self):
        pass

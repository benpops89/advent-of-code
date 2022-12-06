def parse():
    with open("2022/1/input.txt", "r") as f:
        elfs = [
            x.strip().split("\n")
            for x in "".join([x for x in f.readlines()]).split("\n\n")
        ]

    return elfs


if __name__ == "__main__":
    calories = sorted([sum(map(int, x)) for x in parse()], reverse=True)

    # Part 1
    print(calories[0])

    # Part 2
    print(sum(calories[:3]))

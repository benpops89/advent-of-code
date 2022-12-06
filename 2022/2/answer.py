from itertools import product


def parse():
    with open("2022/2/input.txt") as f:
        data = [tuple(x.strip().split(" ")) for x in f.readlines()]

    return data


if __name__ == "__main__":
    data = parse()

    # Part 1
    scores = {"X": 1, "Y": 2, "Z": 3}
    opponent = ["A", "B", "C"]
    player = ["X", "Y", "Z"]

    results = [3, 6, 0, 0, 3, 6, 6, 0, 3]
    options = list(product(opponent, player))
    outcome = {k: v for k, v in zip(options, results)}
    game_scores = [outcome[x] + scores[x[1]] for x in data]

    answer1 = sum(game_scores)
    print(answer1)

    # Part 2
    values = {"A": 1, "B": 2, "C": 3}
    scores = {"X": 0, "Y": 3, "Z": 6}
    outcome = {
        k: v
        for k, v in zip(
            product(["A", "B", "C"], ["X", "Y", "Z"]),
            ["C", "A", "B", "A", "B", "C", "B", "C", "A"],
        )
    }
    game_scores = [values[outcome[x]] + scores[x[1]] for x in data]

    answer2 = sum(game_scores)
    print(answer2)

def parse():
    with open("2022/6/input_test.txt", "r") as f:
        data = list(map(str.strip("\n"), f.readlines()))

    return data


if __name__ == "__main__":
    data = parse()

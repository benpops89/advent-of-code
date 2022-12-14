def parse():
    with open("2022/7/input_test.txt", "r") as f:
        data = list(map(lambda x: x.strip("\n"), f.readlines()))

    return data


if __name__ == "__main__":
    data = parse()

from itertools import chain


def parse():
    with open("2022/7/input_test.txt", "r") as f:
        data = list(map(lambda x: x.strip("\n"), f.readlines()))

    return data


if __name__ == "__main__":
    data = parse()

    fs = {}
    dirs = set(["/"])
    pwd = ["/"]
    for line in data:
        values = line.split(" ")
        if values[0] == "$":
            if values[1] == "cd":
                if values[2] == "/":
                    del pwd[1:]
                elif values[2] == "..":
                    pwd.pop()
                else:
                    pwd.append(values[2])
        elif values[0] == "dir":
            dirs.add(values[1])
        elif values[0].isdigit():
            for d in pwd:
                fs.setdefault(d, []).append(int(values[0]))

    total_size = 100000
    fs_reduced = {k: v for k, v in fs.items() if sum(v) <= total_size}

    answer1 = sum(chain(*fs_reduced.values()))
    print(answer1)

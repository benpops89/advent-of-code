from collections import defaultdict


def parse():
    with open("2022/7/input.txt", "r") as f:
        data = list(map(lambda x: x.strip("\n"), f.readlines()))

    return data


if __name__ == "__main__":
    data = parse()

    fs = defaultdict(int)
    parents = []
    pwd = []
    for line in data:
        match line.split(" "):
            case "$", "cd", directory:
                if directory == "..":
                    pwd.pop()
                    parents.pop()
                elif directory == "/":
                    pwd.clear()
                    parents.clear()
                else:
                    parents.append(f"/{'/'.join(pwd)}")
                    pwd.append(directory)
            case "$", "ls":
                pass
            case "dir", directory:
                pass
            case size, filename:
                dirname = f"/{'/'.join(pwd)}"
                fs[dirname] += int(size)
                for parent in parents:
                    print(parent)
                    fs[parent] += int(size)

    answer1 = sum(filter(lambda x: x <= 100000, fs.values()))
    print(answer1)

    total_size = 70000000
    required_space = 30000000
    needed_space = abs(total_size - fs["/"] - required_space)

    answer2 = min(
        filter(lambda x: x[1] >= needed_space, fs.items()), key=lambda x: x[1]
    )
    print(answer2)

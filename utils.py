from pathlib import Path
from typing import Optional, Union


def parse_input(
    year: int,
    day: int,
    part: str,
    test: Optional[bool] = False,
    multiple: Optional[bool] = False,
) -> list[Union[str, int]]:
    """
    Parse input data into a useable format

    Args:
        path (str): Location of the raw input data

    Returns:
        list[Union[str, int]]
    """

    if test and multiple:
        filename = f"example{part.value[-1]}.txt"
    elif test and not multiple:
        filename = "example.txt"
    else:
        filename = "input.txt"

    with open(Path(__file__).parent.joinpath(f"{year}/{day}/{filename}"), "r") as f:
        input_data = [line.strip() for line in f.readlines()]

    return input_data


if __name__ == "__main__":
    data = parse_input("2024", "1", test=True)
    print(data)

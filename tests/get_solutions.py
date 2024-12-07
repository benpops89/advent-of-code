import importlib
from pathlib import Path
from typing import Any


def get_day_soultions(year: str) -> list[dict[str, Any]]:
    """
    Dynamically discover day solutions for a given year

    Returns:
        List of dictionaries with day solution information
    """

    solutions = []
    solutions_path = Path(__file__).parent.parent.joinpath(year)
    for day_folder in solutions_path.iterdir():
        print(day_folder)


if __name__ == "__main__":
    get_day_soultions("2024")

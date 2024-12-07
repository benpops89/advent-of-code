import importlib
import os
import shutil
from enum import Enum

import requests
import typer
from bs4 import BeautifulSoup

from utils import parse_input

URL = "https://adventofcode.com"


class Part(str, Enum):
    PART1 = "part1"
    PART2 = "part2"


app = typer.Typer(
    name="aoc",
    help="Run Advent of Code solutions",
    add_completion=True,
)


@app.command()
def solve(
    year: str = typer.Argument(..., help="The Advent of Code year"),
    day: str = typer.Argument(..., help="The Advent of Code day"),
    part: Part = typer.Argument(..., help="Which part to run"),
    test: bool = typer.Option(
        False, "--test", "-t", help="Run solution against example data"
    ),
):
    """
    Run Advent of Code Solution for given year and day.
    """

    # Parse the input for puzzle
    input_data = parse_input(year=year, day=day, test=test)

    # Run the solution for given year, day, part
    solution_module = importlib.import_module(f"{year}.{day}.solution")
    solution = solution_module.Solution(input_data)

    solution_method = getattr(solution, part)
    result = solution_method()

    if test:
        expected = getattr(solution_module.Solution, part.upper())
        if result == expected:
            typer.echo(
                f"✅ Part {part[-1]} Result: {result} (matches expected: {expected})"
            )
        else:
            typer.echo(f"❌ Part {part[-1]} Result: {result} (expected: {expected})")
    else:
        typer.echo(f"Part {part[-1]} Result: {result}")


@app.command()
def setup(
    year: str = typer.Argument(..., help="The Advent of Code year"),
    day: str = typer.Argument(..., help="The Advent of Code day"),
):
    pass

    # Create the directory
    os.makedirs(f"{year}/{day}", exist_ok=True)

    # Create the solution file
    shutil.copy("template.py", f"{year}/{day}/solution.py")

    # Source the example file
    headers = {"User-Agent": "github.com/benpops89/advent-of-code"}
    res = requests.get(f"{URL}/{year}/day/{day}", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    example = soup.select_one("pre > code")
    with open(f"{year}/{day}/example.txt", "w") as f:
        f.write(example.get_text().strip())
    typer.echo(f"\n✅ Downloaded example to {year}/{day}/example.txt")

    # Source the input file
    headers = {
        "User-Agent": "github.com/benpops89/advent-of-code",
        "Cookie": f"session={os.getenv('AOC_SESSION')}",
    }
    res = requests.get(f"{URL}/{year}/day/{day}/input", headers=headers)

    if res.status_code == 200:
        with open(f"{year}/{day}/input.txt", "w") as f:
            f.write(res.text.strip())
        typer.echo(f"\n✅ Downloaded input to {year}/{day}/input.txt")
    else:
        typer.echo(f"❌ Failed to download input: {res.status_code} - {res.text}")
        raise typer.Exit(1)

    typer.echo(f"\n🚀 All set! Ready to solve Year {year} Day {day}")


def main():
    app()


if __name__ == "__main__":
    main()

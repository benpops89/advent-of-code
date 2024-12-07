import importlib
from enum import Enum

import typer

from utils import parse_input


class Part(str, Enum):
    PART1 = "part1"
    PART2 = "part2"

app = typer.Typer(
    name="aoc",
    help="Run Advent of Code solutions",
    add_completion=True,
)


@app.command()
def aoc(
    year: str = typer.Argument(..., help="The Advent of Code year"),
    day: str = typer.Argument(..., help="The Advent of Code day"),
    part: Part = typer.Argument(..., help="Which part to run"),
    test: bool = typer.Option(False, "--test", "-t", help="Run solution against example data"),
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
            typer.echo(f"✅ Part {part[-1]} Result: {result} (matches expected: {expected})")
        else:
            typer.echo(f"❌ Part {part[-1]} Result: {result} (expected: {expected})")
    else:
        typer.echo(f"Part {part[-1]} Result: {result}")


def main():
    app()


if __name__ == "__main__":
    main()

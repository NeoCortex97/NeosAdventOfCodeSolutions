import os
import pathlib

from aocd import get_data

lines = [
    "import pathlib",
    "",
    'with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:',
    "    for line in [l.strip() for l in file.readlines()]:"
    "        pass",
    "",
]


if __name__ == "__main__":
    year: int = int(input("Please select year: "))
    day: int = int(input("Please select day: "))

    if day < 1 or day > 25:
        print("Day must be between 1 and 25!")
        exit(1)

    year_path = pathlib.Path(f'{year}')
    if not year_path.exists():
        year_path.mkdir()

    day_path = year_path.joinpath(f'day{day}')
    if not day_path.exists():
        day_path.mkdir()
        os.system(f"aocd {day} {year} > {day_path.joinpath('input.txt')}")

    for i in range(1, 3):
        part_path = day_path.joinpath(f"part{i}.py")
        if not part_path.exists():
            with part_path.open("w") as file:
                for line in lines:
                    file.write(line + "\n")

    os.system(f'git add {day_path}')

import os
import pathlib

for directory in sorted(filter(lambda item: item.is_dir(), pathlib.Path(".").iterdir())):
    if directory.name[0].isdigit():
        year = int(directory.name)
        for day in sorted(filter(lambda item: item.is_dir(), directory.iterdir())):
            d = int(day.name[3:])
            os.system(f"aocd {d} {year} > {day.joinpath('input.txt')}")

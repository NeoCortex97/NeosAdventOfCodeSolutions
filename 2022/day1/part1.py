import pathlib
from typing import List

with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    elves: List[int] = []
    elve: int = 0
    for line in file.readlines():
        if line.rstrip() != "":
            elve += int(line)
        else:
            elves.append(elve)
            elve = 0
    print(max(elves))

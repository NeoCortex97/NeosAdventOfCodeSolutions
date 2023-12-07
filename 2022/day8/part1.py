import pathlib
from typing import List


def cell(field: List[List[int]], x, y):
    pass


data: List[List[int]] = []
with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    for line in [l.strip() for l in file.readlines()]:
        data.append([])
        for item in line:
            data[-1].append(int(item))




import pathlib
from typing import List

with (pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file):
    result: List[int] = []
    for line in [l.strip() for l in file.readlines()]:
        table = line.split(":")[1]
        winning_str: List[str]
        drawn_str: List[str]
        winning_str, drawn_str = [i.rstrip().lstrip().split(" ") for i in table.split("|")]

        while "" in winning_str:
            winning_str.remove("")

        while "" in drawn_str:
            drawn_str.remove("")

        winning = [int(i) for i in winning_str]
        drawn = [int(i) for i in drawn_str]

        hits = [i in winning for i in drawn].count(True)
        points = int(2**(hits-1))
        result.append(points)

        # print(points, hits, winning, '#', drawn)

print(sum(result))

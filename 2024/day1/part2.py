import csv
import pathlib
import re

with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    puzzle_input = []
    for line in [l.strip() for l in file.readlines()]:
        puzzle_input.append(re.sub(' +', ',', line))
    list_a, list_b = list(zip(*list(csv.reader(puzzle_input))))
    list_a = [int(a) for a in list(sorted(list_a))]
    list_b = [int(b) for b in list(sorted(list_b))]
    list_cnt = [list_b.count(a) for a in list_a]
    print(list_a)
    print(list_b)
    print(list_cnt)
    print(sum([a * cnt for a, cnt in zip(list_a, list_cnt)]))


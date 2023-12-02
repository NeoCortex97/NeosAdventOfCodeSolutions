import pathlib
from typing import List


class Range:
    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high

    def __repr__(self):
        return f'{self.low} to {self.high}'


def completely_overlaps(first: Range, second: Range) -> bool:
    return ((first.low >= second.low and first.high <= second.high) or
            (second.low >= first.low and second.high <= first.high))


def partially_overlaps(first: Range, second: Range) -> bool:
    return len(set(range(first.low, first.high + 1)).intersection(set(range(second.low, second.high + 1)))) > 0


count = 0
with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    pairs: List[List[Range]] = []
    for line in [l.strip() for l in file.readlines()]:
        elves = line.split(",")
        pairs.extend([[Range(int(l.split("-")[0]), int(l.split("-")[1])) for l in elves]])
    for pair in pairs:
        overlapping = partially_overlaps(pair[0], pair[1])
        # print(pair[0], pair[1], partially_overlaps(pair[0], pair[1]))
        if overlapping:
            # print(pair[0], pair[1])
            count += 1
print(count)

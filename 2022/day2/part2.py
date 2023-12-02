import pathlib
from enum import Enum
from typing import Dict, Tuple


class Sign(Enum):
    rock = 1
    paper = 2
    scissors = 3


class Result(Enum):
    loose = 0
    draw = 3
    win = 6


wished: Dict[str, Result] = {
    "X": Result.loose,
    "Y": Result.draw,
    "Z": Result.win,
}

other: Dict[str, Sign] = {
    "A": Sign.rock,
    "B": Sign.paper,
    "C": Sign.scissors,
}

win: Dict[Tuple[Sign, Result], Sign] = {
    (Sign.rock, Result.win): Sign.paper,
    (Sign.rock, Result.draw): Sign.rock,
    (Sign.rock, Result.loose): Sign.scissors,
    (Sign.paper, Result.win): Sign.scissors,
    (Sign.paper, Result.draw): Sign.paper,
    (Sign.paper, Result.loose): Sign.rock,
    (Sign.scissors, Result.win): Sign.rock,
    (Sign.scissors, Result.draw): Sign.scissors,
    (Sign.scissors, Result.loose): Sign.paper,
}


total_score = 0
with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    for line in [l.strip() for l in file.readlines()]:
        parts = line.split(" ")
        other_move = other[parts[0]]
        wished_result = wished[parts[1]]
        your_move = win[(other_move, wished_result)]
        score = your_move.value + wished_result.value
        # print(other_move, your_move, wished_result, score)
        total_score += score

print(total_score)

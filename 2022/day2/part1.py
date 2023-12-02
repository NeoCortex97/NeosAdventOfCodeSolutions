import pathlib
from enum import Enum
from typing import Dict, Tuple, List


class Sign(Enum):
    rock = 1
    paper = 2
    scissors = 3


class Result(Enum):
    loose = 0
    draw = 3
    win = 6


you: Dict[str, Sign] = {
    "X": Sign.rock,
    "Y": Sign.paper,
    "Z": Sign.scissors,
}

other: Dict[str, Sign] = {
    "A": Sign.rock,
    "B": Sign.paper,
    "C": Sign.scissors,
}

win: Dict[Tuple[Sign, Sign], Result] = {
    (Sign.rock, Sign.rock): Result.draw,
    (Sign.rock, Sign.paper): Result.loose,
    (Sign.rock, Sign.scissors): Result.win,
    (Sign.paper, Sign.rock): Result.win,
    (Sign.paper, Sign.paper): Result.draw,
    (Sign.paper, Sign.scissors): Result.loose,
    (Sign.scissors, Sign.rock): Result.loose,
    (Sign.scissors, Sign.paper): Result.win,
    (Sign.scissors, Sign.scissors): Result.draw,
}

scores: List[int] = []
with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    for line in [l.strip() for l in file.readlines()]:
        parts = line.split(" ")
        other_move = other[parts[0]]
        your_move = you[parts[1]]
        result = win[(your_move, other_move)]
        score = int(your_move.value + result.value)
        scores.append(score)
        # print(your_move, other_move, result, score)

    print(sum(scores))

import math
import pathlib
import re
from typing import List, Dict


class Move:
    width: int = 0

    def __init__(self, amount: int, source: int, destination: int):
        self.amount = amount
        self.source = source
        self.destination = destination
        if self.amount > Move.width:
            Move.width = self.amount

    def __repr__(self):
        return f'Move {self.amount:>{int(math.log10(Move.width)) + 1}} from {self.source} to {self.destination}'


def parse_config(config: List[str]) -> Dict[int, List[str]]:
    result: Dict[int, List[str]] = dict()
    stacks = [int(i) for i in config[0].split(" ") if i != ""]
    for i in stacks:
        result[i] = []

    for line in config[1:]:
        offset = 0
        crates = []
        while offset < len(line):
            crate = line[offset: offset + 3]
            # print(crate)
            crates.append(crate)
            offset += 4

        for index, crate in [(i + 1, c) for i, c in enumerate(crates)]:
            designation = crate[1]
            if designation != " ":
                result[index].append(designation)

    return result


def parse_moves(lines: List[str]) -> List[Move]:
    syntax = re.compile(r'move (?P<amount>\d+) from (?P<source>\d+) to (?P<destination>\d+)')
    result: List[Move] = []
    for line in lines:
        match = syntax.match(line).groupdict()
        result.append(Move(int(match["amount"]), int(match["source"]), int(match["destination"])))
    return result


def print_area(area: Dict[int, List[str]]):
    height = max([len(i) for i in area.values()])
    for i in range(height + 1):
        line = []
        for j in range(len(area.keys())):
            if height - i >= len(area[j + 1]):
                line.append("   ")
            else:
                line.append(f'[{area[j + 1][height - i]}]')
        print(" ".join(line))
    print(" ".join([f' {i} ' for i in sorted(area.keys())]))


with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    config: List[str] = []
    moves: List[str] = []
    line = file.readline()
    while line.strip() != "":
        config.append(line[:-1])
        line = file.readline()
    config = list(reversed(config))
    for l in [l.rstrip() for l in file.readlines()]:
        moves.append(l)

    area = parse_config(config)
    # print_area(area)
    procedure = parse_moves(moves)
    for move in procedure:
        for _ in range(move.amount):
            area[move.destination].append(area[move.source].pop())
            # print_area(area)
    print(''.join([area[i][-1] for i in sorted(area.keys())]))

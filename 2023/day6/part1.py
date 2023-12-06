import functools
import pathlib
import re

with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    races = list(zip(*[[int(i) for i in re.sub(' +', ' ', lin.strip()).split(" ")[1:]]
                                for lin in file.readlines()]))
    options = [len(i) for i in [[split for split in range(race[0]) if split * (race[0] - split) > race[1]] for race in races]]
    print(options, functools.reduce(lambda x, y: x * y, options))

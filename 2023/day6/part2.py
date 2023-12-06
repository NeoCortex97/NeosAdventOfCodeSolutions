import pathlib
import re

with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    time, distance = [int("".join(re.sub(' +', ' ', line.strip()).split(" ")[1:])) for line in file.readlines()]
    print(time, distance)
    print(len([split for split in range(time) if split * (time - split) > distance]))

import pathlib

with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    for line in [l.strip() for l in file.readlines()]:        pass


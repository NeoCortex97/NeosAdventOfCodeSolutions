import pathlib

with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    print(sum([int(j[0] + j[-1]) for j in [[i for i in line.strip() if i.isdigit()] for line in file.readlines()]]))

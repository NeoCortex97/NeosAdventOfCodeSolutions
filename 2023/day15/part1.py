import pathlib


def hash(sequence) -> int:
    value = 0
    for v in sequence:
        value = ((value + v) * 17) % 256
    return value


with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    print(sum([hash([ord(i) for i in sequence]) for sequence in file.readline().strip().split(",")]))

import pathlib
from typing import Dict


prios: Dict[str, int] = {
    item: index + 1
    for index, item in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
}


def chunker(iterable, chunk_size: int):
    return zip(* [iter(iterable)] * chunk_size)


total_priorities: int = 0
with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    for index, line in enumerate(chunker([l.strip() for l in file.readlines()], 3)):
        for char in set(line[0]):
            if char in line[1] and char in line[2]:
                # print(index, char)
                total_priorities += prios[char]
print(total_priorities)

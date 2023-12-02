import pathlib
from typing import Dict, List

prios: Dict[str, int] = {
    item: index + 1
    for index, item in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
}

total_priorities: List[int] = []
with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    for line in [l.strip() for l in file.readlines()]:
        first, second = line[:len(line)//2], line[len(line)//2 + len(line) % 2:]
        commons: List[str] = []
        for char in list(set(first)):
            if char in second:
                commons.append(char)
        priorities = [prios[c] for c in commons]
        total_priorities.extend(priorities)
        # print(len(line), first, second, commons, priorities)

print(sum(total_priorities))

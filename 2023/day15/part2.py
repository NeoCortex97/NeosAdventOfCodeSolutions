import pathlib
from typing import Dict, List


def hash_str(label: str) -> int:
    return hash_seq([ord(i) for i in label])


def hash_seq(sequence: List[int]) -> int:
    value = 0
    for v in sequence:
        value = ((value + v) * 17) % 256
    return value


boxmap: Dict[int, Dict[str, int]] = {}


with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    for sequence in file.readline().strip().split(","):
        op = "=" if "=" in sequence else '-'
        label, lens = sequence.split("=") if "=" in sequence else sequence.split("-")
        hash_value = hash_str(label)
        if hash_value not in boxmap.keys():
            boxmap[hash_value] = {}
        if op == "=":
            boxmap[hash_value][label] = int(lens)
        if op == "-":
            if label in boxmap[hash_value].keys():
                boxmap[hash_value].pop(label)

    for i in [key for key in boxmap.keys() if boxmap[key] == {}]:
        boxmap.pop(i)

    total: int = 0
    for index in sorted([(index + 1, idx + 1, val) for index, x in boxmap.items() for idx, val in enumerate(x.values())]):
        print(index, index[0] * index[1] * index[2])
        total += index[0] * index[1] * index[2]
    print(total)

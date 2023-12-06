import itertools
import pathlib
import re
from typing import List, Dict


def lookup(value: int, data: List[Dict[str, int]]):
    for entry in data:
        if entry["src"] <= value <= entry["src"] + entry["len"]:
            return entry["dst"] + (value - entry["src"])
    else:
        return value


seeds: List[int] = []
maps: Dict[str, List[Dict[str, int]]] = {}

locations: List[int] = []

expr = re.compile(r'([\w\-]+) map:')

with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    map_name: str
    for line in [lin.strip() for lin in file.readlines()]:
        if line.startswith("seeds: "):
            seeds = [int(i) for i in line.split(" ")[1:]]
        elif line.strip() == "":
            continue
        elif line.strip().endswith("map:"):
            map_name = line.strip().split(" ")[0]
            maps[map_name] = []
        else:
            destination, src, length = [int(i) for i in line.split(" ")]
            maps[map_name].append({
                "src": src,
                "dst": destination,
                "len": length,
            })

print("seed soil")
for rng in zip(*[iter(seeds)] * 2):
    offset = 0
    # for offset in range(rng[1]):
    seed = rng[0] + offset
    soil: int = lookup(seed, maps["seed-to-soil"])
    fertilizer: int = lookup(soil, maps["soil-to-fertilizer"])
    water: int = lookup(fertilizer, maps["fertilizer-to-water"])
    light: int = lookup(water, maps["water-to-light"])
    temperature: int = lookup(light, maps["light-to-temperature"])
    humidity: int = lookup(temperature, maps["temperature-to-humidity"])
    location: int = lookup(humidity, maps["humidity-to-location"])
    locations.append(location)

    # print(seed, soil, fertilizer, water, light, temperature, humidity)

print(sorted(locations, reverse=True))

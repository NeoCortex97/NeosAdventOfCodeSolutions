# NeosAdventOfCodeSolutions

This repository uses aocd ([advent-of-code-data](https://github.com/wimglenn/advent-of-code-data)) and a valid api-token for advent of code. This token can be extracted from your browser.
The project is written in Python 3.12 and uses `match` statements.

## Usage

Use `main.py` to run all the days at once. The output is a tree with the following pattern:
```
...
2022:
  day1:
    part1:
      71471
    part2:
      211189
  day2:
    part1:
      13565
    part2:
      12424
  day3:
    part1:
      8139
    part2:
      2668
...
```
Use `generateDay.py` to automatically generate a skeleton for a new day. I'd appreciate it if you would contribute a day, but it is mainly for me.
Use `regenerateInputs.py` if you want to get your personal puzzle inputs.

## Participation

I would love it if you wanted to refactor existing solutions or contribute your solutions. You can simply add your solution if it does not exist yet. I will extend the scripts to automatically include multiple solutions per day.
If you discover any bugs, or Exceptions in my solutions, I would be glad if you would be able to open an issue.

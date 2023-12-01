import pathlib

with pathlib.Path("2023/day1/day01.txt").open("r") as file:
    res = 0
    for line in file.readlines():
        line = line.strip()
        for new, old in enumerate("one two three four five six seven eight nine zero".split(" ")):
            line = line.replace(old, str(new + 1))
        numbers = [i for i in line if i.isdigit()]
        number = int(numbers[0] + numbers[-1])
        if len(numbers) > 1:
            res += number
    print(res)

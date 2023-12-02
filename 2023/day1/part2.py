import pathlib

with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    res = 0
    for line in file.readlines():
        line = line.strip()
        for new, old in enumerate("zero one two three four five six seven eight nine".split(" ")):
            line = line.replace(old, " " + str(new) + " ")
        numbers = [i for i in line if i.isdigit()]
        number = int(numbers[0] + numbers[-1])
        if len(numbers) > 1:
            # print(numbers)
            res += number
    print(res)

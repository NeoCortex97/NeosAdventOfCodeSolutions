import pathlib
import re


def test_span(prv, crnt, nxt, span) -> int:
    right: str
    left: str
    top: str
    bottom: str

    if span[0] - 1 >= 0:
        left = crnt[span[0] - 1]
    else:
        left = "."

    try:
        right = crnt[span[1]]
    except IndexError:
        right = "."

    if prev:
        top = prev[span[0] - 1: span[1] + 1]
    else:
        top = "."

    if nxt:
        bottom = nxt[span[0] - 1: span[1] + 1]
    else:
        bottom = "." * ((span[1] - span[0]) + 2)

    space = right + left + top + bottom

    # print(top)
    # print(crnt[span[0] - 1: span[1] + 1])
    # print(bottom)
    # print(space, space.replace(".", ""), len(space.replace(".", "")))

    return len(space.replace(".", ""))


with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    expr = re.compile(r'(\d+)')
    prev: str = None
    current: str = None
    nxt: str = None
    value: int = 0
    lines = file.readlines()
    lines.append("." * len(lines[0]))
    lines.append("." * len(lines[0]))
    for line in [l.strip() for l in lines]:
        prev = current
        current = nxt
        nxt = line
        if current:
            for number in expr.finditer(current):
                value += test_span(prev, current, nxt, number.span()) * int(number.group(0))
        print(value)



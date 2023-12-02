import pathlib

with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    for line in [l.strip() for l in file.readlines()]:
        sig: str = ""
        for index, char in enumerate(line):
            sig += char
            if len(sig) > 4:
                sig = sig[1:]
            # print(sig, set(sig))
            if len(set(sig)) > 3:
                print(index + 1)
                break

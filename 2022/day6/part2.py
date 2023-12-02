import pathlib

with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    for line in [l.strip() for l in file.readlines()]:
        sig: str = ""
        for index, char in enumerate(line):
            sig += char
            if len(sig) > 14:
                sig = sig[1:]
                print(f'{len(set(sig)):>2}', sig, set(sig))
            # print(sig, set(sig))
            if len(set(sig)) >= 14:
                print(index + 1)
                break
        else:
            print(len(line))

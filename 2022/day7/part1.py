import pathlib
from enum import Enum
from typing import List, Dict, Generator, Any


class File:
    def __init__(self, name: str, parent, size: int):
        self.name: str = name
        self.parent: Directory = parent
        self.size: int = size

    @property
    def path(self):
        return self.parent.path + "/" + self.name


class Directory:
    def __init__(self, name: str, parent=None):
        self.contents: Dict[str, Directory or File] = {}
        self.name: str = name
        self.parent: Directory = parent

    def subdirectory(self, name: str):
        return self.contents[name]

    def mkdir(self, name: str):
        tmp = Directory(name, self)
        self.contents[name] = tmp
        return tmp

    def mkfile(self, name: str, size: int):
        self.contents[name] = File(name, self, size)

    @property
    def size(self):
        return sum([i.size for i in self.contents.values()])

    @property
    def path(self):
        if self.parent is None:
            return ""
        else:
            return self.parent.path + "/" + self.name

    def __repr__(self):
        return self.path

    def iterdir(self) -> Generator[Any, None, None]:
        yield self
        for item in self.contents.values():
            if type(item) is not File:
                for i in item.iterdir():
                    yield i
            else:
                yield item


with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    base = Directory("/")
    selected_node = base
    for line in [l.strip() for l in file.readlines()]:
        parts = line.split(" ")
        if parts[0] == "$":
            # print("command", end=" ")
            match parts[1]:
                case "cd":
                    # print("cd", end=" ")
                    if parts[2] != "..":
                        # print(parts[2])
                        try:
                            selected_node = selected_node.contents[parts[2]]
                        except KeyError:
                            pass
                    else:
                        # print("..")
                        selected_node = selected_node.parent
                case "ls":
                    # print("ls")
                    pass
        else:
            match parts[0]:
                case "dir":
                    selected_node.mkdir(parts[1])
                    # print(f'created directory {parts[1]}')
                case other:
                    selected_node.mkfile(parts[1], int(parts[0]))
                    # print(f"created file {parts[1]}")

    dirs = list(filter(lambda d: d.size <= 100000 and type(d) is not File, base.iterdir()))
    print(sum([item.size for item in dirs]))

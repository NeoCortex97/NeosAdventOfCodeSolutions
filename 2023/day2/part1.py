import math
import pathlib
from typing import List


class Draw:
    def __init__(self, text: str = None):
        self.red: int = 0
        self.green: int = 0
        self.blue: int = 0
        if text:
            self.parse(text)

    def parse(self, text: str):
        for color in [i.strip() for i in text.split(",")]:
            amount, name = color.split(" ")
            match name:
                case "red":
                    self.red = int(amount)
                case "green":
                    self.green = int(amount)
                case "blue":
                    self.blue = int(amount)

    def __repr__(self) -> str:
        return f'red: {self.red}, green: {self.green}, blue: {self.blue}'

    def possible(self, red: int, green: int, blue: int) -> bool:
        return self.red <= red and self.green <= green and self.blue <= blue


class Game:
    max_id: int = 0

    def __init__(self):
        self.id: int = 0
        self.draws: List[Draw] = []

    def parse(self, text: str):
        metadata = text.split(":")
        self.id = int(metadata[0].split(" ")[1])
        if self.id > Game.max_id:
            Game.max_id = self.id

        draws = [i.strip() for i in metadata[1].split(";")]
        for draw in draws:
            self.draws.append(Draw(draw))

    def possible(self, red: int, green: int, blue: int) -> bool:
        return all([i.possible(red, green, blue) for i in self.draws])
    
    @property
    def min_red(self):
        return max([draw.red for draw in self.draws])
    
    @property
    def min_green(self):
        return max(draw.green for draw in self.draws)

    @property
    def min_blue(self):
        return max(draw.blue for draw in self.draws)

    def power(self) -> int:
        return self.min_red * self.min_green * self.min_blue

    def __repr__(self) -> str:
        res = f'Game {self.id:>{int(math.log10(self.max_id) + 1)}}: Power: {self.power()} ({self.min_red}, {self.min_green}, {self.min_blue})\n'
        for draw in self.draws:
            res += f'  {draw}\n'
        return res


with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    lines = [i.rstrip() for i in file.readlines()]
    games = []
    for line in lines:
        tmp = Game()
        tmp.parse(line)
        games.append(tmp)

    # for game in games:
    #     if game.possible(12, 13, 14):
    #         print(game)

    print(sum([game.id for game in games if game.possible(12, 13, 14)]))

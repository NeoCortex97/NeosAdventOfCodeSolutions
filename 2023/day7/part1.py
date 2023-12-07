import pathlib
from enum import Enum

card_values = {k: i for i, k in enumerate(reversed("AKQJT98765432"))}


class HandType(Enum):
    FiveOfAKind = 6
    FourOfAKind = 5
    ThreeOfAKind = 4
    FullHouse = 3
    TwoPair = 2
    OnePair = 1
    HighCard = 0


class Hand:
    def __init__(self, text):
        parts = text.split(" ")
        self.contents = [i for i in parts[0]]
        self.bid = int(parts[1])
        self._type: HandType = None

    def __repr__(self):
        return f'{"".join(self.contents)} {self.bid} {self.type()}'

    def type(self):
        if not self._type:
            value_counts = sorted([self.contents.count(i) for i in set(self.contents)], reverse=True)
            if value_counts[0] == 5:
                self._type = HandType.FiveOfAKind
            elif value_counts[0] == 4:
                self._type = HandType.FourOfAKind
            elif value_counts[0] == 3 and value_counts[1] == 2:
                self._type = HandType.FullHouse
            elif value_counts[0] == 3 and value_counts[1] != 2:
                self._type = HandType.ThreeOfAKind
            elif value_counts[0] == 2 and value_counts[1] == 2:
                self._type = HandType.TwoPair
            elif value_counts[0] == 2 and value_counts[1] != 2:
                self._type = HandType.OnePair
            else:
                self._type = HandType.HighCard
        return self._type

    def __lt__(self, other):
        if self.type() != other.type():
            return self.type().value < other.type().value
        else:
            offset = 0
            while card_values[self.contents[offset]] == card_values[other.contents[offset]] and offset < 5:
                offset += 1
            return card_values[self.contents[offset]] < card_values[other.contents[offset]]

    def __gt__(self, other):
        if self.type() != other.type():
            return self.type().value > other.type().value
        else:
            offset = 0
            while card_values[self.contents[offset]] == card_values[other.contents[offset]]:
                offset += 1
            if offset == 5:
                return False
            return card_values[self.contents[offset]] < card_values[other.contents[offset]]

    def __eq__(self, other):
        if self.type() != other.type():
            return False
        else:
            offset = 0
            while card_values[self.contents[offset]] == card_values[other.contents[offset]] and offset < 5:
                offset += 1
            return offset == 5

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other


hands = []
with pathlib.Path(__file__).parent.joinpath("input.txt").open("r") as file:
    for line in [l.strip() for l in file.readlines()]:
        hands.append(Hand(line))

print(sum([hand.bid * (index + 1) for index, hand in enumerate(sorted(hands))]))

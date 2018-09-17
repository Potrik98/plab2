from enum import Enum, unique

ACTION_COUNT = 3


@unique
class Action(Enum):
    PAPER = 0
    SCISSORS = 1
    ROCK = 2

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __gt__(self, other) -> bool:
        return self.value == (other.value + 1) % ACTION_COUNT

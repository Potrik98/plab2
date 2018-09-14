from paper_scissors_rock.Player import Player
from paper_scissors_rock.Action import Action, ACTION_COUNT
import random

class RandomPlayer(Player):
    def choose_action(self) -> Action:
        r = random.randrange(0, ACTION_COUNT)
        return Action(r)

    def accept_result(self, my_action, other_action, result) -> None:
        pass

    def get_name(self) -> str:
        return "Random Player"

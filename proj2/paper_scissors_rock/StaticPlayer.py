from paper_scissors_rock.Player import Player
from paper_scissors_rock.Action import Action, ACTION_COUNT
import random

class StaticPlayer(Player):
    def __init__(self, action: Action):
        super().__init__()
        self._action = action

    def choose_action(self) -> Action:
        return self._action

    def accept_result(self, my_action: Action, other_action: Action, result: int) -> None:
        pass

    def get_name(self) -> str:
        return "Static Player of type %s" % self._action.name

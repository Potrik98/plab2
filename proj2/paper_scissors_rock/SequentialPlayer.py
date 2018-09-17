from paper_scissors_rock.Player import Player
from paper_scissors_rock.Action import Action, ACTION_COUNT


class SequentialPlayer(Player):
    def __init__(self, start_action=Action.PAPER):
        self._action = start_action

    def choose_action(self) -> Action:
        action = self._action
        self._action = Action((self._action.value + 1) % ACTION_COUNT)
        return action

    def accept_result(self,
                      my_action: Action,
                      other_action: Action,
                      result: int) -> None:
        pass

    def get_name(self) -> str:
        return "Sequential Player (last: %s)" % str(self._last_action.name)

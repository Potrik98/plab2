from paper_scissors_rock.Player import Player
from paper_scissors_rock.Action import Action, ACTION_COUNT


class MostUsedPlayer(Player):
    def __init__(self, start_action=Action.PAPER):
        self._action_count = [0] * ACTION_COUNT

    def choose_action(self) -> Action:
        expected_action = self._action_count.index(max(self._action_count))
        action = Action((expected_action + 1) % ACTION_COUNT)
        return action

    def accept_result(self,
                      my_action: Action,
                      other_action: Action,
                      result: int) -> None:
        self._action_count[other_action.value] += 1

    def get_name(self) -> str:
        return "MostUsed Player"

from paper_scissors_rock.Player import Player
from paper_scissors_rock.Action import Action, ACTION_COUNT


class HistoricPlayer(Player):
    def __init__(self, range=2):
        self._range = range
        self._history = []
        self._sequence = []

    def choose_action(self) -> Action:
        history = [self._history]
        for i in range(1, self._range):
            if len(self._history) < i:
                history.append([])
            else:
                history.append(self._history[i:])
        patterns = zip(*history)
        counts = [0] * ACTION_COUNT
        index = 0
        for p in patterns:
            if tuple(self._sequence) == p:
                if index + self._range < len(self._history):
                    # An action has been played after the pattern
                    counts[self._history[index + self._range]] += 1
            index += 1

        expected_action = counts.index(max(counts))
        action = Action((expected_action + 1) % ACTION_COUNT)
        return action

    def accept_result(self,
                      my_action: Action,
                      other_action: Action,
                      result: int) -> None:
        self._history.append(other_action.value)
        self._sequence.append(other_action.value)
        if len(self._sequence) > self._range:
            self._sequence = self._sequence[1:]  # Remove first element

    def get_name(self) -> str:
        return "Historic Player (range: %d)" % self._range

from paper_scissors_rock.Player import Player

class SimpleGame:
    def __init__(self, player1: Player, player2: Player):
        self._player1 = player1
        self._player2 = player2
        self._score = 0

    def do_game(self) -> int:
        action1 = self._player1.choose_action()
        action2 = self._player2.choose_action()
        if action1 > action2:
            self._score = 1
        elif action1 == action2:
            self._score = 0
        else:
            self._score = -1
        self._player1.accept_result(action1, action2, self._score)
        self._player2.accept_result(action2, action1, -self._score)
        return self._score

    def __str__(self):
        return "SimpleGame: %s vs %s, score: %d" % \
        (self._player1.get_name(), self._player2.get_name(), self._score)

from paper_scissors_rock.Player import Player
from paper_scissors_rock.SimpleGame import SimpleGame

class GameSeries:
    def __init__(self, player1: Player, player2: Player, number_of_games: int):
        self._player1 = player1
        self._player2 = player2
        self._number_of_games = number_of_games
        self._score = 0

    def do_games(self) -> int:
        game = SimpleGame(self._player1, self._player2)
        results = [game.do_game() for i in range(self._number_of_games)]
        self._score = sum(results)
        return self._score

    def __str__(self):
        return "GameSeries: %s vs %s, score: %d" % \
        (self._player1.get_name(), self._player2.get_name(), self._score)

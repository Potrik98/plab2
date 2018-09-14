import unittest

from paper_scissors_rock.Action import Action
from paper_scissors_rock.StaticPlayer import StaticPlayer
from paper_scissors_rock.GameSeries import GameSeries

class SimpleGameTest(unittest.TestCase):
    def test_do_games_series_player_1_win(self):
        player1 = StaticPlayer(Action.PAPER)
        player2 = StaticPlayer(Action.ROCK)
        number_of_games = 100
        game_series = GameSeries(player1, player2, number_of_games)
        score = game_series.do_games()
        expected_score = 1 * number_of_games
        self.assertEqual(score, expected_score)

    def test_do_games_series_player_2_win(self):
        player1 = StaticPlayer(Action.PAPER)
        player2 = StaticPlayer(Action.SCISSORS)
        number_of_games = 100
        game_series = GameSeries(player1, player2, number_of_games)
        score = game_series.do_games()
        expected_score = -1 * number_of_games
        self.assertEqual(score, expected_score)

    def test_do_games_series_draw(self):
        player1 = StaticPlayer(Action.ROCK)
        player2 = StaticPlayer(Action.ROCK)
        number_of_games = 100
        game_series = GameSeries(player1, player2, number_of_games)
        score = game_series.do_games()
        expected_score = 0 * number_of_games
        self.assertEqual(score, expected_score)


if __name__ == '__main__':
    unittest.main()

import unittest

from paper_scissors_rock.Action import Action
from paper_scissors_rock.StaticPlayer import StaticPlayer
from paper_scissors_rock.SimpleGame import SimpleGame

class SimpleGameTest(unittest.TestCase):
    def test_do_game_player_1_win(self):
        player1 = StaticPlayer(Action.PAPER)
        player2 = StaticPlayer(Action.ROCK)
        game = SimpleGame(player1, player2)
        score = game.do_game()
        expected_score = 1
        self.assertEqual(score, expected_score)

    def test_do_game_player_2_win(self):
        player1 = StaticPlayer(Action.PAPER)
        player2 = StaticPlayer(Action.SCISSORS)
        game = SimpleGame(player1, player2)
        score = game.do_game()
        expected_score = -1
        self.assertEqual(score, expected_score)

    def test_do_game_draw(self):
        player1 = StaticPlayer(Action.ROCK)
        player2 = StaticPlayer(Action.ROCK)
        game = SimpleGame(player1, player2)
        score = game.do_game()
        expected_score = 0
        self.assertEqual(score, expected_score)


if __name__ == '__main__':
    unittest.main()

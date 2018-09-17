import unittest

from paper_scissors_rock.Action import Action
from paper_scissors_rock.HistoricPlayer import HistoricPlayer


class HistoricPlayerTest(unittest.TestCase):
    def test_choose_action(self):
        player = HistoricPlayer(range=2)
        # Play against Rock Paper Paper Rock Paper
        player.accept_result(Action.PAPER, Action.ROCK, 1)
        player.accept_result(Action.PAPER, Action.PAPER, 1)
        player.accept_result(Action.PAPER, Action.PAPER, 1)
        player.accept_result(Action.PAPER, Action.ROCK, 1)
        player.accept_result(Action.PAPER, Action.PAPER, 1)
        # Next expected action from the other player is paper
        expected_action = Action.SCISSORS
        self.assertEqual(player.choose_action(), expected_action)
        # Play against one paper
        player.accept_result(Action.PAPER, Action.PAPER, 1)
        # Now the other player is expected to play rock
        expected_action = Action.PAPER
        self.assertEqual(player.choose_action(), expected_action)


if __name__ == '__main__':
    unittest.main()

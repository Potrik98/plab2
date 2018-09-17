import unittest

from paper_scissors_rock.Action import Action
from paper_scissors_rock.MostUsedPlayer import MostUsedPlayer


class MostUsedPlayerTest(unittest.TestCase):
    def test_choose_action(self):
        player = MostUsedPlayer()
        # Play against one rock
        player.accept_result(Action.PAPER, Action.ROCK, 1)
        expected_action = Action.PAPER
        self.assertEqual(player.choose_action(), expected_action)
        # Play against two paper
        player.accept_result(Action.PAPER, Action.PAPER, 1)
        player.accept_result(Action.PAPER, Action.PAPER, 1)
        expected_action = Action.SCISSORS
        self.assertEqual(player.choose_action(), expected_action)


if __name__ == '__main__':
    unittest.main()

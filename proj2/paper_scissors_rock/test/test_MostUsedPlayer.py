import unittest

from paper_scissors_rock.Action import Action
from paper_scissors_rock.MostUsedPlayer import MostUsedPlayer
from paper_scissors_rock.StaticPlayer import StaticPlayer
from paper_scissors_rock.SimpleGame import SimpleGame

class MostUsedPlayerTest(unittest.TestCase):
    def test_choose_action(self):
        player = MostUsedPlayer()
        player.accept_result(Action.PAPER, Action.ROCK, 1) # Play against one rock
        expected_action = Action.PAPER
        self.assertEqual(player.choose_action(), expected_action)
        player.accept_result(Action.PAPER, Action.PAPER, 1)
        player.accept_result(Action.PAPER, Action.PAPER, 1) # Play against two paper
        expected_action = Action.SCISSORS
        self.assertEqual(player.choose_action(), expected_action)


if __name__ == '__main__':
    unittest.main()

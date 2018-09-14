import unittest

from paper_scissors_rock.Action import Action
from paper_scissors_rock.HistoricPlayer import HistoricPlayer
from paper_scissors_rock.StaticPlayer import StaticPlayer
from paper_scissors_rock.SimpleGame import SimpleGame

class HistoricPlayerTest(unittest.TestCase):
    def test_choose_action(self):
        player = HistoricPlayer(range=2)
        player.accept_result(Action.PAPER, Action.ROCK, 1) # Play against one rock
        player.accept_result(Action.PAPER, Action.PAPER, 1) # Play against one paper
        player.accept_result(Action.PAPER, Action.PAPER, 1) # Play against one paper
        player.accept_result(Action.PAPER, Action.ROCK, 1) # Play against one paper
        player.accept_result(Action.PAPER, Action.PAPER, 1) # Play against one paper
        # Next expected action from the other player is paper
        expected_action = Action.SCISSORS
        self.assertEqual(player.choose_action(), expected_action)
        player.accept_result(Action.PAPER, Action.PAPER, 1) # Play against one paper
        # Now the other player is expected to play rock
        expected_action = Action.PAPER
        self.assertEqual(player.choose_action(), expected_action)


if __name__ == '__main__':
    unittest.main()

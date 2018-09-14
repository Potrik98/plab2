import unittest

from paper_scissors_rock.Action import Action
from paper_scissors_rock.StaticPlayer import StaticPlayer

class ActionTest(unittest.TestCase):
    def test_choose_action(self):
        player = StaticPlayer(Action.PAPER)
        self.assertEqual(player.choose_action(), Action.PAPER)
        player = StaticPlayer(Action.ROCK)
        self.assertEqual(player.choose_action(), Action.ROCK)
        player = StaticPlayer(Action.SCISSORS)
        self.assertEqual(player.choose_action(), Action.SCISSORS)


if __name__ == '__main__':
    unittest.main()

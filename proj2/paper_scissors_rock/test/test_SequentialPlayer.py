import unittest

from paper_scissors_rock.Action import Action
from paper_scissors_rock.SequentialPlayer import SequentialPlayer


class SequentialPlayerTest(unittest.TestCase):
    def test_choose_action(self):
        player = SequentialPlayer(start_action=Action.ROCK)
        self.assertEqual(player.choose_action(), Action.ROCK)
        self.assertEqual(player.choose_action(), Action.PAPER)
        self.assertEqual(player.choose_action(), Action.SCISSORS)
        self.assertEqual(player.choose_action(), Action.ROCK)


if __name__ == '__main__':
    unittest.main()

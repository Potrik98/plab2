import unittest

from paper_scissors_rock.Action import Action
from paper_scissors_rock.RandomPlayer import RandomPlayer

class ActionTest(unittest.TestCase):
    def test_choose_action(self):
        player = RandomPlayer()
        self.assertIsInstance(player.choose_action(), Action)


if __name__ == '__main__':
    unittest.main()

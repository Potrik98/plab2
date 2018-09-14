import unittest

from paper_scissors_rock.Action import Action

class ActionTest(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(Action.PAPER, Action.PAPER)
        self.assertEqual(Action.ROCK, Action.ROCK)
        self.assertEqual(Action.SCISSORS, Action.SCISSORS)
        self.assertNotEqual(Action.PAPER, Action.ROCK)
        self.assertNotEqual(Action.PAPER, Action.SCISSORS)
        self.assertNotEqual(Action.ROCK, Action.SCISSORS)

    def test_greater_than(self):
        self.assertGreater(Action.PAPER, Action.ROCK)
        self.assertGreater(Action.ROCK, Action.SCISSORS)
        self.assertGreater(Action.SCISSORS, Action.PAPER)
        self.assertLess(Action.ROCK, Action.PAPER)
        self.assertLess(Action.PAPER, Action.SCISSORS)
        self.assertLess(Action.SCISSORS, Action.ROCK)
        self.assertFalse(Action.PAPER > Action.PAPER)
        self.assertFalse(Action.ROCK > Action.ROCK)
        self.assertFalse(Action.SCISSORS > Action.SCISSORS)
        self.assertFalse(Action.PAPER < Action.PAPER)
        self.assertFalse(Action.ROCK < Action.ROCK)
        self.assertFalse(Action.SCISSORS < Action.SCISSORS)


if __name__ == '__main__':
    unittest.main()

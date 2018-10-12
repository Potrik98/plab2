import unittest

from data.DataStructures import Queue
from calculator.Calculator import Calculator


class ActionTest(unittest.TestCase):
    def test_rpn_calculator(self):
        calc = Calculator()
        input = Queue()
        input.enqueue(1)
        input.enqueue(2)
        input.enqueue(3)
        input.enqueue('mul')
        input.enqueue('add')
        input.enqueue('exp')
        answer = 1096.63
        result = calc.evaluate_rpn(input)
        self.assertAlmostEqual(answer, result, places=2)


if __name__ == '__main__':
    unittest.main()

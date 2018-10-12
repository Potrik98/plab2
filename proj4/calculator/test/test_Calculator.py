import unittest

from data.DataStructures import Queue
from calculator.Calculator import Calculator, functions


class CalculatorTest(unittest.TestCase):
    def test_rpn_calculator(self):
        calc = Calculator()
        input = Queue()
        input.enqueue(1)
        input.enqueue(2)
        input.enqueue(3)
        input.enqueue(functions['mul'])
        input.enqueue(functions['add'])
        input.enqueue(functions['exp'])
        answer = 1096.63
        result = calc.evaluate_rpn(input)
        self.assertAlmostEqual(answer, result, places=2)

    def test_priority(self):
        self.assertLess(functions['add'], functions['mul'])
        self.assertLess(functions['sub'], functions['div'])
        self.assertGreater(functions['mul'], functions['add'])
        self.assertGreater(functions['exp'], functions['mul'])


if __name__ == '__main__':
    unittest.main()

import unittest

from data.DataStructures import Queue
from calculator.Calculator import functions
from calculator.Parser import Parser


class ParserTest(unittest.TestCase):
    def test_shunting_yard(self):
        input = [
            functions['exp'],
            '(',
            1,
            functions['add'],
            2,
            functions['mul'],
            3,
            ')'
        ]
        parser = Parser()
        expected_result = Queue()
        expected_result.enqueue(1)
        expected_result.enqueue(2)
        expected_result.enqueue(3)
        expected_result.enqueue(functions['mul'])
        expected_result.enqueue(functions['add'])
        expected_result.enqueue(functions['exp'])
        actual_result = parser.shunting_yard(input)
        self.assertEqual(actual_result, expected_result)

    def test_parser(self):
        input = "exp ( 1 + 2 * 3 )"
        expected_output = [
            functions['exp'],
            '(',
            1,
            functions['+'],
            2,
            functions['*'],
            3,
            ')'
        ]
        parser = Parser()
        actual_output = parser.parse_string(input)
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

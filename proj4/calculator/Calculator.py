import numpy as np
import numbers

from calculator.Function import Function
from data.DataStructures import Stack, Queue

functions = {
    'exp': Function(np.exp, 1, 0),
    'log': Function(np.log, 1, 0),
    'sin': Function(np.sin, 1, 0),
    'cos': Function(np.cos, 1, 0),
    'sqrt': Function(np.sqrt, 1, 0),
    'add': Function(np.add, 2, 2),
    'sub': Function(np.subtract, 2, 2),
    'mul': Function(np.multiply, 2, 1),
    'div': Function(np.divide, 2, 1),
    '+': Function(np.add, 2, 2),
    '-': Function(np.subtract, 2, 2),
    '*': Function(np.multiply, 2, 1),
    '/': Function(np.divide, 2, 1),
    '(': '(',
    ')': ')'
}

from calculator.Parser import Parser

class Calculator:
    def __init__(self):
        self._parser = Parser()

    def evaluate_rpn(self, input_queue: Queue):
        stack = Stack()
        while not input_queue.is_emtpy():
            token = input_queue.dequeue()
            if isinstance(token, numbers.Number):
                stack.push(token)
            else:
                stack.push(token.execute(stack))
        return stack.pop()

    def evaluate_string(self, input: str):
        tokens = self._parser.parse_string(input)
        input_queue = self._parser.shunting_yard(tokens)
        return self.evaluate_rpn(input_queue)

import numbers

from data.DataStructures import Stack, Queue
from calculator.Calculator import functions

class Parser:
    def __init__(self):
        pass

    def shunting_yard(self, input):
        operator_stack = Stack()
        output = Queue()
        for token in input:
            if isinstance(token, numbers.Number):
                output.enqueue(token)
            elif token == '(':
                operator_stack.push(token)
            elif token == ')':
                operator = operator_stack.pop()
                while operator != '(':
                    output.enqueue(operator)
                    operator = operator_stack.pop()
            else:
                while (not operator_stack.is_emtpy()) \
                        and (not isinstance(operator_stack.peek(), str)) \
                        and (not token > operator_stack.peek()):
                    output.enqueue(operator_stack.pop())
                operator_stack.push(token)
        while not operator_stack.is_emtpy():
            output.enqueue(operator_stack.pop())
        
        return output

    def _get_number(self, s: str):
        try:
            return float(s)
        except ValueError:
            return None

    def parse_string(self, input: str):
        result = []
        for token in input.split():
            n = self._get_number(token)
            if n != None:
                result.append(n)
            else:
                result.append(functions[token])
        return result

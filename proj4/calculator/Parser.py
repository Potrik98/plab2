import numbers

from data.DataStructures import Stack, Queue

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

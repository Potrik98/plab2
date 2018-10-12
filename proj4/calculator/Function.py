class Function:
    def __init__(self, func, arg_count, priority):
        self._function = func
        self._arg_count = arg_count
        self.priority = priority

    def execute(self, stack):
        args = []
        for i in range(self._arg_count):
            args.append(stack.pop())
        return self._function(*args)

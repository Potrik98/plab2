class Function:
    def __init__(self, func, arg_count, priority):
        self._function = func
        self._arg_count = arg_count
        self._priority = priority

    def execute(self, stack):
        args = []
        for _ in range(self._arg_count):
            args.append(stack.pop())
        args.reverse()
        print(args)
        return self._function(*args)

    def __gt__(self, other):
        return self._priority < other._priority

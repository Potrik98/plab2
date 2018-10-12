class LinkedList:
    class _Element:
        def __init__(self, value):
            self._value = value
            self._next = None
            self._previous = None

    def __init__(self):
        self._first = None
        self._last = None

    def is_empty(self):
        return self._first == None or self._last == None

    def insert_last(self, value):
        element = self._Element(value)
        if not self.is_empty():
            element._previous = self._last
            self._last._next = element
            self._last = element
        else:
            self._last = element
            self._first = element

    def insert_first(self, value):
        element = self._Element(value)
        if not self.is_empty():
            element._next = self._first
            self._first._previous = element
            self._first = element
        else:
            self._last = element
            self._first = element

    def remove_first(self):
        v = self._first._value
        if self._first._next != None:
            self._first._next._previous = None
        self._first = self._first._next
        if self.is_empty():
            self._last = None
        return v

    def remove_last(self):
        v = self._last._value
        if self._last._previous != None:
            self._last._previous._next = None
        self._last = self._last._previous
        if self.is_empty():
            self._first = None
        return v

    def get_last(self):
        return self._last._value

    def get_first(self):
        return self._first._value

    def __eq__(self, other):
        n1, n2 = self._first, other._first
        while n1 != None and n2 != None:
            if n1._value != n2._value:
                return False
            n1, n2 = n1._next, n2._next
        return n1 == n2

    def __str__(self):
        n = self._first
        r = "Values: "
        while n != None:
            r += str(n._value) + ", "
            n = n._next
        return r


class Stack:
    def __init__(self):
        self._values = LinkedList()

    def push(self, value):
        self._values.insert_last(value)

    def pop(self):
        return self._values.remove_last()

    def peek(self):
        return self._values.get_last()
    
    def is_emtpy(self):
        return self._values.is_empty()

    def __eq__(self, other):
        return self._values == other._values

    def __str__(self):
        return self._values.__str__()


class Queue:
    def __init__(self):
        self._values = LinkedList()
    
    def enqueue(self, value):
        self._values.insert_last(value)

    def dequeue(self):
        return self._values.remove_first()

    def peek_front(self):
        return self._values.get_first()
    
    def is_emtpy(self):
        return self._values.is_empty()

    def __eq__(self, other):
        return self._values == other._values

    def __str__(self):
        return self._values.__str__()

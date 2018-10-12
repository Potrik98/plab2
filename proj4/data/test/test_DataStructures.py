import unittest

from data.DataStructures import Stack, Queue, LinkedList


class DatastructureTest(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        e1 = 1
        e2 = 2
        e3 = 3
        self.assertTrue(stack.is_emtpy())
        stack.push(e1)
        stack.push(e2)
        stack.push(e3)
        self.assertFalse(stack.is_emtpy())
        self.assertEqual(e3, stack.peek())
        self.assertEqual(e3, stack.pop())
        self.assertEqual(e2, stack.pop())
        self.assertEqual(e1, stack.pop())
        self.assertTrue(stack.is_emtpy())

    def test_queue(self):
        queue = Queue()
        e1 = 1
        e2 = 2
        e3 = 3
        self.assertTrue(queue.is_emtpy())
        queue.enqueue(e1)
        queue.enqueue(e2)
        queue.enqueue(e3)
        self.assertFalse(queue.is_emtpy())
        self.assertEqual(e1, queue.peek_front())
        self.assertEqual(e1, queue.dequeue())
        self.assertEqual(e2, queue.dequeue())
        self.assertEqual(e3, queue.dequeue())
        self.assertTrue(queue.is_emtpy())

    def test_equals(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1.insert_last(1)
        l1.insert_last(2)
        l1.insert_last(3)
        l2.insert_last(1)
        l2.insert_last(2)
        l2.insert_last(3)
        self.assertEqual(l1, l2)
        l2.remove_first()
        self.assertNotEqual(l1, l2)
        l2.insert_first(1)
        self.assertEqual(l1, l2)

        s1 = Stack()
        s2 = Stack()
        self.assertEqual(s1, s2)
        s1.push(1)
        self.assertNotEqual(s1, s2)
        s2.push(1)
        self.assertEqual(s1, s2)


if __name__ == '__main__':
    unittest.main()

import unittest
from tdd_stack.stack import Stack


class TestTddStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_create(self):
        self.assertTrue(self.stack.is_empty())

    def test_push_and_top(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.top())
        self.assertFalse(self.stack.is_empty())

    def test_push_and_size(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.size())
        self.stack.push(2)
        self.assertEqual(2, self.stack.size())

    def test_empty_pop(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.pop()
        self.assertEqual(0, self.stack.size())

    def test_empty_top(self):
        with self.assertRaises(IndexError):
            self.stack.top()

    def test_push_push_pop_top(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(2, self.stack.size())
        self.stack.pop()
        self.assertEqual(1, self.stack.top())

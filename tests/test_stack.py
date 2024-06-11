import unittest
from tdd_stack.stack import Stack


class TestTddStack(unittest.TestCase):
    def test_create(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_push_and_top(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.top())

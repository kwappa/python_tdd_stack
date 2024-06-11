import unittest
from tdd_stack.stack import Stack


class TestTddStack(unittest.TestCase):
    def test_create(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

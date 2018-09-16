import unittest

from ..basics import *


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def _stack_fill(self, n):
        """
        Convenience method for filling the stack with values from 0 to n
        Args:
            n (int): the upper bound for range

        Returns (Stack): the stack instance

        """
        for i in range(n):
            self.stack.push(i)
        return self.stack

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty)

    def test_length(self):
        stack = self._stack_fill(25)
        self.assertTrue(stack.length == 25)

    def test_capacity_default(self):
        self.assertTrue(self.stack.capacity == 256)

    def test_set_capacity(self):
        stack = Stack(max_size=512)
        self.assertTrue(stack.capacity == 512)

    def test_overflow_error(self):
        def should_raise():
            self._stack_fill(257)
        self.assertRaises(StackOverflowError, should_raise)

    def test_push_changes_top(self):
        self.stack.push('hello')
        self.assertTrue(self.stack.top == 'hello')

    def test_pops_the_top(self):
        stack = self._stack_fill(25)
        top = stack.top
        popped = stack.pop()
        # <3
        self.assertTrue(top is popped)

    def test_pop_returns_top(self):
        stack = self._stack_fill(25)
        popped = stack.pop()
        self.assertTrue(popped == 24)

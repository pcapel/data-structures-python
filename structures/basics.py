"""
Some of the basic elemental classes that will be used to make up the more complex data structures
"""
import operator


class StackError(Exception):
    """Generic exception class for stack errors"""


class StackOverflowError(StackError):
    """I have always wanted to write this error..."""
    def __init__(self, message):
        self.message = message


class StackUnderflowError(StackError):
    """You done goofed!"""
    def __init__(self, message):
        self.message = message


class Stack:
    """
    A list based stack implementation exposing the following methods:
    push(): load a new top value into the stack
    pop(): unload and return the top value from the stack

    As well as the following properties:
    top: inspect the current top value of the stack without returning it
    is_empty: boolean, True if the stack contains no data, False otherwise
    size: the current number of elements in the stack
    """
    def __init__(self, max_size=256):
        """
        This implementation is from Chapter 6 exercise 6.16
        Args:
            max (int): The desired maximum stack size, default 256
        """
        self._elements = [None] * max_size
        self._stack_cap = max_size - 1
        self._len = 0
        self._top = None
        self._next_index = 0
        self._index = -1

    def __len__(self):
        return self._len

    def __repr__(self):
        return f'<Stack {id(self)} capacity={self.capacity} length={self.length}>'

    @property
    def length(self):
        return len(self)

    @property
    def capacity(self):
        return self._stack_cap + 1

    @property
    def top(self):
        if self.length < 1:
            return None
        return self._elements[self._index]

    @property
    def is_empty(self):
        return self.length == 0

    def _update(self, operation, amount):
        """
        Updates the internal state according to the passed operation
        Args:
            operation (operator.func): the operation to perform on self

        """
        self._len = operation(self._len, amount)
        self._next_index = operation(self._next_index, amount)
        self._index = operation(self._index, amount)

    def push(self, item):
        """
        Push an item onto the stack.
        Args:
            item (any): The item to push to the stack

        Returns: True, or raises

        Raises:
            StackOverflowError
        """
        if self._index == self._stack_cap:
            raise StackOverflowError('The stack is currently at max capacity: {} entries'.format(self.capacity))
        self._elements[self._next_index] = item
        self._update(operator.add, 1)
        return True

    def pop(self):
        """
        Return the current top, removing it from the stack
        Returns: The current top value from the stack
        Raises:
            StackUnderflowError

        """
        if self.is_empty:
            raise StackUnderflowError('The stack is empty!')
        value = self._elements[self._index]
        self._elements[self._index] = None
        self._update(operator.sub, 1)
        return value

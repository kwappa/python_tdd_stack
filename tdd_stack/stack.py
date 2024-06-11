class Stack:
    def __init__(self):
        self._value = 0

    def is_empty(self):
        return True

    def push(self, value):
        self._value = value

    def top(self):
        return self._value

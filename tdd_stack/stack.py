class Stack:
    def __init__(self):
        self._value = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        self._value = value
        self._size += 1

    def top(self):
        if self.is_empty():
            raise IndexError
        return self._value

    def size(self):
        return self._size

    def pop(self):
        if self.is_empty():
            raise IndexError
        self._size -= 1

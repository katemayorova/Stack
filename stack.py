from typing import Any, Iterable


class _StackNode:
    def __init__(self, data: Any = None, previous=None):
        self.data: Any = data
        self.previous: _StackNode = previous


class Stack:
    last: _StackNode = None

    def is_empty(self) -> bool:
        return self.last is None

    def push(self, data: Any) -> None:
        new_none = _StackNode(data, self.last)
        self.last = new_none

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('В стеке больше нет элементов')
        removed = self.last
        self.last = removed.previous
        return removed.data

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError('В стеке больше нет элементов')
        return self.last.data

    def size(self) -> int:
        current = self.last
        index = 0
        while current is not None:
            current = current.previous
            index += 1
        return index

    def push_all(self, iterable: Iterable):
        for item in iterable:
            self.push(item)

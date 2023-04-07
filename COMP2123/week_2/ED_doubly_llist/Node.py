from typing import Generic, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T, nextN = None, prevN = None) -> None:
        self._value = value
        self._next = nextN
        self._prev = prevN

    def get_value(self) -> T:
        return self._value

    def set_value(self, value: T) -> None:
        self._value = value

    def get_next(self) -> 'Node[T]':
        return self._next

    def set_next(self, nextN: 'Node[T]') -> None:
        self._next = nextN
        if nextN is not None:
            nextN._prev = self

    def get_prev(self) -> 'Node[T]':
        return self._prev

    def set_prev(self, prev: 'Node[T]') -> None:
        self._prev = prev
        if prev is not None:
            prev._next = self

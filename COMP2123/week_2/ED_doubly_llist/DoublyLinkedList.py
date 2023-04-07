from Node import Node
from typing import Generic, TypeVar

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    def __init__(self, front: Node[T] = None) -> None:
        self._size = 1 if front else 0
        self._front = front
        self._back = front

    def first(self) -> Node[T]:
        return self._front

    def last(self) -> Node[T]:
        return self._back

    def before(self, p: Node[T]) -> Node[T]:
        if isinstance(p, Node):
            return p.get_prev()
        return None

    def after(self, p: Node[T]) -> Node[T]:
        if isinstance(p, Node):
            return p.get_next()
        return None

    def is_element(self, p: Node[T]) -> bool:
        if p is None or self.first() is None:
            return False 
        curr = self.first()
        while curr is not None:
            if curr is p:
                return True
            if curr is self.last():
                break
            curr = curr.get_next()
        return False

    def insert_before(self, p: Node[T], e: Node[T]) -> None:
        ''' If list and p is empty, insert e at the front
            If the list is not empty and p is None, simply return None '''
        # Chekcs if p is an element of the list, None is always not an element
        if not isinstance(e, Node):
            return None
        if self.is_element(p):
            if p is not self.first():
                p.get_prev().set_next(e)
            else:
                self._front = e
                assert e.get_prev() is None
            e.set_next(p)
            self._size += 1
        else:
            if self.is_empty() and p is None:
                self._front = e
                assert e.get_prev() is None
                self._back = e
                self._size = 1

    def insert_after(self, p: Node[T], e: Node[T]) -> None:
        # If list and p is empty, insert e at the front
        # If the list is not empty and p is None, simply return None
        if not isinstance(e, Node):
            return None
        if self.is_element(p):
            if p is not self.last():
                p.get_next().set_prev(e)
            else:                
                self._back = e
            p.set_next(e) 
            self._size += 1
        else:
            if self.is_empty() and p is None:
                self._front = e
                assert e.get_prev() is None
                self._back = e
                self._size = 1

    def remove(self, p: Node[T]) -> Node[T]:
        # If p is not valid, return None.
        if not self.is_element(p):
            return None
        
        if p is self.first() and p is self.last():
            self._front, self._back = None, None
        elif p is self.first():
            self._front = p.get_next()
            self._front.set_prev(None)
        elif p is self.last():
            self._back = p.get_prev()
            self._back.set_next(None)
        else:
            prevN = p.get_prev()
            nextN = p.get_next()
            prevN.set_next(nextN)
            
        p.set_prev(None)
        p.set_next(None)
        self._size -= 1
        return p
                
    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        if self._size == 0:
            return True
        elif self._size > 0:
            return False
        else:
            return None
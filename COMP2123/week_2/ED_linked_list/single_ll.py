from Node import Node
from typing import Generic, TypeVar

T = TypeVar('T')

class Single_ll(Generic[T]):


    def __init__(self, first_node: Node[T]) -> None:
        self._size = 1
        self._front = first_node
        self._back  = first_node

    def first(self) -> Node[T]:
        return self._front

    def last(self) -> Node[T]:
        return self._back
    
    def after(self, p: Node[T]) -> Node[T]:
        if p is None:
            return None
        return p.get_next()

    def insert_after(self, p: Node[T], e: Node[T]) -> None:
        if e is None:
            return None
        self._size += 1
        if p is None:
            if self.first() is not None:
                e.set_next(self.first())
                self._front = e
            else:
                e.set_next(None)
                self._front, self._back = e, e
        else:
            old_next = p.get_next()
            p.set_next(e)
            if p is self.last():
                self._back = e
            else:
                e.set_next(old_next) 

    def remove(self, p: Node[T]) -> Node[T]:
        """
        Removes node p from list and joins the node previous from p to the node next to p. If p is 
        first node then just remove p and change first accordingly.
        If p is None return None. 
        :param p: Node object that is to be removed
        :return: The node that was removed
        """
        if p is None:
            return None
        
        curr = self.first()
        prev = None 
        while True:
            if curr is p:
                first_or_last = False
                # first
                if curr is self.first():
                    self._front = curr.get_next()
                    curr.set_next(None)
                    first_or_last = True
                # last 
                if curr is self.last():
                    self._back = prev
                    if self._back is not None:
                        self._back.set_next(None)
                    first_or_last = True
                # middle
                if not first_or_last:
                    prev.set_next(curr.get_next())
                self._size -= 1
                return curr
            if curr is self.last():
                break
            prev = curr
            curr = curr.get_next()
        return None

    
    def size(self) -> int:
        """
        Returns the size of the singly linked list
        :return: size of the list
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Returns if the singly linked list is empty of not.
        :return: True or False depending if list is empty or not.
        """
        if self.size() == 0:
            return True
        elif self.size() > 0:
            return False
        else:
            return None
   


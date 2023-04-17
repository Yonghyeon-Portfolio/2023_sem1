from typing import Generic, TypeVar, List
T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value
        self._parent = None
        self._children = []
        self._subtree_size = 1

    def get_value(self) -> T:
        return self._value

    def set_value(self, value: T) -> None:
        self._value = value

    def get_parent(self) -> 'Node[T]':
        return self._parent
    
    def get_subtree_size(self) -> int:
        return self._subtree_size
        
    def set_subtree_size(self, value: int) -> None:
        self._subtree_size = value
    
    def increment_ancestors_height(self):
        child_heights = [child._subtree_size for child in self._children]
        if len(child_heights) == 0:
            max_child_height = 0
        else:
            max_child_height = max(child_heights)
        self_child_gap = self.get_subtree_size() - max_child_height
        if self_child_gap <= 0:
            self._subtree_size -= (self_child_gap - 1)
            if self.get_parent() is not None:
                self.get_parent().increment_ancestors_height()
    
    def add_child(self, new_child: 'Node[T]') -> None:
        self._children.append(new_child)
        new_child._parent = self 
        self.increment_ancestors_height()
        
    def decrement_ancestors_height(self):
        child_heights = [child._subtree_size for child in self._children]
        if len(child_heights) == 0:
            max_child_height = 0
        else:
            max_child_height = max(child_heights)
        self_child_gap = self.get_subtree_size() - max_child_height
        if self_child_gap >= 2:
            self._subtree_size -= (self_child_gap - 1)
            if self.get_parent() is not None:
                self.get_parent().decrement_ancestors_height()
    
    def remove_child(self, rmv_child: 'Node[T]') -> None:
        try:
            self._children.remove(rmv_child)
            self.decrement_ancestors_height()
            return True
        except ValueError:
            return False # child not found
       
    def get_children(self) -> List['Node[T]']:
        return self._children
    
    def num_children(self) -> int:
        return len(self.get_children())

    def is_internal(p: 'Node[T]') -> bool:
        return p.get_subtree_size() > 1
    
    def is_external(p: 'Node[T]') -> bool:
        return p.get_subtree_size() == 1

    def is_root(p: 'Node[T]') -> bool:
        if p is None:
            return None
        return p.get_parent() is None

    def __str__(self):
        info =  f"Node(value: {self._value}, height: {self._subtree_size}, " \
            "children = [ "
        for child in self.get_children():
            info += str(child._value) +  " "
        info += "])"
        return info 


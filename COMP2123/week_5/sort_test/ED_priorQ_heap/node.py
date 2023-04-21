class Node():
    _key: int
    _value: str
    _parent: 'Node'
    _left_child: 'Node'
    _right_child: 'Node'

    def __init__(self, key: int, value: str) -> None:
        self._key = key
        self._value = value
        self._parent = None
        self._right_child = None
        self._left_child = None

    def get_key(self) -> int: 
        return self._key

    def set_key(self, key: int) -> None:
        self._key = key

    def set_value(self, value: str) -> None: 
        self._value = value
    
    def get_value(self) -> str: 
        return self._value

    def remove_from_tree(self) -> 'Node':
        if self._parent is None:
            # already detached from tree / root of tree (case handled by parent method)
            return
        if self._parent._left_child is self:
            self._parent._left_child = None
            # print("left child removed")
        elif self._parent._right_child is self:
            self._parent._right_child = None
            # print("right child removed")
        self._parent = None
    
    def add_left_child(self, child: 'Node') -> None:
        if child == None:
            self._left_child = None
            return
        self._left_child = child
        child._parent = self
    
    def add_right_child(self, child: 'Node') -> None:
        if child == None:
            self._right_child = None
            return
        self._right_child = child
        child._parent = self
    
    def get_left_child(self) -> 'Node':
        return self._left_child

    def get_right_child(self) -> 'Node':
        return self._right_child

    def is_root(self) -> bool: 
        return self._parent == None
    
    def is_left_child(self):
        if self.is_root():
            return False
        if self._parent._left_child is self:
            return True
        else:
            return False
    
    def is_right_child(self):
        if self.is_root():
            return False
        if self._parent._right_child is self:
            return True
        else:
            return False
        
    def up_heap(self) -> None:
        if self.is_root():
            return
        if self._key < self._parent._key:
            self_key, self_val = self._key, self._value
            self._key, self._value = self._parent._key, self._parent._value
            self._parent._key, self._parent._value = self_key, self_val
            self._parent.up_heap()
        
    def down_heap(self) -> None:
        left, right = self.get_left_child(), self.get_right_child()
        if left is None and right is None:
            return
        if left is None:
            smaller_child = right
        elif right is None:
            smaller_child = left
        else: # has both left / right child
            smaller_child = left
            if right._key < left._key:
                smaller_child = right
        
        if smaller_child._key < self._key:
            self_key, self_val = self._key, self._value
            self._key, self._value = smaller_child._key, smaller_child._value
            smaller_child._key, smaller_child._value = self_key, self_val
            smaller_child.down_heap()
    
    def __str__(self):
        return f"N[{self._key}: {self._value}]"
         

if __name__ == "__main__":
    root = Node(1, None)
    left = Node(2, None)
    right = Node(3, None)
    left_left = Node(-1, None)
    
    root.add_left_child(left)
    root.add_right_child(right)
    left.add_left_child(left_left)
    left_left.up_heap()
    print(root.get_key(), left.get_key(), left_left.get_key())
    
    root.set_key(10)
    root.down_heap()
    print(root.get_key(), left.get_key(), left_left.get_key())
    
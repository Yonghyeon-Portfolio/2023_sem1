class Node:
    value: int
    parent: 'Node'
    left: 'Node'
    right: 'Node'
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.parent = None
        self.left = left
        self.right = right
        
    def add_left(self, child):
        self.left = child
        child.parent = self
    
    def add_right(self, child):
        self.right = child
        child.parent = self
    
    def is_left_child(self):
        if self.parent is None:
            return False
        if self.parent.left is self:
            return True
        return False
    
    def is_right_child(self):
        if self.parent is None:
            return False
        if self.parent.right is self:
            return True
        return False

    def is_external(self):
        if self.left is None and self.right is None:
            return True
        return False

def pre_order_next(node: 'Node'):
    if node.left is not None:
        return node.left
    if node.right is not None:
        return node.right
    # At this point, it is obvious that node is external.
    investigate = node
    while True:
        if investigate.is_left_child():
            if investigate.parent.right is not None:
                return investigate.parent.right
            investigate = investigate.parent
        elif investigate.is_right_child():
            investigate = investigate.parent
        else:
            # investigate's parent = None. Hence, investigate has reached the root
            return None

def post_order_next(node: 'Node'):
    if node.is_right_child():
        return node.parent
    elif node.is_left_child():
        if node.parent.right is None:
            return node.parent
        # start post-order traversal
        search = node.parent.right
        while not search.is_external():
            if search.left is not None:
                search = search.left
            elif search.right is not None:
                search = search.right
        return search
    else:
        return None


    

if __name__ == "__main__":
    N1, N2, N3= Node(1), Node(2), Node(3)
    N4, N5, N6, N7= Node(4), Node(5), Node(6), Node(7)
    root = N1
    # second level
    root.add_left(N2)
    root.add_right(N3)
    # third level
    root.left.add_left(N4)
    root.right.add_left(N5)
    root.right.add_right(N6)
    # fourth level
    root.left.left.add_right(N7)
    
    # pre-order test
    assert pre_order_next(N1) is N2
    assert pre_order_next(N2) is N4
    assert pre_order_next(N4) is N7
    assert pre_order_next(N7) is N3
    assert pre_order_next(N3) is N5
    assert pre_order_next(N5) is N6
    assert pre_order_next(N6) is None
    
    # post-order test
    assert post_order_next(N7) is N4 
    assert post_order_next(N4) is N2
    assert post_order_next(N2) is N5
    assert post_order_next(N5) is N6
    assert post_order_next(N6) is N3
    assert post_order_next(N3) is N1
    assert post_order_next(N1) is None
    
    
    



        
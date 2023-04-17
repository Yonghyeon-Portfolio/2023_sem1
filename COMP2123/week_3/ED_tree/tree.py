from node import Node
from typing import Generic, TypeVar, List

T = TypeVar('T')

class Tree(Generic[T]):
    _size: int
    _root: Node[T]

    def __init__(self, root: 'Node[T]') -> None:
        self._root = root
        if root is None:
            self._size = 0
        else:
            self._size = root.get_subtree_size()
    
    def get_root(self) -> 'Node[T]':
        return self._root

    def get_size(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size > 0
        
    def is_root(self, p: 'Node[T]') -> bool:
        if p is self._root and p is not None:
            return True
        else:
            return False

    def is_leaf(self, p: 'Node[T]') -> bool:
        return p.is_external()

    def add_node(self, p: 'Node[T]', parent: 'Node[T]') -> None:
        if parent is None and self.get_root() is None:
            self._root = p
        else:
            parent.add_child(p)
        self._size = self.get_root().get_subtree_size()

    def remove_node(self, p: 'Node[T]', parent = None) -> bool:
        if self.is_root(p):
            self._root = None
            self._size = 0
            return
        if parent is None:
            parent = self._root
        if parent.remove_child(p):
            return True
        else:
            for child in parent.get_children():
                if self.remove_node(p, child):
                    return True
        if parent is self._root:
            print("Node to remove not found in tree")
        self._size = self.get_root().get_subtree_size()


    def preorder(self, p: 'Node[T]', ls: List['Node[T]']) -> None:
        """
        Preorder traversal of the tree
        :param p: the node to visit
        :param ls: Add nodes in preorder fashion to this supplied list
        Note: Add a newly visited node to the END of the supplied list
        """
        
        #TODO
    
    def postorder(self, p: 'Node[T]', ls: List['Node[T]']) -> None:
        """
        Postorder traversal of the tree
        :param p: the node to visit
        :param ls: Add nodes in postorder fashion to this supplied list
        Note: Add a newly visited node to the END of the supplied list 
        """
        
        #TODO

if __name__ == "__main__":
    root = Node(1)
    child_tree_A = Node(2)
    child_tree_A.add_child(Node(3))
    child_tree_A.add_child(Node(4))
    child_tree_B = Node(5)
    root.add_child(child_tree_A)
    child_tree_A.get_children()[0].add_child(Node(100))
    root.add_child(child_tree_B)
    child_tree_B.add_child(Node(10))
    
    tr = Tree(Node(1))
    
    node2, node3= Node(2), Node(3)
    tr.add_node(node2, tr.get_root())
    tr.add_node(node3, tr.get_root())
    
    node4, node5, node6 = Node(4), Node(5), Node(6)
    tr.add_node(node4, node2)
    tr.add_node(node5, node2)
    tr.add_node(node6, node3)    
    
    tr.add_node(Node(7), node4)
    
    print(tr.get_root())
    print(tr.get_root().get_children()[0])
    print(tr.get_root().get_children()[1], end="\n\n")
    assert tr.is_leaf(node6) == True
    assert tr.is_leaf(node6) == True
    assert tr.is_leaf(node4) == False
    
    tr.remove_node(node4)
    print(tr.get_root())
    print(tr.get_root().get_children()[0])
    print(tr.get_root().get_children()[1], end="\n\n")
    
    tr.remove_node(tr.get_root())
    tr.add_node(Node('new'), None)
    print(tr.get_root())
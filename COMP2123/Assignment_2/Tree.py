from Node import Node
from typing import List
import sys

sys.setrecursionlimit(2 ** 31 - 1)

class Tree:
    # These are the defined properties as described above, feel free to add more if you wish!
    root: Node

    def __init__(self) -> None:
        self.root = None
        self.nodes_num = 0

    def add_child(self, u: Node) -> Node:
        self.nodes_num += 1
        new_child = Node(self.nodes_num)
        if u is None:
            self.root = new_child
        else:
            u.add_child(new_child)
        return new_child
    
    def min_pre_order_rank(self, u: Node) -> int:
        return u.depth + 1

    def attach(self, T: "Tree", u: Node) -> None:
        if T.root is None:
            return
        else:
            T.root.set_parent(u)
    
    def master_order_recur(self, node: 'Node', m_order: List[int], result: List[int]):
        if len(node.get_children()) == 0:
            return
        for m_elem in m_order:
            for child in node.get_children():
                if m_elem == child.ID:
                    result.append(child)
                    self.master_order_recur(child, m_order, result)
                    break
            
            
    def pre_order(self, master_order: List[int]) -> List[Node]:
        result_order = [self.root]
        self.master_order_recur(self.root, master_order, result_order)
        return result_order

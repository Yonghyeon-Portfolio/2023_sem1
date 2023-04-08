from typing import List

class Node:
    id: int
    children: List["Node"]
    parent: "Node"

    def __init__(self, id: int) -> None:
        self.ID = id
        self.children = []
        self.parent = None
        self.depth = 0
        
    def depth_increment(self, start_node: 'Node', n: int):
        if start_node is None:
            return
        start_node.depth += n
        for child in start_node.children:
            self.depth_increment(child, n)

    def add_child(self, u: "Node") -> None:
        '''Only call this function for purpose of adding external nodes'''
        # The given node is guaranteed to not be a child of any other node.
        if isinstance(u, Node):
            assert len(u.get_children()) == 0
            u.parent = self
            u.depth = self.depth + 1
            self.children.append(u)
        else:
            print(f"Error: {u} is not a Node")
            # If u is not a Node (eg. None), no need to add it as a child

    def get_children(self) -> List["Node"]:
        return self.children

    def get_parent(self) -> "Node":
        return self.parent
    
    def set_parent(self, u: "Node") -> None:
        if u is None and self.parent is None:
            return
        if self.parent is not None:
            # remove self from previous parent's children list
            self.parent.get_children().remove(self)
        if u is None:
            self.parent = None
            self.depth_increment(self, -self.depth)
        else:
            self.parent = u
            u.children.append(self)
            self.depth_increment(self, u.depth + 1)
    
    @staticmethod
    def getID(node):
        if node is None:
            return None
        else:
            return node.ID
    
    def __str__(self):
        
        msg = f"\nSelf: Node[{self.ID}], Parent: Node[{Node.getID(self.parent)}]\n" \
            "  Children : { "
        for child in self.get_children():
            msg += f"Node[{Node.getID(child)}] "
        msg += "}"
        return msg
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

def subtree_size(node: Node):
    node.subtree_size = 1
    for child in node.children:
        node.subtree_size += subtree_size(child)
    return node.subtree_size

if __name__ == "__main__":
    root = Node(1)
    root.add_child(Node(2))
    root.add_child(Node(3))
    root.children[0].add_child(Node(4))
    root.children[0].add_child(Node(5))
    subtree_size(root)
    assert root.subtree_size == 5
    assert root.children[0].subtree_size == 3
    assert root.children[0].children[0].subtree_size == 1
    assert root.children[1].subtree_size == 1

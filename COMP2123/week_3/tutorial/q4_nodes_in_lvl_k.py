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
        
def find_nodes_at_level_k(root, level):
    result = []
    nodes_at_lvl_k(root, level, 1, result)
    return result

def nodes_at_lvl_k(node, target_lvl, curr_lvl, result):
    if node is None:
        return
    if target_lvl == curr_lvl:
        result.append(node.value)
    nodes_at_lvl_k(node.left, target_lvl, curr_lvl + 1, result)
    nodes_at_lvl_k(node.right, target_lvl, curr_lvl + 1, result)

if __name__ == "__main__":
    # level 1
    root = Node(1) 
    # level 2
    root.add_left(Node(2)) 
    root.add_right(Node(3))
    # level 3
    root.left.add_left(Node(4))
    root.right.add_left(Node(5))
    # level 4
    root.left.left.add_right(Node(6))
    
    print(find_nodes_at_level_k(root, 1))
    print(find_nodes_at_level_k(root, 2))
    print(find_nodes_at_level_k(root, 3))
    print(find_nodes_at_level_k(root, 4))
    
    
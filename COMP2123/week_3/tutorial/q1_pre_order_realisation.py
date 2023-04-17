import time 

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
        
    def add_left(self, child, tree_part_of):
        self.left = child
        child.parent = self
        tree_part_of.size += 1
    
    def add_right(self, child, tree_part_of):
        self.right = child
        child.parent = self
        tree_part_of.size += 1
    
    def get_depth(self):
        depth = 1
        curr = self
        while curr.parent is not None:
            depth += 1
            curr = curr.parent
        return depth

    def __str__(self):
        return f"{self.value} L{self.get_depth()}"

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.arr_idx = 0
    
    def set_root(self, root: Node):
        if root is None:
            self.root = None
            self.size = 0
        else:
            root.parent = None
            self.root = root
            self.size = 1
    
    def get_height(self):
        if self.root is None:
            return 0
        return self.__height_recursive(self.root, 1)
        
    def __height_recursive(self, node, height):
        if node is None:
            return height - 1
        return max([self.__height_recursive(node.left, height + 1),
                   self.__height_recursive(node.right, height + 1)])
    
    def pre_order_traversal(self):
        if self.root is None:
            return []
        result = []
        self.__pre_order_recursive(self.root, result)
        return result

    def __pre_order_recursive(self, node, result):
        if node is None:
            return
        result.append(node.__str__())
        self.__pre_order_recursive(node.left, result)
        self.__pre_order_recursive(node.right, result)
        
    def post_order_traversal(self):
        if self.root is None:
            return []
        result = []
        self.__post_order_recursive(self.root, result)
        return result
    
    def __post_order_recursive(self, node, result):
        if node is None:
            return
        self.__post_order_recursive(node.left, result)
        self.__post_order_recursive(node.right, result)
        result.append(node.__str__())
    
    def initialise_with_array(self, arr):
        if len(arr) == 0:
            self.set_root(None)
            return
        
        self.set_root(Node(None))
        # Add n many noedes to Tree
        self.__add_n_empty_nodes(len(arr), [self.root])
        # add elements accordingly
        self.arr_idx = 0
        self.__set_elements_referring_arr(self.root, arr)

    def __add_n_empty_nodes(self, n, parents: list[Node]):            
        new_parents = []
        for parent in parents:
            if self.size < n:
                new_node = Node(None)
                parent.add_left(new_node, self)
                new_parents.append(new_node)
            else:
                break
            if self.size < n:
                new_node = Node(None)
                parent.add_right(new_node, self)
                new_parents.append(new_node)
            else:
                break
        
        if self.size < n:
            self.__add_n_empty_nodes(n, new_parents)
        
    def __set_elements_referring_arr(self, node, arr):
        if node is None:
            return
        node.value = arr[self.arr_idx]
        self.arr_idx += 1
        self.__set_elements_referring_arr(node.left, arr)
        self.__set_elements_referring_arr(node.right, arr)
        
            
            
        
if __name__ == "__main__":
    tree = Tree()
    test_arr = []
    
    tree.initialise_with_array(test_arr)
    assert tree.get_height() == 0
    assert tree.size == 0
    assert tree.root is None
    print(tree.pre_order_traversal())
    
    test_arr = [1]
    tree.initialise_with_array(test_arr)
    assert tree.get_height() == 1
    assert tree.size == 1
    assert tree.root.value == 1
    print(tree.pre_order_traversal())
    
    test_arr = [1, 2]
    tree.initialise_with_array(test_arr)
    assert tree.get_height() == 2
    assert tree.size == 2
    assert tree.root.left.value == 2
    print(tree.pre_order_traversal())
    
    test_arr = [1, 2, 3]
    tree.initialise_with_array(test_arr)
    assert tree.get_height() == 2
    assert tree.size == 3
    print(tree.pre_order_traversal())
    
    test_arr = [1, 2, 3, 4, 5]
    tree.initialise_with_array(test_arr)
    assert tree.get_height() == 3
    assert tree.size == 5
    print(tree.pre_order_traversal())
    
    test_arr = [1, 2, 3, 4, 5, 6, 7]
    tree.initialise_with_array(test_arr)
    assert tree.get_height() == 3
    assert tree.size == 7
    print(tree.pre_order_traversal())
    
    test_arr = list(range(1, 16))
    tree.initialise_with_array(test_arr)
    assert tree.get_height() == 4
    assert tree.size == 15
    print(tree.pre_order_traversal())
    print(tree.post_order_traversal())
    
    # time complexity : O(n)
    start = time.time()
    test_arr = list(range(1, 10000000))
    tree.initialise_with_array(test_arr)
    print("%.3f seconds" %(time.time() - start))
from node import Node

dir_left, dir_right = -1 , 1

class PriorityQueue():
    _root: Node
    _last: Node
    _size: int

    def __init__(self) -> None:
        self._root = None
        self._last = None
        self._size = 0

    def size(self) -> int:
        return self._size 

    def is_empty(self) -> bool:
        if self._size == 0:
            return True
        return False
    
    def next_position_path(self):
        path = []
        if self.size() == 0:
            return path
        
        level, tree_cap = 1, 1
        while True:
            if self.size() >= tree_cap: # new level
                level += 1
                tree_cap = 2 * (tree_cap + 1) - 1
                continue
            floor_cap = (tree_cap + 1) // 2
            loc_idx = floor_cap - (tree_cap - self.size())
            # print("tree cap", tree_cap, "floor cap", floor_cap)
            while floor_cap != 1:
                floor_cap = floor_cap // 2
                # print("loc_idx", loc_idx, "floor_cap", floor_cap)
                if loc_idx >= floor_cap:
                    path.append(dir_right)
                    loc_idx -= floor_cap
                else:
                    path.append(dir_left)
            return path

    def insert_atlast_by_path(self, node):
        # assumes tree not empty, hence root exists
        position_path = self.next_position_path()
        curr = self._root
        for pp in position_path[:-1]:
            if pp == dir_left:
                curr = curr.get_left_child()
            else: # curr == dir_right
                curr = curr.get_right_child()
        if position_path[-1] == dir_left:
            curr.add_left_child(node)
        else: # curr == dir_right
            curr.add_right_child(node)
    
    def retrieve_last_by_path(self):
        # assumes tree not empty, hence root exists
        self._size -= 1
        position_path = self.next_position_path()
        curr = self._root
        for pp in position_path:
            if pp == dir_left:
                curr = curr.get_left_child()
            else: # curr == dir_right
                curr = curr.get_right_child()
        self._size += 1
        return curr
        

    def insert(self, k: int, v: str) -> None: 
        new_node = Node(k, v)
        if self._last is None:
            self._root = new_node
        elif self._last.is_left_child():
            self._last._parent.add_right_child(new_node)
        else: # last is root or right child
            self.insert_atlast_by_path(new_node)
        
        new_node.up_heap()
        self._last = new_node   
        self._size += 1 

    def remove_min(self) -> Node:
        if self._last is None:
            # no element to remove
            return None
        if self._last.is_root():
            removed_min = self._root
            self._root, self._last, self._size = None, None, 0
            return removed_min
        
        to_be_removed = Node(self._root._key, self._root._value)
        # Insert last's key and value to root
        self._root._key, self._root._value = self._last._key, self._last._value
        # Remove last element (certain it's not the root)
        self._last.remove_from_tree()
        # downheap() then update attributes (size, last)      
        self._root.down_heap()  
        self._size -= 1
        self._last = self.retrieve_last_by_path()
        return to_be_removed
        
    def min(self) -> Node:
        return self._root
    
    def __str__(self):
        if self._root is None:
            return "[]"
        result = [[self._root.__str__()]]
        exp_idx = 2
        while exp_idx <= self._size:
            result.append([])
            exp_idx *= 2
        
        self.str_helper(self._root, 1, result)
        lvl_num , str_res = 1, "--- Heap Priority Queue ---"
        for level_nodes in result:
            str_res += f"\nLevel {lvl_num}: {str(level_nodes)}"
            lvl_num += 1
        return str_res
        
    def str_helper(self, node: 'Node', level, result):
        # print("tmp result", result)
        if node._left_child is not None:
            result[level].append(node._left_child.__str__())
            self.str_helper(node._left_child, level + 1, result)
        if node._right_child is not None:
            result[level].append(node._right_child.__str__())
            self.str_helper(node._right_child, level + 1, result)
        
        return result
        

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(1, "A")
    print(pq.remove_min())
    print(pq)
    print(pq.remove_min())
    
    pq.insert(2, "B")
    pq.insert(3, "C")
    pq.insert(4, "D")
    pq.insert(5, "E")
    pq.insert(6, "F")
    print("Before", pq)
    print("removed", pq.remove_min())
    print(pq)
    print("last", pq._last)
    
    pq.insert(0, "A-")
    print(pq)
    
    print(pq.remove_min())
    print(pq)
    print(pq.remove_min())
    print(pq.remove_min())
    print(pq.remove_min())
    print(pq.remove_min())
    print(pq.remove_min())


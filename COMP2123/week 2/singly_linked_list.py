class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
    
    def get_val(self):
        return self.__value
    
    def set_val(self, value):
        self.__value = value
    
    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

class Positional_LS:
    def __init__(self, ls=[]):
        self.head = Node("HEAD") # The first Node
        self.__size = 0
        
        pointer = self.head
        for elem in ls:
            pointer.set_next(Node(elem))
            pointer = pointer.get_next()
            self.__size += 1
            
    def get_size(self):
        return self.__size
    
    def increment_size(self, n=1):
        self.__size += n
    
    def __str__(self):
        pointer = self.head
        ls = []
        while pointer.get_next() is not None:
            pointer = pointer.get_next()
            ls.append(str(pointer.get_val()))
        return "pos_ls(%s)" % ", ".join(ls)    
    
    def is_empty(self):
        if self.get_size() >= 1:
            return False
        return True
    
    def get_first(self):
        node_1 = self.head.get_next()
        if node_1 is not None:
            return node_1.get_val()
        else:
            return None
    
    def get_last(self):
        if (self.get_size() < 1):
            return None
        last = self.head
        for i in range(self.get_size()):
            last = last.get_next()
        return last.get_val()
    
    def insert(self, idx, value):
        ''' faster at inserting items between nodes closely following HEAD '''
        if (idx < 0 or idx > self.get_size()):
            raise Exception("Index out of bound")
        pointer = self.head
        for i in range(idx):
            pointer = pointer.get_next()
        
        new_node = Node(value)
        new_node.set_next(pointer.get_next())
        pointer.set_next(new_node)
        self.increment_size()
        
    # def get_nth_element(self, idx):
    #     cur_idx = 0
    #     elem = self.head
    #     while cur_idx < idx:
    #         if elem.next is not None:
    #             elem = elem.next
    #         else:
    #             return 
         
if __name__ == "__main__":
    pls_A = Positional_LS([1, 2, 3, "apple", "banana", "candy"])
    pls_B = Positional_LS()
    
    # size
    assert pls_A.get_size() == 6
    assert pls_B.get_size() == 0
    
    # empty or not
    assert pls_A.is_empty() == False
    assert pls_B.is_empty() == True
    
    # getting first element
    assert pls_A.get_first() == 1
    assert pls_B.get_first() is None
    
    # getting last element
    assert pls_A.get_last() == "candy"
    assert pls_B.get_last() is None
    
    # adding elements
    try:
        pls_A.insert(7, "watermelon")
    except Exception as e:
        # index 7 is out of bounds for pls_A (of size 6)
        pass
        
    try:
        pls_B.insert(1, 100)
    except Exception as e:
        pass
    
    pls_A.insert(0, -5)
    pls_A.insert(7, "watermelon")

    pls_B.insert(0, "first")
    pls_B.insert(1, "second")
    pls_B.insert(0, "negative")
    
    print(pls_A)
    print(pls_B)
    
    
    
from math import sqrt, floor
from time import time

class Node:
    def __init__(self, value, nextN=None):
        self.value = value
        self.next = nextN

def traverse_using_constant_space(HEAD: Node):
    if HEAD is None: return None
    last_element, curr = None, HEAD
    while last_element is not HEAD:
        if curr.next is last_element:
            last_element = curr
            # print("value:", curr.value)
            curr = HEAD
        else:
            curr = curr.next

def traverse_using_sqrtn_space(HEAD: Node):
    if HEAD is None: return None 
    ptr = HEAD
    # first, determine the size of the list
    n = 1
    while ptr.next is not None:
        n += 1
        ptr = ptr.next
    # then set pointers every sqrt(n) elements apart
    sqrt_n = floor(sqrt(n))
    pointers, ptr, ptr_distance = [], HEAD, sqrt_n
    while ptr.next is not None:
        if ptr_distance == sqrt_n:
            pointers.append(ptr)
            ptr_distance = 1
        else:
            ptr_distance += 1
        ptr = ptr.next
    pointers.append(None)
    # starting from lastest to earliest saved pointer,
    # traverse reversly to achieve the objective.
    for saved_ptr_idx in range(len(pointers)-2, -1, -1):
        ptr = pointers[saved_ptr_idx]
        elements = []
        while ptr is not pointers[saved_ptr_idx+1] :
            elements.append(ptr.value)
            ptr = ptr.next
        for e in elements[::-1]:
            # print("val:", e)
            pass
         
if __name__ == "__main__":
    test_list = Node(0)
    pointer = test_list
    for i in range(1, 1000000):
        pointer.next = Node(i)
        pointer = pointer.next
        
    start = time()
    # res1 = traverse_using_constant_space(test_list)
    mid = time()
    res2 = traverse_using_sqrtn_space(test_list)
    end = time()

    print("Space:   O(1)    |Time : %.3f seconds" %(mid - start))
    print("Space: O(sqrt_n) |Time : %.3f seconds" %(end - mid))
    
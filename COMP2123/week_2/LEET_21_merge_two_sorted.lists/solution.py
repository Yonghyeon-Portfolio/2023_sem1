import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Merge_Tool:
    def add(self, merge_node, list_node):
        merge_node.next = list_node
        return merge_node.next
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        merge_head = ListNode('Head')
        merge_node = merge_head
        while True:
            if list1 is None and list2 is None:
                return merge_head.next
            if list1 is None:
                while list2 is not None:
                    merge_node = self.add(merge_node, list2)
                    list2 = list2.next
                return merge_head.next
            if list2 is None:
                while list1 is not None:
                    merge_node = self.add(merge_node, list1)
                    list1 = list1.next
                return merge_head.next
            
            if list1.val <= list2.val:
                merge_node = self.add(merge_node, list1)
                list1 = list1.next
            elif list1.val > list2.val:
                merge_node = self.add(merge_node, list2)
                list2 = list2.next 


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    MT = Merge_Tool()
    
    merged = MT.mergeTwoLists(list1, list2)
    while merged is not None:
        print(merged.val)
        merged = merged.next
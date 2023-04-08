# medium
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], 
                        l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode(0)
        curr = result
        prev = None
        while (l1 is not None) or (l2 is not None):
            added = 0
            if l1 is not None: added += l1.val
            if l2 is not None: added += l2.val
            curr.next = ListNode((curr.val + added) // 10)
            curr.val = (curr.val + added) % 10
            prev = curr
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if prev.next.val == 0:
            prev.next = None            
        
        return result  

if __name__ == "__main__":
    ADDER = Solution()
    ls_1 = ListNode(1, ListNode(0, ListNode(1)))
    ls_2 = ListNode(9, ListNode(9))
    result = ADDER.addTwoNumbers(ls_1, ls_2)
    print(result)
    while result is not None:
        print(result.val)
        result = result.next
    
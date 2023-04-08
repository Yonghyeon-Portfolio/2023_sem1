from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        while curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

if __name__ == "__main__":
    Remover = Solution()
    ls = ListNode(1, ListNode(1, ListNode(1, ListNode(5))))
    ls2 = ListNode(5)
    ls3 = None
    cleaned = Remover.deleteDuplicates(ls)
    cleaned = Remover.deleteDuplicates(ls2)
    cleaned = Remover.deleteDuplicates(ls3)
    while cleaned is not None:
        print(cleaned.val)
        cleaned = cleaned.next
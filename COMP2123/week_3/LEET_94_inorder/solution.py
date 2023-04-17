from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def inorder_helper(self, node: TreeNode, result: List[int]):
        if node.left is not None:
            self.inorder_helper(node.left, result)
        result.append(node.val)
        if node.right is not None:
            self.inorder_helper(node.right, result)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        self.inorder_helper(root, result)
        return result
            
if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    result = s.inorderTraversal(root)
    print(result)
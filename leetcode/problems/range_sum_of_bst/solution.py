# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        
        def traverse(node):
            if node:
                if low <= node.val <= high:
                    self.total += node.val
                if low < node.val:
                    traverse(node.left)
                if node.val < high:
                    traverse(node.right)
        
        traverse(root)
        
        return self.total
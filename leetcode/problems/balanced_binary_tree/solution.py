# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def height(node):
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))
        
        return (abs(height(root.left) - height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right))
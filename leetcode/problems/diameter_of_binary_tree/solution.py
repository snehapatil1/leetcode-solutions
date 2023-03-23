# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def depth(root):
            if not root:
                return
            
            left = depth(root.left) if root.left else 0
            right = depth(root.right) if root.right else 0

            if left + right > self.diameter:
                self.diameter = left + right
            
            return 1 + (left if left > right else right)
        
        depth(root)
        return self.diameter
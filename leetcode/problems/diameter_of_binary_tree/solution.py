# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            
            left = depth(node.left) if node.left else 0
            right = depth(node.right) if node.right else 0

            if left + right > self.diameter:
                self.diameter = left + right
            
            return max(left, right) + 1
        
        depth(root)

        return self.diameter
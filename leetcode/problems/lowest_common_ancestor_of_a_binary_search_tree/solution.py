# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        minVal = min(p.val, q.val)
        maxVal = max(p.val, q.val)

        while root:
            if root.val > maxVal:
                root = root.left
            elif root.val < minVal:
                root = root.right
            else:
                return root
        
        return None
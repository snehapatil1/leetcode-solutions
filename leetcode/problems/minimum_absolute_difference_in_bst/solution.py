# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def bfs(node, low, high):
            if not node:
                return high - low
            
            return min(bfs(node.left, low, node.val), bfs(node.right, node.val, high))
        
        return bfs(root, -float('inf'), float('inf'))